from typing import Dict
import requests
from datetime import datetime
from utils import get_nearest_hour_ts
import os

BASE_URL = "https://services.surfline.com/kbyg/spots/forecasts/"

def get_forecast(type:str, spot_id: str, timestamp: datetime) -> Dict:
    params = {
        "spotId": spot_id,
        "days": 1,
        "intervalHours": 1,
    }
    url = os.path.join(BASE_URL, type)
    forecasts = requests.get(url, params=params).json()["data"][type]

    unix_timestamp = get_nearest_hour_ts(timestamp)
    for f in forecasts:
        if f["timestamp"] == unix_timestamp:
            return f
    
    return None

if __name__=="__main__":
    spot_id = "604f9d394046841199fe5d9b" #Llandudno
    timestamp = datetime.now()

    print(get_forecast("wave", spot_id, timestamp))
    print(get_forecast("wind", spot_id, timestamp))
    print(get_forecast("tides", spot_id, timestamp))