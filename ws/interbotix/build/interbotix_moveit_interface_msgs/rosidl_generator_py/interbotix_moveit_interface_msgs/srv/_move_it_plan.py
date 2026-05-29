# generated from rosidl_generator_py/resource/_idl.py.em
# with input from interbotix_moveit_interface_msgs:srv/MoveItPlan.idl
# generated code does not contain a copyright notice

# This is being done at the module level and not on the instance level to avoid looking
# for the same variable multiple times on each instance. This variable is not supposed to
# change during runtime so it makes sense to only look for it once.
from os import getenv

ros_python_check_fields = getenv('ROS_PYTHON_CHECK_FIELDS', default='')


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_MoveItPlan_Request(type):
    """Metaclass of message 'MoveItPlan_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'CMD_NONE': 0,
        'CMD_PLAN_POSE': 1,
        'CMD_PLAN_POSITION': 2,
        'CMD_PLAN_ORIENTATION': 3,
        'CMD_EXECUTE': 4,
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('interbotix_moveit_interface_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'interbotix_moveit_interface_msgs.srv.MoveItPlan_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__move_it_plan__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__move_it_plan__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__move_it_plan__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__move_it_plan__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__move_it_plan__request

            from geometry_msgs.msg import Pose
            if Pose.__class__._TYPE_SUPPORT is None:
                Pose.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'CMD_NONE': cls.__constants['CMD_NONE'],
            'CMD_PLAN_POSE': cls.__constants['CMD_PLAN_POSE'],
            'CMD_PLAN_POSITION': cls.__constants['CMD_PLAN_POSITION'],
            'CMD_PLAN_ORIENTATION': cls.__constants['CMD_PLAN_ORIENTATION'],
            'CMD_EXECUTE': cls.__constants['CMD_EXECUTE'],
        }

    @property
    def CMD_NONE(self):
        """Message constant 'CMD_NONE'."""
        return Metaclass_MoveItPlan_Request.__constants['CMD_NONE']

    @property
    def CMD_PLAN_POSE(self):
        """Message constant 'CMD_PLAN_POSE'."""
        return Metaclass_MoveItPlan_Request.__constants['CMD_PLAN_POSE']

    @property
    def CMD_PLAN_POSITION(self):
        """Message constant 'CMD_PLAN_POSITION'."""
        return Metaclass_MoveItPlan_Request.__constants['CMD_PLAN_POSITION']

    @property
    def CMD_PLAN_ORIENTATION(self):
        """Message constant 'CMD_PLAN_ORIENTATION'."""
        return Metaclass_MoveItPlan_Request.__constants['CMD_PLAN_ORIENTATION']

    @property
    def CMD_EXECUTE(self):
        """Message constant 'CMD_EXECUTE'."""
        return Metaclass_MoveItPlan_Request.__constants['CMD_EXECUTE']


class MoveItPlan_Request(metaclass=Metaclass_MoveItPlan_Request):
    """
    Message class 'MoveItPlan_Request'.

    Constants:
      CMD_NONE
      CMD_PLAN_POSE
      CMD_PLAN_POSITION
      CMD_PLAN_ORIENTATION
      CMD_EXECUTE
    """

    __slots__ = [
        '_cmd',
        '_ee_pose',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'cmd': 'int8',
        'ee_pose': 'geometry_msgs/Pose',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Pose'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        if 'check_fields' in kwargs:
            self._check_fields = kwargs['check_fields']
        else:
            self._check_fields = ros_python_check_fields == '1'
        if self._check_fields:
            assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
                'Invalid arguments passed to constructor: %s' % \
                ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.cmd = kwargs.get('cmd', int())
        from geometry_msgs.msg import Pose
        self.ee_pose = kwargs.get('ee_pose', Pose())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.cmd != other.cmd:
            return False
        if self.ee_pose != other.ee_pose:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def cmd(self):
        """Message field 'cmd'."""
        return self._cmd

    @cmd.setter
    def cmd(self, value):
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'cmd' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'cmd' field must be an integer in [-128, 127]"
        self._cmd = value

    @builtins.property
    def ee_pose(self):
        """Message field 'ee_pose'."""
        return self._ee_pose

    @ee_pose.setter
    def ee_pose(self, value):
        if self._check_fields:
            from geometry_msgs.msg import Pose
            assert \
                isinstance(value, Pose), \
                "The 'ee_pose' field must be a sub message of type 'Pose'"
        self._ee_pose = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_MoveItPlan_Response(type):
    """Metaclass of message 'MoveItPlan_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('interbotix_moveit_interface_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'interbotix_moveit_interface_msgs.srv.MoveItPlan_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__move_it_plan__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__move_it_plan__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__move_it_plan__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__move_it_plan__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__move_it_plan__response

            from std_msgs.msg import String
            if String.__class__._TYPE_SUPPORT is None:
                String.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class MoveItPlan_Response(metaclass=Metaclass_MoveItPlan_Response):
    """Message class 'MoveItPlan_Response'."""

    __slots__ = [
        '_msg',
        '_success',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'msg': 'std_msgs/String',
        'success': 'boolean',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'String'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        if 'check_fields' in kwargs:
            self._check_fields = kwargs['check_fields']
        else:
            self._check_fields = ros_python_check_fields == '1'
        if self._check_fields:
            assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
                'Invalid arguments passed to constructor: %s' % \
                ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import String
        self.msg = kwargs.get('msg', String())
        self.success = kwargs.get('success', bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.msg != other.msg:
            return False
        if self.success != other.success:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def msg(self):
        """Message field 'msg'."""
        return self._msg

    @msg.setter
    def msg(self, value):
        if self._check_fields:
            from std_msgs.msg import String
            assert \
                isinstance(value, String), \
                "The 'msg' field must be a sub message of type 'String'"
        self._msg = value

    @builtins.property
    def success(self):
        """Message field 'success'."""
        return self._success

    @success.setter
    def success(self, value):
        if self._check_fields:
            assert \
                isinstance(value, bool), \
                "The 'success' field must be of type 'bool'"
        self._success = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_MoveItPlan_Event(type):
    """Metaclass of message 'MoveItPlan_Event'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('interbotix_moveit_interface_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'interbotix_moveit_interface_msgs.srv.MoveItPlan_Event')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__move_it_plan__event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__move_it_plan__event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__move_it_plan__event
            cls._TYPE_SUPPORT = module.type_support_msg__srv__move_it_plan__event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__move_it_plan__event

            from service_msgs.msg import ServiceEventInfo
            if ServiceEventInfo.__class__._TYPE_SUPPORT is None:
                ServiceEventInfo.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class MoveItPlan_Event(metaclass=Metaclass_MoveItPlan_Event):
    """Message class 'MoveItPlan_Event'."""

    __slots__ = [
        '_info',
        '_request',
        '_response',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'info': 'service_msgs/ServiceEventInfo',
        'request': 'sequence<interbotix_moveit_interface_msgs/MoveItPlan_Request, 1>',
        'response': 'sequence<interbotix_moveit_interface_msgs/MoveItPlan_Response, 1>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['service_msgs', 'msg'], 'ServiceEventInfo'),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['interbotix_moveit_interface_msgs', 'srv'], 'MoveItPlan_Request'), 1),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['interbotix_moveit_interface_msgs', 'srv'], 'MoveItPlan_Response'), 1),  # noqa: E501
    )

    def __init__(self, **kwargs):
        if 'check_fields' in kwargs:
            self._check_fields = kwargs['check_fields']
        else:
            self._check_fields = ros_python_check_fields == '1'
        if self._check_fields:
            assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
                'Invalid arguments passed to constructor: %s' % \
                ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from service_msgs.msg import ServiceEventInfo
        self.info = kwargs.get('info', ServiceEventInfo())
        self.request = kwargs.get('request', [])
        self.response = kwargs.get('response', [])

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.info != other.info:
            return False
        if self.request != other.request:
            return False
        if self.response != other.response:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def info(self):
        """Message field 'info'."""
        return self._info

    @info.setter
    def info(self, value):
        if self._check_fields:
            from service_msgs.msg import ServiceEventInfo
            assert \
                isinstance(value, ServiceEventInfo), \
                "The 'info' field must be a sub message of type 'ServiceEventInfo'"
        self._info = value

    @builtins.property
    def request(self):
        """Message field 'request'."""
        return self._request

    @request.setter
    def request(self, value):
        if self._check_fields:
            from interbotix_moveit_interface_msgs.srv import MoveItPlan_Request
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) <= 1 and
                 all(isinstance(v, MoveItPlan_Request) for v in value) and
                 True), \
                "The 'request' field must be a set or sequence with length <= 1 and each value of type 'MoveItPlan_Request'"
        self._request = value

    @builtins.property
    def response(self):
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value):
        if self._check_fields:
            from interbotix_moveit_interface_msgs.srv import MoveItPlan_Response
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) <= 1 and
                 all(isinstance(v, MoveItPlan_Response) for v in value) and
                 True), \
                "The 'response' field must be a set or sequence with length <= 1 and each value of type 'MoveItPlan_Response'"
        self._response = value


class Metaclass_MoveItPlan(type):
    """Metaclass of service 'MoveItPlan'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('interbotix_moveit_interface_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'interbotix_moveit_interface_msgs.srv.MoveItPlan')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__move_it_plan

            from interbotix_moveit_interface_msgs.srv import _move_it_plan
            if _move_it_plan.Metaclass_MoveItPlan_Request._TYPE_SUPPORT is None:
                _move_it_plan.Metaclass_MoveItPlan_Request.__import_type_support__()
            if _move_it_plan.Metaclass_MoveItPlan_Response._TYPE_SUPPORT is None:
                _move_it_plan.Metaclass_MoveItPlan_Response.__import_type_support__()
            if _move_it_plan.Metaclass_MoveItPlan_Event._TYPE_SUPPORT is None:
                _move_it_plan.Metaclass_MoveItPlan_Event.__import_type_support__()


class MoveItPlan(metaclass=Metaclass_MoveItPlan):
    from interbotix_moveit_interface_msgs.srv._move_it_plan import MoveItPlan_Request as Request
    from interbotix_moveit_interface_msgs.srv._move_it_plan import MoveItPlan_Response as Response
    from interbotix_moveit_interface_msgs.srv._move_it_plan import MoveItPlan_Event as Event

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
