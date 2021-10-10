import re
import requests
from bs4 import BeautifulSoup


def split_string_data(string_data):
    string_data = string_data.replace("\t", "")
    string_data = string_data.replace("\n", " ").strip()
    string_data = re.split("(?<=:\d\d) ", string_data)
    high_value = re.split(" at ", string_data[0])[0]
    high_time = re.split(" at ", string_data[0])[1]
    low_value = re.split(" at ", string_data[1])[0]
    low_time = re.split(" at ", string_data[1])[1]
    return {"High": {"value": high_value, "time": high_time}, "Low": {"value": low_value, "time": low_time}}


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


def get_metadata(soup):
    station = soup.find_all(class_="station_name")[1].text
    title = soup.find(class_="headline gradient").text
    time = re.findall("\d+:\d+", title)[0]
    date = re.findall("\d+\/\d+\/\d+", title)[0]
    data["station"] = station
    data["time"] = time
    data["date"] = date


def get_live_data(soup):
    live_data_names = ["Temperature", "Humidity", "Dewpoint", "Wind", "Barometer", "Today's Rain", "Rain Rate",
                       "Storm Total", "Monthly Rain", "Yearly Rain", "Wind Chill", "Heat Index", "Solar Radiation",
                       "UV Index", "Sunrise", "Sunset"]
    for data_name in live_data_names:
        result = soup.find(text=data_name).find_next("div").text
        data[data_name] = result
        # print(data_name)
        # print(result)


def get_highs_lows(soup):
    high_low_names = ["High Temperature", "High Humidity", "High Dew Point", "High Barometer"]
    for data_name in high_low_names:
        result = soup.find(text=data_name).find_next("div").text
        data[re.sub("High", "High/Low", data_name)] = split_string_data(result)
        # print(data_name)
        # print(split_data(result))


def get_today_highs(soup):
    today_highs_names = ["High Wind Gust", "High Rain Rate", "Low Wind Chill", "High Heat Index",
                         "High Solar Radiation",
                         "High UV Index"]
    for data_name in today_highs_names:
        result = soup.find(text=data_name).find_next("div").text.strip()
        value = re.split(" at ", result)[0]
        time = re.split(" at ", result)[1]
        data[data_name] = {"value": value, "time": time}
        # print(data_name)
        # print(value)
        # print(time)


def get_data(station):
    url = 'http://penteli.meteo.gr/stations/' + station
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    get_metadata(soup)
    get_live_data(soup)
    get_highs_lows(soup)
    get_today_highs(soup)
    return data
