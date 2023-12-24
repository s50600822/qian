import json
import os

# Set the directory path where the JSON files are located
directory_path = './'

# Initialize an empty list to store data from individual files
consolidated_data = []

# Iterate through each file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.json'):
        file_path = os.path.join(directory_path, filename)
        
        # Extract the source key from the filename (assuming it's the first part before '.json')
        source_key = filename.split('.')[0]
        
        with open(file_path, 'r') as file:
            # Load the data from the current file
            file_data = json.load(file)
            
            # Add the source key to the data
            file_data['date'] = source_key
            
            # Append the modified data to the consolidated list
            consolidated_data.append(file_data)

# Write the consolidated data to a new JSON file
consolidated_file_path = 'data/storage.json'
with open(consolidated_file_path, 'w') as consolidated_file:
    json.dump(consolidated_data, consolidated_file, indent=2)

print(f"Consolidated data has been written to {consolidated_file_path}")