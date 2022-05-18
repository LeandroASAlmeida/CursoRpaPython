import scheduler
import time
from robo01 import bot01


scheduler.every().day.at("18:01").do(bot01)


while True:
    scheduler.run_pending()
    time.sleep(1)