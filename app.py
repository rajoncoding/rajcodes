command = " "
started = False

while True:
    command = input('>  ').lower()
    if command == 'start':
        if started:
            print("Car is already started...")
        else:
            started = True
            print("Car is started")
    elif command == 'stop':
        if not started:
            print("Car is already Stopped")
        else:
            started = False
            print("Car is Stopped")
    elif command == 'help':
        print("""
start  'to start the car'
stop   'to stop the car'
quit   'to come out'
        """)
    elif command == 'quit':
        print("Game quitted")
        break
    else:
        print("Please enter something")





