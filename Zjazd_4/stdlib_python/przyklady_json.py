import json

#tworze pythonowy obiekt

meble = ["krzesło", "szafa", "komoda","stół"]

print(type(meble))

meble_as_json = json.dumps(meble)
print(type(meble_as_json))


print(meble_as_json)

odczyatne_z_json_meble = json.loads(meble_as_json)

print(type(odczyatne_z_json_meble))

print(odczyatne_z_json_meble)


with open ("meble.json", "w") as f:
    json.dump(meble, f)
print (meble)

with open ("meble.json") as f:
    meble = json.load(f)
    meble.append("taboret")

with open ("meble.json", "w") as f:
    json.dump (meble, f)


print (meble)

