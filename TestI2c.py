import time
import board
import busio
import adafruit_vl53l0x

from smbus2 import SMBus

# Адрес TCA9548A
TCA_ADDR = 0x70

# Открываем I2C
i2c = busio.I2C(board.SCL, board.SDA)

# SMBus для управления мультиплексором
bus = SMBus(1)

def select_channel(channel):
    """
    Выбор канала TCA9548A
    """
    bus.write_byte(TCA_ADDR, 1 << channel)
    time.sleep(0.01)

# Создаем объекты датчиков
sensors = []

for ch in range(3):
    select_channel(ch)

    sensor = adafruit_vl53l0x.VL53L0X(i2c)

    sensors.append(sensor)

print("Датчики инициализированы")

while True:

    for ch in range(3):

        select_channel(ch)

        distance = sensors[ch].range

        print(f"Sensor {ch}: {distance} mm")

    print("-----")

    time.sleep(0.5)
