#python library for json functions
import json

#open the json file
f = open('temp/services.json')

#read the json data
#the data gets converted to dictionary data type
data = json.load(f)

#iterating through the data
for i in data['services']:
    #check whether the child item is of type dictionary
    if(type(data['services'][i]) == dict):
        print(f"{i}: {data['services'][i]['name']}")

#close the file
f.close()
