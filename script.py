# TODO: Load timetable (station, departure time, train id) from json
# TODO: Load stations from json
# TODO: Send notification at 1h, 30m and 15m before

from typing import List, Dict
import requests as r
import rich
import pydantic
import json
import gevent
import datetime


class Station(pydantic.BaseModel):
    name: str
    id: str


class Trip(pydantic.BaseModel):
    start_station: str
    end_station: str
    planned_departure: datetime.datetime
    train_id: str


stations_file_path: str = "stations.json"
stations: List[Dict]
with open(stations_file_path, "r") as stations_file:
    stations = json.load(stations_file)

trips_file_path: str = "trips.json"
trips: list[Dict]
with open(trips_file_path, "r") as trips_file:
    trips = json.load(trips_file)

ntfy_topic: str
with open("config.json", "r") as config_file:
    config = json.load(config_file)
    ntfy_topic = config["ntfy_topic"]


base_url = "https://kalkulatorkolejowy.pl/bilkom/api"
type = "departures"
mode = "normal"


def get_departures_url(station: Dict):
    return "/".join([base_url, type, mode, station.get("id", "")])


rich.print(stations)
rich.print(trips)
rich.print(ntfy_topic)


def find_station(query: str):
    return [s for s in stations if s.get("name", "") == query][0]


odjazdy_sroda = r.get(get_departures_url(find_station("Środa Wielkopolska"))).json()

# gevent spawn later
rich.print(odjazdy_sroda)

# a = [f for f in odjazdy_sroda if f["trainCode"] == pociag_poznan_staroleka_20_27]

# r.post("https://ntfy.sh/" + ntfy_topic, data=f"{a}".encode(encoding="utf-8"))

# rich.print(a)
