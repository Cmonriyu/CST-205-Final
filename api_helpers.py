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

def areas_with_meals():
    areasList = get_areas()
    areasWithMeals = []
    for area in areasList:
        areaMeals = get_meals_by_area(area)
        if areaMeals:
            areasWithMeals.append(area)
    return areasWithMeals

def get_meal_instructions(meal):
    lines = [line for line in meal["strInstructions"].splitlines() if line.strip()]
    count = 1
    
    newlines = []

    for line in lines:
        clean = line.lower().strip()

        if clean.startswith("step"):
            continue

        newlines.append(f"Step {count}.")
        newlines.append(line)

        count += 1



#     # if line[0] == "1" or line[0].lower() == "step 1":

    # for line in lines:
    #     if line.lower().strip() == str(count) or line.lower().strip() == "step " + str(count):
    #         line = "Step " + str(count) + ". new"
    #         count += 1
    #     else:
    #         line = f"Step {count}. {line}"
    #         count += 1

    return newlines