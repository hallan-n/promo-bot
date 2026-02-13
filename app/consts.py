from datetime import datetime, time

WORK_START = datetime.combine(datetime.today(), time(hour=11, minute=0))
WORK_END = datetime.combine(datetime.today(), time(hour=18, minute=0))

WORK_SECONDS = (WORK_START - WORK_END).seconds
MESSAGE_DELAY = 5
REDIS_CONN = "redis://localhost:6379"
