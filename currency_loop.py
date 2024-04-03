import pandas as pd
from datetime import datetime
import time
import json



# alarm_set_cur = int(input("Set Alarm Timer In Minutes: "))
while True:
    set_alarm = datetime.now()
    showClock = "%s:%s:%s" % (set_alarm.hour, set_alarm.minute, set_alarm.second)
   
    print("\r", showClock, end="")
    time.sleep(1)

    # if set_alarm.minute == alarm_set_cur and set_alarm.second < 1:
    #     print("Alarm Activated")
    # if set_alarm.hour == 0 and set_alarm.minute == 42:
    try:
        if set_alarm.second == 42:
        # Fetch data from web and convert it into pandas data frame
            url = 'https://www.forex.com.pk/open_market_rates.asp'
            data = pd.read_html(url)
            currency_data = data[11]
            currency_data = currency_data.rename(columns={0: "Currency", 1: "Buying", 2: "Selling"})
            currency_data["Date"] = datetime.today().strftime("%d-%m-%Y %H:%M")
            currency_data["Date"] = pd.to_datetime(currency_data.Date)
        # currency_usd = currency_data.loc[currency_data["Currency"] == "US Dollar"]
            print("\n", currency_data)
            currency_data.to_csv("currency_data.csv", index=False)
            continue
    except Exception as e:
        print("\nUnable to fetch data from website Or server down --", e)
        continue


