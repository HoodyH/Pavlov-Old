from datetime import datetime, timedelta


def log_data():

    log_time_by_day = []

    now = datetime.utcnow()
    last_log_time_day = now.replace(day=1)
    # datetime.strptime()
    td = now.replace(hour=0, minute=0, second=0, microsecond=0)
    sub = td - last_log_time_day.replace(hour=0, minute=0, second=0, microsecond=0)
    if sub > timedelta(days=1):
        i = 1


log_data()
