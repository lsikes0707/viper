#! /usr/bin/env python
from __future__ import print_function
import sys,os,subprocess
from testXML import *
class Bash2Py(object):
  __slots__ = ["val"]
  def __init__(self, value=''):
    self.val = value

def GetVariable(name, local=locals()):
  if name in local:
    return local[name]
  if name in globals():
    return globals()[name]
  return None

def Make(name, local=locals()):
  ret = GetVariable(name, local)
  if ret is None:
    ret = Bash2Py(0)
    globals()[name] = ret
  return ret

def Array(value):
  if isinstance(value, list):
    return value
  if isinstance(value, basestring):
    return value.strip().split(' ')
  return [ value ]

def quotesOkay(LIST):
	LIST=Bash2Py(LIST)
	for Make("i").val in Array(LIST.val):
	    _rcr1, _rcw1 = os.pipe()
	    if os.fork():
	        os.close(_rcw1)
	        os.dup2(_rcr1, 0)
	        subprocess.call(["sed -e 's|\"|\\\"|g'", i.val],shell=True)
	    else:
	        os.close(_rcr1)
	        os.dup2(_rcw1, 1)
	        print(i.val)
	        sys.exit(0)

