import json
import csv

# JSON file path
json_file_path = 'SemanticshesNetsNaturkatastrophen(1).json'

# CSV file path
csv_file_path = 'SemanticshesNetsNaturkatastrophen.csv'

# Load JSON data
with open(json_file_path) as json_file:
    data = json.load(json_file)

# Check if the JSON data is a list of dictionaries
if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
    # Open CSV file
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())

        # Write header row
        writer.writeheader()

        # Write data rows
        writer.writerows(data)
else:
    # JSON data is a single dictionary
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data.keys())

        # Write header row
        writer.writeheader()

        # Write data row
        writer.writerow(data)
