#include "timer_package/Timer.hpp"

//# Start User Globals Marker
//# End User Globals Marker

// Initialization Function
//# Start Init Marker
void Timer::Init(const ros::TimerEvent& event)
{
  // Initialize Here

  // Stop Init Timer
  initOneShotTimer.stop();
}
//# End Init Marker

// Timer Callback - periodic_timer
//# Start periodic_timerCallback Marker
void Timer::periodic_timerCallback(const ros::TimerEvent& event)
{
  // Business Logic for periodic_timer Timer
  LOGGER.INFO("Timer::Periodic Timer triggered!");
}
//# End periodic_timerCallback Marker
// Timer Callback - sporadic_timer
//# Start sporadic_timerCallback Marker
void Timer::sporadic_timerCallback(const ros::TimerEvent& event)
{
  // Business Logic for sporadic_timer Timer
  LOGGER.INFO("Timer::Sporadic Timer triggered!");
}
//# End sporadic_timerCallback Marker


// Destructor - Cleanup Ports & Timers
Timer::~Timer()
{
  periodic_timer.stop();
  sporadic_timer.stop();
  //# Start Destructor Marker
  //# End Destructor Marker
}

// Startup - Setup Component Ports & Timers
void Timer::startUp()
{
  ros::NodeHandle nh;
  std::string advertiseName;

  // Init Timer
  ros::TimerOptions timer_options;
  timer_options = 
    ros::TimerOptions
    (ros::Duration(-1),
     boost::bind(&Timer::Init, this, _1),
     &this->compQueue,
     true);
  this->initOneShotTimer = nh.createTimer(timer_options);  
  
  // Component Timer - periodic_timer
  timer_options = 
    ros::TimerOptions
    (ros::Duration(1.0),
     boost::bind(&Timer::periodic_timerCallback, this, _1),
     &this->compQueue);
  this->periodic_timer = nh.createTimer(timer_options);
  // Component Timer - sporadic_timer
  timer_options = 
    ros::TimerOptions
    (ros::Duration(-1),
     boost::bind(&Timer::sporadic_timerCallback, this, _1),
     &this->compQueue, true);
  this->sporadic_timer = nh.createTimer(timer_options);

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
}

extern "C" {
  Component *maker(ComponentConfig &config, int argc, char **argv) {
    return new Timer(config,argc,argv);
  }
}
