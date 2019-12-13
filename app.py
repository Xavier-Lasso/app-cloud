from flask import Flask, request, json, jsonify, make_response, render_template, Response
from bson import json_util
from mongo_requests import S1, S2, C2

application = Flask("app_cloud_application")

@application.route("/user", methods=["GET"])
def user():
    if(request.method == "GET"):
        return render_template("user.html")
    return "App Cloud: Project"

@application.route("/user/movies/<id>", methods=["GET"])
def getMoviesId(id):
    movies = S1(int(id))
    return render_template("movies.html", movies=movies)

@application.route("/user/movies/year/<year>", methods=["GET"])
def getMoviesYear(year):
    movies = S2(int(year))
    return render_template("movies.html", movies=movies)

@application.route("/analyst")
def analyst():
    return render_template("analyst.html")

@application.route("/analyst/genre/<userSex>", methods=["GET"])
def getTopGenre(userSex):
    topNb = int(request.args["q"])
    genres = C2(userSex, topNb)
    return render_template("c2.html", genres=genres)


if __name__ ==  "__main__":
    application.run(host="0.0.0.0", port=80)