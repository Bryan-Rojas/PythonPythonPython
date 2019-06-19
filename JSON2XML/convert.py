from json2xml import json2xml, readfromurl, readfromstring, readfromjson

# get the xml from an URL that return json
data = readfromurl("https://coderwall.com/vinitcool76.json")
print(json2xml.Json2xml(data).to_xml())
print('-----------------------------------------')

# get the xml from a json string
data = readfromstring(
    '{"login":"mojombo","id":1,"avatar_url":"https://avatars0.githubusercontent.com/u/1?v=4"}'
)
print(json2xml.Json2xml(data, wrapper="custom", indent=8).to_xml())
print('-----------------------------------------')

# get the data from an URL
# check for empty
data = readfromjson("example.json")
print(json2xml.Json2xml(data).to_xml())
print('-----------------------------------------')