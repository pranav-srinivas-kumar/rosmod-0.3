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

  bool GetActiveVessel(uint64_t& id);
  bool GetVessels(std::vector<uint64_t>& ids);
  bool GetVesselName(uint64_t vesselID, std::string& name);
  bool GetVesselPosition(uint64_t vesselID, uint64_t refFrame, double &x, double &y, double &z);
  bool GetVesselVelocity(uint64_t vesselID, uint64_t refFrame, double &x, double &y, double &z);
  bool GetVesselRotation(uint64_t vesselID, uint64_t refFrame, double &x, double &y, double &z);
  bool GetVesselOrbitalReferenceFrame(uint64_t vesselID, uint64_t& refFrame);
  bool GetVesselOrbit(uint64_t vesselID, uint64_t& orbit);

  bool GetOrbitApoapsis(uint64_t vesselID, double& apo);
  bool GetOrbitPeriapsis(uint64_t vesselID, double& peri);
  bool GetOrbitSpeed(uint64_t vesselID, double& speed);
  bool GetOrbitTimeToApoapsis(uint64_t vesselID, double& time);
  bool GetOrbitTimeToPeriapsis(uint64_t vesselID, double& time);

  bool SetTargetVessel(uint64_t vesselID);
  bool SetControlSAS(uint64_t vesselID, bool on);
  bool SetControlRCS(uint64_t vesselID, bool on);
  bool SetThrottle(uint64_t vesselID, float value);
  bool SetPitch(uint64_t vesselID, float value);
  bool SetRoll(uint64_t vesselID, float value);
  bool SetYaw(uint64_t vesselID, float value);
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
