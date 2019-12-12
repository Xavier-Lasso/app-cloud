from flask import Flask, request, json, jsonify, make_response, render_template, Response
from bson import json_util
from mongo_requests import S1, S2, C2

application = Flask("app_cloud_application")

@application.route("/app", methods=["GET"])
def index():
    if(request.method == "GET"):
        return render_template("user.html", movies=movies)
    return "App Cloud: Project"

    
"""
@application.route("/errors", methods=["GET"])
def getAllErrors():
    number = int(request.args["q"])
    errs = errorsAllWorkers(number)
    return render_template("errors.html", errs=errs)

@application.route("/errors/<worker>", methods=["GET"])
def getErrorsOneWorker(worker):
    number = int(request.args["q"])
    errs = errorsOneWorker(worker, number)
    return render_template("errors.html", errs=errs)

@application.route("/events", methods=["GET"])
def getEventsAllJobs():
    number = int(request.args["q"])
    events = eventsAllJobs(number)
    return render_template("events.html", events=events)
"""
@application.route("/movies/<id>", methods=["GET"])
def getMoviesId(id):
    number = int(request.args["q"])
    movies = eventsOneJob(job, number)
    return render_template("s1.html", events=events)
"""
@application.route("/graphs/weekly", methods=["GET"])
def graphWeeklyAllWorkers():
    graphJSONWeeks = graphWeeklyExecutionTimeAverageAllWorkers()
    return Response(graphJSONWeeks, mimetype='application/json; charset=utf-8')

@application.route("/graphs/monthly", methods=["GET"])
def graphMonthlyAllWorkers():
    graphJSONMonths = graphMonthlyExecutionTimeAverageAllWorkers()
    return Response(graphJSONMonths, mimetype='application/json; charset=utf-8')

@application.route("/graphs/weekly/<worker>", methods=["GET"])
def graphWeeklyOneWorker(worker):
    graphJSONMonths = graphWeeklyExecutionTimeAverageOneWorker(worker)
    return Response(graphJSONMonths, mimetype='application/json; charset=utf-8')

@application.route("/graphs/monthly/<worker>", methods=["GET"])
def graphMonthlyOneWorker(worker):
    graphJSONMonths = graphMonthlyExecutionTimeAverageOneWorker(worker)
    return Response(graphJSONMonths, mimetype='application/json; charset=utf-8')
"""

@application.route("/analyst/")
def analyst():
    return render_template("analyst.html")

@application.route("/analyst/genre/<userSex>", methods=["GET"])
def getTopGenre(userSex):
    topNb = int(request.args["q"])
    genres = C2(userSex, topNb)
    return render_template("c2.html", genres=genres)


if __name__ ==  "__main__":
    application.run(host="0.0.0.0", port=80)