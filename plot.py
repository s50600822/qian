import json
import os
import re
import matplotlib.pyplot as plt

json_files = [file for file in os.listdir() if file.endswith('.json')]

dates = []
values = []

for json_file in json_files:
    with open(json_file, 'r') as file:
        data = json.load(file)
        date = re.match(r"(\d+)", json_file).group()
        print(data)
        eur_value = data["data"]["EUR"]
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

# chart_data = {
#     "dates": dates,
#     "values": values
# }

# chart_data_file = "eur_value_chart_data.json"
# with open(chart_data_file, 'w') as data_file:
#     json.dump(chart_data, data_file)