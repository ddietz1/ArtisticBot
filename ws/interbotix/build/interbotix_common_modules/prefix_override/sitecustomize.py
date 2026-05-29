import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/derek-dietz/MSAI/ComputerVision/Final_Project/ws/interbotix/install'
