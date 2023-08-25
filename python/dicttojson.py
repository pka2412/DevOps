#python library for json functions
import json

#define the dictionary data
dict_data = {
    "name": "Alice",
    "age": 25,
    "city": "Los Angeles",
    "is_student": True,
    "hobbies": ["reading", "painting", "hiking"],
    "address": {
        "street": "123 Main St",
        "city": "Los Angeles",
        "zipcode": "90001"
    }
}

#convert dictionary data to json data
#indent=3 formats the json data in organized manner
jsonData = json.dumps(dict_data, indent=3)

#display json data
print(jsonData)
