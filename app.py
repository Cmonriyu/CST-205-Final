# Daniel Medina
# CST 205 Final Project
# Culture and Food Recipe Finder

from flask import Flask, render_template, request, url_for
from api_helpers import get_areas, get_meals_by_area, get_meal_details, areas_with_meals, get_meal_instructions, add_history, get_history
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    areas = get_areas()
    print(f"DEBUG: areas = {areas}")
    return render_template("index.html", areas=areas)


@app.route("/foods", methods=["GET", "POST"])
def foods():
    area = request.form.get("area") or request.args.get("area")
    if not area:
        return "No area selected", 400
    
    meals = get_meals_by_area(area)

    # only keep first 5 meals
    chosen_meals = meals[:5]

    return render_template("foods.html", area=area, meals=chosen_meals)


@app.route("/recipe/<meal_id>")
def recipe(meal_id):
    meal = get_meal_details(meal_id)
    mealinstr = get_meal_instructions(meal)
    print(mealinstr)
    add_history(meal_id, meal)
    return render_template("recipie.html", meal=meal, instructions = mealinstr)

@app.route("/history")
def history():
    his = get_history()
    return render_template("history.html", history=his)

if __name__ == "__main__":
    app.run(debug=True)