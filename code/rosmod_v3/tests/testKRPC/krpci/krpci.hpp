#include <iostream>
#include <fstream>
#include <string>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include "KRPC.pb.h"
#include <google/protobuf/io/zero_copy_stream.h>
#include <google/protobuf/io/zero_copy_stream_impl.h>
#include <google/protobuf/io/coded_stream.h>
using namespace google::protobuf::io;
#include <boost/thread.hpp>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>
#include <errno.h>
#include <netinet/in.h>
#include <ifaddrs.h>

const int maxBufferSize = 65535;
const char helloMessage[] = { 0x48, 0x45, 0x4C, 0x4C, 0x4F, 0x2D, 0x52, 0x50, 0x43, 0x00, 0x00, 0x00 };
const char helloStreamMessage[] = { 0x48, 0x45, 0x4C, 0x4C, 0x4F, 0x2D, 0x53, 0x54, 0x52, 0x45, 0x41, 0x4D };
const char streamAck[] = { 0x4F, 0x4B };

class KRPCI
{
public:
  KRPCI(std::string name, std::string ip="127.0.0.1", int port=50000, int streamPort=50001);
  ~KRPCI();

  bool Connect();
  bool Close();

  bool CreateStream(std::string streamName, krpc::Request req);
  bool GetLatestStreamData(std::string streamName, krpc::Response& res);
  bool ClearTarget();
  bool WarpTo(double UT, float maxRate);
  bool TransformPosition(double position_x, double position_y, double position_z, uint64_t from, uint64_t to, double& x, double& y, double& z);
  bool TransformDirection(double direction_x, double direction_y, double direction_z, uint64_t from, uint64_t to, double& x, double& y, double& z);
  bool TransformRotation(double rotation_x, double rotation_y, double rotation_z, uint64_t from, uint64_t to, double& x, double& y, double& z);
  bool TransformVelocity(double position_x, double position_y, double position_z, double velocity_x, double velocity_y, double velocity_z, uint64_t from, uint64_t to, double& x, double& y, double& z);
  bool DrawDirection(double direction_x, double direction_y, double direction_z, uint64_t referenceFrame, double color_x, double color_y, double color_z, float length);
  bool ClearDirections();
  bool get_ActiveVessel(uint64_t& return_value);
  bool get_Vessels(std::vector<uint64_t>& return_vector);
  bool get_Bodies(krpc::Dictionary& return_dict);
  bool get_TargetBody(uint64_t& return_value);
  bool set_TargetBody(uint64_t value);
  bool get_TargetVessel(uint64_t& return_value);
  bool set_TargetVessel(uint64_t value);
  bool get_TargetDockingPort(uint64_t& return_value);
  bool set_TargetDockingPort(uint64_t value);
  bool get_UT(double& return_value);
  bool get_G(float& return_value);
  bool get_FARAvailable(bool& return_value);
  bool get_RemoteTechAvailable(bool& return_value);
  bool AutoPilot_SetRotation(uint64_t AutoPilot_ID, float pitch, float heading, float roll, uint64_t referenceFrame, bool wait);
  bool AutoPilot_SetDirection(uint64_t AutoPilot_ID, double direction_x, double direction_y, double direction_z, float roll, uint64_t referenceFrame, bool wait);
  bool AutoPilot_Disengage(uint64_t AutoPilot_ID);
  bool AutoPilot_get_SAS(uint64_t AutoPilot_ID, bool& return_value);
  bool AutoPilot_set_SAS(uint64_t AutoPilot_ID, bool value);
  bool AutoPilot_get_SASMode(uint64_t AutoPilot_ID, int32_t& return_value);
  bool AutoPilot_set_SASMode(uint64_t AutoPilot_ID, int32_t value);
  bool AutoPilot_get_SpeedMode(uint64_t AutoPilot_ID, int32_t& return_value);
  bool AutoPilot_set_SpeedMode(uint64_t AutoPilot_ID, int32_t value);
  bool AutoPilot_get_Error(uint64_t AutoPilot_ID, float& return_value);
  bool AutoPilot_get_RollError(uint64_t AutoPilot_ID, float& return_value);
  bool CelestialBody_Position(uint64_t CelestialBody_ID, uint64_t referenceFrame, double& x, double& y, double& z);
  bool CelestialBody_Velocity(uint64_t CelestialBody_ID, uint64_t referenceFrame, double& x, double& y, double& z);
  bool CelestialBody_Rotation(uint64_t CelestialBody_ID, uint64_t referenceFrame, double& x, double& y, double& z);
  bool CelestialBody_Direction(uint64_t CelestialBody_ID, uint64_t referenceFrame, double& x, double& y, double& z);
  bool CelestialBody_AngularVelocity(uint64_t CelestialBody_ID, uint64_t referenceFrame, double& x, double& y, double& z);
  bool CelestialBody_get_Name(uint64_t CelestialBody_ID, std::string& return_value);
  bool CelestialBody_get_Satellites(uint64_t CelestialBody_ID, std::vector<uint64_t>& return_vector);
  bool CelestialBody_get_Mass(uint64_t CelestialBody_ID, float& return_value);
  bool CelestialBody_get_GravitationalParameter(uint64_t CelestialBody_ID, float& return_value);
  bool CelestialBody_get_SurfaceGravity(uint64_t CelestialBody_ID, float& return_value);
  bool CelestialBody_get_RotationalPeriod(uint64_t CelestialBody_ID, float& return_value);
  bool CelestialBody_get_RotationalSpeed(uint64_t CelestialBody_ID, float& return_value);
  bool CelestialBody_get_EquatorialRadius(uint64_t CelestialBody_ID, float& return_value);
  bool CelestialBody_get_SphereOfInfluence(uint64_t CelestialBody_ID, float& return_value);
  bool CelestialBody_get_Orbit(uint64_t CelestialBody_ID, uint64_t& return_value);
  bool CelestialBody_get_HasAtmosphere(uint64_t CelestialBody_ID, bool& return_value);
  bool CelestialBody_get_AtmosphereDepth(uint64_t CelestialBody_ID, float& return_value);
  bool CelestialBody_get_HasAtmosphericOxygen(uint64_t CelestialBody_ID, bool& return_value);
  bool CelestialBody_get_ReferenceFrame(uint64_t CelestialBody_ID, uint64_t& return_value);
  bool CelestialBody_get_NonRotatingReferenceFrame(uint64_t CelestialBody_ID, uint64_t& return_value);
  bool CelestialBody_get_OrbitalReferenceFrame(uint64_t CelestialBody_ID, uint64_t& return_value);
  bool Comms_SignalDelayToVessel(uint64_t Comms_ID, uint64_t other, double& return_value);
  bool Comms_get_HasFlightComputer(uint64_t Comms_ID, bool& return_value);
  bool Comms_get_HasConnection(uint64_t Comms_ID, bool& return_value);
  bool Comms_get_HasConnectionToGroundStation(uint64_t Comms_ID, bool& return_value);
  bool Comms_get_SignalDelay(uint64_t Comms_ID, double& return_value);
  bool Comms_get_SignalDelayToGroundStation(uint64_t Comms_ID, double& return_value);
  bool Control_ActivateNextStage(uint64_t Control_ID, std::vector<uint64_t>& return_vector);
  bool Control_GetActionGroup(uint64_t Control_ID, uint32_t group, bool& return_value);
  bool Control_SetActionGroup(uint64_t Control_ID, uint32_t group, bool state);
  bool Control_ToggleActionGroup(uint64_t Control_ID, uint32_t group);
  bool Control_AddNode(uint64_t Control_ID, double UT, float prograde, float normal, float radial, uint64_t& return_value);
  bool Control_RemoveNodes(uint64_t Control_ID);
  bool Control_get_SAS(uint64_t Control_ID, bool& return_value);
  bool Control_set_SAS(uint64_t Control_ID, bool value);
  bool Control_get_RCS(uint64_t Control_ID, bool& return_value);
  bool Control_set_RCS(uint64_t Control_ID, bool value);
  bool Control_get_Gear(uint64_t Control_ID, bool& return_value);
  bool Control_set_Gear(uint64_t Control_ID, bool value);
  bool Control_get_Lights(uint64_t Control_ID, bool& return_value);
  bool Control_set_Lights(uint64_t Control_ID, bool value);
  bool Control_get_Brakes(uint64_t Control_ID, bool& return_value);
  bool Control_set_Brakes(uint64_t Control_ID, bool value);
  bool Control_get_Abort(uint64_t Control_ID, bool& return_value);
  bool Control_set_Abort(uint64_t Control_ID, bool value);
  bool Control_get_Throttle(uint64_t Control_ID, float& return_value);
  bool Control_set_Throttle(uint64_t Control_ID, float value);
  bool Control_get_Pitch(uint64_t Control_ID, float& return_value);
  bool Control_set_Pitch(uint64_t Control_ID, float value);
  bool Control_get_Yaw(uint64_t Control_ID, float& return_value);
  bool Control_set_Yaw(uint64_t Control_ID, float value);
  bool Control_get_Roll(uint64_t Control_ID, float& return_value);
  bool Control_set_Roll(uint64_t Control_ID, float value);
  bool Control_get_Forward(uint64_t Control_ID, float& return_value);
  bool Control_set_Forward(uint64_t Control_ID, float value);
  bool Control_get_Up(uint64_t Control_ID, float& return_value);
  bool Control_set_Up(uint64_t Control_ID, float value);
  bool Control_get_Right(uint64_t Control_ID, float& return_value);
  bool Control_set_Right(uint64_t Control_ID, float value);
  bool Control_get_WheelThrottle(uint64_t Control_ID, float& return_value);
  bool Control_set_WheelThrottle(uint64_t Control_ID, float value);
  bool Control_get_WheelSteering(uint64_t Control_ID, float& return_value);
  bool Control_set_WheelSteering(uint64_t Control_ID, float value);
  bool Control_get_CurrentStage(uint64_t Control_ID, int32_t& return_value);
  bool Control_get_Nodes(uint64_t Control_ID, std::vector<uint64_t>& return_vector);
  bool Flight_get_GForce(uint64_t Flight_ID, float& return_value);
  bool Flight_get_MeanAltitude(uint64_t Flight_ID, double& return_value);
  bool Flight_get_SurfaceAltitude(uint64_t Flight_ID, double& return_value);
  bool Flight_get_BedrockAltitude(uint64_t Flight_ID, double& return_value);
  bool Flight_get_Elevation(uint64_t Flight_ID, double& return_value);
  bool Flight_get_Latitude(uint64_t Flight_ID, double& return_value);
  bool Flight_get_Longitude(uint64_t Flight_ID, double& return_value);
  bool Flight_get_Velocity(uint64_t Flight_ID, double& x, double& y, double& z);
  bool Flight_get_Speed(uint64_t Flight_ID, double& return_value);
  bool Flight_get_HorizontalSpeed(uint64_t Flight_ID, double& return_value);
  bool Flight_get_VerticalSpeed(uint64_t Flight_ID, double& return_value);
  bool Flight_get_CenterOfMass(uint64_t Flight_ID, double& x, double& y, double& z);
  bool Flight_get_Rotation(uint64_t Flight_ID, double& x, double& y, double& z);
  bool Flight_get_Direction(uint64_t Flight_ID, double& x, double& y, double& z);
  bool Flight_get_Pitch(uint64_t Flight_ID, float& return_value);
  bool Flight_get_Heading(uint64_t Flight_ID, float& return_value);
  bool Flight_get_Roll(uint64_t Flight_ID, float& return_value);
  bool Flight_get_Prograde(uint64_t Flight_ID, double& x, double& y, double& z);
  bool Flight_get_Retrograde(uint64_t Flight_ID, double& x, double& y, double& z);
  bool Flight_get_Normal(uint64_t Flight_ID, double& x, double& y, double& z);
  bool Flight_get_AntiNormal(uint64_t Flight_ID, double& x, double& y, double& z);
  bool Flight_get_Radial(uint64_t Flight_ID, double& x, double& y, double& z);
  bool Flight_get_AntiRadial(uint64_t Flight_ID, double& x, double& y, double& z);
  bool Flight_get_AtmosphereDensity(uint64_t Flight_ID, float& return_value);
  bool Flight_get_DynamicPressure(uint64_t Flight_ID, float& return_value);
  bool Flight_get_StaticPressure(uint64_t Flight_ID, float& return_value);
  bool Flight_get_AerodynamicForce(uint64_t Flight_ID, double& x, double& y, double& z);
  bool Flight_get_Lift(uint64_t Flight_ID, double& x, double& y, double& z);
  bool Flight_get_Drag(uint64_t Flight_ID, double& x, double& y, double& z);
  bool Flight_get_SpeedOfSound(uint64_t Flight_ID, float& return_value);
  bool Flight_get_Mach(uint64_t Flight_ID, float& return_value);
  bool Flight_get_EquivalentAirSpeed(uint64_t Flight_ID, float& return_value);
  bool Flight_get_TerminalVelocity(uint64_t Flight_ID, float& return_value);
  bool Flight_get_AngleOfAttack(uint64_t Flight_ID, float& return_value);
  bool Flight_get_SideslipAngle(uint64_t Flight_ID, float& return_value);
  bool Flight_get_TotalAirTemperature(uint64_t Flight_ID, float& return_value);
  bool Flight_get_StaticAirTemperature(uint64_t Flight_ID, float& return_value);
  bool Flight_get_StallFraction(uint64_t Flight_ID, float& return_value);
  bool Flight_get_DragCoefficient(uint64_t Flight_ID, float& return_value);
  bool Flight_get_LiftCoefficient(uint64_t Flight_ID, float& return_value);
  bool Flight_get_PitchingMomentCoefficient(uint64_t Flight_ID, float& return_value);
  bool Flight_get_BallisticCoefficient(uint64_t Flight_ID, float& return_value);
  bool Flight_get_ThrustSpecificFuelConsumption(uint64_t Flight_ID, float& return_value);
  bool Flight_get_FARStatus(uint64_t Flight_ID, std::string& return_value);
  bool Node_BurnVector(uint64_t Node_ID, uint64_t referenceFrame, double& x, double& y, double& z);
  bool Node_RemainingBurnVector(uint64_t Node_ID, uint64_t referenceFrame, double& x, double& y, double& z);
  bool Node_Remove(uint64_t Node_ID);
  bool Node_Position(uint64_t Node_ID, uint64_t referenceFrame, double& x, double& y, double& z);
  bool Node_Direction(uint64_t Node_ID, uint64_t referenceFrame, double& x, double& y, double& z);
  bool Node_get_Prograde(uint64_t Node_ID, float& return_value);
  bool Node_set_Prograde(uint64_t Node_ID, float value);
  bool Node_get_Normal(uint64_t Node_ID, float& return_value);
  bool Node_set_Normal(uint64_t Node_ID, float value);
  bool Node_get_Radial(uint64_t Node_ID, float& return_value);
  bool Node_set_Radial(uint64_t Node_ID, float value);
  bool Node_get_DeltaV(uint64_t Node_ID, float& return_value);
  bool Node_set_DeltaV(uint64_t Node_ID, float value);
  bool Node_get_RemainingDeltaV(uint64_t Node_ID, float& return_value);
  bool Node_get_UT(uint64_t Node_ID, double& return_value);
  bool Node_set_UT(uint64_t Node_ID, double value);
  bool Node_get_TimeTo(uint64_t Node_ID, double& return_value);
  bool Node_get_Orbit(uint64_t Node_ID, uint64_t& return_value);
  bool Node_get_ReferenceFrame(uint64_t Node_ID, uint64_t& return_value);
  bool Node_get_OrbitalReferenceFrame(uint64_t Node_ID, uint64_t& return_value);
  bool Orbit_ReferencePlaneNormal(uint64_t referenceFrame, double& x, double& y, double& z);
  bool Orbit_ReferencePlaneDirection(uint64_t referenceFrame, double& x, double& y, double& z);
  bool Orbit_get_Body(uint64_t Orbit_ID, uint64_t& return_value);
  bool Orbit_get_Apoapsis(uint64_t Orbit_ID, double& return_value);
  bool Orbit_get_Periapsis(uint64_t Orbit_ID, double& return_value);
  bool Orbit_get_ApoapsisAltitude(uint64_t Orbit_ID, double& return_value);
  bool Orbit_get_PeriapsisAltitude(uint64_t Orbit_ID, double& return_value);
  bool Orbit_get_SemiMajorAxis(uint64_t Orbit_ID, double& return_value);
  bool Orbit_get_SemiMinorAxis(uint64_t Orbit_ID, double& return_value);
  bool Orbit_get_Radius(uint64_t Orbit_ID, double& return_value);
  bool Orbit_get_Speed(uint64_t Orbit_ID, double& return_value);
  bool Orbit_get_Period(uint64_t Orbit_ID, double& return_value);
  bool Orbit_get_TimeToApoapsis(uint64_t Orbit_ID, double& return_value);
  bool Orbit_get_TimeToPeriapsis(uint64_t Orbit_ID, double& return_value);
  bool Orbit_get_Eccentricity(uint64_t Orbit_ID, double& return_value);
  bool Orbit_get_Inclination(uint64_t Orbit_ID, double& return_value);
  bool Orbit_get_LongitudeOfAscendingNode(uint64_t Orbit_ID, double& return_value);
  bool Orbit_get_ArgumentOfPeriapsis(uint64_t Orbit_ID, double& return_value);
  bool Orbit_get_MeanAnomalyAtEpoch(uint64_t Orbit_ID, double& return_value);
  bool Orbit_get_Epoch(uint64_t Orbit_ID, double& return_value);
  bool Orbit_get_MeanAnomaly(uint64_t Orbit_ID, double& return_value);
  bool Orbit_get_EccentricAnomaly(uint64_t Orbit_ID, double& return_value);
  bool Orbit_get_NextOrbit(uint64_t Orbit_ID, uint64_t& return_value);
  bool Orbit_get_TimeToSOIChange(uint64_t Orbit_ID, double& return_value);
  bool Decoupler_Decouple(uint64_t Decoupler_ID);
  bool Decoupler_get_Part(uint64_t Decoupler_ID, uint64_t& return_value);
  bool Decoupler_get_Decoupled(uint64_t Decoupler_ID, bool& return_value);
  bool Decoupler_get_Impulse(uint64_t Decoupler_ID, float& return_value);
  bool DockingPort_Undock(uint64_t DockingPort_ID, uint64_t& return_value);
  bool DockingPort_Position(uint64_t DockingPort_ID, uint64_t referenceFrame, double& x, double& y, double& z);
  bool DockingPort_Direction(uint64_t DockingPort_ID, uint64_t referenceFrame, double& x, double& y, double& z);
  bool DockingPort_Rotation(uint64_t DockingPort_ID, uint64_t referenceFrame, double& x, double& y, double& z);
  bool DockingPort_get_Part(uint64_t DockingPort_ID, uint64_t& return_value);
  bool DockingPort_get_Name(uint64_t DockingPort_ID, std::string& return_value);
  bool DockingPort_set_Name(uint64_t DockingPort_ID, std::string value);
  bool DockingPort_get_State(uint64_t DockingPort_ID, int32_t& return_value);
  bool DockingPort_get_DockedPart(uint64_t DockingPort_ID, uint64_t& return_value);
  bool DockingPort_get_ReengageDistance(uint64_t DockingPort_ID, float& return_value);
  bool DockingPort_get_HasShield(uint64_t DockingPort_ID, bool& return_value);
  bool DockingPort_get_Shielded(uint64_t DockingPort_ID, bool& return_value);
  bool DockingPort_set_Shielded(uint64_t DockingPort_ID, bool value);
  bool DockingPort_get_ReferenceFrame(uint64_t DockingPort_ID, uint64_t& return_value);
  bool Engine_get_Part(uint64_t Engine_ID, uint64_t& return_value);
  bool Engine_get_Active(uint64_t Engine_ID, bool& return_value);
  bool Engine_set_Active(uint64_t Engine_ID, bool value);
  bool Engine_get_Thrust(uint64_t Engine_ID, float& return_value);
  bool Engine_get_AvailableThrust(uint64_t Engine_ID, float& return_value);
  bool Engine_get_MaxThrust(uint64_t Engine_ID, float& return_value);
  bool Engine_get_MaxVacuumThrust(uint64_t Engine_ID, float& return_value);
  bool Engine_get_ThrustLimit(uint64_t Engine_ID, float& return_value);
  bool Engine_set_ThrustLimit(uint64_t Engine_ID, float value);
  bool Engine_get_SpecificImpulse(uint64_t Engine_ID, float& return_value);
  bool Engine_get_VacuumSpecificImpulse(uint64_t Engine_ID, float& return_value);
  bool Engine_get_KerbinSeaLevelSpecificImpulse(uint64_t Engine_ID, float& return_value);
  bool Engine_get_Propellants(uint64_t Engine_ID, std::vector<uint64_t>& return_vector);
  bool Engine_get_HasFuel(uint64_t Engine_ID, bool& return_value);
  bool Engine_get_Throttle(uint64_t Engine_ID, float& return_value);
  bool Engine_get_ThrottleLocked(uint64_t Engine_ID, bool& return_value);
  bool Engine_get_CanRestart(uint64_t Engine_ID, bool& return_value);
  bool Engine_get_CanShutdown(uint64_t Engine_ID, bool& return_value);
  bool Engine_get_Gimballed(uint64_t Engine_ID, bool& return_value);
  bool Engine_get_GimbalRange(uint64_t Engine_ID, float& return_value);
  bool Engine_get_GimbalLocked(uint64_t Engine_ID, bool& return_value);
  bool Engine_set_GimbalLocked(uint64_t Engine_ID, bool value);
  bool Engine_get_GimbalLimit(uint64_t Engine_ID, float& return_value);
  bool Engine_set_GimbalLimit(uint64_t Engine_ID, float value);
  bool LandingGear_get_Part(uint64_t LandingGear_ID, uint64_t& return_value);
  bool LandingGear_get_State(uint64_t LandingGear_ID, int32_t& return_value);
  bool LandingGear_get_Deployed(uint64_t LandingGear_ID, bool& return_value);
  bool LandingGear_set_Deployed(uint64_t LandingGear_ID, bool value);
  bool LandingLeg_get_Part(uint64_t LandingLeg_ID, uint64_t& return_value);
  bool LandingLeg_get_State(uint64_t LandingLeg_ID, int32_t& return_value);
  bool LandingLeg_get_Deployed(uint64_t LandingLeg_ID, bool& return_value);
  bool LandingLeg_set_Deployed(uint64_t LandingLeg_ID, bool value);
  bool LaunchClamp_Release(uint64_t LaunchClamp_ID);
  bool LaunchClamp_get_Part(uint64_t LaunchClamp_ID, uint64_t& return_value);
  bool Light_get_Part(uint64_t Light_ID, uint64_t& return_value);
  bool Light_get_Active(uint64_t Light_ID, bool& return_value);
  bool Light_set_Active(uint64_t Light_ID, bool value);
  bool Light_get_PowerUsage(uint64_t Light_ID, float& return_value);
  bool Module_HasField(uint64_t Module_ID, std::string name, bool& return_value);
  bool Module_GetField(uint64_t Module_ID, std::string name, std::string& return_value);
  bool Module_HasEvent(uint64_t Module_ID, std::string name, bool& return_value);
  bool Module_TriggerEvent(uint64_t Module_ID, std::string name);
  bool Module_HasAction(uint64_t Module_ID, std::string name, bool& return_value);
  bool Module_SetAction(uint64_t Module_ID, std::string name, bool value);
  bool Module_get_Name(uint64_t Module_ID, std::string& return_value);
  bool Module_get_Part(uint64_t Module_ID, uint64_t& return_value);
  bool Module_get_Fields(uint64_t Module_ID, krpc::Dictionary& return_dict);
  bool Module_get_Events(uint64_t Module_ID, std::vector<uint64_t>& return_vector);
  bool Module_get_Actions(uint64_t Module_ID, std::vector<uint64_t>& return_vector);
  bool Parachute_Deploy(uint64_t Parachute_ID);
  bool Parachute_get_Part(uint64_t Parachute_ID, uint64_t& return_value);
  bool Parachute_get_Deployed(uint64_t Parachute_ID, bool& return_value);
  bool Parachute_get_State(uint64_t Parachute_ID, int32_t& return_value);
  bool Parachute_get_DeployAltitude(uint64_t Parachute_ID, float& return_value);
  bool Parachute_set_DeployAltitude(uint64_t Parachute_ID, float value);
  bool Parachute_get_DeployMinPressure(uint64_t Parachute_ID, float& return_value);
  bool Parachute_set_DeployMinPressure(uint64_t Parachute_ID, float value);
  bool Part_Position(uint64_t Part_ID, uint64_t referenceFrame, double& x, double& y, double& z);
  bool Part_Direction(uint64_t Part_ID, uint64_t referenceFrame, double& x, double& y, double& z);
  bool Part_Velocity(uint64_t Part_ID, uint64_t referenceFrame, double& x, double& y, double& z);
  bool Part_Rotation(uint64_t Part_ID, uint64_t referenceFrame, double& x, double& y, double& z);
  bool Part_get_Name(uint64_t Part_ID, std::string& return_value);
  bool Part_get_Title(uint64_t Part_ID, std::string& return_value);
  bool Part_get_Cost(uint64_t Part_ID, double& return_value);
  bool Part_get_Vessel(uint64_t Part_ID, uint64_t& return_value);
  bool Part_get_Parent(uint64_t Part_ID, uint64_t& return_value);
  bool Part_get_Children(uint64_t Part_ID, std::vector<uint64_t>& return_vector);
  bool Part_get_AxiallyAttached(uint64_t Part_ID, bool& return_value);
  bool Part_get_RadiallyAttached(uint64_t Part_ID, bool& return_value);
  bool Part_get_Stage(uint64_t Part_ID, int32_t& return_value);
  bool Part_get_DecoupleStage(uint64_t Part_ID, int32_t& return_value);
  bool Part_get_Massless(uint64_t Part_ID, bool& return_value);
  bool Part_get_Mass(uint64_t Part_ID, double& return_value);
  bool Part_get_DryMass(uint64_t Part_ID, double& return_value);
  bool Part_get_ImpactTolerance(uint64_t Part_ID, double& return_value);
  bool Part_get_Temperature(uint64_t Part_ID, double& return_value);
  bool Part_get_MaxTemperature(uint64_t Part_ID, double& return_value);
  bool Part_get_Resources(uint64_t Part_ID, uint64_t& return_value);
  bool Part_get_Crossfeed(uint64_t Part_ID, bool& return_value);
  bool Part_get_FuelLinesFrom(uint64_t Part_ID, std::vector<uint64_t>& return_vector);
  bool Part_get_FuelLinesTo(uint64_t Part_ID, std::vector<uint64_t>& return_vector);
  bool Part_get_Modules(uint64_t Part_ID, std::vector<uint64_t>& return_vector);
  bool Part_get_Decoupler(uint64_t Part_ID, uint64_t& return_value);
  bool Part_get_DockingPort(uint64_t Part_ID, uint64_t& return_value);
  bool Part_get_Engine(uint64_t Part_ID, uint64_t& return_value);
  bool Part_get_LandingGear(uint64_t Part_ID, uint64_t& return_value);
  bool Part_get_LandingLeg(uint64_t Part_ID, uint64_t& return_value);
  bool Part_get_LaunchClamp(uint64_t Part_ID, uint64_t& return_value);
  bool Part_get_Light(uint64_t Part_ID, uint64_t& return_value);
  bool Part_get_Parachute(uint64_t Part_ID, uint64_t& return_value);
  bool Part_get_ReactionWheel(uint64_t Part_ID, uint64_t& return_value);
  bool Part_get_Sensor(uint64_t Part_ID, uint64_t& return_value);
  bool Part_get_SolarPanel(uint64_t Part_ID, uint64_t& return_value);
  bool Part_get_ReferenceFrame(uint64_t Part_ID, uint64_t& return_value);
  bool Parts_WithName(uint64_t Parts_ID, std::string name, std::vector<uint64_t>& return_vector);
  bool Parts_WithTitle(uint64_t Parts_ID, std::string title, std::vector<uint64_t>& return_vector);
  bool Parts_WithModule(uint64_t Parts_ID, std::string moduleName, std::vector<uint64_t>& return_vector);
  bool Parts_InStage(uint64_t Parts_ID, int32_t stage, std::vector<uint64_t>& return_vector);
  bool Parts_InDecoupleStage(uint64_t Parts_ID, int32_t stage, std::vector<uint64_t>& return_vector);
  bool Parts_ModulesWithName(uint64_t Parts_ID, std::string moduleName, std::vector<uint64_t>& return_vector);
  bool Parts_DockingPortWithName(uint64_t Parts_ID, std::string name, uint64_t& return_value);
  bool Parts_get_All(uint64_t Parts_ID, std::vector<uint64_t>& return_vector);
  bool Parts_get_Root(uint64_t Parts_ID, uint64_t& return_value);
  bool Parts_get_Controlling(uint64_t Parts_ID, uint64_t& return_value);
  bool Parts_set_Controlling(uint64_t Parts_ID, uint64_t value);
  bool Parts_get_Decouplers(uint64_t Parts_ID, std::vector<uint64_t>& return_vector);
  bool Parts_get_DockingPorts(uint64_t Parts_ID, std::vector<uint64_t>& return_vector);
  bool Parts_get_Engines(uint64_t Parts_ID, std::vector<uint64_t>& return_vector);
  bool Parts_get_LandingGear(uint64_t Parts_ID, std::vector<uint64_t>& return_vector);
  bool Parts_get_LandingLegs(uint64_t Parts_ID, std::vector<uint64_t>& return_vector);
  bool Parts_get_LaunchClamps(uint64_t Parts_ID, std::vector<uint64_t>& return_vector);
  bool Parts_get_Lights(uint64_t Parts_ID, std::vector<uint64_t>& return_vector);
  bool Parts_get_Parachutes(uint64_t Parts_ID, std::vector<uint64_t>& return_vector);
  bool Parts_get_ReactionWheels(uint64_t Parts_ID, std::vector<uint64_t>& return_vector);
  bool Parts_get_Sensors(uint64_t Parts_ID, std::vector<uint64_t>& return_vector);
  bool Parts_get_SolarPanels(uint64_t Parts_ID, std::vector<uint64_t>& return_vector);
  bool PartResources_HasResource(uint64_t PartResources_ID, std::string name, bool& return_value);
  bool PartResources_Max(uint64_t PartResources_ID, std::string name, float& return_value);
  bool PartResources_Amount(uint64_t PartResources_ID, std::string name, float& return_value);
  bool PartResources_get_Names(uint64_t PartResources_ID, std::vector<uint64_t>& return_vector);
  bool ReactionWheel_get_Part(uint64_t ReactionWheel_ID, uint64_t& return_value);
  bool ReactionWheel_get_Active(uint64_t ReactionWheel_ID, bool& return_value);
  bool ReactionWheel_set_Active(uint64_t ReactionWheel_ID, bool value);
  bool ReactionWheel_get_Broken(uint64_t ReactionWheel_ID, bool& return_value);
  bool ReactionWheel_get_PitchTorque(uint64_t ReactionWheel_ID, float& return_value);
  bool ReactionWheel_get_YawTorque(uint64_t ReactionWheel_ID, float& return_value);
  bool ReactionWheel_get_RollTorque(uint64_t ReactionWheel_ID, float& return_value);
  bool Sensor_get_Part(uint64_t Sensor_ID, uint64_t& return_value);
  bool Sensor_get_Active(uint64_t Sensor_ID, bool& return_value);
  bool Sensor_set_Active(uint64_t Sensor_ID, bool value);
  bool Sensor_get_Value(uint64_t Sensor_ID, std::string& return_value);
  bool Sensor_get_PowerUsage(uint64_t Sensor_ID, float& return_value);
  bool SolarPanel_get_Part(uint64_t SolarPanel_ID, uint64_t& return_value);
  bool SolarPanel_get_Deployed(uint64_t SolarPanel_ID, bool& return_value);
  bool SolarPanel_set_Deployed(uint64_t SolarPanel_ID, bool value);
  bool SolarPanel_get_State(uint64_t SolarPanel_ID, int32_t& return_value);
  bool SolarPanel_get_EnergyFlow(uint64_t SolarPanel_ID, float& return_value);
  bool SolarPanel_get_SunExposure(uint64_t SolarPanel_ID, float& return_value);
  bool Vessel_Flight(uint64_t Vessel_ID, uint64_t referenceFrame, uint64_t& return_value);
  bool Vessel_Position(uint64_t Vessel_ID, uint64_t referenceFrame, double& x, double& y, double& z);
  bool Vessel_Velocity(uint64_t Vessel_ID, uint64_t referenceFrame, double& x, double& y, double& z);
  bool Vessel_Rotation(uint64_t Vessel_ID, uint64_t referenceFrame, double& x, double& y, double& z);
  bool Vessel_Direction(uint64_t Vessel_ID, uint64_t referenceFrame, double& x, double& y, double& z);
  bool Vessel_AngularVelocity(uint64_t Vessel_ID, uint64_t referenceFrame, double& x, double& y, double& z);
  bool Vessel_get_Name(uint64_t Vessel_ID, std::string& return_value);
  bool Vessel_set_Name(uint64_t Vessel_ID, std::string value);
  bool Vessel_get_Type(uint64_t Vessel_ID, int32_t& return_value);
  bool Vessel_set_Type(uint64_t Vessel_ID, int32_t value);
  bool Vessel_get_Situation(uint64_t Vessel_ID, int32_t& return_value);
  bool Vessel_get_MET(uint64_t Vessel_ID, double& return_value);
  bool Vessel_get_Target(uint64_t Vessel_ID, uint64_t& return_value);
  bool Vessel_set_Target(uint64_t Vessel_ID, uint64_t value);
  bool Vessel_get_Orbit(uint64_t Vessel_ID, uint64_t& return_value);
  bool Vessel_get_Control(uint64_t Vessel_ID, uint64_t& return_value);
  bool Vessel_get_AutoPilot(uint64_t Vessel_ID, uint64_t& return_value);
  bool Vessel_get_Resources(uint64_t Vessel_ID, uint64_t& return_value);
  bool Vessel_get_Parts(uint64_t Vessel_ID, uint64_t& return_value);
  bool Vessel_get_Comms(uint64_t Vessel_ID, uint64_t& return_value);
  bool Vessel_get_Mass(uint64_t Vessel_ID, float& return_value);
  bool Vessel_get_DryMass(uint64_t Vessel_ID, float& return_value);
  bool Vessel_get_Thrust(uint64_t Vessel_ID, float& return_value);
  bool Vessel_get_AvailableThrust(uint64_t Vessel_ID, float& return_value);
  bool Vessel_get_MaxThrust(uint64_t Vessel_ID, float& return_value);
  bool Vessel_get_MaxVacuumThrust(uint64_t Vessel_ID, float& return_value);
  bool Vessel_get_SpecificImpulse(uint64_t Vessel_ID, float& return_value);
  bool Vessel_get_VacuumSpecificImpulse(uint64_t Vessel_ID, float& return_value);
  bool Vessel_get_KerbinSeaLevelSpecificImpulse(uint64_t Vessel_ID, float& return_value);
  bool Vessel_get_ReferenceFrame(uint64_t Vessel_ID, uint64_t& return_value);
  bool Vessel_get_OrbitalReferenceFrame(uint64_t Vessel_ID, uint64_t& return_value);
  bool Vessel_get_SurfaceReferenceFrame(uint64_t Vessel_ID, uint64_t& return_value);
  bool Vessel_get_SurfaceVelocityReferenceFrame(uint64_t Vessel_ID, uint64_t& return_value);
  bool VesselResources_HasResource(uint64_t VesselResources_ID, std::string name, bool& return_value);
  bool VesselResources_Max(uint64_t VesselResources_ID, std::string name, int32_t stage, bool cumulative, float& return_value);
  bool VesselResources_Amount(uint64_t VesselResources_ID, std::string name, int32_t stage, bool cumulative, float& return_value);
  bool VesselResources_get_Names(uint64_t VesselResources_ID, std::vector<uint64_t>& return_vector);
  bool GetStatus(krpc::Status& return_value);
  bool GetServices(krpc::Services& return_value);
  bool AddStream(krpc::Request input_request, uint32_t& return_value);
  bool RemoveStream(uint32_t id);
protected:
  bool createRequestString(krpc::Request req, std::string& str);
  bool getResponseFromRequest(krpc::Request req, krpc::Response& res);
  void streamThreadFunc();

  void PrintBytesHex(const char *buf, int size);
  void EncodeVarint(uint32_t value, char *buf, int &size);
  void EncodeVarint(uint64_t value, char *buf, int &size);
  void DecodeVarint(uint32_t &value, char *buf, int size);
  void DecodeVarint(uint64_t &value, char *buf, int size);
  void DecodeString(std::string &str, char *buf, int size);
  void EncodeTuple(double x, double y, double z, krpc::Tuple &tuple);
  void DecodeTuple(krpc::Tuple tuple, double &x, double &y, double &z);
private:
  std::map<std::string,krpc::Response> activeStreams_;

  int port_;
  int streamPort_;
  std::string ip_;
  std::string id_;
  std::string name_;
  int socket_;
  int streamSocket_;
  int timeout_;
};
