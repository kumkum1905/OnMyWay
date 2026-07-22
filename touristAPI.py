'''
from flask import Flask, jsonify, request, render_template
import json
import random

app = Flask(__name__)

with open("tourism.json", "r", encoding="utf-8") as file:
    tourism = json.load(file)["cities"]




@app.route("/")
def Home():
    return render_template("home.html")


@app.route("/city")
def City():
    return render_template("city.html")


@app.route("/cities")
def Cities():
    return jsonify(tourism)

@app.route("/random")
def Random():
    return jsonify(random.choice(tourism))

@app.route("/<int:id>")
def WithID(id):

    for city in tourism:
        if city["id"] == id:
            return jsonify(city)

    return jsonify({"Message": "City Not Found!"}),404


@app.route("/search")
def Search():

    city_name = request.args.get("city")
    state_name = request.args.get("state")

    if city_name:
        print(city_name)
        print(tourism)
        for city in tourism:
            print("city")

            if city["city"].lower() == city_name.lower():
                print(city)
                return render_template("city.html",a = city)
                # return jsonify(city)
            

        return jsonify({
            "message":"City Not Found"
        }),404


    if state_name:

        data=[]

        for city in tourism:

            if city["state"].lower()==state_name.lower():
                data.append(city)

        return jsonify(data)

    return jsonify({
        "message":"No Search Parameter Provided"
    }),400

@app.route("/add", methods=["POST"])
def Add():

    d = request.get_json()

    d["id"] = len(tourism) + 1

    tourism.append(d)

    return jsonify({
        "Message": "New City Added",
        "Data": d
    })
@app.route("/<int:id>", methods=["DELETE"])
def Delete(id):

    for city in tourism:

        if city["id"] == id:

            tourism.remove(city)

            return jsonify({
                "Message": "City Deleted",
                "Data": city
            })

    return jsonify({"Message": "City Not Found"}),404



if __name__ == "__main__":
    app.run(debug=True)
'''

from flask import Flask, jsonify, request, render_template
import json
import random

app = Flask(__name__)

with open("tourism.json", "r", encoding="utf-8") as file:
    tourism = json.load(file)["cities"]


@app.route("/")
def Home():
    return render_template("home.html")


@app.route("/city")
def City():
    return render_template("city.html")


@app.route("/cities")
def Cities():
    return jsonify(tourism)


@app.route("/random")
def Random():
    return jsonify(random.choice(tourism))


@app.route("/<int:id>")
def WithID(id):
    for city in tourism:
        if city["id"] == id:
            return jsonify(city)
    return jsonify({"message": "City Not Found!"}), 404


@app.route("/search")
def Search():
    city_name = request.args.get("city")
    state_name = request.args.get("state")

    if city_name:
        for city in tourism:
            if city["city"].lower() == city_name.lower():
                return jsonify(city)
        return jsonify({"message": "City Not Found"}), 404

    if state_name:
        data = [c for c in tourism if c["state"].lower() == state_name.lower()]
        return jsonify(data)

    return jsonify({"message": "No Search Parameter Provided"}), 400


@app.route("/add", methods=["POST"])
def Add():
    d = request.get_json()
    d["id"] = len(tourism) + 1
    tourism.append(d)
    return jsonify({"Message": "New City Added", "Data": d})


@app.route("/<int:id>", methods=["DELETE"])
def Delete(id):
    for city in tourism:
        if city["id"] == id:
            tourism.remove(city)
            return jsonify({"Message": "City Deleted", "Data": city})
    return jsonify({"Message": "City Not Found"}), 404


if __name__ == "__main__":
    app.run(debug=True)