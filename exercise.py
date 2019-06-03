command = ()
in_motion = False
while True:
    command = input(">")
    if command == "help":
        print("""
start - start the car
stop - stop the car
quit - exit game
        """)
    elif command == "start" and not in_motion:
        print("car started")
        in_motion = True
    elif command == "start" and in_motion:
        print("car is already started")
    elif command == "stop" and not in_motion:
        print("car already stopped")
    elif command == "stop" and in_motion:
        print("car stopped")
        in_motion = False
    elif command == "quit":
        break
    else:
        print("sorry i don't understand")
