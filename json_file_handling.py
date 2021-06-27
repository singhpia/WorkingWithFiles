import json

#using load function
with open("C:\\Users\\Prateek.THINKPAD\\Downloads\\json_file.json") as file_json:
    content = json.load(file_json)
    print(content)

#retrieving the value(s)
print(content['quiz']['sport']['q1']['options'])
a = content['quiz']['sport']['q1']['options']
print(a)

#using loads function when variable has a json format string
string_Var= """
{
    "Name":  "bits",
    "Status":  4
}
"""

#parse the string in json
b = json.loads(string_Var)
print(b['Name'])
print(b['Status'])