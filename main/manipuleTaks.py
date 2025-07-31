# Add, Update, and Delete tasks
# Mark a task as in progress or done
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress

import json
import os

class color:
    BOLD = '\033[1m'
    GREEN = '\033[32m'
    END = '\033[0m'

tasks = [{
    "name": "Play games",
    "date": "24/07/2025",
    "progress": "not done",
    "priority": 5
}]

# json.dumps(tasks)
# print(tasks)

name = "Another Task"
date = "26/07/2025"
priority = 2

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
def addTaskToJson(taskRegistry):
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
        if(listOfTasks[i]["name"]==taskSelect["name"]):
            listOfTasks[i][parameterToUpdate] = newNameToTask
    # print(listOfTasks)

    createFileJson(listOfTasks)

taskSelect = "Frio"

#Delete tasks
def deleteTaskJson(taskSelect):
    listOfTasks = listAllTasks()
    for i in range(len(listOfTasks)):
        if(listOfTasks[i]["name"]==taskSelect):
            listOfTasks.pop(i)
            print("Deleted Task!")
            break
    createFileJson(listOfTasks)

# addTaskToJson(taskRegistry)

# deleteTaskJson(taskSelect)

def clear_terminal():
    """Clears the terminal screen."""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

option = ""
while (option != 6):
    print("Option: " + str(option))
    print(
        color.BOLD+ "TASK TRACKER\n" + color.END +
        "1. Add task\n" +
        "2. Update task\n"+
        "3. Delete task\n"+
        "4. List tasks\n" +
        "5. Change task status\n"+
        "6. Exit"
    )
    option = int(input(">>"))
    clear_terminal()

    if(option == 1):
        print(color.BOLD+ "TASK TRACKER - ADD TASK\n" + color.END)
        taskName = input("Task name: ")
        date = input("Date: ")
        priority = int(input("Priority: "))

        clear_terminal()
        taskRegistry = {
            "name": taskName,
            "date": date,
            "progress": "not done",
            "priority": priority
        }

        addTaskToJson(taskRegistry)

        optionAdd = ""
        while (optionAdd != 0):
            print(color.BOLD + color.GREEN + "✅ TASK SUCESSFUL ADDED" + color.END +
                "\n0. Back"
                )
            optionAdd = int(input(">>"))
            clear_terminal()

    if(option == 2):
        print(color.BOLD+ "TASK TRACKER - UPDATE TASK\n" + color.END)

        allTasks = listAllTasks()
        print(
            "COD ",
            "DATE\t",
            "PRIORITY\t",
            "NAME\t",
        )
        for i in range(len(allTasks)):
            print(
                  i+1, "",
                  allTasks[i]["date"], "\t",
                  allTasks[i]["priority"], "\t",
                  allTasks[i]["name"]
                  )
        print("Enter the task number you want to update:")
        numberTaskChoosen = int(input(">>"))
        numberTaskChoosen = numberTaskChoosen-1
        taskChoosen = allTasks[numberTaskChoosen]
        clear_terminal()
        optionUpdate = int(input("What do you want to update?\n"+
              "1. Date\n"+
              "2. Priority\n"+
              "3. Name\n"
              ">>"
              ))
        clear_terminal()
        

        
        if(optionUpdate==1):
            updateTasksJson(taskChoosen, input("New date \n>>"), "date")
            print(color.BOLD + color.GREEN + "✅ TASK SUCESSFUL UPDATE" + color.END)
        elif(optionUpdate==2):
            updateTasksJson(taskChoosen, input("New priority \n>>"), "priority")
            print(color.BOLD + color.GREEN + "✅ TASK SUCESSFUL UPDATE" + color.END)
        elif(optionUpdate==3):
            updateTasksJson(taskChoosen, input("New name \n>>"), "name")
            print(color.BOLD + color.GREEN + "✅ TASK SUCESSFUL UPDATE" + color.END)

    if(option==3):
        print(color.BOLD+ "TASK TRACKER - DELETE TASK\n" + color.END)

        allTasks = listAllTasks()
        print(
            "COD ",
            "DATE\t",
            "PRIORITY\t",
            "NAME\t",
            "PROGRESS\t",
        )
        for i in range(len(allTasks)):
            print(
                  i+1, "",
                  allTasks[i]["date"], "\t",
                  allTasks[i]["priority"], "\t",
                  allTasks[i]["name"], "\t",
                  allTasks[i]["progress"], "\t"
                  )
        print("Enter the task number you want to delete:")
        numberTaskChoosen = int(input(">>"))
        taskChoosen = allTasks[numberTaskChoosen-1]
        deleteTaskJson(taskChoosen["name"])

    if(option == 4):
        print(color.BOLD+ "TASK TRACKER - LIST ALL TASKS\n" + color.END)

        allTasks = listAllTasks()
        print(
            "COD ",
            "DATE\t",
            "PRIORITY\t",
            "PROGRESS\t",
            "NAME\t"
        )
        for i in range(len(allTasks)):
            print(
                  i+1, "",
                  allTasks[i]["date"], "\t",
                  allTasks[i]["priority"], "\t",
                  allTasks[i]["progress"], "\t",
                  allTasks[i]["name"], "\t"
                  )
        listOption = ""
        while (listOption != 0):
            listOption = int(input("\n0. Back\n >>"))
        clear_terminal()

    if(option == 5):
        print(color.BOLD+ "TASK TRACKER - UPDATE TASK\n" + color.END)

        allTasks = listAllTasks()
        print(
            "COD ",
            "DATE\t",
            "PRIORITY\t",
            "PROGRESS\t",
            "NAME\t",
        )
        for i in range(len(allTasks)):
            print(
                  i+1, "",
                  allTasks[i]["date"], "\t",
                  allTasks[i]["priority"], "\t",
                  allTasks[i]["progress"], "\t",
                  allTasks[i]["name"]
                  )
        print("Enter the task number you want to update progress:")
        numberTaskChoosen = int(input(">>"))
        taskChoosen = allTasks[numberTaskChoosen-1]

        progressUpdate = int(input("What do you want to change?\n"+
              "1. Not done\n"+
              "2. In Progress\n"+
              "3. Done\n"
              ">>"
              ))
        clear_terminal()

        progressList=["Not done", "In Progress", "Done"]


        



        updateTasksJson(taskChoosen, progressList[progressUpdate-1], "progress")
        print(color.BOLD + color.GREEN + "✅ TASK SUCESSFUL UPDATE PROGRESS" + color.END)







print(
    color.BOLD+ "TASK TRACKER - TO LIST\n" + color.END +
    "0. Back\n"
    "1. List all tasks\n" +
    "2. List done tasks\n" +
    "3. List not done tasks\n" +
    "4. List in progress tasks\n"
)

print(
    color.BOLD+ "TASK TRACKER - CHANGE TASK STATUS\n" + color.END +
    "0. Back\n" +
    '1. Change in progress\n' +
    "2. Change done"
)




input(">>")

clear_terminal()

