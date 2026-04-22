# api_helpers.py
# helper functions for TheMealDB API

import requests

AREA_LIST_URL = "https://www.themealdb.com/api/json/v1/1/list.php?a=list"
FILTER_BY_AREA_URL = "https://www.themealdb.com/api/json/v1/1/filter.php?a="
LOOKUP_MEAL_URL = "https://www.themealdb.com/api/json/v1/1/lookup.php?i="


def get_areas():
    response = requests.get(AREA_LIST_URL)
    data = response.json()

    areas = []

    for item in data["meals"]:
        areas.append(item["strArea"])

    return areas


def get_meals_by_area(area):
    response = requests.get(FILTER_BY_AREA_URL + area)
    data = response.json()

    meals = []

    if data["meals"] is not None:
        for item in data["meals"]:
            meals.append(item)

    return meals


def get_meal_details(meal_id):
    response = requests.get(LOOKUP_MEAL_URL + meal_id)
    data = response.json()

    if data["meals"] is not None:
        return data["meals"][0]

    return None
