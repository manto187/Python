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


mission_ids = np.arange(1, TOTAL_MISSIONS + 1)
years = np.random.randint(
    2000, 
    2026,
    TOTAL_MISSIONS
)

countries_data = np.random.choice(
    countries,
    TOTAL_MISSIONS
)

agencies_data = np.random.choice(
    agencies,
    TOTAL_MISSIONS
)

rockets_data = np.random.choice(
    rockets,
    TOTAL_MISSIONS
)   

launch_sites_data = np.random.choice(
    launch_sites,
    TOTAL_MISSIONS
)   

payload = np.random.randint(
    500,
    50001,
    TOTAL_MISSIONS
)

launch_cost = np.random.randint(
    20, 
    501,
    TOTAL_MISSIONS

) * 1_000_000

fuel = np.random.randint(
    50,
    1001,
    TOTAL_MISSIONS
)

mission_duration = np.random.randint(
    1,
    366,
    TOTAL_MISSIONS
)

delay = np.random.randint(
    0,
    15,
    TOTAL_MISSIONS
)

crew_size = np.random.randint(
    0,
    8,
    TOTAL_MISSIONS
)

weather = np.random.choice(
    weather_conditions,
    TOTAL_MISSIONS
)

orbit = np.random.choice(
    orbit_types,
    TOTAL_MISSIONS
)

satellite = np.random.choice(
    satellite_types,
    TOTAL_MISSIONS
)

mission_status = np.random.choice(
    ["Success", "Failure"],
    TOTAL_MISSIONS,
    p=[0.90, 0.10]
)

failure_reason = []

for status in mission_status:

    if status == "Success":
        failure_reason.append("No Failure")

    else:
        failure_reason.append(
            np.random.choice(failure_reasons[:-1])
        )

revenue = launch_cost + np.random.randint(
    10,
    200,
    TOTAL_MISSIONS
) * 1_000_000

launch_month = np.random.randint(
    1,
    13,
    TOTAL_MISSIONS
)

launch_day = np.random.randint(
    1,
    29,
    TOTAL_MISSIONS
)
