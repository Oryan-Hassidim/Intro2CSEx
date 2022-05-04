"""Runs test(s) in process"""

import subprocess as sp
import multiprocessing as mp

import sys
import os
import signal
import tarfile
import zipfile
import fnmatch
from difflib import SequenceMatcher
from collections import namedtuple
import itertools

class Error(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message
    def __str__(self):
        return repr(self.code)+": "+repr(self.message)


def check_io(*popenargs, timeout=None, input=None, **kwargs):
    if 'stdin' in kwargs:
        raise ValueError('stdin argument not allowed, it will be overridden.')
    if 'stdout' in kwargs:
        raise ValueError('stdout argument not allowed, it will be overridden.')

    with sp.Popen(*popenargs, stdout=sp.PIPE, stdin=sp.PIPE, **kwargs) as process:
        try:
            output, unused_err = process.communicate(input=input, timeout=timeout)
        except sp.TimeoutExpired:
            process.kill()
            output, unused_err = process.communicate()
            raise sp.TimeoutExpired(process.args, timeout, output=output)
        except:
            process.kill()
            process.wait()
            raise
        retcode = process.poll()
        if retcode:
            raise sp.CalledProcessError(retcode, process.args, output=output)
        return output

def sp_test(args, timeout=None, input=None, universal_newlines=False):
    """runs test in subprocess"""
    
    try:
        output = check_io(args, timeout=timeout, input=input,
                          universal_newlines=universal_newlines)

    except sp.TimeoutExpired as e:
        return ("timeout",e)

    except sp.CalledProcessError as e:
        return ("retcode",e)

    except Exception as e:
        return ("exception",e)

    else:
        return (None,output)

def mp_test(target, args=(), kwargs={}, timeout=None):
    """runs test in multiprocess. (must be picklable)"""

    if os.name =='nt':
        return target(*args,**kwargs)

    r, w = mp.Pipe(duplex=False)
    def wrap(target=None, args=(), kwargs={}):
        r.close()
        res=target(*args, **kwargs)
        try:
            w.send(res)
        except:
            os.kill(os.getpid(),signal.SIGTERM)
        else:
            w.close()
            
    p = mp.Process(target=wrap, args=[target, args, kwargs])
    p.start()
    w.close()
    p.join(timeout) # Can't timeout pipe recv, so risking block on send.
    if p.is_alive():
        p.terminate()
        raise Error("timeout","Test timed out and did not complete.\nTimeout limit was "+str(timeout)+" seconds.\nYou may have an infinite loop or a big inefficiency.")
    if p.exitcode:
        raise Error("exception","Test did not complete, exited with exitcode "+str(p.exitcode)+".\nThis probably means your code caused an exception to be raised.")
    output = r.recv()
    r.close()
    return output
    #return (None,output)

def res_code(name, res="", output=None, ratio=1):
    if output:
        print (output)
    print("\t".join(["result_code",name, res, str(ratio)]))

def announce_failure(tname, filelist=False):
    if sys.stdout.isatty():
        head = '\033[31;1;7mThere is a problem:\n'
        tail = '\033[0m'
    else:
        head = '*'*70+'\n'+'*'*20+' '*5+'There is a problem:\n'+'*'*20+' '*5
        tail = '\n'+'*'*70
    if filelist:
        body = "Archive does not contain the correct files (or is the wrong format)."
    else:
        body = "The test named '"+tname+"' failed."
    print(head+body+tail)

def filelist_test(filename, required=(), permitted=(), forbidden=(), alternates=(), format='tar'):
    failed=0
    if format == 'tar':
        tf = tarfile.open(name=filename)
        names = tf.getnames()
        tf.close()
    elif format == 'zip':
        zf = zipfile.ZipFile(filename)
        names = zf.namelist()
        zf.close()
    else:
        res_code("unknown_format",str(format),"Unknown file format: "+format)
        return -1
    missing = [n for n in required if not n in names]
    tmpper = [n for n in names for pattern in permitted if fnmatch.fnmatch(n,pattern)]
    tmpper.extend([n for n in names for pattern in list(itertools.chain(*alternates)) if fnmatch.fnmatch(n,pattern)])
    tmpfor = [n for n in names for pattern in forbidden if fnmatch.fnmatch(n,pattern)]
    extra = [n for n in names if n not in required and (n in tmpfor or n not in tmpper)
                                                   and not n.startswith("__MACOSX/")]
    for alt in alternates:
        found = [n for n in names for pattern in alt if fnmatch.fnmatch(n,pattern)]
        if not found:
            missing.append('|'.join(alt))
        extra.extend(found[1:])
        
    for n in missing:
        failed+=1
        res_code("missing_file",n,"Missing required file: "+n)
    for n in extra:
        failed+=1
        res_code("extra_file",n,"Extra file submitted: "+n)
    return failed

def read_res_codes(file=None):
    res = []
    for line in file:
        rec = line.split("\t")
        if len(rec)==4 and rec[0]=="result_code":
            rec[3]=float(rec[3])
            res.append(rec)
    return res

def long_sequence_compare(name, expected, actual, contextpreview=20, res="wrong"):
    if expected==actual:
        return

    sm = SequenceMatcher(a=expected, b=actual)
    diffs = sm.get_opcodes()
    dstart = 0
    if diffs[0][0]=='equal':
        dstart = diffs[0][2] - contextpreview
        if dstart<0:
            dstart=0
    res_code(name, res, "\n".join(["Showing output from element "+str(dstart),
                                   "expected: "+str(expected[dstart:dstart+300]),
                                   "actual:   "+str(actual[dstart:dstart+300])]))
   
TestSet = namedtuple('TestSet',['defaults','testcases'])
