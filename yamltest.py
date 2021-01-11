#!/usr/bin/python3
import yaml
fname = "data.yaml"

#dct = {"Jan": {"score": 3, "city": "Karvina"}, "David": {"score": 33, "city": "Brno"}}

#with open(fname, "w") as f:
#    yaml.dump(dct, f)

with open(fname) as f:
    newdct = yaml.safe_load(f)

print(newdct)
#newdct["Pipi"] = {"score": 1000000, "city": ["Delhi","Bangalore","Kolkata"],"salary": 180}
cities = ["Mandya","Shimoga","Mysore","Mangalore"]
for i in cities:
    newdct["Pipi"]["city"].append(i)

with open(fname, "w") as f:
    yaml.dump(newdct, f)
