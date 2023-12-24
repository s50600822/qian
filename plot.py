import json
import re
import matplotlib.pyplot as plt
import requests
from datetime import datetime

# Make the HTTP GET request
response = requests.get(f"https://api.freecurrencyapi.com/v1/latest?apikey=${FREECURRENCYAPI}&currencies=EUR&base_currency=AUD")
data = response.json()

# Get the current timestamp
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

# Update consolidated JSON file
consolidated_file_path = 'data/storage.json'
with open(consolidated_file_path, 'r') as consolidated_file:
    consolidated_data = json.load(consolidated_file)

# Append new data with timestamp
consolidated_data.append({'date': timestamp, 'data': data})

# Write the updated data back to the file
with open(consolidated_file_path, 'w') as consolidated_file:
    json.dump(consolidated_data, consolidated_file, indent=2)


# Specify the path to the consolidated JSON file
consolidated_file_path = 'data/storage.json'

# Read data from the consolidated JSON file
with open(consolidated_file_path, 'r') as consolidated_file:
    consolidated_data = json.load(consolidated_file)

dates = []
values = []

for entry in consolidated_data:
    date = entry["date"]
    eur_value = entry["data"]["EUR"]
    dates.append(date)
    values.append(eur_value)

plt.figure(figsize=(10, 5))
plt.plot(dates, values, marker='o')
plt.title("EUR Value Over Time")
plt.xlabel("Date and Time")
plt.ylabel("EUR Value")
plt.xticks(rotation=45)
plt.tight_layout()

chart_file = "eur_value_chart.png"
plt.savefig(chart_file)

print(f"Chart has been saved to {chart_file}")
