#importing the datetime library.
import datetime

#global variables which are dictionaries and an empty string.
user_login_details ={}
user_task = {}    
data = ''

#function for registering a user as well as gathering username and password from the user. 
def reg_user():
    user_text = open('user.txt','a') 
    user_input_username = input('Please enter a username: ') 
    while user_input_username in user_login_details: 
            print('Error: This username has been used. Please try again.') 
            user_input_username = input('Please enter a username: ') 
    user_input_password = input('Please enter a password: ') 
    user_input_confirm_password = input('Please confirm password: ')

#Writing to the text file only if the passwords match.
    if user_input_password == user_input_confirm_password:
        user_text.write('\n'+user_input_username + ", " + user_input_password)
        
#An error message is displayed to the user if the passwords do not match.  
    elif user_input_password != user_input_confirm_password:
        print("Error: Please try again.")
   
    user_text.close()

#Creating a function for the add task and prompting the user for various information about a task. 
def add_task():
     task_text = open('tasks.txt','a')
     username_input = input('Please enter a username. ') 
     user_task = input('Please enter the title of the task. ') 
     user_description_task = input('Please give a description of the task. ') 
     user_due_date = input('Please provide the due date of the task. (In the format of YYYY-MM-DD) ') 
     user_complete = 'No' 
     task_text.write(username_input + ", " + user_task + ", " + user_description_task  +
    ", " + ", " + user_due_date + ", " + user_complete + '\n') 
     task_text.close()

#Creating a view_mine function
#This shows the description of the task assigned to a specific user.
def view_mine():
    task_file = open('tasks.txt','r+') 
    task_numb = 1
    task_dic = {}
    for i in task_file: 
        split_i = i.split(", ")
        task_dic[task_numb] = split_i
        if usernames == split_i[0]: 
            print('Task Number:         ' + str(task_numb))  
            print('1.Task               ' + split_i[1])  
            print('2.Assigned to        ' + split_i[0])  
            print('3.Date assigned:     ' + split_i[4]) 
            print('4.Due date:          ' + split_i[3])  
            print('5.Task Completed:    ' + split_i[5])         
            print('6.Task Description:  ' + split_i[2])  
        task_numb += 1

#Allowing the user to select a specific task.
#Allowing the user to mark the task as complete or editing the task.
    while 1:
        message = int(input('Please select a task using a task number.If you would like to return to the main menu please type in -1.'))
        if message == -1:
            break
        else:
            task = task_dic[message]
            
            mark_task_edit_task = input('Would you like to (m) mark the task as complete or (e) edit the task ? ')
            
            if mark_task_edit_task == 'm':
                task[-1] = 'Yes'
            
            if mark_task_edit_task == 'e':
                if task[-1] != 'Yes':
                    task_selection = input('Please choose to select either a (nu) new username or a (nd) new due date ')

                    if task_selection == 'nu':
                        task[0] = input('Please choose a new username ')

                    elif task_selection == 'nd':
                        task[3] = input('Please enter a new due date ')
                else:
                    print('Error: Task has been completed.')
            task_dic[message] = task

#Writing to the task text file the updated changes. 
    taskList = [', '.join(tas).strip('\n') for tas in task_dic.values()]
    datafile = '\n'.join(taskList)
    task_text = open('tasks.txt','w')
    task_text.write(datafile)
    task_text.close()
        
#Creating a function to store the statistics related to the task. 
def task_overview():
    task_overview_file = open('task_overview.txt','w')
    task_text = open('tasks.txt','r')
    total = 0
    count_no = 0
    count_yes = 0
    task_overdue = 0
    date_overdue = 0
    for element in task_text:
        total = total + 1
        split_i = element.strip('\n').split(', ')
        if split_i[5].lower() == 'no':
            count_no = count_no + 1
            stringdate = split_i[4]

            dateObject = datetime.datetime.strptime(stringdate, '%Y-%m-%d')

            currentdate = datetime.datetime.now()

            if dateObject < currentdate:
                date_overdue = date_overdue + 1
    
            percentage_overdue = (date_overdue/total) * 100
            
        else:
            count_yes = count_yes + 1
    
    percentage_incomplete = (count_no/total) * 100

#Writing to the task_overview_file the statistics related to the task.
    task_overview_file.write('The total number of tasks is ' + str(total))
    task_overview_file.write('\nThe total number of uncompleted tasks is ' + str(count_no))
    task_overview_file.write('\nThe total number of completed tasks is ' + str(count_yes))
    task_overview_file.write('\nThe percentage of incompleted tasks is ' + str(percentage_incomplete) + '%')
    task_overview_file.write('\nThe percentage of overdue tasks is ' + str(percentage_overdue) + '%')
    task_overview_file.close()
    task_text.close()

#Creating a function for user_overview and calculating the various statistics related to the user. 
def for_each_user(user, total_num_task):
    task_text = open('tasks.txt','r')
    total_user = 0
    count_no = 0
    count_yes = 0
    perc_incomplete_user = 0.0
    perc_complete_user = 0.0
    date_overdue = 0
    percentage_overdue = 0.0
    
    for i in task_text:
        split_i = i.strip('\n').split(', ')
        if split_i[0] == user:
            total_user = total_user + 1
            if split_i[5].lower() == 'no':
                count_no = count_no + 1
                stringdate = split_i[4]

                dateObject = datetime.datetime.strptime(stringdate, '%Y-%m-%d')

                currentdate = datetime.datetime.now()

                if dateObject < currentdate:
                    date_overdue = date_overdue + 1
                      
            else:
                count_yes = count_yes + 1
            
    if total_user != 0:
        perc_incomplete_user = (count_no/total_user) * 100
        perc_complete_user = (count_yes/total_user) * 100
        percentage_overdue = (date_overdue/total_user) * 100

#Calculating the various statistics for the user.    
    userdata = "\nfor username: "+ user +'\n---------\n'
    userdata += '\nTotal for the user: ' + str(total_user)
    userdata += '\nTotal completed tasks for the user: ' + str(count_yes)
    userdata += '\n Total incompleted tasks for the user: ' + str(count_no)
    userdata += '\n Percentage of incompleted tasks for the user: ' + str(perc_incomplete_user) + '%'
    userdata += '\n Percentage of completed tasks for the user: ' + str(perc_complete_user) + '%'
    userdata += '\n Percentage of incompleted and overdue tasks for the user: ' + str(percentage_overdue) + '%'

    return userdata
    
    task_text.close()

#Creating a function to write to the text files. 
def user_overview():
    task_text = open('tasks.txt','r')
    user_overview = open('user_overview.txt','w')
    total_num_task =  len(task_text.readlines())
    task_text.close()

    peruser = ''
    for u in user_login_details.keys():
        peruser += for_each_user(u, total_num_task)
    
    print(peruser)
    user_overview.write(peruser)
    user_overview.close()

#Generate reports function 
def gen_reports():
    task_overview()
    user_overview()
      
#Displaying a message to the user.
print('Welcome to the Task Manager.\n ')

#Opening the text file and appending it to the dictionary with the key and corresponding value
#given to the user.txt file which is the username for the key and the password for the value.
user_text = open('user.txt','r')
for element in user_text:
    usrn, passw = element.strip('\n').split(', ')
    user_login_details[usrn] = passw

#Asking the user for the username and password.
usernames = input('Please enter Username: ')
passwords = input('Please enter Password: ')

#If the user selects va from the menu the user can view the task descriptions. 
def view_all():
    task_file = open('tasks.txt','r')
    for i in task_file:
         i.split(", ")
         split_i = i.split(", ")
         print('Task                ' + split_i[1])
         print('Assigned to:        ' + split_i[0])
         print('Date assigned:      ' + split_i[4])
         print('Due date:           ' + split_i[3])
         print('Task Completed:     No')
         print('Task Description:   ' + split_i[2])
         print('\n')

#Creating the Statistics function
#It opens the user_overview and task_overview.
def statistics_task():
    with open('user_overview.txt','r') as user_file:
        print(user_file.read())

    with open('task_overview.txt','r') as task_file:
        print(task_file.read())

#Creating a while loop for the login and password credentials as well as an Error message. 
while 1:
    if usernames in user_login_details:
        if user_login_details[usernames] == passwords:
             print('You are successfully logged in.')
             break

    print('Error: Please try again. ')
    usernames = input('Please enter Username: ')
    passwords = input('Please enter Password: ')

#Displaying the menu to the user if the username is admin.
while 1:
    if usernames == 'admin':
            user_select = input('''Please select one of the following options:
                  r - register user
                  a - add task
                  va - view all tasks
                  vm - view my tasks
                  gr - generate reports
                  ds - display statistics
                  e - exit
                  \n
                  ''')

#Otherwise displaying another menu to the user.
    else:
        user_select = input('''Please select one of the following options:
                  r - register user
                  a - add task
                  va - view all tasks
                  vm - view my tasks
                  gr - generate reports
                  ds - display statistics
                  e - exit
                  \n
                  ''')

#Calling a specific funtion based upon the user's input. 
    if user_select == 'r':
        reg_user()

    if user_select == 'a':
        add_task()

    if user_select == 'vm':
        view_mine()

    if user_select == 'gr':
        gen_reports()

    if user_select == 'va':
        view_all()

    if user_select == 'ds':
        statistics_task()

    if user_select == 'e':
        break



