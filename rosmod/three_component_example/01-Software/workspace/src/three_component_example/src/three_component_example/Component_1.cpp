#include "three_component_example/Component_1.hpp"


//# Start User Globals Marker
//# End User Globals Marker

// Initialization Function
//# Start Init Marker
void Component_1::Init(const rosmod::TimerEvent& event)
{
  compQueue.ROSMOD_LOGGER.DEBUG("Entering Component_1::Init");
  // Initialize Here

  // Stop Init Timer
  initOneShotTimer.stop();
  compQueue.ROSMOD_LOGGER.DEBUG("Exiting Component_1::Init");
}
//# End Init Marker

// Subscriber Callback - Name_Subscriber
//# Start Name_Subscriber_OnOneData Marker
void Component_1::Name_Subscriber_OnOneData(const three_component_example::ComponentName::ConstPtr& received_data)
{
  compQueue.ROSMOD_LOGGER.DEBUG("Entering Component_1::Name_Subscriber_OnOneData");
  // Business Logic for Name_Subscriber Subscriber

  compQueue.ROSMOD_LOGGER.DEBUG("Exiting Component_1::Name_Subscriber_OnOneData");
}
//# End Name_Subscriber_OnOneData Marker

// Timer Callback - Timer_1
//# Start Timer_1Callback Marker
void Component_1::Timer_1Callback(const rosmod::TimerEvent& event)
{
  compQueue.ROSMOD_LOGGER.DEBUG("Entering Component_1::Timer_1Callback");
  // Business Logic for Timer_1 Timer

  compQueue.ROSMOD_LOGGER.DEBUG("Exiting Component_1::Timer_1Callback");
}
//# End Timer_1Callback Marker


// Destructor - Cleanup Ports & Timers
Component_1::~Component_1()
{
  Timer_1.stop();
  Name_Publisher.shutdown();
  Name_Subscriber.shutdown();
  //# Start Destructor Marker
  //# End Destructor Marker
}

// Startup - Setup Component Ports & Timers
void Component_1::startUp()
{
  rosmod::NodeHandle nh;
  std::string advertiseName;

  // Scheduling Scheme is FIFO
  this->compQueue.scheduling_scheme = scheduling_scheme;
  rosmod::ROSMOD_Callback_Options callback_options;

  callback_options.alias = "Name_Subscriber_OnOneData";
  callback_options.priority = 50;
  callback_options.deadline.sec = 0;
  callback_options.deadline.nsec = 300000000;
  // Component Subscriber - Name_Subscriber
  advertiseName = "ComponentName";
  if (portGroupMap.find("Name_Subscriber") != portGroupMap.end())
    advertiseName += "_" + portGroupMap["Name_Subscriber"];
  rosmod::SubscribeOptions Name_Subscriber_options;
  Name_Subscriber_options = rosmod::SubscribeOptions::create<three_component_example::ComponentName>
      (advertiseName.c_str(),
       1000,
       boost::bind(&Component_1::Name_Subscriber_OnOneData, this, _1),
       rosmod::VoidPtr(),
       &this->compQueue,
       callback_options);
  this->Name_Subscriber = nh.subscribe(Name_Subscriber_options);

  // Component Publisher - Name_Publisher
  advertiseName = "ComponentName";
  if (portGroupMap.find("Name_Publisher") != portGroupMap.end())
    advertiseName += "_" + portGroupMap["Name_Publisher"];
  this->Name_Publisher = nh.advertise<three_component_example::ComponentName>(advertiseName.c_str(), 1000);

  // Init Timer
  callback_options.alias = "Init_Timer";
  callback_options.priority = 99;
  callback_options.deadline.sec = 1;
  callback_options.deadline.nsec = 0;
  rosmod::TimerOptions timer_options;
  timer_options = 
    rosmod::TimerOptions
    (ros::Duration(-1),
     boost::bind(&Component_1::Init, this, _1),
     &this->compQueue,
     callback_options,
     true,
     true);
  this->initOneShotTimer = nh.createTimer(timer_options);
  this->initOneShotTimer.stop();
  callback_options.alias = "Timer_1Callback";
  callback_options.priority = 50;
  callback_options.deadline.sec = 0;
  callback_options.deadline.nsec = 200000000;
  // Component Timer - Timer_1
  timer_options = 
    rosmod::TimerOptions
    (ros::Duration(0.5),
     boost::bind(&Component_1::Timer_1Callback, this, _1),
     &this->compQueue,
     callback_options,
     false,
     false);
  this->Timer_1 = nh.createTimer(timer_options);

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
  std::string log_file_path = pwd + nodeName + "." + compName + ".log"; 
  
  // Create the log file & open file stream
  LOGGER.CREATE_FILE(log_file_path);
  
  // Establish log levels of LOGGER
  LOGGER.SET_LOG_LEVELS(logLevels);


  this->comp_sync_pub = nh.advertise<std_msgs::Bool>("component_synchronization", 1000);
  
  rosmod::SubscribeOptions comp_sync_sub_options;
  rosmod::ROSMOD_Callback_Options sync_callback_options;
  comp_sync_sub_options = rosmod::SubscribeOptions::create<std_msgs::Bool>
    ("component_synchronization",
     1000,
     boost::bind(&Component_1::component_synchronization_OnOneData, this, _1),
     rosmod::VoidPtr(),
     &this->compQueue,
     sync_callback_options);
  this->comp_sync_sub = nh.subscribe(comp_sync_sub_options);

  rosmod::Time now = rosmod::Time::now();
  while ( this->comp_sync_sub.getNumPublishers() < this->num_comps_to_sync &&
	  (rosmod::Time::now() - now) < rosmod::Duration(comp_sync_timeout) );
  this->comp_sync_sub.shutdown();
  this->comp_sync_pub.shutdown();

  this->initOneShotTimer.start();
  this->Timer_1.start();
  
  compQueue.ROSMOD_LOGGER.CREATE_FILE(pwd + "ROSMOD_DEBUG." + nodeName + "." + compName + ".log");
}

extern "C" {
  Component *maker(ComponentConfig &config, int argc, char **argv) {
    return new Component_1(config,argc,argv);
  }
}
