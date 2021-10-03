import pymongo


client = pymongo.MongoClient("mongodb+srv://admin:<amdmin>@review-cluster."
                             "y16gr.mongodb.net/myFirstDatabase?"
                             "retryWrites=true&w=majority")

db = client.test

print('hello')