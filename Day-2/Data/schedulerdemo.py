#pip install schedule

import schedule
import time

def export():
    #export csv to json data
    print("Export Completed Successfully")

schedule.every(1).minute.do(export)
schedule.every().hour.do(export)
schedule.every().day.at("17:00").do(export)

while 1:
    schedule.run_pending()
    print("Hi All")
    time.sleep(1)