from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__)

app.config["SECRET_KEY"] = "2c5e068f60b7dbb1406874bccaf824efc5f34ffe"
app.config["MONGO_URI"] = "mongodb+srv://vasiljkovdarko:codewithvasiljkovdarko@cluster0.upiu5.mongodb.net/cluster0"


# username:vasiljkovdarko pw:9Y0tJOdWIq2wLvWb Cluster0
# mongodb database
mongodb_client = PyMongo(app)
db = mongodb_client.db


from application import routes
