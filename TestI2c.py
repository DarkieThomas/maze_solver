import time
import VL53L0X
from smbus2 import SMBus

TCA_ADDR = 0x70

bus = SMBus(1)

def select_channel(channel):
    bus.write_byte(TCA_ADDR, 1 << channel)
    time.sleep(0.01)

sensors = []

for ch in range(3):

    select_channel(ch)

    sensor = VL53L0X.VL53L0X(
        i2c_bus=1,
        i2c_address=0x29
    )

    sensor.open()
    sensor.start_ranging(
        VL53L0X.Vl53l0xAccuracyMode.BEST
    )

    sensors.append(sensor)

print("Sensors initialized")

while True:

    for ch in range(3):

        select_channel(ch)

        distance = sensors[ch].get_distance()

        print(f"Sensor {ch}: {distance} mm")

    print("------")

    time.sleep(0.2)
