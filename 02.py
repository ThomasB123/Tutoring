
# 1.
infile = open('airports.txt','r')
airports = []
for line in infile:
    airports.append(line.split('\n')[0].split(','))
infile.close()
airports = airports[1:]

ukAirports = ['LPL','BOH']

intAirports = []
for i in range(len(airports)):
    intAirports.append(airports[i][0])

aircraft = [['Medium narrow body',8,2650,180,8],['Large narrow body',7,5600,220,10],['Medium wide body',5,4050,406,14]]

# 2.
while True:
    choice = input('''Select an option:
    1. Enter airport details
    2. Enter flight details
    3. Enter price plan and calculate profit
    4. Clear data
    5. Quit
    Your Choice > ''')
    if choice == '1':
# 4.
        valid1 = False
        ukCode = input('Enter the 3-letter code for the UK airport > ')
        if ukCode in ukAirports:
            intCode = input('Enter the 3-letter code for the overseas airport > ')
            if intCode in intAirports:
                print(airports[intAirports.index(intCode)][1])
                valid1 = True
            else:
                print('Invalid overseas airport code')
        else:
            print('Incorrect UK airport code')
    if choice == '2':
# 5.
        valid2 = False
        valid3 = False
        airType = input('Enter the type of aircraft > ')
        types = ['Medium narrow body','Large narrow body','Medium wide body']
        if airType in types:
            index = types.index(airType)
            print('''
            Type: {}
            Running cost: £{}
            Range: {}km
            Capacity: {}
            Min first-class seats: {}
            '''.format(aircraft[index][0],aircraft[index][1],aircraft[index][2],aircraft[index][3],aircraft[index][4]))
            valid2 = True
            first = int(input('Enter the number of first-class seats > '))
            if first != 0:
                if first < aircraft[index][4]:
                    print('Number of first-class seats must be at least {}'.format(aircraft[index][4]))
                elif first > aircraft[index][3] /2:
                    print('Number of first-class seats must be no more than {}'.format(aircraft[index][3] //2))
                else:
                    standard = aircraft[index][3] - first * 2
                    print('Number of standard-class seats: {}'.format(standard))
                    valid3 = True
            else:
                standard = aircraft[index][3]
                print('Number of standard-class seats: {}'.format(standard))
                valid3 = True
        else:
            print('Invalid aircraft type')
    if choice == '3':
# 6.
        if 'valid1' in locals() and valid1:
            if 'valid2' in locals() and valid2:
                if 'valid3' in locals() and valid3:
                    planeRange = aircraft[index][2]
                    distance = int(airports[intAirports.index(intCode)][ukAirports.index(ukCode)+2])
                    if planeRange >= distance:
                        standardPrice = int(input('Enter price of standard-class seat > '))
                        firstPrice = int(input('Enter price of first-class seat > '))
                        perSeat = aircraft[index][1] * distance /100
                        cost = perSeat * (first + standard)
                        income = first * firstPrice + standard * standardPrice
                        profit = income - cost
                        print('''
                        Flight cost per seat: £{}
                        Flight cost: £{}
                        Flight income: £{}
                        Flight profit: £{}
                        '''.format(perSeat,cost,income,profit))
                    else:
                        print('The aircraft range is {} but the distance between the airports is {}'.format(planeRange,distance))
                else:
                    print('You must first enter number of first-class seats')
            else:
                print('You must first enter the aircraft details')
        else:
            print('You must first enter the airport details')
    if choice == '4':
# 7.
        ukCode = None
        intCode = None
        airType = None
        first = None
        standardPrice = None
        firstPrice = None
        valid1 = None
        valid2 = None
        valid3 = None
        print('Data cleared')
    if choice == '5':
# 3.
        print('You have chosen to quit')
        quit()
