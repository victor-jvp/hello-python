from pymongo import MongoClient

# Base de datos local
# db_client = MongoClient().local

# Base de datos remota
db_client = MongoClient(
    "mongodb+srv://vvelizp:vvelizp@cluster0.twzvhgv.mongodb.net/?retryWrites=true&w=majority").test
