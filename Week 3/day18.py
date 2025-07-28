# introduction
import json

# with open("Week 3\sample_data\json_data", "r") as file:
#     tasks = json.load(file)
#     print(tasks)

# tasks = [
#     {"task": "Complete Project", "status": "Incomplete"}
# ]

# with open("Week 3\sample_data/tasks.json", "w") as file:
#     json.dump(tasks, file, indent=4)

with open("Week 3\sample_data/tasks.json", "r") as file:
    tasks = json.load(file)
    
tasks.append({"task": "Learn Python", "status": "Incomplete"})

with open("Week 3\sample_data/tasks.json", "w") as file:
    json.dump(tasks, file, indent=4)