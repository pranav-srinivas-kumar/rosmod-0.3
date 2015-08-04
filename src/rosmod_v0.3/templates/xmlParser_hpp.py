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
__CHEETAH_genTime__ = 1438654570.87066
__CHEETAH_genTimestamp__ = 'Mon Aug  3 21:16:10 2015'
__CHEETAH_src__ = '/home/jeb/Repositories/rosmod-gui/src/rosmod_v0.3/templates/xmlParser_hpp.tmpl'
__CHEETAH_srcLastModified__ = 'Mon Aug  3 18:38:23 2015'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class xmlParser_hpp(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(xmlParser_hpp, self).__init__(*args, **KWs)
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
        
        write(u'''#include <iostream>
#include <fstream>
#include <vector>
#include <string.h>
#include <stdio.h>
#include <map>

#include "boost/filesystem.hpp"

''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"hash_include",True) # u'$hash_include' on line 10, col 1
        if _v is not None: write(_filter(_v, rawExpr=u'$hash_include')) # from line 10, col 1.
        write(u''' "''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"package_name",True) # u'$package_name' on line 10, col 16
        if _v is not None: write(_filter(_v, rawExpr=u'$package_name')) # from line 10, col 16.
        write(u'''/rapidxml.hpp"
''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"hash_include",True) # u'$hash_include' on line 11, col 1
        if _v is not None: write(_filter(_v, rawExpr=u'$hash_include')) # from line 11, col 1.
        write(u''' "''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"package_name",True) # u'$package_name' on line 11, col 16
        if _v is not None: write(_filter(_v, rawExpr=u'$package_name')) # from line 11, col 16.
        write(u'''/rapidxml_utils.hpp"
''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"hash_include",True) # u'$hash_include' on line 12, col 1
        if _v is not None: write(_filter(_v, rawExpr=u'$hash_include')) # from line 12, col 1.
        write(u''' "''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"package_name",True) # u'$package_name' on line 12, col 16
        if _v is not None: write(_filter(_v, rawExpr=u'$package_name')) # from line 12, col 16.
        write(u'''/Logger.hpp"

class ComponentConfig
{
public:
  std::string libraryLocation;
  std::string schedulingScheme;
  std::string hostName;
  std::string nodeName;
  std::string compName;
  std::map<std::string,std::string> portGroupMap;
  Log_Levels logLevels;
  uint64_t num_comps_to_sync;
  double comp_sync_timeout;
  double tg_time;
  uint64_t oob_uuid;
  std::string profileName;
};

using namespace rapidxml;

class XMLParser
{
public:
  std::vector<ComponentConfig> compConfigList;
  std::vector<std::string> libList;
  std::string nodeName;

  bool Return_Boolean(std::string value) { return (value == "True"); }

  void PrintNode(xml_node<> *node, std::string& prepend)
  {
    std::string local_prepend = prepend;
    printf("%s%s:\\n",local_prepend.c_str(),node->name());
    for (xml_attribute<> *tmpAttr = node->first_attribute();
\t tmpAttr; tmpAttr = tmpAttr->next_attribute())
      {
\tprintf("%s\\t%s: %s\\n",
\t       local_prepend.c_str(),
\t       tmpAttr->name(),
\t       tmpAttr->value());
      }
    local_prepend += "\\t";
    for (xml_node<> *tmpNode = node->first_node();
\t tmpNode; tmpNode = tmpNode->next_sibling())
      {
\tPrintNode(tmpNode, local_prepend);
      }
  }

  bool Parse(std::string fName)
  {
    if (!boost::filesystem::exists(fName))
      return false;
    rapidxml::file<> xmlFile(fName.c_str());
    rapidxml::xml_document<> doc;
    doc.parse<0>(xmlFile.data());

    xml_node<> *node = doc.first_node("node");
    nodeName = node->first_attribute()->value();
    
    for (xml_node<> *lib_location = node->first_node("library");
\t lib_location; lib_location = lib_location->next_sibling("library"))
      {
\tlibList.push_back(lib_location->first_attribute()->value());
      }

    for (xml_node<> *comp_inst = node->first_node("component_instance"); 
\t comp_inst; comp_inst = comp_inst->next_sibling("component_instance"))
      {
\tComponentConfig config;
\tconfig.num_comps_to_sync = 1;
\tconfig.comp_sync_timeout = 1.0;
\tconfig.compName = comp_inst->first_attribute()->value();
\tconfig.nodeName = nodeName;

\txml_node<> *nCompsSync = comp_inst->first_node("numCompsToSync");
\tif (nCompsSync != NULL)
\t  config.num_comps_to_sync = atoi(nCompsSync->first_attribute()->value());
\t
\txml_node<> *syncTimeout = comp_inst->first_node("syncTimeout");
\tif (syncTimeout != NULL)
\t  config.comp_sync_timeout = atof(syncTimeout->first_attribute()->value());
\t
\txml_node<> *oob_uuid = comp_inst->first_node("oob_uuid");
\tif (oob_uuid != NULL)
\t  config.oob_uuid = atoi(oob_uuid->first_attribute()->value());
\t
\txml_node<> *profileName = comp_inst->first_node("profileName");
\tif (profileName != NULL)
\t  config.profileName = profileName->first_attribute()->value();
\t
\txml_node<> *tg_time = comp_inst->first_node("tg_time");
\tif (tg_time != NULL)
\t  config.tg_time = atof(tg_time->first_attribute()->value());
\t
\txml_node<> *lib_location = comp_inst->first_node("library");
\tconfig.libraryLocation = lib_location->first_attribute()->value();
\t
\txml_node<> *sched_scheme = comp_inst->first_node("scheduling_scheme");
\tconfig.schedulingScheme = sched_scheme->first_attribute()->value();
\t
\txml_node<> *logger = comp_inst->first_node("logging");
\tconfig.logLevels.DEBUG = 
\t  Return_Boolean(logger->first_node("debug")->first_attribute()->value());
\tconfig.logLevels.INFO = 
\t  Return_Boolean(logger->first_node("info")->first_attribute()->value());
\tconfig.logLevels.WARNING = 
\t  Return_Boolean(logger->first_node("warning")->first_attribute()->value());
\tconfig.logLevels.ERROR = 
\t  Return_Boolean(logger->first_node("error")->first_attribute()->value());
\tconfig.logLevels.CRITICAL = 
\t  Return_Boolean(logger->first_node("critical")->first_attribute()->value());
\t
\tfor (xml_node<> *port_inst = comp_inst->first_node("port_instance"); 
\t     port_inst; port_inst = port_inst->next_sibling("port_instance"))
\t  {
\t    std::string portInstName = port_inst->first_attribute()->value();
\t    xml_node<> *port = port_inst->first_node("port");
\t    std::string portName = port->first_attribute()->value();
\t    xml_node<> *group = port_inst->first_node("group");
\t    std::string groupID = group->first_attribute()->value();
\t    config.portGroupMap.insert(std::pair<std::string,std::string>(portName,groupID));
\t  }
\tcompConfigList.push_back(config);
      }
    return true;
  }
};



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

    _mainCheetahMethod_for_xmlParser_hpp= 'respond'

## END CLASS DEFINITION

if not hasattr(xmlParser_hpp, '_initCheetahAttributes'):
    templateAPIClass = getattr(xmlParser_hpp, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(xmlParser_hpp)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=xmlParser_hpp()).run()


