import pymongo

client = pymongo.MongoClient("mongodb+srv://ineuron:ineuron1@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['myinfo']
collection = database["sudh"]


#data = collection.find({"companyName" : "iNeuron"})
data = collection.find({"courseOffered" :{"$gt" :"E"}})
for i in data :
    print(i)
