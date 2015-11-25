#include "three_component_example/Component_2.hpp"

//# Start User Globals Marker
//# End User Globals Marker

// Initialization Function
//# Start Init Marker
void Component_2::init_timer_operation(const NAMESPACE::TimerEvent& event)
{
#ifdef USE_ROSMOD
  comp_queue.ROSMOD_LOGGER->log("DEBUG", "Entering Component_2::init_timer_operation");
#endif
  // Initialize Here
  // Stop Init Timer
  init_timer.stop();
#ifdef USE_ROSMOD
  comp_queue.ROSMOD_LOGGER->log("DEBUG", "Exiting Component_2::init_timer_operation");
#endif  
}
//# End Init Marker


// Server Operation - Service_Server
//# Start ComponentService_operation Marker
bool Component_2::ComponentService_operation(three_component_example::ComponentService::Request  &req,
  three_component_example::ComponentService::Response &res)
{
#ifdef USE_ROSMOD
  comp_queue.ROSMOD_LOGGER->log("DEBUG", "Entering Component_2::ComponentService_operation");
#endif
  // Business Logic for Service_Server_operation
  three_component_example::ComponentName compName;
  compName.name = "Component_2";
  res.name = compName.name;
  logger->log("INFO", 
	      "Component_2::Name_Publisher::Publishing Component Name %s from ComponentServiceCallback", compName.name.c_str());
  Name_Publisher.publish(compName);
#ifdef USE_ROSMOD
  comp_queue.ROSMOD_LOGGER->log("DEBUG", "Exiting Component_2::ComponentService_operation");
#endif
  return true;
}
//# End ComponentService_operation Marker

// Timer Callback - Timer_2
//# Start Timer_2_operation Marker
void Component_2::Timer_2_operation(const NAMESPACE::TimerEvent& event)
{
#ifdef USE_ROSMOD
  comp_queue.ROSMOD_LOGGER->log("DEBUG", "Entering Component_2::Timer_2_operation");
#endif
  // Business Logic for Timer_2_operation
  three_component_example::ComponentName compName;
  compName.name = "Component_2";
  logger->log("INFO", 
	      "Component_2::Name_Publisher::Publishing Component Name %s from Timer_2 Callback", compName.name.c_str());
  Name_Publisher.publish(compName);
#ifdef USE_ROSMOD
  comp_queue.ROSMOD_LOGGER->log("DEBUG", "Exiting Component_2::Timer_2_operation");
#endif
}
//# End Timer_2_operation Marker


// Destructor - Cleanup Ports & Timers
Component_2::~Component_2()
{
  Timer_2.stop();
  Name_Publisher.shutdown();
  Service_Server.shutdown();
  //# Start Destructor Marker
  //# End Destructor Marker
}

// Startup - Setup Component Ports & Timers
void Component_2::startUp()
{
  NAMESPACE::NodeHandle nh;
  std::string advertiseName;

  // Identify the pwd of Node Executable
  std::string s = node_argv[0];
  std::string exec_path = s;
  std::string delimiter = "/";
  std::string exec, pwd;
  size_t pos = 0;
  while ((pos = s.find(delimiter)) != std::string::npos) {
    exec = s.substr(0, pos);
    s.erase(0, pos + delimiter.length());
  }
  exec = s.substr(0, pos);
  pwd = exec_path.erase(exec_path.find(exec), exec.length());
  std::string log_file_path = pwd + config.nodeName + "." + config.compName + ".log"; 

  logger->create_file(pwd + config.nodeName + "." + config.compName + ".log");
  logger->set_is_periodic(config.is_periodic_logging);
  logger->set_max_log_unit(config.periodic_log_unit);

#ifdef USE_ROSMOD
  comp_queue.ROSMOD_LOGGER->create_file(pwd + "ROSMOD_DEBUG." + config.nodeName + "." + config.compName + ".log");
  comp_queue.ROSMOD_LOGGER->set_is_periodic(config.is_periodic_logging);
  comp_queue.ROSMOD_LOGGER->set_max_log_unit(config.periodic_log_unit);
#endif    
  
#ifdef USE_ROSMOD 
  this->comp_queue.scheduling_scheme = config.schedulingScheme;
  rosmod::ROSMOD_Callback_Options callback_options;
#endif  
  // Configure all publishers associated with this component
  // Component Publisher - Name_Publisher
  advertiseName = "ComponentName";
  if (config.portGroupMap.find("Name_Publisher") != config.portGroupMap.end())
    advertiseName += "_" + config.portGroupMap["Name_Publisher"];
  this->Name_Publisher = nh.advertise<three_component_example::ComponentName>(advertiseName.c_str(), 1000);

  // Configure all provided services associated with this component
#ifdef USE_ROSMOD  
  callback_options.alias = "ComponentService_operation";
  callback_options.priority = 50;
  callback_options.deadline.sec =0;
  callback_options.deadline.nsec = 500000000;
#endif    
  // Component Server - Service_Server
  advertiseName = "ComponentService";
  if (config.portGroupMap.find("Service_Server") != config.portGroupMap.end())
    advertiseName += "_" + config.portGroupMap["Service_Server"];
  NAMESPACE::AdvertiseServiceOptions Service_Server_server_options;
  Service_Server_server_options = NAMESPACE::AdvertiseServiceOptions::create<three_component_example::ComponentService>
      (advertiseName.c_str(),
       boost::bind(&Component_2::ComponentService_operation, this, _1, _2),
       NAMESPACE::VoidPtr(),
#ifdef USE_ROSMOD       
       &this->comp_queue,
       callback_options);
#else
       &this->comp_queue);
#endif
  this->Service_Server = nh.advertiseService(Service_Server_server_options);

  // Synchronize components now that all publishers and servers have been initialized
  this->comp_sync_pub = nh.advertise<std_msgs::Bool>("component_synchronization", 1000);
  
#ifdef USE_ROSMOD  
  rosmod::SubscribeOptions comp_sync_sub_options;
  rosmod::ROSMOD_Callback_Options sync_callback_options;
#else
  ros::SubscribeOptions comp_sync_sub_options;
#endif
  
  comp_sync_sub_options = NAMESPACE::SubscribeOptions::create<std_msgs::Bool>
    ("component_synchronization",
     1000,
     boost::bind(&Component_2::component_sync_operation, this, _1),
     NAMESPACE::VoidPtr(),
#ifdef USE_ROSMOD     
     &this->comp_queue,
     sync_callback_options);
#else
     &this->comp_queue);
#endif
  this->comp_sync_sub = nh.subscribe(comp_sync_sub_options);

  ros::Time now = ros::Time::now();
  while ( this->comp_sync_sub.getNumPublishers() < this->config.num_comps_to_sync &&
	  (ros::Time::now() - now) < ros::Duration(config.comp_sync_timeout))
  ros::Duration(0.1).sleep();
  ros::Duration(0.5).sleep();
  this->comp_sync_sub.shutdown();  
  this->comp_sync_pub.shutdown();


  // Init Timer
#ifdef USE_ROSMOD    
  callback_options.alias = "init_timer_operation";
  callback_options.priority = 99;
  callback_options.deadline.sec = 1;
  callback_options.deadline.nsec = 0;
#endif
  NAMESPACE::TimerOptions timer_options;
  timer_options = 
    NAMESPACE::TimerOptions
    (ros::Duration(-1),
     boost::bind(&Component_2::init_timer_operation, this, _1),
     &this->comp_queue,
#ifdef USE_ROSMOD     
     callback_options,
#endif     
     true,
     false); 
  this->init_timer = nh.createTimer(timer_options);
  this->init_timer.stop();
#ifdef USE_ROSMOD   
  callback_options.alias = "Timer_2_operation";
  callback_options.priority = 50;
  callback_options.deadline.sec = 0;
  callback_options.deadline.nsec = 200000000;
#endif
  // Component Timer - Timer_2
  timer_options = 
    NAMESPACE::TimerOptions
    (ros::Duration(1.0),
     boost::bind(&Component_2::Timer_2_operation, this, _1),
     &this->comp_queue,
#ifdef USE_ROSMOD     
     callback_options,
#endif 
     false,
     false);
  this->Timer_2 = nh.createTimer(timer_options);


  this->init_timer.start();
  this->Timer_2.start();
}

extern "C" {
  Component *maker(ComponentConfig &config, int argc, char **argv) {
    return new Component_2(config,argc,argv);
  }
}
