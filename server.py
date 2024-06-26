#Create an API object
from flask import Flask, request # to import a library into the project / request comes with http
import json
from config import db

# define golbal variables
items = []

def fix_id(obj): #turn the object id from mongodb into a string/text
    obj["_id"]=str(obj["_id"])
    return obj
#
app = Flask(__name__) # To use the name of the server / for backwards compatibility

@app.get("/") # Try to get something from the server /= the root
def home():
    return "Whats up from flask"
@app.get("/hello") # Another API method
def hello():
    return "Hello, How may I help you"

#API endpoints
#JSON need to use whenever is trying to connect to the internet to be able to covert the languages
#create an API to this url: /api/about
#return your name as a meassage

@app.get("/api/about")
def about():
    me = {"name": "Christina"}
    return json.dumps(me)

@app.post("/api/products")
def saveProducts():
    product = request.get_json() #converts json to python object
    print (product)
    db.products.insert_one(product) #sends it to the database "project1"
    #mock the save
    #items.append(product)
    return json.dumps(fix_id(product)) #returns the product id in json format/string
    #



@app.get("/api/products")
def getProduct():
    return json.dumps(items)


app.run(debug = True) # every time I change something in the code, the changes will be reflected in the server