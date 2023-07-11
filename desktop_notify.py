from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title="Drink Water",
            message="drink water half hour over",
            app_icon="D:/Python Project/water.ico",
            timeout=5
        )
        time.sleep(3600)

# to run the file automatic without running code
# pythonw file.py
