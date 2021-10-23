# meteostations-api
---
An api that can fetch live data from weather stations all over Greece.

It support most of the stations visible [here](https://www.meteo.gr/Gmap.cfm).

## Endpoints:
The api endpoints can be accessed with **GET** requests at:

- ip:port/api/available_stations
0 Returns all available stations and their corresponding *station_id*, *url*, and *area*
- ip:port/api/data?station=[station_id]
0 Returns all the available data a station can offer

## Data available:
The api will try to return the following data:

- Barometer
- Dewpoing
- Heat Index
- Monthly Rain
- Rain Rate
- Solar Radiation
- Storm Total
- Sunrise
- Sunset
- Temperature
- Today's Rain
- UV Index
- Wind
- Wind Chill
- Yearly Rain
- Date of data
- Station name
- Time of data
- *Today's Highest* Heat Index
- *Today's Highest* Rain Rate
- *Today's Highest* Solar Radiation
- *Today's Highest* UV Index
- *Today's Highest* Wind Gust
- *Today's Lowest* Wind Chill
- *Today's Highest and Lowest* Barometer
- *Today's Highest and Lowest* Dew Point
- *Today's Highest and Lowest* Humidity
- *Today's Highest and Lowest* Temperature

Note that not all of the stations are up and running, and some don't give all the data mentioned above.

## Active now:
There is an instance of the api running at:
https://meteostations-gr-api.herokuapp.com/api/

