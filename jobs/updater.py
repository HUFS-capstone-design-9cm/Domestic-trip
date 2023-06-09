from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import scheduler_api

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduler_api, 'cron', second=10)
    # scheduler.add_job(scheduler_api, 'interval', seconds=1)
    scheduler.start()