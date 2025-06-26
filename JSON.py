import json

# some JSON:
x =  '{ "name":"Arun Jain", "age":32, "city":"Jaipur"}'

y = json.loads(x)

print(y['name'])

# a Python object (dict):
x = {
  "name": "Arun Jain",
  "age": 32,
  "city": "Jaipur"
}

# convert into JSON:
y = json.dumps(x,indent=4, separators=(". ", " = "),sort_keys=True)

# the result is a JSON string:
print(y)


#All DataType Conversion
print(json.dumps({"name": "Arun Jain", "age": 32}, indent=4))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))