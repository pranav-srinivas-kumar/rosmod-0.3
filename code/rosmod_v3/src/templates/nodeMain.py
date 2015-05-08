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
__CHEETAH_genTime__ = 1431104647.9396
__CHEETAH_genTimestamp__ = 'Fri May  8 12:04:07 2015'
__CHEETAH_src__ = '/home/kelsier/Repositories/rosmod/code/rosmod_v3/src/templates/nodeMain.tmpl'
__CHEETAH_srcLastModified__ = 'Sun Apr 19 17:15:22 2015'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class nodeMain(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(nodeMain, self).__init__(*args, **KWs)
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
        
        _v = VFFSL(SL,"hash_include",True) # u'$hash_include' on line 1, col 1
        if _v is not None: write(_filter(_v, rawExpr=u'$hash_include')) # from line 1, col 1.
        write(u''' "ros/ros.h"
''')
        _v = VFFSL(SL,"hash_include",True) # u'$hash_include' on line 2, col 1
        if _v is not None: write(_filter(_v, rawExpr=u'$hash_include')) # from line 2, col 1.
        write(u''' <cstdlib>
''')
        _v = VFFSL(SL,"hash_include",True) # u'$hash_include' on line 3, col 1
        if _v is not None: write(_filter(_v, rawExpr=u'$hash_include')) # from line 3, col 1.
        write(u''' <string.h>

// Required for boost::thread
''')
        _v = VFFSL(SL,"hash_include",True) # u'$hash_include' on line 6, col 1
        if _v is not None: write(_filter(_v, rawExpr=u'$hash_include')) # from line 6, col 1.
        write(u''' <boost/thread.hpp>

// Include all components this actor requires
''')
        if VFFSL(SL,"len",False)(VFFSL(SL,"component_instances",True)) > 0: # generated from line 9, col 1
            for instance in VFFSL(SL,"component_instances",True): # generated from line 10, col 1
                _v = VFFSL(SL,"hash_include",True) # u'$hash_include' on line 11, col 1
                if _v is not None: write(_filter(_v, rawExpr=u'$hash_include')) # from line 11, col 1.
                write(u''' "''')
                _v = VFFSL(SL,"package_name",True) # u'$package_name' on line 11, col 16
                if _v is not None: write(_filter(_v, rawExpr=u'$package_name')) # from line 11, col 16.
                write(u'''/''')
                _v = VFN(VFN(VFFSL(SL,"instance",True),"properties",True)["component_reference"],"properties",True)["name"] # u'${instance.properties["component_reference"].properties["name"]}' on line 11, col 30
                if _v is not None: write(_filter(_v, rawExpr=u'${instance.properties["component_reference"].properties["name"]}')) # from line 11, col 30.
                write(u'''.hpp" 
''')
            write(u'''
''')
        write(u'''
void componentThread(Component* compPtr)
{
    compPtr->startUp();
    compPtr->processQueue();
}

int main(int argc, char **argv)
{
    std::string nodeName = "''')
        _v = VFFSL(SL,"node_name",True) # u'$node_name' on line 24, col 29
        if _v is not None: write(_filter(_v, rawExpr=u'$node_name')) # from line 24, col 29.
        write(u'''";
    std::string hostName = "localhost";

    for(int i = 0; i < argc; i++)
    {
        if(!strcmp(argv[i], "-nodename"))
            nodeName = argv[i+1];
\tif(!strcmp(argv[i], "-hostname"))
\t    hostName = argv[i+1];
    }

    ros::init(argc, argv, nodeName.c_str());

    // Create Node Handle
    ros::NodeHandle n;

    // Create Component Objects
''')
        if VFFSL(SL,"len",False)(VFFSL(SL,"component_instances",True)) > 0: # generated from line 41, col 5
            for instance in VFFSL(SL,"component_instances",True): # generated from line 42, col 5
                write(u'''    ''')
                _v = VFN(VFN(VFFSL(SL,"instance",True),"properties",True)["component_reference"],"properties",True)["name"] # u'$instance.properties["component_reference"].properties["name"]' on line 43, col 5
                if _v is not None: write(_filter(_v, rawExpr=u'$instance.properties["component_reference"].properties["name"]')) # from line 43, col 5.
                write(u''' ''')
                _v = VFN(VFFSL(SL,"instance",True),"properties",True)["name"] # u'${instance.properties["name"]}' on line 43, col 68
                if _v is not None: write(_filter(_v, rawExpr=u'${instance.properties["name"]}')) # from line 43, col 68.
                write(u'''(hostName, nodeName, "''')
                _v = VFN(VFFSL(SL,"instance",True),"properties",True)["name"] # u'${instance.properties["name"]}' on line 43, col 120
                if _v is not None: write(_filter(_v, rawExpr=u'${instance.properties["name"]}')) # from line 43, col 120.
                write(u'''", argc, argv); 
''')
            write(u'''
''')
        write(u'''    // Create Component Threads
''')
        if VFFSL(SL,"len",False)(VFFSL(SL,"component_instances",True)) > 0: # generated from line 48, col 5
            for instance in VFFSL(SL,"component_instances",True): # generated from line 49, col 5
                write(u'''    boost::thread ''')
                _v = VFN(VFFSL(SL,"instance",True),"properties",True)["name"] # u'${instance.properties["name"]}' on line 50, col 19
                if _v is not None: write(_filter(_v, rawExpr=u'${instance.properties["name"]}')) # from line 50, col 19.
                write(u'''_thread(componentThread, &''')
                _v = VFN(VFFSL(SL,"instance",True),"properties",True)["name"] # u'${instance.properties["name"]}' on line 50, col 75
                if _v is not None: write(_filter(_v, rawExpr=u'${instance.properties["name"]}')) # from line 50, col 75.
                write(u''');
    ROS_INFO("Node ''')
                _v = VFFSL(SL,"node_name",True) # u'${node_name}' on line 51, col 20
                if _v is not None: write(_filter(_v, rawExpr=u'${node_name}')) # from line 51, col 20.
                write(u''' has started ''')
                _v = VFN(VFFSL(SL,"instance",True),"properties",True)["name"] # u'${instance.properties["name"]}' on line 51, col 45
                if _v is not None: write(_filter(_v, rawExpr=u'${instance.properties["name"]}')) # from line 51, col 45.
                write(u'''");
''')
            write(u'''
''')
        write(u'''
    ROS_INFO_STREAM("NodeMain thread id = " << boost::this_thread::get_id());

    // Create Component Threads
''')
        if VFFSL(SL,"len",False)(VFFSL(SL,"component_instances",True)) > 0: # generated from line 59, col 5
            for instance in VFFSL(SL,"component_instances",True): # generated from line 60, col 5
                write(u'''    ''')
                _v = VFN(VFFSL(SL,"instance",True),"properties",True)["name"] # u'${instance.properties["name"]}' on line 61, col 5
                if _v is not None: write(_filter(_v, rawExpr=u'${instance.properties["name"]}')) # from line 61, col 5.
                write(u'''_thread.join();
''')
            write(u'''
''')
        write(u'''
    return 0; 
}

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

    _mainCheetahMethod_for_nodeMain= 'respond'

## END CLASS DEFINITION

if not hasattr(nodeMain, '_initCheetahAttributes'):
    templateAPIClass = getattr(nodeMain, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(nodeMain)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=nodeMain()).run()


