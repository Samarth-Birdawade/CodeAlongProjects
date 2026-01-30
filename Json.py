import json

personal_data = {
    "Name": "Samarth",
    "Age": 23,
    "City": "Pune"
}

print(f"Personal Data: \n{personal_data}\n{type(personal_data)}")

json_data = json.dumps(personal_data)
print(f"JSON Data: \n{json_data}\n{type(json_data)}")

parsed_data = json.loads(json_data)
print(f"Parsed Data: \n{parsed_data}\n{type(parsed_data)}")

with open("persondata.json", 'w') as f:
    json.dump(personal_data, f, indent = 4)

with open("persondata.json", 'r') as f:
    loaded_data = json.load(f)
    print(f"{loaded_data}")