import pymongo
from pymongo import DESCENDING,MongoClient
from datetime import datetime
from bson.son import SON
import pprint
client = MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false")

#CREATE
simpleData = { "item": "journal", "qty": 25, "size": { "h": 14, "w": 21, "uom": "cm" }, "status": "A" }
#client.databaseName.collectionName.method
simpleResult = client.pyMongoExample.inventory.insert_one(simpleData)
pprint.pprint(simpleResult.acknowledged) #acknowledged (boolean flag to check if the item was added successfully)

client.pyMongoExample.inventory.remove({})
data=[
{ "item": "journal", "qty": 25, "size": { "h": 14, "w": 21, "uom": "cm" }, "status": "A", "tags": ["blank", "red"], "dim_cm": [ 14, 21 ] },
{ "item": "notebook", "qty": 50, "size": { "h": 8.5, "w": 11, "uom": "in" }, "status": "A","tags": ["red", "blank"], "dim_cm": [ 14, 21 ] },
{ "item": "paper", "qty": 100, "size": { "h": 8.5, "w": 11, "uom": "in" }, "status": "D", "tags": ["red", "blank", "plain"], "dim_cm": [ 14, 21 ] },
{ "item": "planner", "qty": 75, "size": { "h": 22.85, "w": 30, "uom": "cm" }, "status": "D" , "tags": ["blank", "red"], "dim_cm": [ 22.85, 30 ]},
{ "item": "postcard", "qty": 45, "size": { "h": 18.3, "w": 12, "uom": "cm" },"tags": ["blue"], "dim_cm": [ 10, 15.25 ] }]
dataResult=client.pyMongoExample.inventory.insert_many(data)
print(dataResult)

#--------------------------------------------->READ<--------------------------------------------------

#SELECT * FROM inventory
listAll=list(client.pyMongoExample.inventory.find( {} )) #We have to convert cursor object into a list
pprint.pprint(listAll)
print("-------------------------------->1<-----------------------------------")
#SELECT * FROM inventory WHERE status = "D"
journal=client.pyMongoExample.inventory.find_one( { "item": "journal" } )
pprint.pprint(journal)
print("-------------------------------->2<-----------------------------------")
#SELECT * FROM inventory WHERE status = "D"
listAll=list(client.pyMongoExample.inventory.find( { "status": "D" } ).sort("qty", DESCENDING).limit(10))
pprint.pprint(listAll)
print("-------------------------------->3<-----------------------------------")
#SELECT * FROM inventory WHERE status = "D" OR status = "A"
listAll=list(client.pyMongoExample.inventory.find( { "status": { "$in": [ "A", "D" ] } } ))
pprint.pprint(listAll)
print("-------------------------------->4<-----------------------------------")
#SELECT * FROM inventory WHERE status = "A" AND qty < 30
listAll=list(client.pyMongoExample.inventory.find( { "status":  "A" ,"qty":{ "$lt": 30 } } ))
pprint.pprint(listAll)
print("-------------------------------->5<-----------------------------------")
#SELECT * FROM inventory WHERE status = "A" OR qty < 30
listAll=list(client.pyMongoExample.inventory.find( { "$or":[{"status":"A"} ,{"qty":{ "$lt": 30 }}]}))
pprint.pprint(listAll)
print("-------------------------------->6<-----------------------------------")
#SELECT * FROM inventory WHERE status = "A" AND ( qty < 30 OR item LIKE "p%")
listAll=list(client.pyMongoExample.inventory.find( {"status":"A" , "$or": [ { "qty": { "$lt": 30 } }, { "item": "/^p/" }]}))
pprint.pprint(listAll)
print("-------------------------------->7<-----------------------------------")
#Selects all documents where the field size equals the document { h: 14, w: 21, uom: "cm" }
#Here when we are looking inside embedded documents is important to use the same order
listAll=list(client.pyMongoExample.inventory.find({ "size": { "h": 14, "w": 21, "uom": "cm" } } ))
pprint.pprint(listAll)
print("-------------------------------->8<-----------------------------------")
#Selects all documents where the field uom nested in the size field equals "in"
listAll=list(client.pyMongoExample.inventory.find({"size.uom": "in"} ))
pprint.pprint(listAll)
print("-------------------------------->9<-----------------------------------")
#Selects all documents where the field h nested in the size field is lower than 15
listAll=list(client.pyMongoExample.inventory.find({"size.h": {"$lt":15}} ))
pprint.pprint(listAll)
print("-------------------------------->10<-----------------------------------")
#Selects all documents where the nested field h is less than 15, the nested field uom equals "in", and the status field equals "D"
listAll=list(client.pyMongoExample.inventory.find({ "size.h": { "$lt": 15 }, "size.uom": "in", "status": "D" } ))
pprint.pprint(listAll)
print("-------------------------------->11<-----------------------------------")
#All documents where the field tags value is an array with exactly two elements, "red" and "blank", in the specified order
listAll=list(client.pyMongoExample.inventory.find( { "tags": ["red", "blank"] } ))
pprint.pprint(listAll)
print("-------------------------------->12<-----------------------------------")
#All documents where the field tags value is an array with exactly two elements, "red" and "blank", without regarding the order or other elements in the array
listAll=list(client.pyMongoExample.inventory.find( { "tags": { "$all": ["red", "blank"] } } ))
pprint.pprint(listAll)
print("-------------------------------->13<-----------------------------------")
#All documents where tags is an array that contains the string "red" as one of its elements
listAll=list(client.pyMongoExample.inventory.find( { "tags": "red" } ))
pprint.pprint(listAll)
print("-------------------------------->14<-----------------------------------")
#All documents where the array dim_cm contains at least one element whose value is greater than 25
listAll=list(client.pyMongoExample.inventory.find( { "dim_cm": {"$gt":25} } ))
pprint.pprint(listAll)
print("-------------------------------->15<-----------------------------------")
#One element can satisfy the greater than 15 condition and another element can satisfy the less than 20 condition, or a single element can satisfy both
listAll=list(client.pyMongoExample.inventory.find( { "dim_cm": {"$gt":15,"$lt":20} } ))
pprint.pprint(listAll)
print("-------------------------------->16<-----------------------------------")
#Documents where the dim_cm array contains at least one element that is both greater than ($gt) 22 and less than ($lt) 30
listAll=list(client.pyMongoExample.inventory.find( { "dim_cm": {"$elemMatch":{"$gt":22,"$lt":30}}} ))
pprint.pprint(listAll)
print("-------------------------------->17<-----------------------------------")
#All documents where the second element in the array dim_cm is greater than 25
listAll=list(client.pyMongoExample.inventory.find( { "dim_cm.1":{"$gt":25}} ))
pprint.pprint(listAll)
print("-------------------------------->18<-----------------------------------")
#All documents where the array tags has 3 elements
listAll=list(client.pyMongoExample.inventory.find( { "tags":{"$size":3}} ))
pprint.pprint(listAll)
print("-------------------------------->19<-----------------------------------")
#SELECT _id, item, status from inventory WHERE status = "A"
listAll=list(client.pyMongoExample.inventory.find({"status":"A"}, {"item": 1, "status": 1}))
pprint.pprint(listAll)
print("-------------------------------->20<-----------------------------------")
#SELECT item, status from inventory WHERE status = "A"
listAll=list(client.pyMongoExample.inventory.find({"status":"A"}, {"item": 1, "status": 1,"_id": 0}))
pprint.pprint(listAll)
print("-------------------------------->21<-----------------------------------")
#SELECT all the fields except status from inventory WHERE status = "A"
listAll=list(client.pyMongoExample.inventory.find({"status":"A"}, {"status": 0}))
pprint.pprint(listAll)
print("-------------------------------->22<-----------------------------------")
#selects item,status and the last tags element from the documents where status = "A"
# $slice projection operator to return the last element in the tags array
listAll=list(client.pyMongoExample.inventory.find({"status": "A"},{"item": 1, "status": 1, "tags": {"$slice": -1}}))
pprint.pprint(listAll)
print("-------------------------------->23<-----------------------------------")
#SELECT all the documents that doesn't have status
listAll=list(client.pyMongoExample.inventory.find({"status":None}))
pprint.pprint(listAll)
print("-------------------------------->24<-----------------------------------")
#SELECT all the documents that has status
listAll=list(client.pyMongoExample.inventory.find({"status":{"$exists": True}}))
pprint.pprint(listAll)
print("-------------------------------->25<-----------------------------------")

#--------------------------------------------->UPDATE<--------------------------------------------------
#Update the first document where item equals "paper"
listAll=client.pyMongoExample.inventory.update_one({"item": "paper"},
    {"$set": {"size.uom": "cm", "status": "P"},
    "$currentDate": {"lastModified": True}})
print("-------------------------------->26<-----------------------------------")
#Update all documents where qty is less than 50
listAll=client.pyMongoExample.inventory.update_many({"qty": {"$lt": 50}},
    {"$set": {"size.uom": "in", "status": "P"},
    "$currentDate": {"lastModified": True}})
print("-------------------------------->27<-----------------------------------")
#Update first document with item = pencil if it doesn't exist it create
listAll=client.pyMongoExample.inventory.replace_one({"item": "pencil"},
    {"item": "pencil", "qty": 30, "size": { "h": 15, "w": 2, "uom": "cm" },
    "status": "A","tags": ["yellow", "green"], "dim_cm": [ 14, 21 ] })
print("-------------------------------->28<-----------------------------------")
#Update first document with item = pencil if it doesn't exist it create
listAll=client.pyMongoExample.inventory.find_one_and_replace({"item": "pencil"},
    {"item": "pencil", "qty": 0, "size": { "h": 15, "w": 2, "uom": "cm" },
    "status": "D","tags": ["yellow"], "dim_cm": [ 14, 21 ] })
print("-------------------------------->29<-----------------------------------")

#--------------------------------------------->Subdocument<--------------------------------------------------
# Subdocument key order matters in a few of these examples so we have
# to use bson.son.SON instead of a Python dict.
client.pyMongoExample.inventory.delete_many({})
client.pyMongoExample.inventory.insert_many([
    {"item": "journal", "instock": [ SON([("warehouse", "A"), ("qty", 5)]), SON([("warehouse", "C"), ("qty", 15)])]},
    {"item": "notebook","instock": [SON([("warehouse", "C"), ("qty", 5)])]},
    {"item": "paper","instock": [SON([("warehouse", "A"), ("qty", 60)]), SON([("warehouse", "B"), ("qty", 15)])]},
    {"item": "planner", "instock": [SON([("warehouse", "A"), ("qty", 40)]), SON([("warehouse", "B"), ("qty", 5)])]},
    {"item": "postcard","instock": [SON([("warehouse", "B"), ("qty", 15)]),SON([("warehouse", "C"), ("qty", 35)])]}])
#selects all documents where an element in the instock array matches the specified document
listAll=list( client.pyMongoExample.inventory.find(
    {"instock": SON([("warehouse", "A"), ("qty", 5)])}))
pprint.pprint(listAll)
print("-------------------------------->30<-----------------------------------")
#In this case it wont return anything because there are no elements with the specified order
listAll=list( client.pyMongoExample.inventory.find(
    {"instock": SON([("qty", 5),("warehouse", "A")])}))
pprint.pprint(listAll)
print("-------------------------------->31<-----------------------------------")
#selects all documents where the instock array has as its first element a document that contains the field qty whose value is less than or equal to 20
listAll=list( client.pyMongoExample.inventory.find({'instock.0.qty': {"$lte": 20}}))
pprint.pprint(listAll)
print("-------------------------------->32<-----------------------------------")