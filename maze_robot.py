from dynamixel_sdk import *


DEVICENAME = '/dev/ttyACM0' #OpenCR board
BAUDRATE = 1000000 #baudrate default 1000000
PROTOCOL_VERSION = 2.0

#DXL_ID = 1
DXL_ID_Left_Front_Motor = 4
DXL_ID_Right_Front_Motor = 3
DXL_ID_Left_Rear_Motor = 2
DXL_ID_Right_Rear_Motor = 1

DXL_ID_Victim_Motor = 5 



ADDR_TORQUE_ENABLE = 64
ADDR_OPERATING_MODE = 11
ADDR_GOAL_VELOCITY = 104

TORQUE_DISABLE = 0
TORQUE_ENABLE = 1
VELOCITY_MODE = 1

portHandler = PortHandler(DEVICENAME)
packetHandler = PacketHandler(PROTOCOL_VERSION)

if not portHandler.openPort():
    print("Failed open port")
    quit()

if not portHandler.setBaudRate(BAUDRATE):
    print("Failed baudrate")
    quit()

print("Connected")

# 1 disable torque
packetHandler.write1ByteTxRx(
    portHandler,
    DXL_ID_Victim_Motor,
    ADDR_TORQUE_ENABLE,
    TORQUE_DISABLE
)
packetHandler.write1ByteTxRx(
    portHandler,
    DXL_ID_Left_Front_Motor,
    ADDR_TORQUE_ENABLE,
    TORQUE_DISABLE
)
packetHandler.write1ByteTxRx(
    portHandler,
    DXL_ID_Right_Front_Motor,
    ADDR_TORQUE_ENABLE,
    TORQUE_DISABLE
)
packetHandler.write1ByteTxRx(
    portHandler,
    DXL_ID_Left_Rear_Motor,
    ADDR_TORQUE_ENABLE,
    TORQUE_DISABLE
)
packetHandler.write1ByteTxRx(
    portHandler,
    DXL_ID_Right_Rear_Motor,
    ADDR_TORQUE_ENABLE,
    TORQUE_DISABLE
)

print("Torque disabled")

# 2 set velocity mode
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
    portHandler,
    
    DXL_ID_Left_Front_Motor,
    ADDR_OPERATING_MODE,
    VELOCITY_MODE
    
)
print("Mode:", dxl_comm_result, dxl_error)
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
    portHandler,
    
    DXL_ID_Right_Front_Motor,
    ADDR_OPERATING_MODE,
    VELOCITY_MODE
)
print("Mode:", dxl_comm_result, dxl_error)
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
    portHandler,
    
    DXL_ID_Left_Rear_Motor,
    ADDR_OPERATING_MODE,
    VELOCITY_MODE
)
print("Mode:", dxl_comm_result, dxl_error)
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
    portHandler,
    
    DXL_ID_Right_Rear_Motor,

    ADDR_OPERATING_MODE,
    VELOCITY_MODE
)

print("Mode:", dxl_comm_result, dxl_error)

# 3 enable torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
    portHandler,
    DXL_ID_Left_Front_Motor,
    ADDR_TORQUE_ENABLE,
    TORQUE_ENABLE
    
    
)
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
    portHandler,
    DXL_ID_Right_Front_Motor,
    ADDR_TORQUE_ENABLE,
    TORQUE_ENABLE
)
print("Torque:", dxl_comm_result, dxl_error)
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
    portHandler,
    DXL_ID_Left_Rear_Motor,
    ADDR_TORQUE_ENABLE,
    TORQUE_ENABLE
)
print("Torque:", dxl_comm_result, dxl_error)
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
    portHandler,
    DXL_ID_Right_Rear_Motor,
    ADDR_TORQUE_ENABLE,
    TORQUE_ENABLE
)
print("Torque:", dxl_comm_result, dxl_error)
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
    portHandler,
    DXL_ID_Right_Rear_Motor,
    ADDR_TORQUE_ENABLE,
    TORQUE_ENABLE
)
print("Torque:", dxl_comm_result, dxl_error)
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
    portHandler,
    DXL_ID_Victim_Motor,
    
    ADDR_TORQUE_ENABLE,
    TORQUE_ENABLE
)
print("Torque:", dxl_comm_result, dxl_error)
# 4 set velocity
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(
    portHandler,
    DXL_ID_Left_Front_Motor,
        ADDR_GOAL_VELOCITY,
        int(0)
)
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(
    portHandler,
    DXL_ID_Right_Front_Motor,
        ADDR_GOAL_VELOCITY,
        int(0)
)
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(
    portHandler,
    DXL_ID_Left_Rear_Motor,
        ADDR_GOAL_VELOCITY,
        int(0)
)
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(
    portHandler,
    DXL_ID_Right_Rear_Motor,
        ADDR_GOAL_VELOCITY,
        int(0)
)

print("Velocity:", dxl_comm_result, dxl_error)
