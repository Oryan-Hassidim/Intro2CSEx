#!/usr/bin/env python3

from pathlib import Path

source_path = Path(__file__).resolve()
source_dir = source_path.parent

import shutil

shutil.copy(f"{source_dir}/../hangman.py", f"{source_dir}/hangman.py")

from sys import argv,stdout
from importlib import import_module
import operator as op
from copy import copy,deepcopy

from autotest import mp_test,res_code,TestSet,announce_failure
import autotest as at
import testrunners

# Setting levels:
# Global
# Exercise
# Set
# Test

class FakeException(Exception):
    pass

def diff_str(intro,exp,act):
    return "\n".join([intro+":",
                      "expected: "+repr(exp),
                      "actual:   "+repr(act)])

global_defaults = {'timeout':4,
                   'comparemethod':op.eq,
                   'runner':testrunners.import_runner,
                   'args':[],
                   'kwargs':{},
                   'ans':[None],
                   'options':{},
               }
def set_summary(name,correct,total):
    output = str(correct)+' passed tests out of '+str(total)+" in test set named '"+name+"'."
    if stdout.isatty():
        if correct==total:
            output = '\033[32;1;7m'+output+'\033[0m'
        else:
            output = '\033[35;1;7m'+output+'\033[0m'
                            
    res_code(name, str(correct),output)

def buildcallstr(fname,args,kwargs):
    if fname is None:
        fname = "None"
    argsbuild = []
    for a in args:
        argsbuild.append(repr(a))
    for k,v in kwargs.items():
        argsbuild.append(repr(k)+'='+repr(v))
    return fname+'('+','.join(argsbuild)+')'

def test_info(tname,getarg):
    lines = ['--> BEGIN TEST INFORMATION','Test name: '+tname]
    modulename = getarg('modulename')
    lines.append('Module tested: '+modulename)
    fname = getarg('fname')
    args = getarg('args')
    kwargs = getarg('kwargs')
    lines.append('Function call: '+buildcallstr(fname,args,kwargs))
    options = getarg('options')
    ans = getarg('ans')
    if 'input' in options:
        lines.append('Provided input: '+repr(options['input']))
    if 'output' in options and options['output'] is None:
        lines.append('Expected return value: '+repr(None))
    else:
        lines.append('Expected return value: '+repr(ans[0]))
    if 'output' in options:
        if options['output'] is None:
            lines.append('Expected print string: '+repr(ans[0]))
        else:
            lines.append('Expected print string: '+repr(options['output']))
    lines.append('More test options: '+repr(options))
    lines.append('--> END TEST INFORMATION')
    return '\n'.join(lines)

def run_all_tests(testfile,tests=None,dryrun=False):
    testmodule = import_module(testfile)
    defaults = global_defaults.copy()
    defaults.update(testmodule.defaults)

    if tests and not dryrun:
        print('Remember: Not all tests are being run.')
    for name,data in testmodule.tsets.items():
        if not tests or name in tests:
            test_sets(name, data, defaults, None, dryrun)
        elif any(t.startswith(name+'_') for t in tests):
            test_sets(name, data, defaults, tests, dryrun)

def test_sets(name, data, moddefaults, tests=None, dryrun=False):
    defaults = moddefaults.copy()
    defaults.update(data.defaults)

    def getarg(key):
        try:
            return val[key]
        except KeyError:
            return defaults[key]

    correct=0
    total=0
    for key,val in data.testcases.items():
        tname = '_'.join([name,str(key)])
        if tests and tname not in tests:
            continue
            
        total += 1

        try:
            if dryrun:
                print(test_info(tname,getarg))
                continue
            runner = getarg('runner')
            timeout = getarg('timeout')
            modulename = getarg('modulename')
            fname = getarg('fname')
            args = getarg('args')
            ans = getarg('ans')
            comparemethod = getarg('comparemethod')
            kwargs = getarg('kwargs')
            options = getarg('options')

            teststr = test_info(tname,getarg)

            code,res = mp_test(runner,[modulename,fname,args,kwargs,options],{"tname":tname}, timeout=timeout)

            if code:
                print(teststr)
                announce_failure(tname)
                res_code(tname, code, res)
                continue
            if any(comparemethod(a, res) for a in ans):
                correct+=1
                continue
            else:
                print(teststr)
                announce_failure(tname)
                res_code(tname, "wrong",diff_str("Wrong result, input: "+str(args),ans[0],res))

        except at.Error as e:
            print(teststr)
            announce_failure(tname)
            res_code(tname, e.code, e.message)
            continue
        except Exception as e:
            announce_failure(tname)
            res_code(tname, "testingFailed", e.__repr__())
            continue

    if not dryrun:
        set_summary(name,correct,total)


if __name__=="__main__":
    argv.pop(0)
    dryrun = False
    if '--dryrun' in argv:
        dryrun = True
        argv.remove('--dryrun')
    run_all_tests('ex4tests', set(argv[1:]), dryrun)
