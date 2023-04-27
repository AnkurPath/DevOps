from pymongo import MongoClient


#MongoDB attribuites
mongodb_uri="mongodb+srv://root:localhost@cluster0.esvnakk.mongodb.net/?retryWrites=true&w=majority"
port = 8000

client = MongoClient(mongodb_uri, port)
db=client["project_1"]         # project_1 is database name

