from dynamixel_sdk import *
import time
import random


STATE_FILE = "/tmp/robot_state"

def is_running():
    try:
        return open(STATE_FILE).read().strip() == "1"
    except:
        return False

DEVICENAME = '/dev/ttyACM0' #OpenCR board
BAUDRATE = 1000000 #baudrate default 1000000
PROTOCOL_VERSION = 2.0

#DXL_ID = 1
DXL_ID_Left_Front_Motor = 4
DXL_ID_Right_Front_Motor = 3
DXL_ID_Left_Rear_Motor = 2
DXL_ID_Right_Rear_Motor = 1
dxl_id = 0
DXL_ID_Victim_Motor = 5 

speed = 100 # Basic Speed 
rotate_speed = 100 #Scorost povorotov 

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

def set_motor_velocity(dxl_id, velocity):
    
    if velocity < 0:
        velocity = (1 << 32) + velocity

    packetHandler.write4ByteTxRx(

        portHandler,
        dxl_id,
        ADDR_GOAL_VELOCITY,
        velocity
    )

def forward(speed):
    set_motor_velocity(DXL_ID_Left_Front_Motor, -speed)
    set_motor_velocity(DXL_ID_Right_Front_Motor, -speed)
    set_motor_velocity(DXL_ID_Left_Rear_Motor, -speed)
    set_motor_velocity(DXL_ID_Right_Rear_Motor, -speed)

def back(speed):
    set_motor_velocity(DXL_ID_Left_Front_Motor, speed)
    set_motor_velocity(DXL_ID_Right_Front_Motor, speed)
    set_motor_velocity(DXL_ID_Left_Rear_Motor, speed)
    set_motor_velocity(DXL_ID_Right_Rear_Motor, speed)

def stop():
    set_motor_velocity(DXL_ID_Left_Front_Motor, 0)
    set_motor_velocity(DXL_ID_Right_Front_Motor, 0)
    set_motor_velocity(DXL_ID_Left_Rear_Motor, 0)
    set_motor_velocity(DXL_ID_Right_Rear_Motor, 0)

def turn_left(rotate_speed):
    set_motor_velocity(DXL_ID_Left_Front_Motor, -rotate_speed)
    set_motor_velocity(DXL_ID_Right_Front_Motor, rotate_speed)
    set_motor_velocity(DXL_ID_Left_Rear_Motor, -rotate_speed)
    set_motor_velocity(DXL_ID_Right_Rear_Motor, rotate_speed)

def turn_right(rotate_speed):
    set_motor_velocity(DXL_ID_Left_Front_Motor, rotate_speed)
    set_motor_velocity(DXL_ID_Right_Front_Motor, -rotate_speed)
    set_motor_velocity(DXL_ID_Left_Rear_Motor, rotate_speed)
    set_motor_velocity(DXL_ID_Right_Rear_Motor, -rotate_speed)

def stop_all():
    for motor in [
        DXL_ID_Left_Front_Motor,
        DXL_ID_Right_Front_Motor,
        DXL_ID_Left_Rear_Motor,
        DXL_ID_Right_Rear_Motor
    ]:
        packetHandler.write4ByteTxRx(
            portHandler,
            motor,
            ADDR_GOAL_VELOCITY,
            0
        )


try:
    while True:

        if not is_running():
            stop_all()
            time.sleep(0.1)
            continue

            
        forward(speed)
        time.sleep(3)
        stop()
        time.sleep(0.5)
        direction = random.choice(["left", "right"])
        if direction == "left":

            turn_left(rotate_speed)
            
        else: 
        
            turn_right(rotate_speed)
        
        time.sleep(2.4) # Velichina povorota na 90 gradusov po suti eto vse chto mojno trogat :)

        stop()
        time.sleep(0.5)  

        back(speed)
        time.sleep(1.2) # // Nazad viravnivaemsa po stene. nu i eto toje
        stop()
        time.sleep(0.5)  

except KeyboardInterrupt:
    
    stop()

    print("stopped")
