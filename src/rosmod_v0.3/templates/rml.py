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
__CHEETAH_genTime__ = 1440196044.751232
__CHEETAH_genTimestamp__ = 'Fri Aug 21 17:27:24 2015'
__CHEETAH_src__ = '/home/jeb/Repositories/rosmod-gui/src/rosmod_v0.3/templates/rml.tmpl'
__CHEETAH_srcLastModified__ = 'Sat Jul 11 17:49:35 2015'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class rml(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(rml, self).__init__(*args, **KWs)
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
 * ROSMOD Software Model
 */

''')
        if VFSL([locals()]+SL+[globals(), builtin],"workspace.children",True) != []: # generated from line 5, col 1
            for package in VFSL([locals()]+SL+[globals(), builtin],"workspace.children",True): # generated from line 6, col 1
                write(u'''// ROSMOD Package - ''')
                _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"package",True),"properties",True)["name"] # u'$package.properties["name"]' on line 7, col 21
                if _v is not None: write(_filter(_v, rawExpr=u'$package.properties["name"]')) # from line 7, col 21.
                write(u'''
package ''')
                _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"package",True),"properties",True)["name"] # u'$package.properties["name"]' on line 8, col 9
                if _v is not None: write(_filter(_v, rawExpr=u'$package.properties["name"]')) # from line 8, col 9.
                write(u'''
{
''')
                if VFN(VFSL([locals()]+SL+[globals(), builtin],"package",True),"getChildrenByKind",False)("Component") != []: # generated from line 10, col 1
                    for component in VFN(VFSL([locals()]+SL+[globals(), builtin],"package",True),"getChildrenByKind",False)("Component"): # generated from line 11, col 1
                        write(u'''  // ROSMOD Component - ''')
                        _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"component",True),"properties",True)["name"] # u'$component.properties["name"]' on line 12, col 25
                        if _v is not None: write(_filter(_v, rawExpr=u'$component.properties["name"]')) # from line 12, col 25.
                        write(u'''
  component ''')
                        _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"component",True),"properties",True)["name"] # u'$component.properties["name"]' on line 13, col 13
                        if _v is not None: write(_filter(_v, rawExpr=u'$component.properties["name"]')) # from line 13, col 13.
                        write(u''' : ''')
                        _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"component",True),"properties",True)["datatype"] # u'$component.properties["datatype"]' on line 13, col 45
                        if _v is not None: write(_filter(_v, rawExpr=u'$component.properties["datatype"]')) # from line 13, col 45.
                        write(u''' 
  {
''')
                        if VFN(VFSL([locals()]+SL+[globals(), builtin],"component",True),"getChildrenByKind",False)("Server") != []: # generated from line 15, col 1
                            for server in VFN(VFSL([locals()]+SL+[globals(), builtin],"component",True),"getChildrenByKind",False)("Server"): # generated from line 16, col 1
                                write(u'''    // ROSMOD Server - ''')
                                _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"server",True),"properties",True)["name"] # u'$server.properties["name"]' on line 17, col 24
                                if _v is not None: write(_filter(_v, rawExpr=u'$server.properties["name"]')) # from line 17, col 24.
                                write(u'''
    server <''')
                                _v = VFN(VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"server",True),"properties",True)["service_reference"],"parent",True),"properties",True)["name"] # u'$server.properties["service_reference"].parent.properties["name"]' on line 18, col 13
                                if _v is not None: write(_filter(_v, rawExpr=u'$server.properties["service_reference"].parent.properties["name"]')) # from line 18, col 13.
                                write(u'''/''')
                                _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"server",True),"properties",True)["service_reference"],"properties",True)["name"] # u'$server.properties["service_reference"].properties["name"]' on line 18, col 79
                                if _v is not None: write(_filter(_v, rawExpr=u'$server.properties["service_reference"].properties["name"]')) # from line 18, col 79.
                                write(u'''> ''')
                                _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"server",True),"properties",True)["name"] # u'$server.properties["name"]' on line 18, col 139
                                if _v is not None: write(_filter(_v, rawExpr=u'$server.properties["name"]')) # from line 18, col 139.
                                write(u''' 
    {
''')
                                if VFN(VFSL([locals()]+SL+[globals(), builtin],"server",True),"properties",True)["priority"] != "": # generated from line 20, col 1
                                    write(u'''      priority = ''')
                                    _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"server",True),"properties",True)["priority"] # u'$server.properties["priority"]' on line 21, col 18
                                    if _v is not None: write(_filter(_v, rawExpr=u'$server.properties["priority"]')) # from line 21, col 18.
                                    write(u''';
''')
                                if VFN(VFSL([locals()]+SL+[globals(), builtin],"server",True),"properties",True)["deadline"] != "": # generated from line 23, col 1
                                    write(u'''      deadline = ''')
                                    _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"server",True),"properties",True)["deadline"] # u'$server.properties["deadline"]' on line 24, col 18
                                    if _v is not None: write(_filter(_v, rawExpr=u'$server.properties["deadline"]')) # from line 24, col 18.
                                    write(u''';
''')
                                write(u'''    }       
''')
                        if VFN(VFSL([locals()]+SL+[globals(), builtin],"component",True),"getChildrenByKind",False)("Client") != []: # generated from line 29, col 1
                            for client in VFN(VFSL([locals()]+SL+[globals(), builtin],"component",True),"getChildrenByKind",False)("Client"): # generated from line 30, col 1
                                write(u'''    // ROSMOD Client - ''')
                                _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"client",True),"properties",True)["name"] # u'$client.properties["name"]' on line 31, col 24
                                if _v is not None: write(_filter(_v, rawExpr=u'$client.properties["name"]')) # from line 31, col 24.
                                write(u'''
    client <''')
                                _v = VFN(VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"client",True),"properties",True)["service_reference"],"parent",True),"properties",True)["name"] # u'$client.properties["service_reference"].parent.properties["name"]' on line 32, col 13
                                if _v is not None: write(_filter(_v, rawExpr=u'$client.properties["service_reference"].parent.properties["name"]')) # from line 32, col 13.
                                write(u'''/''')
                                _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"client",True),"properties",True)["service_reference"],"properties",True)["name"] # u'$client.properties["service_reference"].properties["name"]' on line 32, col 79
                                if _v is not None: write(_filter(_v, rawExpr=u'$client.properties["service_reference"].properties["name"]')) # from line 32, col 79.
                                write(u'''> ''')
                                _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"client",True),"properties",True)["name"] # u'$client.properties["name"]' on line 32, col 139
                                if _v is not None: write(_filter(_v, rawExpr=u'$client.properties["name"]')) # from line 32, col 139.
                                write(u''';
''')
                        if VFN(VFSL([locals()]+SL+[globals(), builtin],"component",True),"getChildrenByKind",False)("Publisher") != []: # generated from line 35, col 1
                            for pub in VFN(VFSL([locals()]+SL+[globals(), builtin],"component",True),"getChildrenByKind",False)("Publisher"): # generated from line 36, col 1
                                write(u'''    // ROSMOD Publisher - ''')
                                _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"pub",True),"properties",True)["name"] # u'$pub.properties["name"]' on line 37, col 27
                                if _v is not None: write(_filter(_v, rawExpr=u'$pub.properties["name"]')) # from line 37, col 27.
                                write(u'''
    publisher <''')
                                _v = VFN(VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"pub",True),"properties",True)["message_reference"],"parent",True),"properties",True)["name"] # u'$pub.properties["message_reference"].parent.properties["name"]' on line 38, col 16
                                if _v is not None: write(_filter(_v, rawExpr=u'$pub.properties["message_reference"].parent.properties["name"]')) # from line 38, col 16.
                                write(u'''/''')
                                _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"pub",True),"properties",True)["message_reference"],"properties",True)["name"] # u'$pub.properties["message_reference"].properties["name"]' on line 38, col 79
                                if _v is not None: write(_filter(_v, rawExpr=u'$pub.properties["message_reference"].properties["name"]')) # from line 38, col 79.
                                write(u'''> ''')
                                _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"pub",True),"properties",True)["name"] # u'$pub.properties["name"]' on line 38, col 136
                                if _v is not None: write(_filter(_v, rawExpr=u'$pub.properties["name"]')) # from line 38, col 136.
                                write(u''';
''')
                        if VFN(VFSL([locals()]+SL+[globals(), builtin],"component",True),"getChildrenByKind",False)("Subscriber") != []: # generated from line 41, col 1
                            for sub in VFN(VFSL([locals()]+SL+[globals(), builtin],"component",True),"getChildrenByKind",False)("Subscriber"): # generated from line 42, col 1
                                write(u'''    // ROSMOD Subscriber - ''')
                                _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"sub",True),"properties",True)["name"] # u'$sub.properties["name"]' on line 43, col 28
                                if _v is not None: write(_filter(_v, rawExpr=u'$sub.properties["name"]')) # from line 43, col 28.
                                write(u'''
    subscriber <''')
                                _v = VFN(VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"sub",True),"properties",True)["message_reference"],"parent",True),"properties",True)["name"] # u'$sub.properties["message_reference"].parent.properties["name"]' on line 44, col 17
                                if _v is not None: write(_filter(_v, rawExpr=u'$sub.properties["message_reference"].parent.properties["name"]')) # from line 44, col 17.
                                write(u'''/''')
                                _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"sub",True),"properties",True)["message_reference"],"properties",True)["name"] # u'$sub.properties["message_reference"].properties["name"]' on line 44, col 80
                                if _v is not None: write(_filter(_v, rawExpr=u'$sub.properties["message_reference"].properties["name"]')) # from line 44, col 80.
                                write(u'''> ''')
                                _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"sub",True),"properties",True)["name"] # u'$sub.properties["name"]' on line 44, col 137
                                if _v is not None: write(_filter(_v, rawExpr=u'$sub.properties["name"]')) # from line 44, col 137.
                                write(u''' 
    {
''')
                                if VFN(VFSL([locals()]+SL+[globals(), builtin],"sub",True),"properties",True)["priority"] != "": # generated from line 46, col 1
                                    write(u'''      priority = ''')
                                    _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"sub",True),"properties",True)["priority"] # u'$sub.properties["priority"]' on line 47, col 18
                                    if _v is not None: write(_filter(_v, rawExpr=u'$sub.properties["priority"]')) # from line 47, col 18.
                                    write(u''';
''')
                                if VFN(VFSL([locals()]+SL+[globals(), builtin],"sub",True),"properties",True)["deadline"] != "": # generated from line 49, col 1
                                    write(u'''      deadline = ''')
                                    _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"sub",True),"properties",True)["deadline"] # u'$sub.properties["deadline"]' on line 50, col 18
                                    if _v is not None: write(_filter(_v, rawExpr=u'$sub.properties["deadline"]')) # from line 50, col 18.
                                    write(u''';
''')
                                write(u'''    }       
''')
                        if VFN(VFSL([locals()]+SL+[globals(), builtin],"component",True),"getChildrenByKind",False)("Timer") != []: # generated from line 55, col 1
                            for timer in VFN(VFSL([locals()]+SL+[globals(), builtin],"component",True),"getChildrenByKind",False)("Timer"): # generated from line 56, col 1
                                write(u'''    // ROSMOD Timer - ''')
                                _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"timer",True),"properties",True)["name"] # u'$timer.properties["name"]' on line 57, col 23
                                if _v is not None: write(_filter(_v, rawExpr=u'$timer.properties["name"]')) # from line 57, col 23.
                                write(u'''
    timer ''')
                                _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"timer",True),"properties",True)["name"] # u'$timer.properties["name"]' on line 58, col 11
                                if _v is not None: write(_filter(_v, rawExpr=u'$timer.properties["name"]')) # from line 58, col 11.
                                write(u''' 
    {
''')
                                if VFN(VFSL([locals()]+SL+[globals(), builtin],"timer",True),"properties",True)["period"] != "": # generated from line 60, col 1
                                    write(u'''\tperiod = ''')
                                    _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"timer",True),"properties",True)["period"] # u'$timer.properties["period"]' on line 61, col 11
                                    if _v is not None: write(_filter(_v, rawExpr=u'$timer.properties["period"]')) # from line 61, col 11.
                                    write(u''';
''')
                                if VFN(VFSL([locals()]+SL+[globals(), builtin],"timer",True),"properties",True)["priority"] != "": # generated from line 63, col 1
                                    write(u'''\tpriority = ''')
                                    _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"timer",True),"properties",True)["priority"] # u'$timer.properties["priority"]' on line 64, col 13
                                    if _v is not None: write(_filter(_v, rawExpr=u'$timer.properties["priority"]')) # from line 64, col 13.
                                    write(u''';
''')
                                if VFN(VFSL([locals()]+SL+[globals(), builtin],"timer",True),"properties",True)["deadline"] != "": # generated from line 66, col 1
                                    write(u'''\tdeadline = ''')
                                    _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"timer",True),"properties",True)["deadline"] # u'$timer.properties["deadline"]' on line 67, col 13
                                    if _v is not None: write(_filter(_v, rawExpr=u'$timer.properties["deadline"]')) # from line 67, col 13.
                                    write(u''';
''')
                                write(u'''    }       
''')
                        write(u'''  }
''')
                write(u'''}
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

    _mainCheetahMethod_for_rml= 'respond'

## END CLASS DEFINITION

if not hasattr(rml, '_initCheetahAttributes'):
    templateAPIClass = getattr(rml, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(rml)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=rml()).run()


