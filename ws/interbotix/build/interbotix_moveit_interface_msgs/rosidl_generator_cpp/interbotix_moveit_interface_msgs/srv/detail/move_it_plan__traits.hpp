// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interbotix_moveit_interface_msgs:srv/MoveItPlan.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "interbotix_moveit_interface_msgs/srv/move_it_plan.hpp"


#ifndef INTERBOTIX_MOVEIT_INTERFACE_MSGS__SRV__DETAIL__MOVE_IT_PLAN__TRAITS_HPP_
#define INTERBOTIX_MOVEIT_INTERFACE_MSGS__SRV__DETAIL__MOVE_IT_PLAN__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "interbotix_moveit_interface_msgs/srv/detail/move_it_plan__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'ee_pose'
#include "geometry_msgs/msg/detail/pose__traits.hpp"

namespace interbotix_moveit_interface_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const MoveItPlan_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: cmd
  {
    out << "cmd: ";
    rosidl_generator_traits::value_to_yaml(msg.cmd, out);
    out << ", ";
  }

  // member: ee_pose
  {
    out << "ee_pose: ";
    to_flow_style_yaml(msg.ee_pose, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const MoveItPlan_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: cmd
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "cmd: ";
    rosidl_generator_traits::value_to_yaml(msg.cmd, out);
    out << "\n";
  }

  // member: ee_pose
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ee_pose:\n";
    to_block_style_yaml(msg.ee_pose, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MoveItPlan_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace interbotix_moveit_interface_msgs

namespace rosidl_generator_traits
{

[[deprecated("use interbotix_moveit_interface_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const interbotix_moveit_interface_msgs::srv::MoveItPlan_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  interbotix_moveit_interface_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interbotix_moveit_interface_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const interbotix_moveit_interface_msgs::srv::MoveItPlan_Request & msg)
{
  return interbotix_moveit_interface_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<interbotix_moveit_interface_msgs::srv::MoveItPlan_Request>()
{
  return "interbotix_moveit_interface_msgs::srv::MoveItPlan_Request";
}

template<>
inline const char * name<interbotix_moveit_interface_msgs::srv::MoveItPlan_Request>()
{
  return "interbotix_moveit_interface_msgs/srv/MoveItPlan_Request";
}

template<>
struct has_fixed_size<interbotix_moveit_interface_msgs::srv::MoveItPlan_Request>
  : std::integral_constant<bool, has_fixed_size<geometry_msgs::msg::Pose>::value> {};

template<>
struct has_bounded_size<interbotix_moveit_interface_msgs::srv::MoveItPlan_Request>
  : std::integral_constant<bool, has_bounded_size<geometry_msgs::msg::Pose>::value> {};

template<>
struct is_message<interbotix_moveit_interface_msgs::srv::MoveItPlan_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'msg'
#include "std_msgs/msg/detail/string__traits.hpp"

namespace interbotix_moveit_interface_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const MoveItPlan_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: msg
  {
    out << "msg: ";
    to_flow_style_yaml(msg.msg, out);
    out << ", ";
  }

  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const MoveItPlan_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: msg
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "msg:\n";
    to_block_style_yaml(msg.msg, out, indentation + 2);
  }

  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MoveItPlan_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace interbotix_moveit_interface_msgs

namespace rosidl_generator_traits
{

[[deprecated("use interbotix_moveit_interface_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const interbotix_moveit_interface_msgs::srv::MoveItPlan_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  interbotix_moveit_interface_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interbotix_moveit_interface_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const interbotix_moveit_interface_msgs::srv::MoveItPlan_Response & msg)
{
  return interbotix_moveit_interface_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<interbotix_moveit_interface_msgs::srv::MoveItPlan_Response>()
{
  return "interbotix_moveit_interface_msgs::srv::MoveItPlan_Response";
}

template<>
inline const char * name<interbotix_moveit_interface_msgs::srv::MoveItPlan_Response>()
{
  return "interbotix_moveit_interface_msgs/srv/MoveItPlan_Response";
}

template<>
struct has_fixed_size<interbotix_moveit_interface_msgs::srv::MoveItPlan_Response>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::String>::value> {};

template<>
struct has_bounded_size<interbotix_moveit_interface_msgs::srv::MoveItPlan_Response>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::String>::value> {};

template<>
struct is_message<interbotix_moveit_interface_msgs::srv::MoveItPlan_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__traits.hpp"

namespace interbotix_moveit_interface_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const MoveItPlan_Event & msg,
  std::ostream & out)
{
  out << "{";
  // member: info
  {
    out << "info: ";
    to_flow_style_yaml(msg.info, out);
    out << ", ";
  }

  // member: request
  {
    if (msg.request.size() == 0) {
      out << "request: []";
    } else {
      out << "request: [";
      size_t pending_items = msg.request.size();
      for (auto item : msg.request) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: response
  {
    if (msg.response.size() == 0) {
      out << "response: []";
    } else {
      out << "response: [";
      size_t pending_items = msg.response.size();
      for (auto item : msg.response) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const MoveItPlan_Event & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: info
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "info:\n";
    to_block_style_yaml(msg.info, out, indentation + 2);
  }

  // member: request
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.request.size() == 0) {
      out << "request: []\n";
    } else {
      out << "request:\n";
      for (auto item : msg.request) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: response
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.response.size() == 0) {
      out << "response: []\n";
    } else {
      out << "response:\n";
      for (auto item : msg.response) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MoveItPlan_Event & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace interbotix_moveit_interface_msgs

namespace rosidl_generator_traits
{

[[deprecated("use interbotix_moveit_interface_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const interbotix_moveit_interface_msgs::srv::MoveItPlan_Event & msg,
  std::ostream & out, size_t indentation = 0)
{
  interbotix_moveit_interface_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interbotix_moveit_interface_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const interbotix_moveit_interface_msgs::srv::MoveItPlan_Event & msg)
{
  return interbotix_moveit_interface_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<interbotix_moveit_interface_msgs::srv::MoveItPlan_Event>()
{
  return "interbotix_moveit_interface_msgs::srv::MoveItPlan_Event";
}

template<>
inline const char * name<interbotix_moveit_interface_msgs::srv::MoveItPlan_Event>()
{
  return "interbotix_moveit_interface_msgs/srv/MoveItPlan_Event";
}

template<>
struct has_fixed_size<interbotix_moveit_interface_msgs::srv::MoveItPlan_Event>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<interbotix_moveit_interface_msgs::srv::MoveItPlan_Event>
  : std::integral_constant<bool, has_bounded_size<interbotix_moveit_interface_msgs::srv::MoveItPlan_Request>::value && has_bounded_size<interbotix_moveit_interface_msgs::srv::MoveItPlan_Response>::value && has_bounded_size<service_msgs::msg::ServiceEventInfo>::value> {};

template<>
struct is_message<interbotix_moveit_interface_msgs::srv::MoveItPlan_Event>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interbotix_moveit_interface_msgs::srv::MoveItPlan>()
{
  return "interbotix_moveit_interface_msgs::srv::MoveItPlan";
}

template<>
inline const char * name<interbotix_moveit_interface_msgs::srv::MoveItPlan>()
{
  return "interbotix_moveit_interface_msgs/srv/MoveItPlan";
}

template<>
struct has_fixed_size<interbotix_moveit_interface_msgs::srv::MoveItPlan>
  : std::integral_constant<
    bool,
    has_fixed_size<interbotix_moveit_interface_msgs::srv::MoveItPlan_Request>::value &&
    has_fixed_size<interbotix_moveit_interface_msgs::srv::MoveItPlan_Response>::value
  >
{
};

template<>
struct has_bounded_size<interbotix_moveit_interface_msgs::srv::MoveItPlan>
  : std::integral_constant<
    bool,
    has_bounded_size<interbotix_moveit_interface_msgs::srv::MoveItPlan_Request>::value &&
    has_bounded_size<interbotix_moveit_interface_msgs::srv::MoveItPlan_Response>::value
  >
{
};

template<>
struct is_service<interbotix_moveit_interface_msgs::srv::MoveItPlan>
  : std::true_type
{
};

template<>
struct is_service_request<interbotix_moveit_interface_msgs::srv::MoveItPlan_Request>
  : std::true_type
{
};

template<>
struct is_service_response<interbotix_moveit_interface_msgs::srv::MoveItPlan_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // INTERBOTIX_MOVEIT_INTERFACE_MSGS__SRV__DETAIL__MOVE_IT_PLAN__TRAITS_HPP_
