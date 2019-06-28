from classes.robot import Robot
robot = Robot()
condition = True

print('--------------------------\n'
    '''
                          (                                                                          
          *   )           )\ )       )         )     (      )      (  (                              
        ` )  /(   (      (()/(    ( /(      ( /(     )\  ( /(    ) )\ )\  (       (  (    (          
   ______( )(_)|  )\ )___ /(_))(  )\())  (  )\())__(((_) )\())( /(((_|(_)))\ (    )\))(  ))\  ______ 
  / / / (_(_()))\(()/(___(_))  )\((_)\   )\(_))/___)\___((_)\ )(_))_  _ /((_))\ )((_))\ /((_)/ / / / 
 / / / /|_   _((_))(_))  | _ \((_) |(_) ((_) |_   ((/ __| |(_|(_)_| || (_)) _(_/( (()(_|_)) / / / /  
/_/_/_/   | |/ _ \ || |  |   / _ \ '_ \/ _ \  _|   | (__| ' \/ _` | || / -_) ' \)) _` |/ -_)_/_/_/   
          |_|\___/\_, |  |_|_\___/_.__/\___/\__|    \___|_||_\__,_|_||_\___|_||_|\__, |\___|         
                  |__/                                                           |___/                                                                                                                                                                                                                   
    ''')
print("--------------------------")
print("Toy Robot Simulator Challenge Solution")
print("Developed by: Niroo Arjuna")
print("--------------------------")

while condition:
    text_entered = input("Enter new command (QUIT for end): ")

    # convert user input to uppercase, so command comparison is case insensitive
    text_upper = text_entered.upper()
    # split user input to a list
    words = text_upper.split()

    # first word should contain command
    if words[0] == "PLACE":
        # command + three parameters - PLACE X Y FACING
        if len(words) == 4:
            try:
                xCoord = int(words[1])
                yCoord = int(words[2])
                facing = words[3]

                robot.place(xCoord, yCoord, facing)
            except ValueError:
                print("Invalid command parameters")
        else:
            print("Invalid syntax")
    elif words[0] == "MOVE":
        robot.move()
    elif words[0] == "LEFT":
        robot.left()
    elif words[0] == "RIGHT":
        robot.right()
    elif words[0] == "REPORT":
        robot.report()
    elif words[0] == "QUIT":
        condition = False
    else:
        print("Unknown command...")