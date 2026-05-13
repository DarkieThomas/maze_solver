from gpiozero import Button
from signal import pause
import subprocess
import os
import signal
import time

button = Button(17, pull_up=True, bounce_time=0.2)

process = None

def toggle_program():
    global process

    # запуск
    if process is None or process.poll() is not None:

        print("START")

        process = subprocess.Popen(
            ["python3", "/home/darkie/ros2_ws/test.py"],
            preexec_fn=os.setsid   # ⭐ ВАЖНО: новая группа процессов
        )

    # остановка
    else:

        print("STOP")

        try:
            # убиваем всю группу процессов
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)

            # даём время закрыться
            time.sleep(1)

            # если не умерло — жёстко убиваем
            if process.poll() is None:
                os.killpg(os.getpgid(process.pid), signal.SIGKILL)

        except Exception as e:
            print("Kill error:", e)

        process = None

button.when_pressed = toggle_program

print("Ready")
pause()
