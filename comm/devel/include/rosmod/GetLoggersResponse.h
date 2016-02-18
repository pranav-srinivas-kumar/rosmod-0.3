// Generated by gencpp from file rosmod/GetLoggersResponse.msg
// DO NOT EDIT!


#ifndef ROSMOD_MESSAGE_GETLOGGERSRESPONSE_H
#define ROSMOD_MESSAGE_GETLOGGERSRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <rosmod/Logger.h>

namespace rosmod
{
template <class ContainerAllocator>
struct GetLoggersResponse_
{
  typedef GetLoggersResponse_<ContainerAllocator> Type;

  GetLoggersResponse_()
    : loggers()  {
    }
  GetLoggersResponse_(const ContainerAllocator& _alloc)
    : loggers(_alloc)  {
    }



   typedef std::vector< ::rosmod::Logger_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::rosmod::Logger_<ContainerAllocator> >::other >  _loggers_type;
  _loggers_type loggers;




  typedef boost::shared_ptr< ::rosmod::GetLoggersResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rosmod::GetLoggersResponse_<ContainerAllocator> const> ConstPtr;

}; // struct GetLoggersResponse_

typedef ::rosmod::GetLoggersResponse_<std::allocator<void> > GetLoggersResponse;

typedef boost::shared_ptr< ::rosmod::GetLoggersResponse > GetLoggersResponsePtr;
typedef boost::shared_ptr< ::rosmod::GetLoggersResponse const> GetLoggersResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rosmod::GetLoggersResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rosmod::GetLoggersResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace rosmod

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'rosmod': ['/home/jeb/Repositories/rosmod/comm/src/rosmod/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::rosmod::GetLoggersResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rosmod::GetLoggersResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rosmod::GetLoggersResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rosmod::GetLoggersResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rosmod::GetLoggersResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rosmod::GetLoggersResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rosmod::GetLoggersResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "32e97e85527d4678a8f9279894bb64b0";
  }

  static const char* value(const ::rosmod::GetLoggersResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x32e97e85527d4678ULL;
  static const uint64_t static_value2 = 0xa8f9279894bb64b0ULL;
};

template<class ContainerAllocator>
struct DataType< ::rosmod::GetLoggersResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rosmod/GetLoggersResponse";
  }

  static const char* value(const ::rosmod::GetLoggersResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rosmod::GetLoggersResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Logger[] loggers\n\
\n\
================================================================================\n\
MSG: rosmod/Logger\n\
string name\n\
string level\n\
";
  }

  static const char* value(const ::rosmod::GetLoggersResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rosmod::GetLoggersResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.loggers);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct GetLoggersResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rosmod::GetLoggersResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::rosmod::GetLoggersResponse_<ContainerAllocator>& v)
  {
    s << indent << "loggers[]" << std::endl;
    for (size_t i = 0; i < v.loggers.size(); ++i)
    {
      s << indent << "  loggers[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::rosmod::Logger_<ContainerAllocator> >::stream(s, indent + "    ", v.loggers[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROSMOD_MESSAGE_GETLOGGERSRESPONSE_H