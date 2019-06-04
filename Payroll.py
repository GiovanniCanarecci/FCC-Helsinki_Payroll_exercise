#1) enter new employee (they have to be unique: so dictionary) -> Enter name
#it enters the name and than comes back to the screen
#2) calculate pay -> which employee (show the list) + enter #hours worked.
#then display: gross pay, (-) Tax, Net pay
#3) List employees in alphabetical order
#Employee list>: name, net pay
#x) quit

#A set of lists!
employees= list()
employeesDict= dict()
quit=False
userImput = None
#Payrolls calculation variables
#assumption (7x24 is the maximum #hours) 
hours=0.0
gross=0.0
tax=0.0
nett=0.0
taxRate=0.18   #Tax rate: 18%
otRate=1.5     #overtime: 15/h (only after regHours hours)
regHours=40 
basicPay=10    #payrate: 10/h (minimum wage)

print('Hello!')
while not quit: #quit == False:
    print('Your choices are:')
    print('1 - Enter new employee')
    print('2 - Calculate pay')
    print('3 - List employees')
    print('x - Quit')
    userInput = input('Please make your choice: ') #IT RECEIVES ONLY STRINGS
    #print(userInput)
    #1) enter new employee (they have to be unique: so dictionary). It enters the name and than comes back to the screen.
    if userInput =='1':
        userInput = None
        NewName = input('Enter name of the employee, then press Enter: ') #IT RECEIVES ONLY STRINGS
        employees.append([NewName,0])
        employeesDict[NewName] =(0,0,0) #a tuple of three values, to be filled later
        #print(NewName)#for debugging
    #2) calculate pay: ask which employee (show the list) + enter #hours worked. Then display: gross pay, (-) Tax, Net pay
    elif userInput =='2':
        if len(employees) == 0:
            print('First add at least one employee.')
        else:
            userInput = None
            print('Here there is the list of your employees. Choose one: ')
            for counter in range(len(employees)):
                #print(counter)#for debugging
                listEmployees = '{0} - {1}'.format(counter, employees[counter][0]) #but it's a set and it must be in alphabetical order!
                print(listEmployees)
                #print(len(employees))#for debugging
            try:
                InputEmployee = input('Choose the number(!) of the employee whose pay you want to enter: ') #IT RECEIVES ONLY STRINGS
                #print(InputEmployee)#for debugging
                try:
                    InputEmployee_index = int(InputEmployee)
                    result = employeesDict.get(employees[InputEmployee_index][0],'No such employee')
                    #print(result)#for debugging
                    if result != 'No such employee':
                        hours = float(input('Enter # hours worked this week by {}: '.format(employees[InputEmployee_index][0])))
                        if hours <= 24*7:
                            if hours > regHours:
                                gross=((hours-regHours)*otRate*basicPay)+ (regHours*basicPay)
                            else:
                                gross=hours*basicPay
                            tax=gross*taxRate
                            net=gross-tax
                            employeesDict[userInput] = (gross,tax,net)
                            print('Gross salary: {0} €'.format(gross))
                            print('Taxation: {0} €'.format(tax))
                            print('Net salary: {0} €'.format(net))
                            employees[InputEmployee_index][1] = net
                        else:
                            print('This is cheating! This amount of hours is impossible even for me (the computer)! Now I am offended!')
                    else:
                        print('No such employee.')
                except ValueError:
                    print("That's not a correct number!")
            except IndexError:
                print("That's not a correct index value!")
    #3) List employees in alphabetical order. Employee list: name, net pay
    elif userInput =='3':
        userInput = None
        if len(employees) == 0:
            print('Enter at least one employee first!')
        else:
            print('Employee List')
            for counter in range(0,len(employees)):
                listEmployees_net = '{0} -> {1} euro'.format(employees[counter][0], employees[counter][1]) #but it's a set and it must be in alphabetical order!
                print(listEmployees_net)
    #x) quit
    elif userInput =='x':
        quit=True
    else:
       print('Invalid sintax! Try again!')
