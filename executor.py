#!/usr/bin/env python
# encoding: utf-8
## This is a simple class to wrap the given class as if it were a command
## line executable, for example, if you had this class:
## def A:
##     def method1(var1, var2=3, var4='four'):
##     ....
##     return result
##
## Then this code (in an executable file named a_cmd):
##   e = Executor(A())
##   print e.run()
##
## will act as a command line commmand, with all the parameters and the
## functions as subcommands, then you culd run:
##  >$ ./a_cmd method1 value1 --var4 'value4'
##
## And that will print the result of the execution of
##  A().method1('value1', var4='value4')


import argparse
import inspect


class Executor:
    def __init__(self, object):
        self.parser = argparse.ArgumentParser(
            description=('Simple command to execute the methods of the class '
                        '%s' % object.__class__.__name__))
        subparsers = self.parser.add_subparsers(
                        title='subcommands',
                        description='Valid subcommands',
                        help='Extra help on the commands')
        for mname, method in inspect.getmembers(object, inspect.ismethod):
            if mname.startswith('_'):
                continue
            args, varargs, keywords, defaults = inspect.getargspec(method)
            subp = subparsers.add_parser(mname)
            args.reverse()
            for arg in args:
                if arg == 'self':
                    continue
                if defaults:
                    defvalue = defaults[len(defaults) - 1]
                    subp.add_argument('--' + arg,
                            type=type(defvalue),
                            default=defvalue,
                            help='Default value %s' % defvalue.__repr__())
                    defaults = defaults[:-1]
                else:
                    subp.add_argument(arg, type=str)
                subp.set_defaults(func=method)

    def run(self):
        options = self.parser.parse_args()
        func = options.func
        del options.__dict__['func']
        return func(**options.__dict__)
