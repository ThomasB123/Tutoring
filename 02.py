
# 1.
inFile = open('airports.txt','r')

airports = []
for line in inFile:
    airports.append(line.split('\n')[0].split(','))
inFile.close()

intAirports = []
for i in range(len(airports)):
    intAirports.append(airports[i][0])

ukAirports = ['LPL','BOH']

aircraft = [['Medium narrow body',8,2650,180,8],['Large narrow body',7,5600,220,10],['Medium wide body',5,4050,406,14]]

valid1 = False
valid2 = False
valid3 = False

# 2.
while True:

    choice = input('''
    Select an option:
    1. Enter airport details
    2. Enter flight details
    3. Enter price plan and calculate profit
    4. Clear data
    5. Quit
    Your Choice > ''') # user input here

    if choice == '1':
# 4.
        ukCode = input('Enter the 3-letter code for the UK airport > ') # user input here

        if ukCode in ukAirports:
            intCode = input('Enter the 3-letter code for the overseas airport > ') # user input here
            if intCode in intAirports:
                print(airports[intAirports.index(intCode)][1]) # program output here
                valid1 = True
            else:
                print('Invalid overseas airport code') # program output here
                valid1 = False
        else:
            print('Invalid UK airport code') # program output here
            valid1 = False
    if choice == '2':
# 5.
        airType = input('Enter the type of aircraft > ') # user input here

        types = ['Medium narrow body','Large narrow body','Medium wide body']
        if airType in types:
            x = types.index(airType)

            print('''
            Type:  {}
            Running cost per seat per 100km:  £{}
            Maximum flight range:  {}km
            Capacity if all standard-class:  {}
            Minimum number of first-class seats (if any):  {}
            '''.format(aircraft[x][0],aircraft[x][1],aircraft[x][2],aircraft[x][3],aircraft[x][4])) # program output here

            valid2 = True
            first = int(input('Enter the number of first-class seats > ')) # user input here
            
            if first != 0:
                if first < aircraft[x][4]:
                    print('Number of first-class seats must be at least {}'.format(aircraft[x][4])) # program output here
                    valid3 = False
                elif first > aircraft[x][3] /2:
                    print('Number of first-class seats must be no more than {}'.format(aircraft[x][3] // 2)) # program output here
                    valid3 = False
                else:
                    standard = aircraft[x][3] - first * 2
                    print('Number of standard-class seats: {}'.format(standard)) # program output here
                    valid3 = True
            else:
                standard = aircraft[x][3]
                print('Number of standard-class seats: {}'.format(standard)) # program output here
                valid3 = True
        else:
            print('Invalid aircraft type') # program output here
            valid2 = False
    if choice == '3':
# 6.
        if valid1:
            if valid2:
                if valid3:
                    planeRange = aircraft[x][2]
                    distance = int(airports[intAirports.index(intCode)][ukAirports.index(ukCode)+2])
                    if planeRange >= distance:

                        standardPrice = int(input('Enter price of standard-class seat > ')) # user input here

                        firstPrice = int(input('Enter price of first-class seat > ')) # user input here

                        perSeat = aircraft[x][1] * distance / 100
                        cost = perSeat * (first + standard)
                        income = first * firstPrice + standard * standardPrice
                        profit = income - cost
                        
                        print('''
                        Flight cost per seat: £{}
                        Flight cost: £{}
                        Flight income: £{}
                        Flight profit: £{}
                        '''.format(perSeat,cost,income,profit)) # program output here
                    else:
                        print('The aircraft range is {}km but the distance between the airports is {}km'.format(planeRange,distance)) # program output here
                else:
                    print('You must first enter number of first-class seats') # program output here
            else:
                print('You must first enter the aircraft details') # program output here
        else: 
            print('You must first enter the airport details') # program output here
    if choice == '4':
# 7.
        ukCode = None
        intCode = None
        airType = None
        first = None
        standardPrice = None
        firstPrice = None
        
        valid1 = False
        valid2 = False
        valid3 = False
        print('Data cleared') # program output here
    if choice == '5':
# 3.
        print('You have chosen to quit') # program output here
        quit() # close the program
