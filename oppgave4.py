import requests
import pandas as pd

def work_data(data_dict):

    df = pd.DataFrame(data_dict)
    



url = "https://api.met.no/weatherapi/nowcast/2.0/complete?lat=59.9333&lon=10.7166"
headers = {"User-Agent": "WeatherTest/1.0 skybert@gmail.com"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    result = response.json()
    work_data(result)
else:
    print(f"Error: {response.status_code}")
    print(response.text)