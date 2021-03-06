from json import dumps
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)



@app.route("/")
@app.route("/get_properties")
def get_properties():
    properties = mongo.db.properties.find()
    return render_template("properties.html", properties=properties)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    properties = mongo.db.properties.find({"$text": {"$search": query}})
    return render_template("properties.html", properties=properties, query=query)

@app.route("/filter")
def filter():
    properties = mongo.db.properties.find({"price":{"$lte":"150000"}})
    return render_template("properties.html", properties=properties)

@app.route("/filter200k")
def filter200k():
    properties = mongo.db.properties.find({"price":{"$lte":"200000"}})
    return render_template("properties.html", properties=properties)

@app.route("/filter250k")
def filter250k():
    properties = mongo.db.properties.find({"price":{"$lte":"250000"}})
    return render_template("properties.html", properties=properties)

@app.route("/filter275k")
def filter275k():
    properties = mongo.db.properties.find({"price":{"$lte":"275000"}})
    return render_template("properties.html", properties=properties)

@app.route("/filter300k")
def filter300k():
    properties = mongo.db.properties.find({"price":{"$lte":"300000"}})
    return render_template("properties.html", properties=properties)

@app.route("/filter320k")
def filter320k():
    properties = mongo.db.properties.find({"price":{"$lte":"320000"}})
    return render_template("properties.html", properties=properties)





@app.route("/property_detail/<property_id>")
def property_detail(property_id):
    property_id = mongo.db.properties.find({
        "_id": ObjectId(property_id),
    })
    return render_template("property_detail.html", property_id=property_id)



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
        


