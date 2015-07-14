#include "client_server_package/Server.hpp"

//# Start User Globals Marker
#include <math.h>
//# End User Globals Marker

// Initialization Function
//# Start Init Marker
void Server::Init(const rosmod::TimerEvent& event)
{
  compQueue.ROSMOD_LOGGER.DEBUG("Entering sporadic_timerCallback");
  // Initialize Here

  // Stop Init Timer
  initOneShotTimer.stop();
  compQueue.ROSMOD_LOGGER.DEBUG("Exiting sporadic_timerCallback");
}
//# End Init Marker

// Server Callback - server_port
//# Start PowerCallback Marker
bool Server::PowerCallback(client_server_package::Power::Request  &req,
  client_server_package::Power::Response &res)
{
  compQueue.ROSMOD_LOGGER.DEBUG("Entering PowerCallback");
  // Business Logic for server_port Server
  res.result = pow(req.base, req.exponent);
  compQueue.ROSMOD_LOGGER.DEBUG("Exiting PowerCallback");
  return true;
}
//# End PowerCallback Marker


// Destructor - Cleanup Ports & Timers
Server::~Server()
{
  server_port.shutdown();
  //# Start Destructor Marker
  //# End Destructor Marker
}

// Startup - Setup Component Ports & Timers
void Server::startUp()
{
  rosmod::NodeHandle nh;
  std::string advertiseName;

  // Scheduling Scheme is FIFO
  this->compQueue.scheduling_scheme = rosmod::CallbackQueue::SchedulingScheme::FIFO;
    
  rosmod::ROSMOD_Callback_Options callback_options;
  callback_options.alias = "PowerCallback";
  callback_options.priority = 50;
  callback_options.deadline.sec = 0.0;
  callback_options.deadline.nsec = 40000;

  // Component Server - server_port
  advertiseName = "Power";
  if (portGroupMap.find("server_port") != portGroupMap.end())
    advertiseName += "_" + portGroupMap["server_port"];
  rosmod::AdvertiseServiceOptions server_port_server_options;
  server_port_server_options =
    rosmod::AdvertiseServiceOptions::create<client_server_package::Power>
      (advertiseName.c_str(),
       boost::bind(&Server::PowerCallback, this, _1, _2),
       rosmod::VoidPtr(),
       &this->compQueue,
       callback_options);
  this->server_port = nh.advertiseService(server_port_server_options);

  callback_options.alias = "Init_Timer";
 
  // Init Timer
  rosmod::TimerOptions timer_options;
  timer_options = 
    rosmod::TimerOptions
    (ros::Duration(-1),
     boost::bind(&Server::Init, this, _1),
     &this->compQueue,
     callback_options,
     true,
     true);
  this->initOneShotTimer = nh.createTimer(timer_options);  
  
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

  compQueue.ROSMOD_LOGGER.CREATE_FILE(pwd + "ROSMOD_DEBUG."
				      + nodeName + "." + compName + ".log");  
}

extern "C" {
  Component *maker(ComponentConfig &config, int argc, char **argv) {
    return new Server(config,argc,argv);
  }
}
