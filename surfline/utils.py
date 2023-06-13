from datetime import datetime, timedelta


def get_nearest_hour_ts(timestamp: datetime):
    nearest_hour = timestamp.replace(minute=0, second=0, microsecond=0) + timedelta(
        hours=timestamp.minute // 30
    )
    return datetime.timestamp(nearest_hour)
