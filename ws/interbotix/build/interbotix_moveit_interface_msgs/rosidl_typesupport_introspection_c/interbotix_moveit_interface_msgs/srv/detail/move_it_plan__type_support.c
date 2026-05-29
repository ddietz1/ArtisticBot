// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from interbotix_moveit_interface_msgs:srv/MoveItPlan.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "interbotix_moveit_interface_msgs/srv/detail/move_it_plan__rosidl_typesupport_introspection_c.h"
#include "interbotix_moveit_interface_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "interbotix_moveit_interface_msgs/srv/detail/move_it_plan__functions.h"
#include "interbotix_moveit_interface_msgs/srv/detail/move_it_plan__struct.h"


// Include directives for member types
// Member `ee_pose`
#include "geometry_msgs/msg/pose.h"
// Member `ee_pose`
#include "geometry_msgs/msg/detail/pose__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__rosidl_typesupport_introspection_c__MoveItPlan_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__init(message_memory);
}

void interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__rosidl_typesupport_introspection_c__MoveItPlan_Request_fini_function(void * message_memory)
{
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__rosidl_typesupport_introspection_c__MoveItPlan_Request_message_member_array[2] = {
  {
    "cmd",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interbotix_moveit_interface_msgs__srv__MoveItPlan_Request, cmd),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "ee_pose",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interbotix_moveit_interface_msgs__srv__MoveItPlan_Request, ee_pose),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__rosidl_typesupport_introspection_c__MoveItPlan_Request_message_members = {
  "interbotix_moveit_interface_msgs__srv",  // message namespace
  "MoveItPlan_Request",  // message name
  2,  // number of fields
  sizeof(interbotix_moveit_interface_msgs__srv__MoveItPlan_Request),
  false,  // has_any_key_member_
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__rosidl_typesupport_introspection_c__MoveItPlan_Request_message_member_array,  // message members
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__rosidl_typesupport_introspection_c__MoveItPlan_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__rosidl_typesupport_introspection_c__MoveItPlan_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__rosidl_typesupport_introspection_c__MoveItPlan_Request_message_type_support_handle = {
  0,
  &interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__rosidl_typesupport_introspection_c__MoveItPlan_Request_message_members,
  get_message_typesupport_handle_function,
  &interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__get_type_hash,
  &interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__get_type_description,
  &interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interbotix_moveit_interface_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interbotix_moveit_interface_msgs, srv, MoveItPlan_Request)() {
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__rosidl_typesupport_introspection_c__MoveItPlan_Request_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, Pose)();
  if (!interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__rosidl_typesupport_introspection_c__MoveItPlan_Request_message_type_support_handle.typesupport_identifier) {
    interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__rosidl_typesupport_introspection_c__MoveItPlan_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__rosidl_typesupport_introspection_c__MoveItPlan_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "interbotix_moveit_interface_msgs/srv/detail/move_it_plan__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interbotix_moveit_interface_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interbotix_moveit_interface_msgs/srv/detail/move_it_plan__functions.h"
// already included above
// #include "interbotix_moveit_interface_msgs/srv/detail/move_it_plan__struct.h"


// Include directives for member types
// Member `msg`
#include "std_msgs/msg/string.h"
// Member `msg`
#include "std_msgs/msg/detail/string__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__rosidl_typesupport_introspection_c__MoveItPlan_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__init(message_memory);
}

void interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__rosidl_typesupport_introspection_c__MoveItPlan_Response_fini_function(void * message_memory)
{
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__rosidl_typesupport_introspection_c__MoveItPlan_Response_message_member_array[2] = {
  {
    "msg",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interbotix_moveit_interface_msgs__srv__MoveItPlan_Response, msg),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "success",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interbotix_moveit_interface_msgs__srv__MoveItPlan_Response, success),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__rosidl_typesupport_introspection_c__MoveItPlan_Response_message_members = {
  "interbotix_moveit_interface_msgs__srv",  // message namespace
  "MoveItPlan_Response",  // message name
  2,  // number of fields
  sizeof(interbotix_moveit_interface_msgs__srv__MoveItPlan_Response),
  false,  // has_any_key_member_
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__rosidl_typesupport_introspection_c__MoveItPlan_Response_message_member_array,  // message members
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__rosidl_typesupport_introspection_c__MoveItPlan_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__rosidl_typesupport_introspection_c__MoveItPlan_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__rosidl_typesupport_introspection_c__MoveItPlan_Response_message_type_support_handle = {
  0,
  &interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__rosidl_typesupport_introspection_c__MoveItPlan_Response_message_members,
  get_message_typesupport_handle_function,
  &interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__get_type_hash,
  &interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__get_type_description,
  &interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interbotix_moveit_interface_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interbotix_moveit_interface_msgs, srv, MoveItPlan_Response)() {
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__rosidl_typesupport_introspection_c__MoveItPlan_Response_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, String)();
  if (!interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__rosidl_typesupport_introspection_c__MoveItPlan_Response_message_type_support_handle.typesupport_identifier) {
    interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__rosidl_typesupport_introspection_c__MoveItPlan_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__rosidl_typesupport_introspection_c__MoveItPlan_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "interbotix_moveit_interface_msgs/srv/detail/move_it_plan__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interbotix_moveit_interface_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interbotix_moveit_interface_msgs/srv/detail/move_it_plan__functions.h"
// already included above
// #include "interbotix_moveit_interface_msgs/srv/detail/move_it_plan__struct.h"


// Include directives for member types
// Member `info`
#include "service_msgs/msg/service_event_info.h"
// Member `info`
#include "service_msgs/msg/detail/service_event_info__rosidl_typesupport_introspection_c.h"
// Member `request`
// Member `response`
#include "interbotix_moveit_interface_msgs/srv/move_it_plan.h"
// Member `request`
// Member `response`
// already included above
// #include "interbotix_moveit_interface_msgs/srv/detail/move_it_plan__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__MoveItPlan_Event_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__init(message_memory);
}

void interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__MoveItPlan_Event_fini_function(void * message_memory)
{
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__fini(message_memory);
}

size_t interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__size_function__MoveItPlan_Event__request(
  const void * untyped_member)
{
  const interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__Sequence * member =
    (const interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__Sequence *)(untyped_member);
  return member->size;
}

const void * interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__get_const_function__MoveItPlan_Event__request(
  const void * untyped_member, size_t index)
{
  const interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__Sequence * member =
    (const interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__Sequence *)(untyped_member);
  return &member->data[index];
}

void * interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__get_function__MoveItPlan_Event__request(
  void * untyped_member, size_t index)
{
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__Sequence * member =
    (interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__Sequence *)(untyped_member);
  return &member->data[index];
}

void interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__fetch_function__MoveItPlan_Event__request(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const interbotix_moveit_interface_msgs__srv__MoveItPlan_Request * item =
    ((const interbotix_moveit_interface_msgs__srv__MoveItPlan_Request *)
    interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__get_const_function__MoveItPlan_Event__request(untyped_member, index));
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Request * value =
    (interbotix_moveit_interface_msgs__srv__MoveItPlan_Request *)(untyped_value);
  *value = *item;
}

void interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__assign_function__MoveItPlan_Event__request(
  void * untyped_member, size_t index, const void * untyped_value)
{
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Request * item =
    ((interbotix_moveit_interface_msgs__srv__MoveItPlan_Request *)
    interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__get_function__MoveItPlan_Event__request(untyped_member, index));
  const interbotix_moveit_interface_msgs__srv__MoveItPlan_Request * value =
    (const interbotix_moveit_interface_msgs__srv__MoveItPlan_Request *)(untyped_value);
  *item = *value;
}

bool interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__resize_function__MoveItPlan_Event__request(
  void * untyped_member, size_t size)
{
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__Sequence * member =
    (interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__Sequence *)(untyped_member);
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__Sequence__fini(member);
  return interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__Sequence__init(member, size);
}

size_t interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__size_function__MoveItPlan_Event__response(
  const void * untyped_member)
{
  const interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__Sequence * member =
    (const interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__Sequence *)(untyped_member);
  return member->size;
}

const void * interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__get_const_function__MoveItPlan_Event__response(
  const void * untyped_member, size_t index)
{
  const interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__Sequence * member =
    (const interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__Sequence *)(untyped_member);
  return &member->data[index];
}

void * interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__get_function__MoveItPlan_Event__response(
  void * untyped_member, size_t index)
{
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__Sequence * member =
    (interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__Sequence *)(untyped_member);
  return &member->data[index];
}

void interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__fetch_function__MoveItPlan_Event__response(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const interbotix_moveit_interface_msgs__srv__MoveItPlan_Response * item =
    ((const interbotix_moveit_interface_msgs__srv__MoveItPlan_Response *)
    interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__get_const_function__MoveItPlan_Event__response(untyped_member, index));
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Response * value =
    (interbotix_moveit_interface_msgs__srv__MoveItPlan_Response *)(untyped_value);
  *value = *item;
}

void interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__assign_function__MoveItPlan_Event__response(
  void * untyped_member, size_t index, const void * untyped_value)
{
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Response * item =
    ((interbotix_moveit_interface_msgs__srv__MoveItPlan_Response *)
    interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__get_function__MoveItPlan_Event__response(untyped_member, index));
  const interbotix_moveit_interface_msgs__srv__MoveItPlan_Response * value =
    (const interbotix_moveit_interface_msgs__srv__MoveItPlan_Response *)(untyped_value);
  *item = *value;
}

bool interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__resize_function__MoveItPlan_Event__response(
  void * untyped_member, size_t size)
{
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__Sequence * member =
    (interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__Sequence *)(untyped_member);
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__Sequence__fini(member);
  return interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__MoveItPlan_Event_message_member_array[3] = {
  {
    "info",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interbotix_moveit_interface_msgs__srv__MoveItPlan_Event, info),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "request",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    true,  // is array
    1,  // array size
    true,  // is upper bound
    offsetof(interbotix_moveit_interface_msgs__srv__MoveItPlan_Event, request),  // bytes offset in struct
    NULL,  // default value
    interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__size_function__MoveItPlan_Event__request,  // size() function pointer
    interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__get_const_function__MoveItPlan_Event__request,  // get_const(index) function pointer
    interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__get_function__MoveItPlan_Event__request,  // get(index) function pointer
    interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__fetch_function__MoveItPlan_Event__request,  // fetch(index, &value) function pointer
    interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__assign_function__MoveItPlan_Event__request,  // assign(index, value) function pointer
    interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__resize_function__MoveItPlan_Event__request  // resize(index) function pointer
  },
  {
    "response",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    true,  // is array
    1,  // array size
    true,  // is upper bound
    offsetof(interbotix_moveit_interface_msgs__srv__MoveItPlan_Event, response),  // bytes offset in struct
    NULL,  // default value
    interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__size_function__MoveItPlan_Event__response,  // size() function pointer
    interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__get_const_function__MoveItPlan_Event__response,  // get_const(index) function pointer
    interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__get_function__MoveItPlan_Event__response,  // get(index) function pointer
    interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__fetch_function__MoveItPlan_Event__response,  // fetch(index, &value) function pointer
    interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__assign_function__MoveItPlan_Event__response,  // assign(index, value) function pointer
    interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__resize_function__MoveItPlan_Event__response  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__MoveItPlan_Event_message_members = {
  "interbotix_moveit_interface_msgs__srv",  // message namespace
  "MoveItPlan_Event",  // message name
  3,  // number of fields
  sizeof(interbotix_moveit_interface_msgs__srv__MoveItPlan_Event),
  false,  // has_any_key_member_
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__MoveItPlan_Event_message_member_array,  // message members
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__MoveItPlan_Event_init_function,  // function to initialize message memory (memory has to be allocated)
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__MoveItPlan_Event_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__MoveItPlan_Event_message_type_support_handle = {
  0,
  &interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__MoveItPlan_Event_message_members,
  get_message_typesupport_handle_function,
  &interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__get_type_hash,
  &interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__get_type_description,
  &interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interbotix_moveit_interface_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interbotix_moveit_interface_msgs, srv, MoveItPlan_Event)() {
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__MoveItPlan_Event_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_msgs, msg, ServiceEventInfo)();
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__MoveItPlan_Event_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interbotix_moveit_interface_msgs, srv, MoveItPlan_Request)();
  interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__MoveItPlan_Event_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interbotix_moveit_interface_msgs, srv, MoveItPlan_Response)();
  if (!interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__MoveItPlan_Event_message_type_support_handle.typesupport_identifier) {
    interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__MoveItPlan_Event_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__MoveItPlan_Event_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "interbotix_moveit_interface_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "interbotix_moveit_interface_msgs/srv/detail/move_it_plan__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers interbotix_moveit_interface_msgs__srv__detail__move_it_plan__rosidl_typesupport_introspection_c__MoveItPlan_service_members = {
  "interbotix_moveit_interface_msgs__srv",  // service namespace
  "MoveItPlan",  // service name
  // the following fields are initialized below on first access
  NULL,  // request message
  // interbotix_moveit_interface_msgs__srv__detail__move_it_plan__rosidl_typesupport_introspection_c__MoveItPlan_Request_message_type_support_handle,
  NULL,  // response message
  // interbotix_moveit_interface_msgs__srv__detail__move_it_plan__rosidl_typesupport_introspection_c__MoveItPlan_Response_message_type_support_handle
  NULL  // event_message
  // interbotix_moveit_interface_msgs__srv__detail__move_it_plan__rosidl_typesupport_introspection_c__MoveItPlan_Response_message_type_support_handle
};


static rosidl_service_type_support_t interbotix_moveit_interface_msgs__srv__detail__move_it_plan__rosidl_typesupport_introspection_c__MoveItPlan_service_type_support_handle = {
  0,
  &interbotix_moveit_interface_msgs__srv__detail__move_it_plan__rosidl_typesupport_introspection_c__MoveItPlan_service_members,
  get_service_typesupport_handle_function,
  &interbotix_moveit_interface_msgs__srv__MoveItPlan_Request__rosidl_typesupport_introspection_c__MoveItPlan_Request_message_type_support_handle,
  &interbotix_moveit_interface_msgs__srv__MoveItPlan_Response__rosidl_typesupport_introspection_c__MoveItPlan_Response_message_type_support_handle,
  &interbotix_moveit_interface_msgs__srv__MoveItPlan_Event__rosidl_typesupport_introspection_c__MoveItPlan_Event_message_type_support_handle,
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_CREATE_EVENT_MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c,
    interbotix_moveit_interface_msgs,
    srv,
    MoveItPlan
  ),
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_DESTROY_EVENT_MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c,
    interbotix_moveit_interface_msgs,
    srv,
    MoveItPlan
  ),
  &interbotix_moveit_interface_msgs__srv__MoveItPlan__get_type_hash,
  &interbotix_moveit_interface_msgs__srv__MoveItPlan__get_type_description,
  &interbotix_moveit_interface_msgs__srv__MoveItPlan__get_type_description_sources,
};

// Forward declaration of message type support functions for service members
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interbotix_moveit_interface_msgs, srv, MoveItPlan_Request)(void);

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interbotix_moveit_interface_msgs, srv, MoveItPlan_Response)(void);

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interbotix_moveit_interface_msgs, srv, MoveItPlan_Event)(void);

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interbotix_moveit_interface_msgs
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interbotix_moveit_interface_msgs, srv, MoveItPlan)(void) {
  if (!interbotix_moveit_interface_msgs__srv__detail__move_it_plan__rosidl_typesupport_introspection_c__MoveItPlan_service_type_support_handle.typesupport_identifier) {
    interbotix_moveit_interface_msgs__srv__detail__move_it_plan__rosidl_typesupport_introspection_c__MoveItPlan_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)interbotix_moveit_interface_msgs__srv__detail__move_it_plan__rosidl_typesupport_introspection_c__MoveItPlan_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interbotix_moveit_interface_msgs, srv, MoveItPlan_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interbotix_moveit_interface_msgs, srv, MoveItPlan_Response)()->data;
  }
  if (!service_members->event_members_) {
    service_members->event_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interbotix_moveit_interface_msgs, srv, MoveItPlan_Event)()->data;
  }

  return &interbotix_moveit_interface_msgs__srv__detail__move_it_plan__rosidl_typesupport_introspection_c__MoveItPlan_service_type_support_handle;
}
