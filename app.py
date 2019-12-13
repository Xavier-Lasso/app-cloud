from flask import Flask, request, render_template
from mongo_requests import S1, S2, C1, C2, D2

application = Flask("app_cloud_application")

@application.route("/user", methods=["GET"])
def user():
    genres = C1()
    return render_template("user.html", genres=genres)

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
    resultsD2 = D2()
    return render_template("analyst.html", resultsD2=resultsD2)

@application.route("/analyst/genre/<userSex>", methods=["GET"])
def getTopGenre(userSex):
    topNb = int(request.args["q"])
    genres = C2(userSex, topNb)
    return render_template("c2.html", genres=genres)


if __name__ ==  "__main__":
    application.run(host="0.0.0.0", port=80)