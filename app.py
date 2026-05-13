# Daniel Medina
# CST 205 Final Project
#5/13/26
#this is for the app with our routes, connections to index, recipie html files, and history and category.
# Culture and Food Recipe Finder

from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap5
from api_helpers import get_areas, get_meals_by_area, get_meal_details, areas_with_meals, get_meal_instructions, add_history, get_history, get_meals_by_catagory, clear_history
# Daniel Medina EXPLANATION: FLASK CREATES THE WEB APPLICATION, RENDER TEMPLATE LOADS THE HTML FILES FROM TEMPLATES/
#Daniel Medina REQUEST GETS FORM DATA SUBMITTED BY USER
#Daniel Medina URL_FOR CREATES CORRECT FLASK LINKS

app = Flask(__name__)
bootstrap = Bootstrap5(app)
not_first = False

#Daniel Medina set up our routes
@app.route("/")
def home():
    areas = get_areas()
    return render_template("index.html", areas=areas)
 #

@app.route("/foods", methods=["GET", "POST"])
def foods():
    area = request.form.get("area") or request.args.get("area")
    if not area:
        return "No area selected", 400
    
    meals = get_meals_by_area(area)

    chosen_meals = meals

    return render_template("foods.html", area=area, meals=chosen_meals)
#daniel Medina home route runs when user visits homepage, calls api helper function, then sends culture list to index
#food recieves selected culture uses request form area then gets meals for that culture through api, list slice then to get 5 meals, then send results to food.html.

@app.route("/recipe/<meal_id>")
def recipe(meal_id):
    meal = get_meal_details(meal_id)
    mealinstr = get_meal_instructions(meal)
    print(mealinstr)
    # Phoenix, adds the recipe being accessed to the history dict
    add_history(meal_id, meal)
    print(meal)
    return render_template("recipe.html", meal=meal, instructions = get_meal_instructions(meal))

# Phoenix Caine, route that runs when the user clicks "view history"
# Passes the dictionary of stored meal ids into the template

@app.route("/history")
def history():
    his = get_history()
    return render_template("history.html", history=his)

# Phoenix Caine, clears the history then redirects
@app.route("/cleared")
def clear():
    clear_history()
    return redirect(url_for('home'))

@app.route("/catagory")
def catagory(meal_id):
    catlist = get_meals_by_catagory(meal_id)
    return render_template("catagory.html", catlist = catlist)

if __name__ == "__main__":
    app.run(debug=True)
