import copy
from importlib import import_module
import sys
from io import StringIO

def peel(runners, modulename, fname, args=[], kwargs={}, options={}):
    return runners[-1](modulename, fname, args, kwargs,options,runners[:-1])

def base_runner(modulename, fname, args=[], kwargs={}, options={}, runners=[]):
    module = import_module(modulename)
    func = getattr(module, fname)
    return None,func(*args, **kwargs)

def check_args(modulename, fname, args=[], kwargs={}, options={}, runners=[base_runner]):
    args2 = copy.deepcopy(args)
    kwargs2 = copy.deepcopy(kwargs)
    code,res = peel(runners, modulename, fname, args, kwargs)
    if code:
        return code,res
    if not (args==args2 and kwargs==kwargs2): #good enough for now
        return ("modified", None)
    return None,res

def import_runner(modulename, fname, args=[], kwargs={}, options={},
                  resfilter=None,tname=''):
    if 'input' in options:
        return input_runner(modulename, fname, args, kwargs, options,tname)

    if 'output' in options:
        return print_runner(modulename, fname, args, kwargs, options,tname)

    check_input=options.pop('check_input') if 'check_input' in options else True
    resfilter=options.pop('resfilter') if 'resfilter' in options else None

    if check_input:
        runners = [base_runner,check_args]
    else:
        runners = [base_runner]
    code,res = peel(runners, modulename, fname, args, kwargs)
    if code:
        return code,res
    if resfilter:
        res = resfilter(res)
    return None,res

def print_runner(modulename, fname, args=[], kwargs={}, options={},tname=''):
    try:
        output=options.pop('output') if 'output' in options else None
        _stdout = sys.stdout
        tmpout = StringIO()
        sys.stdout = tmpout
        code,res = import_runner(modulename, fname, args, kwargs, options,
                                 tname=tname)
        if code:
            return code,res
        if output is None:
            if res is not None:
                return("wrong", 'return value should be None')
            res = tmpout.getvalue()
        else:
            if tmpout.getvalue() != output:
                return("wrong", 'wrong string printed to stdout')

        return None,res
    finally:
        sys.stdout = _stdout
        
def input_runner(modulename, fname, args=[], kwargs={}, options={},tname=''):
    try:
        input=options.pop('input')
        _stdin = sys.stdin
        tmpin = StringIO(input)
        sys.stdin = tmpin
        code,res = import_runner(modulename, fname, args, kwargs, options,
                                 tname=tname)
        if code:
            return code,res
        if tmpin.read():
            return("inputerr", 'did not read all input')
        return None,res
    finally:
        sys.stdin = _stdin
        
def functionname_runner(modulename, fname, args=[], kwargs={}, options={},tname=''):
    try:
        module = import_module(modulename)
    except:
        return None,"importfailed"
    if fname not in module.__dict__:
        return None,"notexist"
    if not callable(module.__dict__[fname]):
        return None,"notcallable"
    return None,True
