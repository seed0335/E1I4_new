# from pymongo import MongoClient
# client = MongoClient('mongodb+srv://leepari20:test@cluster0.bn6xn4r.mongodb.net/')
# db = client.dbsparta

doc = {
    'name':'name b',
    'about_me':'about_me b',
    'photo':'photo b',
    'imoge':'imoge b',
    'Q1':'Q1 b',
    'Q2':'Q2 b',
    'Q3':'Q3 b',
    'Q4':'Q4 b',
}
db.profiles.insert_one(doc) 