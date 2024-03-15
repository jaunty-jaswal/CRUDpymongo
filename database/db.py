import pymongo
from bson.objectid import ObjectId
client = pymongo.MongoClient("mongodb+srv://jaunty:9410993055@mydb.drbzqzi.mongodb.net/")

db = client["mongo_data_new"] #dbase name
#collection
collection = db["user_details_new"]
def parser(data):
    return {
        "name":data["name"],
        "age":data["age"]
    }

def add_Data(data):
    try: 
        collection.insert_one(data)
        return True
    except Exception as e:
        print(e)
        return False
    
def read_Data():
    var = list()
    for i in collection.find():
        var.append(parser(i))   
    return var     

def update_Details(data):
    if(collection.find_one({"name":data.name})):
        collection.update_one({"name":data.name},{"$set":{"name":"new_name"}})
        return {"RESPONSE":"OK"}
    else:
        return {"RESPONSE":"CANNOT FIND"}
    
def delete_Details(data):
    if(collection.find_one({"name":data.name})):
        collection.delete_one({"name":data.name})
        return {"RESPONSE":f"{data.name} DELETED SUCCESSFULLY"}
    else:
        return {f"NO SUCH RECORD AS {data.name}"}   
    
def find_Details(data):
    ans = collection.find_one({"name":data.name})
    if ans:
        # if isinstance(ans["_id"],ObjectId):
        #     ans["_id"] = str(ans["_id"])
        #     return ans 
        ans.pop('_id',None) 
        return ans  
    else:
        return {"RESPONSE":"ERROR,resource not found"}



