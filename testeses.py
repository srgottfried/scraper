import json

file = open("config/options.json", mode="r")
content = file.read()

format_content = json.loads(content)

for x in format_content["labels"]:
    print(x)