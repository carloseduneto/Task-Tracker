# Add, Update, and Delete tasks
# Mark a task as in progress or done
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress

import json

tasks = [{
    "name": "Play games",
    "date": "24/07/2025",
    "progress": "not done",
    "priority": 5
}]

# json.dumps(tasks)
# print(tasks)

name = "Nobody stop nobody"
date = "26/07/2025"
priority = 4

taskRegistry = {
    "name": name,
    "date": date,
    "progress": "not done",
    "priority": priority
}

# json.dumps(taskRegistry)
# print(taskRegistry)

# print(json.dumps(True))

# Create a file JSON
def createFileJson(data):
    with open("allTasks.json", mode="w", encoding="utf-8") as write_file:
        json.dump(data, write_file, indent=4)

# List all tasks
def listAllTasks():
    with open("allTasks.json", mode="r", encoding="utf-8") as read_file:
        allTasks = json.load(read_file)
        # print("All task: " , allTasks)
        # print("All task: " , type(allTasks))
        # print(allTasks[0]["name"])
        return allTasks

#Add new Task to list
def addNewTask(task, allTasks):
    allTasks.append(task)
    return allTasks

#Add new Task to JSON
def addTaskToJson():
    listOfTasks = listAllTasks()
    listOfTasksAdded = addNewTask(taskRegistry, listOfTasks)
    createFileJson(listOfTasksAdded)



old = "Nobody stop nobody 2"
new = "Vim aqui embora"
parameter = "name"


#Update tasks
def updateTasksJson(taskSelect, newNameToTask, parameterToUpdate):
    listOfTasks = listAllTasks()
    for i in range(len(listOfTasks)):
        if(listOfTasks[i][parameterToUpdate]==taskSelect):
            listOfTasks[i][parameterToUpdate] = newNameToTask
    # print(listOfTasks)

    createFileJson(listOfTasks)

taskSelect = "Abobora"

#Delete tasks
def deleteTaskJson(taskSelect):
    listOfTasks = listAllTasks()
    for i in range(len(listOfTasks)):
        if(listOfTasks[i]["name"]==taskSelect):
            listOfTasks.pop(i)
            print("Deleted Task!")
    createFileJson(listOfTasks)

deleteTaskJson(taskSelect)