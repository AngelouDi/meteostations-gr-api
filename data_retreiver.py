import data_fetcher, data_fetcher_2
from bs4 import BeautifulSoup
import requests


def get_data(station):
    url = 'http://penteli.meteo.gr/stations/' + station
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    if '<!DOCTYPE html>' in html:
        return data_fetcher.get_data(soup)
    else:
        return data_fetcher_2.get_data(soup)
