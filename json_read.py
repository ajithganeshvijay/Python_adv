import json
# read operation of json file
#
# f=open('sample3.json','r')
# content=json.load(f)
# print(content)

u=open('file.json','r')
x=json.load(u)
print(x)

l=[{
  "name": "India",
  "capital": "Delhi",
  "population": 1007364357,
  "area": 552341695,
  "currency": "Rupees",
  "languages":"Hindi"
}]
u=open('data.json','w')
u.write(json.dumps(l))

# l=[{"name":"AJITH","age":20},
#     {"name":"amal","age":21}]
# f=open('data.json','w')
# f.write(json.dumps(l))