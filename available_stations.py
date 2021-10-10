import re
import requests
from bs4 import BeautifulSoup


def get_stations():
    data = {"stations": []}
    url = "https://www.meteo.gr/Gmap.cfm"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    for station in soup.find_all("option", class_="option"):
        area = re.sub("\*", "", station.text)
        station_url = station['value']
        id = re.split("\/", station_url)[-2]
        data["stations"].append({"station_id": id, "area": area, "official_url": station_url})
    return data
