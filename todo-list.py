tasks = []

class task:
    def __init__(self, description, status):
        self.status = status
        self.description = description

    def completed(self):
        taskNum = int(input('Enter the task number to mark as completed:'))
        print('Task: '+tasks[taskNum-1]+' marked as completed.')
        tasks[taskNum-1] = "[Completed] " + tasks[taskNum-1]

    def remove(self):
        taskNum = int(input('Enter the task number to remove:'))
        task = tasks[taskNum-1]
        tasks.remove(task)
        print('Task: '+task+' removed successfully.')


while True:
    print('''Welcome to the To-Do List Application!
        1. Add task
        2. Mark task as completed
        3. View tasks
        4. Remove task
        5. Quit''')

    choice = int(input('Enter your choice:'))
    if (choice == 1):
        tsk = input('Enter the task: ')
        task1 = task(tsk, 'incompleted')
        tasks.append(task1.description)
        print('Task: ' + task1.description + ' added successfully.')
    elif (choice == 2):
        task1.completed()
    elif (choice == 3):
        print('Tasks:')
        index = 1
        for task in tasks:
            print(str(index) +'. '+ task)
            index += 1
    elif (choice == 4): 
        task1.remove()
    elif (choice == 5):
        print("Goodbye! Have a productive day!")
        quit()
    else:
        print("Invalid choice. Please try again.")
