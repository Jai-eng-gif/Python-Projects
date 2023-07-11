import datetime
import time
from plyer import notification
import yfinance as yf

amzn = yf.Ticker("AMZN")
data = amzn.info
while True:
    notification.notify(
        title="To-Do List".format(datetime.date.today()),
        message="1.Current Price: {cp} \n2.Day Low: {dl} \n3.Day high: {dh}".format(
            cp=data["currentPrice"],
            dl=data["regularMarketDayLow"],
            dh=data["regularMarketDayHigh"],

        ),
        app_icon="D:/Python Project/notify.ico",
        timeout=5
    )
    time.sleep(10)


# print(msft.info)
