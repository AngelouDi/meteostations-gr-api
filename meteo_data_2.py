import requests
import re
from bs4 import BeautifulSoup



data = {"station": "", "time": "", "date": "", "Temperature": "", "Humidity": "", "Dewpoint": "",
        "Wind": "",
        "Barometer": "", "Today's Rain": "", "Rain Rate": "", "Storm Total": "", "Monthly Rain": "",
        "Yearly Rain": "",
        "Wind Chill": "", "Heat Index": "", "Solar Radiation": "", "UV Index": "", "Sunrise": "",
        "Sunset": "",
        "High/Low Temperature": {"High": {"value": "", "time": ""}, "Low": {"value": "", "time": ""}},
        "High/Low Humidity": {"High": {"value": "", "time": ""}, "Low": {"value": "", "time": ""}},
        "High/Low Dew Point": {"High": {"value": "", "time": ""}, "Low": {"value": "", "time": ""}},
        "High/Low Barometer": {"High": {"value": "", "time": ""}, "Low": {"value": "", "time": ""}},
        "High Wind Gust": {"value": "", "time": ""}, "High Rain Rate": {"value": "", "time": ""},
        "Low Wind Chill": {"value": "", "time": ""}, "High Heat Index": {"value": "", "time": ""},
        "High Solar Radiation": {"value": "", "time": ""}, "High UV Index": {"value": "", "time": ""}}


live_data_names = ["Temperature", "Humidity", "Dewpoint", "Wind", "Barometer", "Today's Rain", "Rain Rate",
                   "Storm Total", "Monthly Rain", "Yearly Rain", "Wind Chill", "Heat Index", "Solar Radiation",
                   "UV Index", "Sunrise", "Sunset"]

def split_string_double_data(string_data):
    times = re.findall("\d?\d:\d\d", string_data)
    temp = re.findall("\d\d.\d°C", string_data)
    humidity = re.findall("\d\d%", string_data)
    pressure = re.findall("\d\d\d\d\.\d", string_data)
    for i in range(len(pressure)):
        pressure[i] = pressure[i] + " hPa"
    print(times)
    print(humidity)
    print(pressure)
    print(temp)

    if times != []

def get_live_data(soup):
    for data_name in live_data_names:
        result = soup.find(text=data_name)

        if result:
            value = result.find_next("td").text.strip()
            data[data_name] = value
            # print(result.text)
            # print(value)

def get_highs_lows(soup):
    high_low_names = ["High Temperature", "High Humidity", "High Dewpoint", "High Barometer"] #change dew point
    for data_name in high_low_names:
        result = soup.find(text=data_name).find_next("td").text.strip()
        print(result)
        print("#########")
        split_string_double_data(result)
        # data[re.sub("High", "High/Low", data_name)] = split_string_data(result)
        # print(data_name)
        # print(split_data(result))


def get_data(station):
    url = 'http://penteli.meteo.gr/stations/' + station
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    # get_metadata(soup)
    get_live_data(soup)
    get_highs_lows(soup)
    # get_today_highs(soup)
    return data

get_data("athens")


