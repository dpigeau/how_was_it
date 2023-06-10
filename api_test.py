import requests

baseurl = "https://services.surfline.com/kbyg/spots/forecasts/"
type = "wave"
params = {
    "spotId": "5842041f4e65fad6a7708890",
    "days": 1,
    "intervalHours": 1,
}
res = requests.get(baseurl + type, params=params).json()
len(res)
print(res["data"])