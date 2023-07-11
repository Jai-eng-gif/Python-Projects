from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title="Drink Water",
            message="It's time to drink some water and quench your thirst. Remember, proper hydration is essential for your well-being and overall health.",
            app_icon="D:/Python Project/water.ico",
            timeout=5
        )
        time.sleep(3600)


