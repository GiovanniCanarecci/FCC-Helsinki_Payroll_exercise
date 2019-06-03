#1) enter new employee (they have to be unique: so dictionary) -> Enter name
#it enters the name and than comes back to the screen
#2) calculate pay -> which employee (show the list) + enter #hours worked.
#then display
#gross pay
#(-) Tax
#Net pay
#3) List employees in alphabetical order
#Employee list
#name, net pay
#x) quit

#assumption (7x24 is the maximum)
#payrate: 10/h (minimum wage) #they may change later on
#overtime: 15/h
#OTime only after 40 hours
#Tax rate: 18%
#A SET OF LISTS!!!
employees= list()
employeesDict= dict()
quit=False
userImput = None
#Payrolls calculation variables
Minimum=10
OTime=15
Taxperc=18
hours=0.0
gross=0.0
tax=0.0
nett=0.0
taxRate=0.18
otRate=1.5
regHours=40
basicPay=10

while not quit: #quit == False:

    print('Hello! Your choices are:')
    print('1 - Enter new employee')
    print('2 - Calculate pay')
    print('3 - List employees')
    print('x - Quit')
    userInput = input('Please make your choice:') #IT RECEIVES ONLY STRINGS
    print(userInput)
    #1) enter new employee (they have to be unique: so dictionary) -> Enter name
    #it enters the name and than comes back to the screen
    if userInput =='1':
        userInput = None
        NewName = input('Enter name and surname separeted by a space, then press Enter:') #IT RECEIVES ONLY STRINGS
        employees.append([NewName,0])
        employeesDict[NewName] =(0,0,0) #a tuple of three values
        #print(NewName)
    #2) calculate pay -> which employee (show the list) + enter #hours worked.
    #then display
    #gross pay
    #(-) Tax
    #Net pay
    elif userInput =='2':
        userInput = None
        userInput =input('For which employee: ')
        result = employeesDict.get(userInput,'No such employee')
        if result != 'No such employee':
            hours = float(input('Enter # hours wordes: '))
            if hours > regHours:
                gross=((hours-regHours)*otRate*basicPay)+ (regHours*basicPay)
            else:
                gross=hours*basicPay
            tax=gross*taxRate
            net=gross-tax
            employeesDict[userInput] = (gross,tax,net)

        if len(employees) == 0:
            print('Enter at least one employee first!')
        else:
            print('Here there is the list of your employees. Choose one:')
            for counter in (0,len(employees)):
                listEmployees = '{0} - {1}'.format(counter, employees[counter][0]) #but it's a set and it must be in alphabetical order!
                print(listEmployees)
            InputEmployee = input('Choose the number of the employee whose pay you want to enter') #IT RECEIVES ONLY STRINGS
            print(InputEmployee)
            InputHours = input('Enter the number of hours of {0} for this week',employees[InputEmployee][0]) #IT RECEIVES ONLY STRINGS
            print(InputHours)
            #COMPUTATION
            if InputHours >= 168:
                print('He is cheating, he does not work that much! Now I am offended!')
            if InputHours <= 40:
                Payrate = InputHours*Minimum
                Overtime =0
            else:
                Payrate = 40*Minimum
                Overtime = (InputHours-40)*OTime
            Gross = Payrate + Overtime
            Taxation = Gross*(100-Taxperc)*100
            Net = Gross - Taxation
            print('Gross salary: {0} €',Gross)
            print('Taxation: {0} €',Taxation)
            print('Net salary: {0} €',Net)
            employees[InputEmployee][1] = Net
    #3) List employees in alphabetical order
    #Employee list
    #name, net pay
    elif userInput =='3':
        userInput = None
        if len(employees) == 0:
            print('Enter at least one employee first!')
        else:
            print('Employee List')
            nameList = employeesDict.keys()
            nameList.sort()
            for name in nameList:
                print('{} -> {}'.format(name,employeesDict[name][2]))

            employees.sort()
            for countershow in (0,len(employees)):
                print('{0}: {1} euro',employees[countershow][0],employees[countershow][1])
    #x) quit
    elif userInput =='x':
        quit=True
    else:
       print('Invalid sintax!')
    #    print(countries.get('cn','Country not found!'))