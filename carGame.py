command = ''

started = False

while True:   ##while command != "quit":
    command = input('> ').lower()

    if command == "start":
        if started:
            print('car is already started')
        else:
            started = True
            print("car started")

    elif command == "stop":
        if not started:
            print('car is already stopped')
        else:
            started = False
            print("card stopped")
    elif command == "help":
        print("""
        start- to start the car
        stop- to stop the car
        quit- the quite
        
        """)
    elif command == "quite":
        break
    else:
        print("sorry! i don't understand that.")
