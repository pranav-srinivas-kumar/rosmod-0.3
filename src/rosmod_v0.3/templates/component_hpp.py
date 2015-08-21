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
__CHEETAH_genTime__ = 1440190063.156892
__CHEETAH_genTimestamp__ = 'Fri Aug 21 15:47:43 2015'
__CHEETAH_src__ = '/home/jeb/Repositories/rosmod-gui/src/rosmod_v0.3/templates/component_hpp.tmpl'
__CHEETAH_srcLastModified__ = 'Fri Aug 21 13:09:58 2015'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class component_hpp(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(component_hpp, self).__init__(*args, **KWs)
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
        
        write(u'''#ifndef ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"define_guard",True) # u'${define_guard}' on line 1, col 9
        if _v is not None: write(_filter(_v, rawExpr=u'${define_guard}')) # from line 1, col 9.
        write(u'''_HPP
#define ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"define_guard",True) # u'${define_guard}' on line 2, col 9
        if _v is not None: write(_filter(_v, rawExpr=u'${define_guard}')) # from line 2, col 9.
        write(u'''_HPP
''')
        if VFSL([locals()]+SL+[globals(), builtin],"mod",True) != "": # generated from line 3, col 1
            _v = VFSL([locals()]+SL+[globals(), builtin],"hash_include",True) # u'$hash_include' on line 4, col 1
            if _v is not None: write(_filter(_v, rawExpr=u'$hash_include')) # from line 4, col 1.
            write(u''' "rosmod/rosmod_ros.h"
''')
        else: # generated from line 5, col 1
            _v = VFSL([locals()]+SL+[globals(), builtin],"hash_include",True) # u'$hash_include' on line 6, col 1
            if _v is not None: write(_filter(_v, rawExpr=u'$hash_include')) # from line 6, col 1.
            write(u''' "ros/ros.h"
''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"hash_include",True) # u'$hash_include' on line 8, col 1
        if _v is not None: write(_filter(_v, rawExpr=u'$hash_include')) # from line 8, col 1.
        write(u''' "node/Component.hpp"
''')
        for topic in VFSL([locals()]+SL+[globals(), builtin],"topics",True): # generated from line 9, col 1
            _v = VFSL([locals()]+SL+[globals(), builtin],"hash_include",True) # u'$hash_include' on line 10, col 1
            if _v is not None: write(_filter(_v, rawExpr=u'$hash_include')) # from line 10, col 1.
            write(u''' "''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"topic",True)[0] # u'$topic[0]' on line 10, col 16
            if _v is not None: write(_filter(_v, rawExpr=u'$topic[0]')) # from line 10, col 16.
            write(u'''/''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"topic",True)[1] # u'${topic[1]}' on line 10, col 26
            if _v is not None: write(_filter(_v, rawExpr=u'${topic[1]}')) # from line 10, col 26.
            write(u'''.h"
''')
        for service in VFSL([locals()]+SL+[globals(), builtin],"services",True): # generated from line 12, col 1
            _v = VFSL([locals()]+SL+[globals(), builtin],"hash_include",True) # u'$hash_include' on line 13, col 1
            if _v is not None: write(_filter(_v, rawExpr=u'$hash_include')) # from line 13, col 1.
            write(u''' "''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"service",True)[0] # u'$service[0]' on line 13, col 16
            if _v is not None: write(_filter(_v, rawExpr=u'$service[0]')) # from line 13, col 16.
            write(u'''/''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"service",True)[1] # u'${service[1]}' on line 13, col 28
            if _v is not None: write(_filter(_v, rawExpr=u'${service[1]}')) # from line 13, col 28.
            write(u'''.h"
''')
        write(u'''
''')
        if VFSL([locals()]+SL+[globals(), builtin],"component_type",True) == 'KSP': # generated from line 16, col 1
            _v = VFSL([locals()]+SL+[globals(), builtin],"hash_include",True) # u'$hash_include' on line 17, col 1
            if _v is not None: write(_filter(_v, rawExpr=u'$hash_include')) # from line 17, col 1.
            write(u''' "krpci/krpci.hpp"
''')
        write(u'''
''')
        if VFSL([locals()]+SL+[globals(), builtin],"trafficGen",True): # generated from line 20, col 1
            if VFSL([locals()]+SL+[globals(), builtin],"len",False)(VFSL([locals()]+SL+[globals(), builtin],"publishers",True)) > 0: # generated from line 21, col 1
                _v = VFSL([locals()]+SL+[globals(), builtin],"hash_include",True) # u'$hash_include' on line 22, col 1
                if _v is not None: write(_filter(_v, rawExpr=u'$hash_include')) # from line 22, col 1.
                write(u''' "network/sender.hpp"
''')
            if VFSL([locals()]+SL+[globals(), builtin],"len",False)(VFSL([locals()]+SL+[globals(), builtin],"subscribers",True)) > 0: # generated from line 24, col 1
                _v = VFSL([locals()]+SL+[globals(), builtin],"hash_include",True) # u'$hash_include' on line 25, col 1
                if _v is not None: write(_filter(_v, rawExpr=u'$hash_include')) # from line 25, col 1.
                write(u''' "network/receiver.hpp"
''')
        write(u'''
''')
        if VFSL([locals()]+SL+[globals(), builtin],"user_includes",True) == "": # generated from line 29, col 1
            write(u'''//# Start User Includes Marker
//# End User Includes Marker
''')
        else: # generated from line 32, col 1
            write(u'''//# Start User Includes Marker
''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"user_includes",True) # u'$user_includes' on line 34, col 1
            if _v is not None: write(_filter(_v, rawExpr=u'$user_includes')) # from line 34, col 1.
            write(u'''//# End User Includes Marker
''')
        write(u'''
''')
        if VFSL([locals()]+SL+[globals(), builtin],"hpp_globals",True) == "": # generated from line 37, col 1
            write(u'''//# Start User Globals Marker
//# End User Globals Marker
''')
        else: # generated from line 40, col 1
            write(u'''//# Start User Globals Marker
''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"hpp_globals",True) # u'$hpp_globals' on line 42, col 1
            if _v is not None: write(_filter(_v, rawExpr=u'$hpp_globals')) # from line 42, col 1.
            write(u'''//# End User Globals Marker
''')
        write(u'''
class ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"component_name",True) # u'$component_name' on line 45, col 7
        if _v is not None: write(_filter(_v, rawExpr=u'$component_name')) # from line 45, col 7.
        write(u''' : public Component
{
public:
  // Constructor
  ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"component_name",True) # u'${component_name}' on line 49, col 3
        if _v is not None: write(_filter(_v, rawExpr=u'${component_name}')) # from line 49, col 3.
        write(u'''(ComponentConfig& _config, int argc, char **argv) : Component(_config, argc, argv) {}

  // Initialization
  void Init(const ros''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"mod",True) # u'${mod}' on line 52, col 22
        if _v is not None: write(_filter(_v, rawExpr=u'${mod}')) # from line 52, col 22.
        write(u'''::TimerEvent& event);

''')
        if VFSL([locals()]+SL+[globals(), builtin],"len",False)(VFSL([locals()]+SL+[globals(), builtin],"subscribers",True)) > 0: # generated from line 54, col 1
            for sub in VFSL([locals()]+SL+[globals(), builtin],"subscribers",True): # generated from line 55, col 1
                write(u'''  // Subscriber Callback - ''')
                _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"sub",True),"properties",True)["name"] # u'$sub.properties["name"]' on line 56, col 28
                if _v is not None: write(_filter(_v, rawExpr=u'$sub.properties["name"]')) # from line 56, col 28.
                write(u'''
  void ''')
                _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"sub",True),"properties",True)["name"] # u'${sub.properties["name"]}' on line 57, col 8
                if _v is not None: write(_filter(_v, rawExpr=u'${sub.properties["name"]}')) # from line 57, col 8.
                write(u'''_OnOneData(const ''')
                _v = VFN(VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"sub",True),"properties",True)["message_reference"],"parent",True),"properties",True)["name"] # u'$sub.properties["message_reference"].parent.properties["name"]' on line 57, col 50
                if _v is not None: write(_filter(_v, rawExpr=u'$sub.properties["message_reference"].parent.properties["name"]')) # from line 57, col 50.
                write(u'''::''')
                _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"sub",True),"properties",True)["message_reference"],"properties",True)["name"] # u'${sub.properties["message_reference"].properties["name"]}' on line 57, col 114
                if _v is not None: write(_filter(_v, rawExpr=u'${sub.properties["message_reference"].properties["name"]}')) # from line 57, col 114.
                write(u'''::ConstPtr& received_data); 
 
''')
        if VFSL([locals()]+SL+[globals(), builtin],"len",False)(VFSL([locals()]+SL+[globals(), builtin],"provided_services",True)) > 0: # generated from line 61, col 1
            for server in VFSL([locals()]+SL+[globals(), builtin],"servers",True): # generated from line 62, col 1
                write(u'''  // Server Callback - ''')
                _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"server",True),"properties",True)["name"] # u'$server.properties["name"]' on line 63, col 24
                if _v is not None: write(_filter(_v, rawExpr=u'$server.properties["name"]')) # from line 63, col 24.
                write(u'''
  bool ''')
                _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"server",True),"properties",True)["service_reference"],"properties",True)["name"] # u'${server.properties["service_reference"].properties["name"]}' on line 64, col 8
                if _v is not None: write(_filter(_v, rawExpr=u'${server.properties["service_reference"].properties["name"]}')) # from line 64, col 8.
                write(u'''Callback(''')
                _v = VFN(VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"server",True),"properties",True)["service_reference"],"parent",True),"properties",True)["name"] # u'$server.properties["service_reference"].parent.properties["name"]' on line 64, col 77
                if _v is not None: write(_filter(_v, rawExpr=u'$server.properties["service_reference"].parent.properties["name"]')) # from line 64, col 77.
                write(u'''::''')
                _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"server",True),"properties",True)["service_reference"],"properties",True)["name"] # u'$server.properties["service_reference"].properties["name"]' on line 64, col 144
                if _v is not None: write(_filter(_v, rawExpr=u'$server.properties["service_reference"].properties["name"]')) # from line 64, col 144.
                write(u'''::Request &req, 
    ''')
                _v = VFN(VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"server",True),"properties",True)["service_reference"],"parent",True),"properties",True)["name"] # u'$server.properties["service_reference"].parent.properties["name"]' on line 65, col 5
                if _v is not None: write(_filter(_v, rawExpr=u'$server.properties["service_reference"].parent.properties["name"]')) # from line 65, col 5.
                write(u'''::''')
                _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"server",True),"properties",True)["service_reference"],"properties",True)["name"] # u'$server.properties["service_reference"].properties["name"]' on line 65, col 72
                if _v is not None: write(_filter(_v, rawExpr=u'$server.properties["service_reference"].properties["name"]')) # from line 65, col 72.
                write(u'''::Response &res);

''')
        if VFSL([locals()]+SL+[globals(), builtin],"len",False)(VFSL([locals()]+SL+[globals(), builtin],"timers",True)) > 0: # generated from line 69, col 1
            for timer in VFSL([locals()]+SL+[globals(), builtin],"timers",True): # generated from line 70, col 1
                write(u'''  // Timer Callback - ''')
                _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"timer",True),"properties",True)["name"] # u'$timer.properties["name"]' on line 71, col 23
                if _v is not None: write(_filter(_v, rawExpr=u'$timer.properties["name"]')) # from line 71, col 23.
                write(u'''
  void ''')
                _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"timer",True),"properties",True)["name"] # u'${timer.properties["name"]}' on line 72, col 8
                if _v is not None: write(_filter(_v, rawExpr=u'${timer.properties["name"]}')) # from line 72, col 8.
                write(u'''Callback(const ros''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"mod",True) # u'${mod}' on line 72, col 53
                if _v is not None: write(_filter(_v, rawExpr=u'${mod}')) # from line 72, col 53.
                write(u'''::TimerEvent& event);

''')
        write(u'''  // Start up
  void startUp();

  // Destructor
  ~''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"component_name",True) # u'${component_name}' on line 80, col 4
        if _v is not None: write(_filter(_v, rawExpr=u'${component_name}')) # from line 80, col 4.
        write(u'''();

private:

''')
        if VFSL([locals()]+SL+[globals(), builtin],"len",False)(VFSL([locals()]+SL+[globals(), builtin],"timers",True)) > 0: # generated from line 84, col 1
            for timer in VFSL([locals()]+SL+[globals(), builtin],"timers",True): # generated from line 85, col 1
                write(u'''  // Timer
  ros''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"mod",True) # u'${mod}' on line 87, col 6
                if _v is not None: write(_filter(_v, rawExpr=u'${mod}')) # from line 87, col 6.
                write(u'''::Timer ''')
                _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"timer",True),"properties",True)["name"] # u'$timer.properties["name"]' on line 87, col 20
                if _v is not None: write(_filter(_v, rawExpr=u'$timer.properties["name"]')) # from line 87, col 20.
                write(u''';

''')
        if VFSL([locals()]+SL+[globals(), builtin],"len",False)(VFSL([locals()]+SL+[globals(), builtin],"subscribers",True)) > 0: # generated from line 91, col 1
            for sub in VFSL([locals()]+SL+[globals(), builtin],"subscribers",True): # generated from line 92, col 1
                write(u'''  // Subscriber
  ros''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"mod",True) # u'${mod}' on line 94, col 6
                if _v is not None: write(_filter(_v, rawExpr=u'${mod}')) # from line 94, col 6.
                write(u'''::Subscriber ''')
                _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"sub",True),"properties",True)["name"] # u'$sub.properties["name"]' on line 94, col 25
                if _v is not None: write(_filter(_v, rawExpr=u'$sub.properties["name"]')) # from line 94, col 25.
                write(u''';
''')
                if VFSL([locals()]+SL+[globals(), builtin],"trafficGen",True): # generated from line 95, col 1
                    write(u'''  // message id for this data stream
  uint64_t ''')
                    _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"sub",True),"properties",True)['name'] # u"${sub.properties['name']}" on line 97, col 12
                    if _v is not None: write(_filter(_v, rawExpr=u"${sub.properties['name']}")) # from line 97, col 12.
                    write(u'''_id;
  // subscriber receiver middleware
  Network::receiver ''')
                    _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"sub",True),"properties",True)['name'] # u"${sub.properties['name']}" on line 99, col 21
                    if _v is not None: write(_filter(_v, rawExpr=u"${sub.properties['name']}")) # from line 99, col 21.
                    write(u'''_recv_mw;
''')
                write(u'''
''')
        if VFSL([locals()]+SL+[globals(), builtin],"len",False)(VFSL([locals()]+SL+[globals(), builtin],"publishers",True)) > 0: # generated from line 104, col 1
            if VFSL([locals()]+SL+[globals(), builtin],"trafficGen",True): # generated from line 105, col 1
                write(u'''  // size of messages generated
  uint64_t max_data_length;
''')
            for pub in VFSL([locals()]+SL+[globals(), builtin],"publishers",True): # generated from line 109, col 1
                write(u'''  // Publisher 
  ros''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"mod",True) # u'${mod}' on line 111, col 6
                if _v is not None: write(_filter(_v, rawExpr=u'${mod}')) # from line 111, col 6.
                write(u'''::Publisher ''')
                _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"pub",True),"properties",True)["name"] # u'$pub.properties["name"]' on line 111, col 24
                if _v is not None: write(_filter(_v, rawExpr=u'$pub.properties["name"]')) # from line 111, col 24.
                write(u''';
''')
                if VFSL([locals()]+SL+[globals(), builtin],"trafficGen",True): # generated from line 112, col 1
                    write(u'''  // Timer for generating traffic
  ros::Timer ''')
                    _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"pub",True),"properties",True)['name'] # u"${pub.properties['name']}" on line 114, col 14
                    if _v is not None: write(_filter(_v, rawExpr=u"${pub.properties['name']}")) # from line 114, col 14.
                    write(u'''_timer;
  // Timer callback for traffic generation
  void ''')
                    _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"pub",True),"properties",True)['name'] # u"${pub.properties['name']}" on line 116, col 8
                    if _v is not None: write(_filter(_v, rawExpr=u"${pub.properties['name']}")) # from line 116, col 8.
                    write(u'''_timerCallback(const ros::TimerEvent& event);
  // publisher sender middleware
  Network::sender ''')
                    _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"pub",True),"properties",True)['name'] # u"${pub.properties['name']}" on line 118, col 19
                    if _v is not None: write(_filter(_v, rawExpr=u"${pub.properties['name']}")) # from line 118, col 19.
                    write(u'''_send_mw;
''')
                write(u'''
''')
        if VFSL([locals()]+SL+[globals(), builtin],"len",False)(VFSL([locals()]+SL+[globals(), builtin],"provided_services",True)) > 0: # generated from line 123, col 1
            for server in VFSL([locals()]+SL+[globals(), builtin],"servers",True): # generated from line 124, col 1
                write(u'''  // Server 
  ros''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"mod",True) # u'${mod}' on line 126, col 6
                if _v is not None: write(_filter(_v, rawExpr=u'${mod}')) # from line 126, col 6.
                write(u'''::ServiceServer ''')
                _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"server",True),"properties",True)["name"] # u'${server.properties["name"]}' on line 126, col 28
                if _v is not None: write(_filter(_v, rawExpr=u'${server.properties["name"]}')) # from line 126, col 28.
                write(u''';

''')
        if VFSL([locals()]+SL+[globals(), builtin],"len",False)(VFSL([locals()]+SL+[globals(), builtin],"required_services",True)) > 0: # generated from line 130, col 1
            for client in VFSL([locals()]+SL+[globals(), builtin],"clients",True): # generated from line 131, col 1
                write(u'''  // Client 
  ros''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"mod",True) # u'${mod}' on line 133, col 6
                if _v is not None: write(_filter(_v, rawExpr=u'${mod}')) # from line 133, col 6.
                write(u'''::ServiceClient ''')
                _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"client",True),"properties",True)["name"] # u'$client.properties["name"]' on line 133, col 28
                if _v is not None: write(_filter(_v, rawExpr=u'$client.properties["name"]')) # from line 133, col 28.
                write(u''';

''')
        if VFSL([locals()]+SL+[globals(), builtin],"user_private_variables",True) == "": # generated from line 137, col 1
            write(u'''  //# Start User Private Variables Marker
  //# End User Private Variables Marker
''')
        else: # generated from line 140, col 1
            write(u'''  //# Start User Private Variables Marker
''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"user_private_variables",True) # u'$user_private_variables' on line 142, col 1
            if _v is not None: write(_filter(_v, rawExpr=u'$user_private_variables')) # from line 142, col 1.
            write(u'''  //# End User Private Variables Marker
''')
        write(u'''};

#endif
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

    _mainCheetahMethod_for_component_hpp= 'respond'

## END CLASS DEFINITION

if not hasattr(component_hpp, '_initCheetahAttributes'):
    templateAPIClass = getattr(component_hpp, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(component_hpp)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=component_hpp()).run()


