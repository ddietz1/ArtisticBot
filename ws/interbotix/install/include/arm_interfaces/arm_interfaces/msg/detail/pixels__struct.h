// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from arm_interfaces:msg/Pixels.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "arm_interfaces/msg/pixels.h"


#ifndef ARM_INTERFACES__MSG__DETAIL__PIXELS__STRUCT_H_
#define ARM_INTERFACES__MSG__DETAIL__PIXELS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

// Include directives for member types
// Member 'points'
#include "geometry_msgs/msg/detail/point__struct.h"

/// Struct defined in msg/Pixels in the package arm_interfaces.
typedef struct arm_interfaces__msg__Pixels
{
  geometry_msgs__msg__Point__Sequence points;
} arm_interfaces__msg__Pixels;

// Struct for a sequence of arm_interfaces__msg__Pixels.
typedef struct arm_interfaces__msg__Pixels__Sequence
{
  arm_interfaces__msg__Pixels * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} arm_interfaces__msg__Pixels__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ARM_INTERFACES__MSG__DETAIL__PIXELS__STRUCT_H_
