import pymongo #mongo DB driver
import certifi #allows you to not have to provide your credentials all the time, it will remember it

con_str="mongodb+srv://mrsnkya:test@cluster0.exbyu4l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"# connection path to the mongo database
client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where()) #provides security for the connection to the server
db = client.get_database("project1") #creates a database
