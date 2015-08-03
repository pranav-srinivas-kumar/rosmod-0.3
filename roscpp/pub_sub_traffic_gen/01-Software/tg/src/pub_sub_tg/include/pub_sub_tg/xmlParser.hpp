#include <iostream>
#include <fstream>
#include <vector>
#include <string.h>
#include <stdio.h>
#include <map>

#include "boost/filesystem.hpp"

#include "pub_sub_tg/rapidxml.hpp"
#include "pub_sub_tg/rapidxml_utils.hpp"
#include "pub_sub_tg/Logger.hpp"

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
  uint64_t oob_uuid;
  std::string profileName;
  std::map<std::string, std::string> attrMap;
};

using namespace rapidxml;

class XMLParser
{
public:
  std::vector<ComponentConfig> compConfigList;
  std::vector<std::string> libList;
  std::string nodeName;

  bool Return_Boolean(std::string value) 
  {
    if (value == "True") 
      return true;
    else
      return false;
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
	 lib_location; lib_location = lib_location->next_sibling("library"))
      {
	libList.push_back(lib_location->first_attribute()->value());
      }

    for (xml_node<> *comp_inst = node->first_node("component_instance"); 
	 comp_inst; comp_inst = comp_inst->next_sibling("component_instance"))
      {
	ComponentConfig config;
	config.num_comps_to_sync = 1;
	config.comp_sync_timeout = 1.0;
	config.compName = comp_inst->first_attribute()->value();
	config.nodeName = nodeName;

	for (xml_node<> *tmpNode = comp_inst->first_node();
	     tmpNode; tmpNode = tmpNode->next_sibling())
	  {
	    printf("%s , %s\n",
		   tmpNode->first_attribute()->name(),
		   tmpNode->first_attribute()->value());
	  }
	
	xml_node<> *nCompsSync = comp_inst->first_node("numCompsToSync");
	if (nCompsSync != NULL)
	  config.num_comps_to_sync = atoi(nCompsSync->first_attribute()->value());
	
	xml_node<> *syncTimeout = comp_inst->first_node("syncTimeout");
	if (syncTimeout != NULL)
	  config.comp_sync_timeout = atof(syncTimeout->first_attribute()->value());
	
	xml_node<> *oob_uuid = comp_inst->first_node("oob_uuid");
	if (oob_uuid != NULL)
	  config.oob_uuid = atof(oob_uuid->first_attribute()->value());
	
	xml_node<> *profileName = comp_inst->first_node("profileName");
	if (profileName != NULL)
	  config.profileName = atof(profileName->first_attribute()->value());
	
	xml_node<> *lib_location = comp_inst->first_node("library");
	config.libraryLocation = lib_location->first_attribute()->value();
	
	xml_node<> *sched_scheme = comp_inst->first_node("scheduling_scheme");
	config.schedulingScheme = sched_scheme->first_attribute()->value();
	
	xml_node<> *logger = comp_inst->first_node("logging");
	config.logLevels.DEBUG = 
	  Return_Boolean(logger->first_node("debug")->first_attribute()->value());
	config.logLevels.INFO = 
	  Return_Boolean(logger->first_node("info")->first_attribute()->value());
	config.logLevels.WARNING = 
	  Return_Boolean(logger->first_node("warning")->first_attribute()->value());
	config.logLevels.ERROR = 
	  Return_Boolean(logger->first_node("error")->first_attribute()->value());
	config.logLevels.CRITICAL = 
	  Return_Boolean(logger->first_node("critical")->first_attribute()->value());
	
	for (xml_node<> *port_inst = comp_inst->first_node("port_instance"); 
	     port_inst; port_inst = port_inst->next_sibling("port_instance"))
	  {
	    std::string portInstName = port_inst->first_attribute()->value();
	    xml_node<> *port = port_inst->first_node("port");
	    std::string portName = port->first_attribute()->value();
	    xml_node<> *group = port_inst->first_node("group");
	    std::string groupID = group->first_attribute()->value();
	    config.portGroupMap.insert(std::pair<std::string,std::string>(portName,groupID));
	  }
	compConfigList.push_back(config);
      }
    return true;
  }
};



