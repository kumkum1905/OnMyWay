from flask import Flask, jsonify, request, render_template
import json
import random

app = Flask(__name__)

with open("tourism.json", "r", encoding="utf-8") as file:
    tourism = json.load(file)["cities"]


@app.route("/")
def Home():
    return render_template("home.html", msg = "Manage Tourist Places")

@app.route("/search")
def search():

    city = request.args.get("city", "").strip()

    if city == "":
        return render_template(
            "home.html",
            msg="Please Enter a City"
        )

    for place in tourism:
        if place["city"].lower() == city.lower():
            return render_template("city.html",place=place)

    return render_template("home.html", msg=f"{city.title()} Not Found")

@app.route("/add", methods=["POST"])
def add():
    with open("tourism.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    tourism = data["cities"]
    city = request.form["city"].strip()
    state = request.form["state"].strip()
    heroImage = request.form["heroImage"].strip()
    description = request.form["description"].strip()

    places = [place.strip() for place in request.form["places"].split(",") if place.strip()]

    averageHotelPrice = request.form["averageHotelPrice"].strip()

    popularFoods = [ food.strip() for food in request.form["popularFoods"].split(",") if food.strip() ]

    bikeRent = request.form["bikeRent"].strip()
    scooterRent = request.form["scooterRent"].strip()
    carRent = request.form["carRent"].strip()

    for place in tourism:

        if place["city"].lower() == city.lower():

            return render_template( "home.html", msg=f"{city} already exists.")

    new_id = max(place["id"] for place in tourism) + 1 if tourism else 1

    new_place = {
        "id": new_id,
        "city": city,
        "state": state,
        "heroImage": heroImage,
        "description": description,
        "places": places,
        "averageHotelPrice": averageHotelPrice,
        "popularFoods": popularFoods,
        "vehicleRent": {
            "Bike": bikeRent,
            "Scooter": scooterRent,
            "Car": carRent
        }
    }

    tourism.append(new_place)

    with open("tourism.json", "w", encoding="utf-8") as file:
        json.dump(data,file,indent=4,ensure_ascii=False)

    return render_template("city.html",place=new_place)

@app.route("/update", methods=["POST"])
def update():
    with open("tourism.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    tourism = data["cities"]
    city = request.form["city"].strip()

    for place in tourism:

        if place["city"].lower() == city.lower():
            if request.form["state"].strip():
                place["state"] = request.form["state"].strip()

            if request.form["heroImage"].strip():
                place["heroImage"] = request.form["heroImage"].strip()

            if request.form["description"].strip():
                place["description"] = request.form["description"].strip()

            if request.form["places"].strip():
                place["places"] = [p.strip() for p in request.form["places"].split(",") if p.strip()]

            if request.form["averageHotelPrice"].strip():
                place["averageHotelPrice"] = request.form["averageHotelPrice"].strip()

            if request.form["popularFoods"].strip():
                place["popularFoods"] = [ food.strip() for food in request.form["popularFoods"].split(",") if food.strip() ]

            if request.form["bikeRent"].strip():
                place["vehicleRent"]["Bike"] = request.form["bikeRent"].strip()

            if request.form["scooterRent"].strip():
                place["vehicleRent"]["Scooter"] = request.form["scooterRent"].strip()

            if request.form["carRent"].strip():
                place["vehicleRent"]["Car"] = request.form["carRent"].strip()

            with open("tourism.json", "w", encoding="utf-8") as file:
                json.dump( data, file, indent=4, ensure_ascii=False )

            return render_template( "city.html", place=place )

    return render_template( "home.html", msg=f"{city} Not Found" )


@app.route("/delete", methods=["POST"])
def delete():
    with open("tourism.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    tourism = data["cities"]
    city = request.form["city"].strip()

    for i, place in enumerate(tourism):

        if place["city"].lower() == city.lower():
            tourism.pop(i)
            with open("tourism.json", "w", encoding="utf-8") as file:
                json.dump( data, file, indent=4, ensure_ascii=False )

            return render_template( "home.html", msg=f"{city} Deleted Successfully" )

    return render_template( "home.html", msg=f"{city} Not Found" )


if __name__ == "__main__":
    app.run(debug=True)