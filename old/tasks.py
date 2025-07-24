'''
Structure:
Name
Date
Status -> Done, In Progress, Not Done
'''

import json
data = {
    "name": "Play games",
    "when":"12/05/2025",
    "progress":"in progress"
}
new_data = {
    "name": "Programming",
    "when":"25/05/2025",
    "progress":"in progress"
}

def writeJson(data):
    try:
        with open('output.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print("JSON file 'output.json' created successfully.")
    except IOError as e:
        print(f"Error writing to file: {e}")

def readJson():
    try:
        with open("output.json", 'r') as json_file:
            try:
                existing_data = json.load(json_file)
            except json.JSONDecodeError:
                existing_data = []  # Handle cases where the file is empty or invalid JSON
    except FileNotFoundError:
        existing_data = []
    print(existing_data)
    if isinstance(existing_data, list):
        print("Data is a list")
        if isinstance(new_data, list):
            existing_data.extend(new_data)
        else:
            existing_data.append(new_data)
    elif isinstance(existing_data, dict):
        print("Data is a dictionary")
        if isinstance(new_data, dict):
            existing_data.update(new_data)
            writeJson(existing_data)
        else:
            raise TypeError("Cannot concatenate a list with a dictionary.")
    else:
        raise TypeError("Unsupported data type for concatenation.")





'''    
'''



readJson()

# Add, Update, and Delete tasks

# Mark a task as in progress or done

#changeStatus

# List all tasks

# List all tasks that are done

# List all tasks that are not done

# List all tasks that are in progress
