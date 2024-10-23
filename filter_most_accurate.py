import json

# Path to the JSON file
file_path = 'CMEs_2024.json'  # Replace with the actual file path

# Load the JSON data from the file
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract entries with isMostAccurate = True in cmeAnalyses
most_accurate_entries = []
for entry in data:
    cme_analyses = entry.get('cmeAnalyses')
    if cme_analyses and isinstance(cme_analyses, list):
        for analysis in cme_analyses:
            if isinstance(analysis, dict) and analysis.get('isMostAccurate') == True:
                most_accurate_entries.append(entry)
                break  # Add the entry once and move to the next one
# Print the filtered data
print(json.dumps(most_accurate_entries, indent=4))

