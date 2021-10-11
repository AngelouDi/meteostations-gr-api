import re

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

    for data_values in [humidity, pressure, temp, pressure]:
        if len(data_values) == 2:
            high_value = data_values[0]
            low_value = data_values[1]
            high_time = times[0]
            low_time = times[1]
            return {"High": {"value": high_value, "time": high_time}, "Low": {"value": low_value, "time": low_time}}


def split_string_data(string_data):
    time = re.findall("\d?\d:\d\d", string_data)
    temp = re.findall("\d\d.\d°C", string_data)
    wind = re.findall("\d\d.\d", string_data)
    pressure = re.findall("\d\d\d\d\.\d", string_data)

    if pressure:
        pressure[0] += " hPa"
    for value in [temp, wind, pressure]:
        if value:
            return {"value": value[0], "time": time[0]}


def get_live_data(soup):
    for data_name in live_data_names:
        result = soup.find(text=data_name)

        if result:
            value = result.find_next("td").text.strip()
            data[data_name] = value
            # print(result.text)
            # print(value)


def get_highs_lows(soup):
    high_low_names = ["High Temperature", "High Humidity", "High Dewpoint", "High Barometer"]  # change dew point
    for data_name in high_low_names:
        result = soup.find(text=data_name).find_next("td").text.strip()
        split_string_double_data(result)
        data_name = re.sub("High", "High/Low", data_name)
        data_name = re.sub("Dewpoint", "Dew Point", data_name)
        data[data_name] = split_string_double_data(result)
        # print(split_string_double_data(result))


def get_today_highs(soup):
    today_highs_names = ["High Wind Gust", "High Rain Rate", "Low Wind Chill", "High Heat Index"]
    for data_name in today_highs_names:
        result = soup.find(text=data_name).find_next("td").text.strip()
        data[data_name] = split_string_data(result)
        # print(data_name)
        # print(value)
        # print(time)


def get_data(soup):
    # get_metadata(soup)
    get_live_data(soup)
    get_highs_lows(soup)
    get_today_highs(soup)
    return data
