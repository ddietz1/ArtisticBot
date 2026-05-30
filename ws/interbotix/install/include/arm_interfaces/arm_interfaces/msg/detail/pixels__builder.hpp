// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from arm_interfaces:msg/Pixels.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "arm_interfaces/msg/pixels.hpp"


#ifndef ARM_INTERFACES__MSG__DETAIL__PIXELS__BUILDER_HPP_
#define ARM_INTERFACES__MSG__DETAIL__PIXELS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "arm_interfaces/msg/detail/pixels__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace arm_interfaces
{

namespace msg
{

namespace builder
{

class Init_Pixels_points
{
public:
  Init_Pixels_points()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::arm_interfaces::msg::Pixels points(::arm_interfaces::msg::Pixels::_points_type arg)
  {
    msg_.points = std::move(arg);
    return std::move(msg_);
  }

private:
  ::arm_interfaces::msg::Pixels msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::arm_interfaces::msg::Pixels>()
{
  return arm_interfaces::msg::builder::Init_Pixels_points();
}

}  // namespace arm_interfaces

#endif  // ARM_INTERFACES__MSG__DETAIL__PIXELS__BUILDER_HPP_
