import json

# Load the JSON file
with open('config.json', 'r') as file:
    config_data = json.load(file)

# Access values from the loaded JSON data
key1_value = config_data['key1']
key2_value = config_data['key2']
key3_items = config_data['key3']
