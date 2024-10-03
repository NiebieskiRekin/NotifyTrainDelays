import requests as r
import rich
import pydantic
import json

sroda_wlkp = "5103572"
poznan_glowny = "5103572"
poznan_staroleka = "5100226"

base_url = "https://kalkulatorkolejowy.pl/bilkom/api"
type = "departures"
mode = "normal"

get_departures_url = "/".join([base_url, type, mode, sroda_wlkp])

odjazdy_sroda = r.get(get_departures_url).json()

pociag_sroda_10_15 = "R 17503"
pociag_poznan_staroleka_20_27 = "KW 76218"

a = [f for f in odjazdy_sroda if f["trainCode"] == pociag_poznan_staroleka_20_27]

rich.print(a)
