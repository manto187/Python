import numpy as np 
import pandas as pd 
import os 

np.random.seed(42)

TOTAL_MISSIONS = 10000

os.makedirs("data", exist_ok=True)

countries = [
    "USA",
    "Russia",
    "China",
    "India",
    "Japan",
    "France",
    "UAE"
]

agencies = [
    "NASA",
    "SpaceX",
    "Roscosmos",
    "ISRO",
    "ESA",
    "CNSA",
    "JAXA"
]

rockets = [
    "Falcon 9",
    "Falcon Heavy",
    "Starship",
    "Soyuz",
    "GSLV Mk III",
    "Long March 5",
    "Ariane 6",
    "H-IIA"
]

launch_sites = [
    "Kennedy Space Center",
    "Baikonur Cosmodrome",
    "Satish Dhawan Space Centre",
    "Tanegashima Space Center",
    "Guiana Space Centre",
    "Jiuquan Satellite Launch Center"
]

weather_conditions = [
    "Clear",
    "Cloudy",
    "Rain",
    "Storm"
]

orbit_types = [
    "LEO",
    "MEO",
    "GEO",
    "Polar",
    "Sun-Synchronous"
]

satellite_types = [
    "Communication",
    "Military",
    "Navigation",
    "Scientific",
    "Weather"
]

failure_reasons = [
    "Engine Failure",
    "Fuel Leak",
    "Navigation Error",
    "Weather",
    "Communication Failure",
    "Software Bug",
    "No Failure"
]