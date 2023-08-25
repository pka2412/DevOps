#python library for json functions
import json
#python library for yaml functions
import yaml

#read yaml file
with open('temp/services.yaml') as file:
    yaml_data = yaml.safe_load(file)

#convert yaml data to json data
json_data = json.dumps(yaml_data,indent=3)

#display json data
print(json_data)
