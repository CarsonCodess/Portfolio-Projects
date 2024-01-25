import time

class Task():
    def __init__(self, title, description, priority, due_date):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date

    def toString(self):
        return(f"Title: {self.title}\tDescription: {self.description}\tPriority: {self.priority}\tDue Date: {self.due_date}\n")

def add():
    title = input("Title: ")
    description = input("Description: ")
    priority = input("Priority: ")
    due_date = input("Due Date: ")
    newtask = Task(title, description, priority, due_date)
    with open('ToDoList\\reminders.txt', 'a') as file:
        file.write(newtask.toString())




def update(): #See if you can ask the user what specifically they want to change instead of rewriting the whole thing
    count = 0
    secondcount = 1
    with open('ToDoList\\reminders.txt', 'r') as file:
         lines = file.readlines()
         for i in lines:
            print(secondcount, ":" + i)
            secondcount+=1
    delete = input("Which line would you like to update?")
    with open('ToDoList\\reminders.txt', 'w+') as file:
        for i in lines:
            if int(count) != int(delete)-1:
                file.write(i)
                count+=1
            elif int(count) == int(delete)-1:
                title = input("Title: ")
                description = input("Description: ")
                priority = input("Priority: ")
                due_date = input("Due Date: ")
                newtask = Task(title, description, priority, due_date)
                file.write(newtask.toString())
                print("Updated!")
                count+=1




def delete(): #Still need to check if file is in the list
    count = 0
    secondcount = 1
    with open('ToDoList\\reminders.txt', 'r') as file:
         lines = file.readlines()
         for i in lines:
            print(secondcount, ":" + i)
            secondcount+=1
    delete = input("Which line would you like to delete?")
    with open('ToDoList\\reminders.txt', 'w+') as file:
        for i in lines:
            if int(count) != int(delete)-1:
                file.write(i)
                count+=1
            elif int(count) == int(delete)-1:
                print("Deleted!")
                count+=1



def main():

    while True:
        userinput = input("Would you like to:\n1. Add a reminder\n2. Delete a reminder\n3. Update a reminder\n4. Exit\n")
        if(userinput == "1"):
            add()
        elif(userinput == "2"):
            delete()
        elif(userinput == "3"):
            update()
        elif(userinput == "4"):
            exit()
        else:
            print("Not a valid answer!")
            time.sleep(1)
main()