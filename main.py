# Code by Niroo Arjuna

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
    text_entered = input("Enter a new command (Type QUIT to exit script) ")

    # Convert user input to uppercase, so command comparison is case insensitive
    text_upper = text_entered.upper()
    # Split user input to a list
    words = text_upper.split()

    # first word should contain command
    if words[0] == "PLACE":
        # COMMAND + 3 Parameters [PLACE {X} {Y} {Direction}]
        if len(words) == 4:
            try:
                xCoordinate = int(words[1])
                yCoordinate = int(words[2])
                direction = words[3]

                robot.place(xCoordinate, yCoordinate, direction)
            except ValueError:
                print("Error: Invalid command parameters, please enter valid command parameters")
        else:
            print("Error: Invalid syntax, please enter valid syntax")
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
        print("Error: Unknown Command, please enter a valid command")

# Code by Niroo Arjuna