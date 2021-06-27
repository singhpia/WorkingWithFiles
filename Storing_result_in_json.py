import json

#serializing
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
a = open("data_file.json",'r').read()
print(a)

quiz = {
        "sport": {
            "q1": {
                "question": "Which one is correct team name in NBA?",
                "options": [
                    "New York Bulls",
                    "Los Angeles Kings",
                    "Golden State Warriros",
                    "Huston Rocket"
                ],
                "answer": "Huston Rocket"
            }
        }
}

with open("json2.json", "w") as test_quiz:
    json.dump(quiz, test_quiz)

#taking file and storing
with open("C:\\Users\\Prateek.THINKPAD\\Downloads\\json_file.json","a+") as json_file:
    stu = json_file.read()
    json.dump(stu, json_file)

f = open("C:\\Users\\Prateek.THINKPAD\\Downloads\\json_file.json")
g = f.read()
print(g)

tst = json.loads(g)
print(tst)


#de-serializing:
json_string = {
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
v = json.loads(json_string)
print(v)
