import json

x= '{"name": "KAJAL","age" : 24,"CITY": "nashik"}'
y= json.loads(x)    #from json to python
print(y['name'])

z=json.dumps(x)    #from python to json
print(z)

abc = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(abc, indent=4))

print(json.dumps(abc, indent=4,separators=(".","=")))   #more readable data