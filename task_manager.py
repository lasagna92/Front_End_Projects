import datetime
from datetime import date

# Define a function that allows the admin user to register other users
def reg_user():

    with open('user.txt', 'r') as r:
        r = r.readlines()       # Read through the lines of the file
        while True:
            new_username = input('\nPlease enter a Username:\t')  # Ask for a username
            new_password = input('Please enter a Password:\t')  # Ask for a password
            password_confirm = input('Confirm Password:\t')  # Ask for a password confirmation

            for row in r:
                split_line = row.split(', ')

                # If the login details are correct go to the next section
                # If the login details are correct go to the next section
                if new_password == password_confirm and new_username != split_line[0]:
                    x = False

                    continue

                    # Otherwise keep asking to enter the details
                else:
                    x = True
                    print('\nUsername already in use!\nPlease enter a different Username!')
                break
            # If the entered details meet the conditions append them in the 'user.txt' file
            if not x:
                with open('user.txt', 'a+') as _f:
                    _f.write(f'\n{new_username}, {new_password}')
                break
            elif x:
                continue


# Define a function for the user to add tasks
def add_task():
    # Ask the user to enter the task details
    task_username = input('\nPlease enter the username of the person whom the task is assigned to:\n\t')
    task_title = input('Please enter the name of the task:\n\t')
    task_desc = input('Please enter the description of the task:\n\t')
    task_due = input('Please enter the due date:\t')
    today = date.today().strftime('%d %b %Y')
    # Add the just prompted task to the 'task.txt' file
    with open('tasks.txt', 'a+') as f_:
        f_.write(f'\n{task_username}, {task_title}, {task_desc}, {today}, {task_due}, No')


# Define a function that shows all the tasks saved in the 'tasks.txt' file
def view_all():
    with open('tasks.txt', 'r+') as a:
        # Read the file
        # Loop over the lines and display the tasks in a labelled and organized format
        for row in a:
            split_line = row.split(', ')

            split_line.insert(0, '\nName:\t\t\t')
            split_line.insert(2, '\nTask Title:\t\t')
            split_line.insert(4, '\nTask description:')
            split_line.insert(6, '\nDate:\t\t\t')
            split_line.insert(8, '\nDue date:\t\t')
            split_line.insert(10, '\nCompleted?\t\t')

            tasks = ' '.join(split_line)
            print(tasks)


# Define a function to view the tasks assigned to the logged-in user
def view_mine():

    username = username_input
    num_task = 0
    with open('tasks.txt', 'r') as _f:
        view_more = _f.read()
    # Loop through all the task assigned to the logged-in user
    # Print them out in a tidy format with an ascendant number
    for row in view_more:

        line = row.split(',')

        num_task += 1
        if username == line[0]:        # For the entered username print out all the labelled tasks assigned
            print('\nTask Number: ' + str(num_task) + '\nUsername: ' + line[0] + '\nTitle: ' + line[1] +
                  '\nDescription: ' + line[2] + '\nDate: ' + line[3] + '\nDue Date: ' + line[4] + ' ' +
                  '\nCompleted: ' + line[5] + ' ' + '\n')

    # Define the function to edit the file
    def edit_file(complete):
        # Replace the completed status 'Yes'/'No' with the new statement
        userTask = taskFile[taskNum].strip().split(', ')
        new_state = taskFile[taskNum].strip().replace(userTask[5], f' {complete}')

        # Overwrite the new status in the file 'tasks.txt'
        updated_string = view_more.replace(taskFile[taskNum].strip(), new_state)
        with open('tasks.txt', 'w') as f:
            f.write(updated_string)

    # Define a function to edit the name and the date in the file 'tasks.txt'
    def edit(name_input, new_date):

        userTask_d = taskFile[taskNum].strip().split(',')
        userTask_n = taskFile[taskNum].strip().split(',')
        # Replace the old details with the new ones
        new_state_u = taskFile[taskNum].strip().replace(userTask_n[0],
                      f'{name_input}').replace(userTask_d[4], f' {new_date}')

        # Overwrite the new details in the file 'tasks.txt'
        updatedUsername = view_more.replace(taskFile[taskNum].strip(), new_state_u)
        with open('tasks.txt', 'w+') as w:
            w.write(updatedUsername)

    # Ask the user if they want to mark a task as complete, to edit one or to return to the main menu
    editTask = input('\nWould you like to mark a task as complete? (a) '
                     ' Edit a Task? (b) '
                     ' Or return to the menu? (-1)\n')
    # If marking a task as complete
    if editTask == 'a':
        taskNum = int(input('Please enter the Task number?\n'))     # Ask for the task number
        taskNum = taskNum - 1
        with open('tasks.txt', 'r') as file:
            taskFile = file.readlines()     # Read the file

        complete = input('Has this task been completed?\n')     # Ask if the task is completed
        if complete == 'Yes':       # Change the value to Yes
            edit_file(complete)     # Call the function to replace the status in the file

        elif complete == 'No':      # Change the value to No
            edit_file(complete)     # Call the function to replace the status in the file

    # If edit a task ask for the task number that needs to be edited
    elif editTask == 'b':
        taskNum = int(input('Please enter the Task number?\n'))
        taskNum = taskNum - 1

        with open('tasks.txt', 'r+') as f:
            taskFile = f.readlines()        # Read the 'task.txt' file
            # Loop through the file and identify the task chosen by the user
            for line in taskFile:
                line = taskFile[taskNum].strip().split(', ')
                # The task can be modified just if it has not been completed yet
                if line[5] == 'No':
                    name_input = input('Edit the user name:\t')     # Ask for the new name
                    date_input = input('Edit the due date:\t')      # Ask for the new due date
                    # Update the details calling the above functions
                    line[4] = date_input
                    line[0] = name_input

                    edit(name_input, date_input)

                    # Display the updated task
                    print('\nUsername: ' + line[0] + '\nTitle: ' + line[1] + '\nDescription: ' + line[2] + '\nDate: '
                          + line[3] + '\nDue Date: ' + line[4] + '\nCompleted? ' + line[5] + '\n')
                # If a task has been completed print an appropriate message
                else:
                    print('The task has already been completed!')
                break
    # If input -1 return to the main menu
    elif editTask == '-1':
        pass


# Define a function to create a file containing the tasks details overview
def tasksOverview():
    title = 'TASKS OVERVIEW\n'
    print('\n')
    print(title)
    compTask = []
    not_compTask = []
    overdueTask = []
    # Read the file and loop through it
    with open('tasks.txt', 'r') as f:
        content = f.readlines()

    for row in content:
        row = row.split(', ')
        # Append to and empty lis all the completed tasks
        if row[5] == 'Yes' or row[5] == 'Yes\n':
            compTask.append(row[5])

        # Append to and empty list all the not yet completed tasks
        elif row[5] == 'No' or row[5] == 'No\n':
            not_compTask.append(row[5])
        # Calculate if the not completed tasks are overdue
        numOverdueDays = str(datetime.date.today() - (datetime.datetime.strptime(row[4], '%d %b %Y').date()))
        numOverdueDays = int(numOverdueDays[:2])
        # Append the overdue tasks to an empty list
        if numOverdueDays > 0 and row[5] == 'No' or row[5] == 'No\n':
            overdueTask.append(datetime.datetime.strptime(row[4], '%d %b %Y'))
    # Find and display:
    # The total number of tasks
    total_tasks = len(content)
    print(f'\nThe total number of the tasks is: {total_tasks}\n')
    # The number of completed tasks
    total_compTasks = f'The total number of completed tasks is: {len(compTask)}\n'
    print(total_compTasks)
    # The uncompleted tasks
    total_notCompTask = f'The total number of uncompleted tasks is: {len(not_compTask)}\n'
    print(total_notCompTask)
    # The number of overdue tasks
    total_overdueTask = f'The total overdue tasks is: {len(overdueTask)}\n'
    print(total_overdueTask)
    # Find and display the following percentage:
    # The not completed tasks
    not_compTaskPerc = (len(not_compTask) / total_tasks) * 100
    print(f'The {not_compTaskPerc}% of the tasks has not been completed yet\n')
    # The overdue tasks
    overdue_Percent = (len(overdueTask) / total_tasks) * 100
    print(f'The {overdue_Percent}% of the tasks are overdue')
    # Create a file showing all the above results in a tidy manner
    with open('task_overview.txt', 'w+') as w:
        w.write(f'{title}'
                f'{total_compTasks}\n'
                f'{total_notCompTask}\n'
                f'{total_overdueTask}\n'
                f'The {not_compTaskPerc}% of the tasks has not been completed yet\n'
                f'\nThe {overdue_Percent}% of the tasks are overdue')


# Define a function to create and display the user details overview
def userOverview():

    users = []
    # Create a file
    w = open('user_overview.txt', 'a+')
    title = 'USERS OVERVIEW\n'
    print('\n')
    print(title)
    w.write(title)

    # Open the 'user.txt' file and loop over it
    with open('user.txt', 'r') as u:
        for row in map(str.strip, u):
            if not row:
                continue
            # Using a for loop append a dictionary to an empty list with the usernames and the passwords from the file
            username, password = [r.strip() for r in row.split(', ')]
            users.append(
                {'username' : username,
                 'password' : password}
            )

    tasks = []
    with open('tasks.txt', 'r') as content:     # Read the 'task.txt' file
        # Using a for loop append to an empty list a dictionary with the tasks details
        for line in map(str.strip, content):
            if not line:
                continue
            username, title, desc, date, due_date, completed = [
                l.strip() for l in line.split(',')
            ]
            tasks.append(
                {
                    'username': username,
                    'title': title,
                    'description': desc,
                    'date': datetime.datetime.strptime(date, '%d %b %Y').date(),
                    'due_date': datetime.datetime.strptime(due_date, '%d %b %Y').date(),
                    'completed': completed,
                }
            )

    # Find and print out the total number of registered users
    num = len(set(u['username'] for u in users))
    totalUsers = f'Total number of registered users: {num}\n'
    print(totalUsers)

    # Find and print out the total number of tasks
    num = len(set(t["title"] for t in tasks))
    totalTasks = f'Total number of tasks: {num}'
    print(totalTasks)
    print('\n')
    # Write the above data into the new created file

    w.write(f'{totalUsers}\n{totalTasks}\n')


    # Find and print out the total number of tasks assigned to each user
    tmp = {}
    for t in tasks:
        for u in users:
            # If the username is matching the username task append the task to and empty dictionary
            if u['username'] == t['username']:
                tmp.setdefault(t['username'], []).append(t['title'])
    # Loop through the dictionary and find out the number of tasks assigned to the user
    for user in tmp:
        taskAssigned = f'Total tasks assigned to user {user} is {len(tmp[user])}'
        print(taskAssigned)
        # Add the data to the file

        w.write(f'\n{taskAssigned}')

        print('\n')
    # Find and print out what percentage of the total number of tasks have been assigned to that user
    total_tasks = len(set(d['title'] for d in tasks))       # Define the variable with the total number of tasks
    # Loop through the dictionary
    for user in tmp:
        # Divide the user assigned tasks number for the total number of task and multiply by 100 to find the percentage
        taskAssignedPerc =\
            f'TASK PERCENTAGE FOR EACH USER\n' \
            f'The percentage of the total number of tasks have been assigned to user {user} is '\
            f'{(len(tmp[user]) / total_tasks) * 100}%'
        print(taskAssignedPerc)
        # Write the data into the file
        w.write(f'\n\n{taskAssignedPerc}')

    print('\n')

    comp = {}
    not_comp = {}
    overdue = {}
    numOverdueDays = str(datetime.date.today() - (datetime.datetime.strptime(date, '%d %b %Y').date()))
    numOverdueDays = int(numOverdueDays[:2])

    for t in tasks:
        # For every task append every completed one and every related username to an empty dictionary
        if t['completed'] == 'Yes':
            comp.setdefault(t['username'], []).append(t['completed'])
        # For every task append every not completed one and every related username to an empty dictionary
        elif t['completed'] == 'No':
            not_comp.setdefault(t['username'], []).append(t['completed'])
            # If the task is not completed and overdue append it with every related username to an empty dictionary
            if numOverdueDays > 0:
                overdue.setdefault(t['username'], []).append(t['completed'])

    # Find and print out the completed tasks percentage for every user
    for user in comp:
        taskCompPerc = f'COMPLETED TASKS\n' \
                       f'Total percentage of the completed tasks assign to the user {user} is ' \
                       f'{round((len(comp[user])/len(tmp[user]))* 100, 2)}%'
        print(taskCompPerc)

        # Write the data to the file
        w.write(f'\n\n{taskCompPerc}\n')

    # Find and print out the not completed tasks percentage for every user
    for user in not_comp:
        taskNotCompPerc = f'NOT COMPLETED TASKS\n' \
                          f'Total percentage of the NOT completed tasks assign to the user {user} is ' \
                          f'{round((len(not_comp[user]) / len(tmp[user])) * 100, 2)}%'
        print(taskNotCompPerc)
        # Write the data to the file
        w.write(f'\n\n{taskNotCompPerc}\n')

    # Find and print out the not completed overdue tasks percentage for every user
    for user in overdue:
        taskOverduePerc = f'OVERDUE TASKS\n' \
                          f'Total percentage of the NOT completed OVERDUE tasks assign to the user {user} is ' \
                          f'{round((len(overdue[user]) / len(tmp[user])) * 100, 2)}%'
        print(taskOverduePerc)
        # Write the data to the file

        w.write(f'\n\n{taskOverduePerc}\n')
        w.close()



# LOGIN SECTION
# Read through the file 'user.txt' and create a login section
# If the username and password are in the file validate the user login
# Otherwise keep on asking the user for their login details
with open('user.txt', 'r') as login:
    login_detail = login.readlines()

complete = False
while not complete:

    username_input = input('\nPlease enter your Username:\t')  # Username input
    password_input = input('Please enter your Password:\t')  # Password input
    # Loop over the file to find out if the login details are correct
    for line in login_detail:

        username, password = line.replace('\n', '').split(', ')
        # If the login details are correct goto the next section
        if username_input == username and password_input == password:
            complete = True
        # Otherwise keep asking to enter the details
            break
        else:
            complete = False
            continue

# After the user logged in print out a menu with different actions
# If the username used is 'admin' print out a different menu
while complete:

    if username_input == 'admin':

        menu = input('''\n\tSelect one of the following Options below:
\tr - Registering a user
\ta - Adding a task
\tva - View all tasks
\tvm - View my task
\tvs - View statistics 
\tgr - Generate reports          
\te - Exit \n\t''').lower()

    else:

        menu = input('''\n\tSelect one of the following Options below:
\tr - Registering a user
\ta - Adding a task
\tva - View all tasks
\tvm - View my task         
\te - Exit \n\t''').lower()

    # NEW USER REGISTRATION SECTION
    # If the username ie equal to 'admin',
    # ask the user to register a new account
    if menu.lower() == 'r' and username == 'admin':
        reg_user()

    # NEW TASK ASSIGNMENT SECTION
    # Call the function that ask the user to input username, title, description and due date for a new task
    elif menu == 'a':

        add_task()
    # TASK LIST SECTION
    # Call the function to display all the task in the file 'task.txt'
    elif menu == 'va':

        view_all()

    # PERSONAL TASK SECTION
    # Based on the username prompted display the task the person is assigned to
    elif menu == 'vm':
        username = username_input
        num_task = 0
        with open('tasks.txt', 'r') as f:
            viewMine = f.readlines()
        # Loop through the file and display a numeric list of task assigned to the user
        for line in viewMine:
            tasks = line.strip().split(",")

            num_task += 1

            if username == tasks[0]:
                print("Task Number: " + str(num_task) + "\nUsername: " + tasks[0] + "\nTitle: " + tasks[1] +
                      "\nDescription: " + tasks[2] + "\nDate: " + tasks[3] + "\nDue date: " + tasks[4] +
                      '\nCompleted? ' + tasks[5] + '\n')

        # Call the function to edit the tasks
        view_mine()

    # STATISTICS SECTION
    # Display the number of tasks and users
    # Just the username 'admin has access to this section
    elif menu == 'vs':

        with open("tasks.txt", "r+") as f:
            # Print out the number of tasks in the 'tasks.txt' file
            count_tasks = len(f.readlines())        # Read all the lines and find the length

            print(f'\nThe total number of tasks is: {count_tasks}')

        with open('user.txt', 'r+') as f:
            # Print out the number of users in the 'user.txt' file
            count_users = len(f.readlines())        # Read all the lines and fine the length

            print(f'\nThe total number of users is: {count_users}')
    elif menu == 'gr' and username == 'admin':
        tasksOverview()

        userOverview()
    # EXIT SECTION
    elif menu == 'e':
        print('\nGoodbye!!!')
        exit()
    else:
        print('Only admin can access this menu!')

# Print out an error message if the input isn't listed above
else:
    print("You have made a wrong choice, Please Try again")
