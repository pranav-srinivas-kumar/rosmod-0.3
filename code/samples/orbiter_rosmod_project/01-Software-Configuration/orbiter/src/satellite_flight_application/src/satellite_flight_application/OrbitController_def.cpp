#include "satellite_flight_application/OrbitController_def.hpp"

//# Start User Globals Marker

//# End User Globals Marker

// -------------------------------------------------------
// BUSINESS LOGIC OF THESE FUNCTIONS SUPPLIED BY DEVELOPER
// -------------------------------------------------------

// Init Function
//# Start Init Marker
void OrbitController_def::Init(const ros::TimerEvent& event)
{
    // Initialize Component

    // Stop Init Timer
    initOneShotTimer.stop();
}
//# End Init Marker

// OnOneData Subscription handler for targetOrbitSub subscriber
//# Start targetOrbitSub_OnOneData Marker
void OrbitController_def::targetOrbitSub_OnOneData(const cluster_flight_application::TargetOrbit::ConstPtr& received_data)
{
    // Business Logic for targetOrbitSub subscriber subscribing to topic TargetOrbit callback 
  ROS_INFO("I got a new target orbit!");
  ROS_INFO("Activating satellite %s thrusters to achieve new orbit", hostName.c_str());

  satellite_flight_application::ThrusterComm srv;
  srv.request.amount = 1.0;
  srv.request.duration = 1.0;
  if (ThrusterComm_client.call(srv))
    {
      ROS_INFO("Successfully activated satellite thrusters");
    }
  else
    {
      ROS_ERROR("Failed to activate satellite thrusters");
      ThrusterComm_client.waitForExistence(ros::Duration(-1));
    }
}
//# End targetOrbitSub_OnOneData Marker

// Callback for Timer0 timer
//# Start Timer0Callback Marker
void OrbitController_def::Timer0Callback(const ros::TimerEvent& event)
{
    // Business Logic for Timer0 

      satellite_flight_application::SatelliteState srv;
      if (SatelliteState_client.call(srv))
	{
	  ROS_INFO("Got state vector from satellite %s bus", hostName.c_str());
	}
      else
	{
	  ROS_ERROR("Failed to get satellite state vector for satellite %s.", hostName.c_str());
	  SatelliteState_client.waitForExistence(ros::Duration(-1));
	}

      satellite_flight_application::SatState satState;
      satState.sat_id = hostName;
      satStatePub.publish(satState);
}
//# End Timer0Callback Marker

// ---------------------------------------------
// EVERYTHING BELOW HERE IS COMPLETELY GENERATED
// ---------------------------------------------

// Destructor - required for clean shutdown when process is killed
OrbitController_def::~OrbitController_def()
{
    Timer0.stop();
    satStatePub.shutdown();
    targetOrbitSub.shutdown();
    SatelliteState_client.shutdown();
    ThrusterComm_client.shutdown();
//# Start Destructor Marker

//# End Destructor Marker
}

void OrbitController_def::startUp()
{
    ros::NodeHandle nh;

    // Need to read in and parse the group configuration xml if it exists
    GroupXMLParser groupParser;
    std::map<std::string,std::string> *portGroupMap = NULL;
    std::string configFileName = nodeName + "." + compName + ".xml";
    if (groupParser.Parse(configFileName))
    {
	portGroupMap = &groupParser.portGroupMap;
    }

    std::string advertiseName;

    // Configure all subscribers associated with this component
    // subscriber: targetOrbitSub
    advertiseName = "TargetOrbit";
    if ( portGroupMap != NULL && portGroupMap->find(advertiseName) != portGroupMap->end() )
        advertiseName += "_" + (*portGroupMap)[advertiseName];
    ros::SubscribeOptions targetOrbitSub_options;
    targetOrbitSub_options = 
	ros::SubscribeOptions::create<cluster_flight_application::TargetOrbit>
	    (advertiseName.c_str(),
	     1000,
	     boost::bind(&OrbitController_def::targetOrbitSub_OnOneData, this, _1),
	     ros::VoidPtr(),
             &this->compQueue);
    this->targetOrbitSub = nh.subscribe(targetOrbitSub_options);

    // Configure all publishers associated with this component
    // publisher: satStatePub
    advertiseName = "SatState";
    if ( portGroupMap != NULL && portGroupMap->find(advertiseName) != portGroupMap->end() )
        advertiseName += "_" + (*portGroupMap)[advertiseName];
    this->satStatePub = nh.advertise<satellite_flight_application::SatState>
	(advertiseName.c_str(), 1000);	

    // Configure all required services associated with this component
    // client: SatelliteState_client
    advertiseName = "SatelliteState";
    if ( portGroupMap != NULL && portGroupMap->find(advertiseName) != portGroupMap->end() )
        advertiseName += "_" + (*portGroupMap)[advertiseName];
    this->SatelliteState_client = nh.serviceClient<satellite_flight_application::SatelliteState>
	(advertiseName.c_str()); 
    // client: ThrusterComm_client
    advertiseName = "ThrusterComm";
    if ( portGroupMap != NULL && portGroupMap->find(advertiseName) != portGroupMap->end() )
        advertiseName += "_" + (*portGroupMap)[advertiseName];
    this->ThrusterComm_client = nh.serviceClient<satellite_flight_application::ThrusterComm>
	(advertiseName.c_str()); 

    // Create Init Timer
    ros::TimerOptions timer_options;
    timer_options = 
	ros::TimerOptions
	    (ros::Duration(-1),
	     boost::bind(&OrbitController_def::Init, this, _1),
	     &this->compQueue,
             true);
    this->initOneShotTimer = nh.createTimer(timer_options);  
  
    // Create all component timers
    // timer: timer.properties["name"]
    timer_options = 
	ros::TimerOptions
             (ros::Duration(1.0),
	     boost::bind(&OrbitController_def::Timer0Callback, this, _1),
	     &this->compQueue);
    this->Timer0 = nh.createTimer(timer_options);

}
