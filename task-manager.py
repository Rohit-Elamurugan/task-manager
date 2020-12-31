# FUNCTION SETUP


# this makes the input into a list of 2 elements: a command and a string
process = lambda string: [string.split()[0],' '.join(string.split()[1:])]

# this adds a new task and mark it as undone
def add(string):
    tasklist.append('\n'+'UNDONE-'+string)

# removes all task which are done or removes only 1 of the task which is provided
def remove(string):
    if string == 'all':
        for i in tasklist:
            _task = i.split('-')
            if _task[0] == 'DONE':
                tasklist.remove(i)
    else:
        for i in tasklist:
            if string in i:
                tasklist.remove(i)

# marks the task as done
def mark(string):
    for i in tasklist:
        if string in i:
            _task = i.split('-')
            tasklist.remove(i)
            tasklist.append('\n'+'DONE-'+_task[1])


# UI SETUP


print('Welcome to task manager !!')
print('\nWhenever you want to add, remove or mark a task, do it in this format:\n<command> <task>')
print('\nIf you don\'t remember the commands, here is the list of commands:\nadd - adds a task\nremove - removes a task\nmark - marks a task\nshow - shows a task\nquit - closes and leaves\n')

# MAIN LOOP


while True:
    # takes in command
    command = process(input('What do you want to do: '))

    # it takes in all the tasks, and stores it in a list
    task = open('tasks.txt')
    tasklist = [i for i in task if i != '\n']
    task.close()

    # it removes all content and makes a fresh new file with same filename
    task = open('tasks.txt', 'w')

    # it adds a task if command is add
    if command[0] == 'add':
        add(command[1])
        print('Successfully added', command[1], '\n')

    # it removes a task if command is remove
    elif command[0] == 'remove':
        remove(command[1])
        print('Successfully removed', command[1], '\n')

    # it marks a task as done if command is mark
    elif command[0] == 'mark':
        mark(command[1])
        print('Successfully marked', command[1], '\n')

    # it will show the list of tasks if command is show
    elif command[0] == 'show':
        if len(tasklist) == 0:
            print('You finished all tasks !! If you have any task, add it !!\n')
        else:
            print('Tasks:')
            for i in tasklist:
                print(i)

    # it quits if command is quit
    # force quitting the program may cause errors in file
    elif command[0] == 'quit':
        print('See you again later\n')
        for i in tasklist:
            task.write(i)
        task.close()
        break

    # if that command doesn't exist, it will ask the user to try again
    else:
        print('Please try again\n')

    # it writes all the task back into the fresh new file
    for i in tasklist:
        task.write(i)
    task.close()