import requests
from datetime import datetime
from api import get_forecast
from dataclasses import dataclass

@dataclass
class SurflineForecast:

    spot_id: str
    timestamp: datetime = datetime.now()

    def swell(self):
        waves = get_forecast("wave", self.spot_id, self.timestamp)
        swell = waves["swells"][0]
        swell["swell_at"] = datetime.fromtimestamp(waves["timestamp"])
        return swell
    
    def wind(self):
        wind = get_forecast("wind", self.spot_id, self.timestamp)
        timestamp = wind.pop("timestamp")
        wind["wind_at"] = datetime.fromtimestamp(timestamp)
        wind.pop("utcOffset")
        return wind
    
    def tide(self):
        tide = get_forecast("tides", self.spot_id, self.timestamp)
        timestamp = tide.pop("timestamp")
        tide["tide_at"] = datetime.fromtimestamp(timestamp)
        tide.pop("utcOffset")
        return tide
    

if __name__=="__main__":
    spot_id = "604f9d394046841199fe5d9b" #Llandudno
    f = SurflineForecast(spot_id)
    print(f.swell())
    print(f.wind())
    print(f.tide())
