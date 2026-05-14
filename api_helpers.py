# api_helpers.py
# helper functions for TheMealDB API
# Created by Riyu, Grabs information from MEALDB using requests. History request created by Phoenix.

import requests

AREA_LIST_URL = "https://www.themealdb.com/api/json/v1/1/list.php?a=list"
FILTER_BY_AREA_URL = "https://www.themealdb.com/api/json/v1/1/filter.php?a="
LOOKUP_MEAL_URL = "https://www.themealdb.com/api/json/v1/1/lookup.php?i="
history = {}

# Gets Areas
def get_areas():
    response = requests.get(AREA_LIST_URL)
    data = response.json()

    areas = []

    for item in data["meals"]:
        areas.append(item["strArea"])

    return areas

# Gets all meals by a certain area
def get_meals_by_area(area):
    response = requests.get(FILTER_BY_AREA_URL + area)
    data = response.json()

    meals = []

    if data["meals"] is not None:
        for item in data["meals"]:
            meals.append(item)

    return meals

# Gets meal details 
def get_meal_details(meal_id):
    response = requests.get(LOOKUP_MEAL_URL + meal_id)
    data = response.json()

    if data["meals"] is not None:
        return data["meals"][0]

    return None

# Gets only areas with meals, slow too many api requests
def areas_with_meals():
    areasList = get_areas()
    areasWithMeals = []
    for area in areasList:
        areaMeals = get_meals_by_area(area)
        if areaMeals:
            areasWithMeals.append(area)
    return areasWithMeals

# Splits instructions, and determines how it starts to properly add steps correctly
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

    return newlines

def add_history(id, meal):
    if id not in history:
        history[id]=meal

def get_history():
    return history


# Gathers all meals with belonging to a certain catagory
def get_meals_by_catagory(meal):

    catlist = []

    return catlist
