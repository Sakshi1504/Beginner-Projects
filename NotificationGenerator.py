import time
from plyer import notification

if __name__ == '__main__':
    notification.notify(
        title="This is my first custom notification!!",
        message="I will learn everything.",
        #app_icon="C:\\Users\\lenovo\\PycharmProjects\\pythonProject\\pythonProject\\NotificationSystem\\pasye.ico",
        timeout=500
    )
    time.sleep(60*60)
