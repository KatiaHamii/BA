import json
import xlwt

def extract_concepts(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        concepts = [value for value in data.values()]
    return concepts

# Funktion zur rekursiven Umwandlung der Werte in einen String
def convert_to_string(value):
    if isinstance(value, dict):
        return ', '.join(convert_to_string(v) for v in value.values())
    return str(value)

# Pfad zur JSON-Datei festlegen
json_file = 'SemanticshesNetsNaturkatastrophen.json'
excel_file = 'konzepte.xls'  # Dateiname für die Excel-Datei

# Extrahiere die Konzepte aus dem JSON
concept_list = extract_concepts(json_file)

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('Konzepte')

# Schreibe den Inhalt der Konzepte in das Arbeitsblatt
for row, concept in enumerate(concept_list):
    content = convert_to_string(concept)  # Konvertiere das Dictionary in einen String
    worksheet.write(row, 0, content)

# Speichere das Workbook als Excel-Datei
workbook.save(excel_file)