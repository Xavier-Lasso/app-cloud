import pymongo

from sshtunnel import SSHTunnelForwarder
from bson.code import Code

MONGO_HOST = "devincimdb1036.westeurope.cloudapp.azure.com"
MONGO_DB = "movieLens"
MONGO_USER = "administrateur"
MONGO_PASS = "V8eOFR%_"

server = SSHTunnelForwarder(
    MONGO_HOST,
    ssh_username=MONGO_USER,
    ssh_password=MONGO_PASS,
    remote_bind_address=('localhost', 27017)
)
server.start()
client = pymongo.MongoClient('localhost', server.local_bind_port) # server.local_bind_port is assigned local port
db = client[MONGO_DB]

def S1(movieid):
    res = db.movies.find({"movieid": movieid}, {"movieid": 1, "year": 1, "is_english": 1, "country": 1, "running_time": 1, "genre": 1})
    return res

def S2(year):
    res = db.movies.find({"year": year}, {"movieid": 1, "year": 1, "is_english": 1, "country": 1, "running_time": 1, "genre": 1})
    return res

def C1():
    res = db.movies.aggregate([
        {"$unwind": "$ratings"}, 
        {"$group": {"_id": {"movieid": "$movieid", "genre": "$genre"}, "moy": {"$avg": { "$toInt": "$ratings.value" }}, "tot": {"$sum":1}}}, 
        {"$match": {"tot": {"$gt":1000}}}, 
        {"$sort": {"moy": -1}}, 
        {"$group": {"_id": "$_id.genre" , "movieid": {"$first": "$_id.movieid"}, "moy": {"$first": "$moy"}}}
    ])
    return res
    
def C2(userSex, topNb):
    res = db.movies.aggregate([
        {"$unwind": "$ratings"}, 
        {"$match": {"ratings.user.u_gender" : userSex}}, 
        {"$group": {"_id":"$genre", "tot":{"$sum":1}}}, 
        {"$sort": {"tot":-1}}, 
        {"$limit": topNb}
    ])
    return res
"""
def D1():
    res = db.movies.aggregate([
	    {"$unwind": "$ratings"},
	    {"$project": {"movieid": 1, "age": {"$toInt": "$ratings.user.age"}}},
	    {"$project": {
	        "movieid": 1,
	        "range": {"$concat": [
	            {"$cond": [{"$lte": ["$age",0]}, "Unknown", ""]}, 
	            {"$cond": [{"$and": [ {"$gt":["$age", 0 ]}, {"$lt": ["$age", 18]}]}, "Under 18", ""]},
	            {$cond: [{"$and": [{"$gte":["$age",18]}, {"$lt":["$age", 25]}]}, "18 - 24", ""]},
	            {$cond: [{"$and": [{"$gte":["$age",25]}, {"$lt":["$age", 35]}]}, "25 - 34", ""]},
	            {$cond: [{"$and": [{"$gte":["$age",35]}, {"$lt":["$age", 51]}]}, "35 - 50", ""]},
	            {$cond: [{"$and": [{"$gte":["$age",51]}, {"$lt":["$age", 66]}]}, "51 - 65", ""]},
	            {$cond: [{"$gte": ["$age", 66]}, "Over 65", ""]}
	          ]}  
	        }    
	    },
	    {"$group": {"_id": {"movieid": "$movieid", "age": "$range"}, "count": {"$sum": 1}}}
	])
    
    let tr_age_doc = {}
	res.forEach(doc => {
	    roles = db.roles.find({"movieid": doc._id.movieid}, {actor: 1});
	    if(roles.hasNext()) {
	    roles.forEach( role => {
	    let tranche_age = doc._id.age
	    let actorid = role.actor.actorid
	    let count = doc.count
	    if(tranche_age in tr_age_doc) {
	        if(actorid in tr_age_doc[tranche_age]) {
	            tr_age_doc[tranche_age][actorid] += count;
	        } else {
	            tr_age_doc[tranche_age][actorid] = count;
	        }
	} else { 
	    tr_age_doc[tranche_age] = {};
	    tr_age_doc[tranche_age][actorid] = count;
	}
	})
	}
	})
	final_doc = {}
	for (key in tr_age_doc) {
	    let max = Object.keys(tr_age_doc[key]).reduce((a, b) => tr_age_doc[key][a] >tr_age_doc[key][b] ? a : b);
	    final_doc[key] = max;
	}

"""


def D2():
    mapFunction = Code(
        "function () {"
        "   if(this.ratings.length > 1000){"
        "       sum = 0;"
        "       for(i=0; i<this.ratings.length; i++){"
        "           sum += parseInt(this.ratings[i].value);"
        "       }"
        "       avg = sum / this.ratings.length;"
        "       emit(this.year, {\"avg\" : avg, \"movieid\": this.movieid});"
        "   }"
        "}")

    reduceFunction = Code(
        "function (key, values) {"
        "   avg = values[0].avg; movieid = values[0].movieid;"
        "   for(i=0; i< values.length; i++){"
        "       if(values[i].avg > avg){"
        "           avg = values[i].avg;"
        "           movieid = values[i].movieid;"
        "       }"
        "   }"
        "return {\"avg\" : avg, \"movieid\": this.movieid};"
        "}")

    res = db.movies.map_reduce(mapFunction, reduceFunction, "myresults").find()
    return res