# reading files

name = input('Tell me your name: ')
print(f'Hello, {name}!')

with open("to_do_list.txt",'r') as file:
    lines = file.readlines() 
    for line in lines:
        print(line)

for item in lines:
    item.strip()
    print(item)

for i in range(len(lines)):
    lines[i] = lines[i].strip()

with open("to_do_list.txt",'a+') as file:
    file.write('Grab more coffee please \n')
    
with open('to_do_list.txt','r') as file:
    lines = file.readlines()
    for line in lines:
        print(line)

with open("to_do_list.txt", "a+") as file: # opens and allows for appending file
    print("Welcome to ToDoVille!") # print the statement
    lines = file.readlines() # save lines in var lines. list object
        
    current_command = "" # input bucket == current_command
    while(current_command != "q"): # main loop
        current_command = input("Awaiting further commands. [q] to quit, [a] to add new item, [p] to print list: ") 
        
        if(current_command == "a"): # if 'a' then write input > file
            new_item = input("Type your todo below: ")
            file.write(new_item + "\n")
            
        elif(current_command == "p"): # if 'p' then search via seek for input 
            file.seek(0)
            lines = file.readlines()
            
            print("Here are your items:") # confirmation for summary print
            for line in lines:
                print(line)

random_die_roll = random.randint(1,7)
while True:
    player_guess = int(input('Enter a number between 1 and 6: '))
    if player_guess == random_die_roll:
        print('You win!')
        break
    else:
        print('Guess again:')

employees = [
  {
    "first_name": "Hennah", 
    "last_name": "Chadwick",
    "job_title": "Vice President",
    "hire_date": 1985,
    "performance_review": "excellent"
  }, {
    "first_name": "Michael", 
    "last_name": "Bolton",
    "job_title": "Programmer",
    "hire_date": 1995,
    "performance_review": "poor"
  }, {
    "first_name": "Ellesse", 
    "last_name": "Jaramillo",
    "job_title": "Programmer",
    "hire_date": 1989,
    "performance_review": "poor"
  }, {
    "first_name": "Samir", 
    "last_name": "Nagheenanajar",
    "job_title": "Programmer",
    "hire_date": 1974,
    "performance_review": "fair"
  }, {
    "first_name": "Milton", 
    "last_name": "Waddams",
    "job_title": "Collator",
    "hire_date": 1974,
    "performance_review": "does he even work here?"
  }, {
    "first_name": "Bob", 
    "last_name": "Porter",
    "job_title": "Consultant",
    "hire_date": 1999,
    "performance_review": "excellent"
  }, {
    "first_name": "Bob", 
    "last_name": "Slydell",
    "job_title": "Consultant",
    "hire_date": 1999,
    "performance_review": "excellent"
  }
]

employees[0]
employees[0].keys()
list(employees[0].keys())

# writing files

with open("test.txt", "w") as file:
    print("hello world")

with open("all_evaluations.csv", "w") as file:
    # Create a fieldnames list that will act as column headers using our dictionary keys 
    fieldnames = list(employees[0].keys())
    
    # Append the "action_item" column to the end of our fieldnames
    fieldnames.append("action_item")
    # Pass the file name and fieldnames list to the DictWriter function 
    writer = csv.DictWriter(file, fieldnames = fieldnames)
    writer.writeheader()
    # Loop through each employee and determine what to put in their action_item column
    for employee in employees:
        row = employee
        if employee['performance_review'] == 'poor':
            row['action_item'] = 'terminate'
        elif employee['performance_review'] == 'excellent':
            row['action_item'] = 'bonus'
        else:
            row['action_item'] = 'attend GA workshop'
        # At the end of the loop, write each row to the file 
        writer.writerow(row)

with open('all_evaluations.csv','r') as file:
    rows = csv.DictReader(file)
    names = []
    
    for row in rows:
        print(row['first_name'], row['last_name'], row['job_title'])
        names = row['first_name'], row['last_name'], row['job_title']