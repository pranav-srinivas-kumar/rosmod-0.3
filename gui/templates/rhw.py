#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1455822786.492051
__CHEETAH_genTimestamp__ = 'Thu Feb 18 11:13:06 2016'
__CHEETAH_src__ = '/home/jeb/Repositories/rosmod/gui/templates/rhw.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Feb  4 08:33:04 2016'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class rhw(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(rhw, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''/*
 * ROSMOD Hardware Model
 */

''')
        if VFFSL(SL,"rhw.children",True) != []: # generated from line 5, col 1
            for hardware in VFFSL(SL,"rhw.children",True): # generated from line 6, col 1
                write(u'''// Hardware - ''')
                _v = VFN(VFFSL(SL,"hardware",True),"properties",True)["name"] # u'$hardware.properties["name"]' on line 7, col 15
                if _v is not None: write(_filter(_v, rawExpr=u'$hardware.properties["name"]')) # from line 7, col 15.
                write(u'''
hardware ''')
                _v = VFN(VFFSL(SL,"hardware",True),"properties",True)["name"] # u'$hardware.properties["name"]' on line 8, col 10
                if _v is not None: write(_filter(_v, rawExpr=u'$hardware.properties["name"]')) # from line 8, col 10.
                write(u'''
{
  ip_address = "''')
                _v = VFN(VFFSL(SL,"hardware",True),"properties",True)["ip_address"] # u'$hardware.properties["ip_address"]' on line 10, col 17
                if _v is not None: write(_filter(_v, rawExpr=u'$hardware.properties["ip_address"]')) # from line 10, col 17.
                write(u'''";
  username = "''')
                _v = VFN(VFFSL(SL,"hardware",True),"properties",True)["username"] # u'$hardware.properties["username"]' on line 11, col 15
                if _v is not None: write(_filter(_v, rawExpr=u'$hardware.properties["username"]')) # from line 11, col 15.
                write(u'''";
  sshkey = "''')
                _v = VFN(VFFSL(SL,"hardware",True),"properties",True)["sshkey"] # u'$hardware.properties["sshkey"]' on line 12, col 13
                if _v is not None: write(_filter(_v, rawExpr=u'$hardware.properties["sshkey"]')) # from line 12, col 13.
                write(u'''"; 
  deployment_path = "''')
                _v = VFN(VFFSL(SL,"hardware",True),"properties",True)["deployment_path"] # u'$hardware.properties["deployment_path"]' on line 13, col 22
                if _v is not None: write(_filter(_v, rawExpr=u'$hardware.properties["deployment_path"]')) # from line 13, col 22.
                write(u'''";
  install_path = "''')
                _v = VFN(VFFSL(SL,"hardware",True),"properties",True)["install_path"] # u'$hardware.properties["install_path"]' on line 14, col 19
                if _v is not None: write(_filter(_v, rawExpr=u'$hardware.properties["install_path"]')) # from line 14, col 19.
                write(u'''";
''')
                if VFN(VFFSL(SL,"hardware",True),"properties",True)["init"] != "": # generated from line 15, col 1
                    write(u'''  init = "''')
                    _v = VFN(VFFSL(SL,"hardware",True),"properties",True)["init"] # u'$hardware.properties["init"]' on line 16, col 11
                    if _v is not None: write(_filter(_v, rawExpr=u'$hardware.properties["init"]')) # from line 16, col 11.
                    write(u'''";
''')
                if VFN(VFFSL(SL,"hardware",True),"properties",True)["arch"] != "": # generated from line 18, col 1
                    write(u'''  arch = ''')
                    _v = VFN(VFFSL(SL,"hardware",True),"properties",True)["arch"] # u'$hardware.properties["arch"]' on line 19, col 10
                    if _v is not None: write(_filter(_v, rawExpr=u'$hardware.properties["arch"]')) # from line 19, col 10.
                    write(u''';
''')
                write(u'''}
''')
        write(u'''
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_rhw= 'respond'

## END CLASS DEFINITION

if not hasattr(rhw, '_initCheetahAttributes'):
    templateAPIClass = getattr(rhw, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(rhw)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=rhw()).run()


