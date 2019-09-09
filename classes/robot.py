# Code by Niroo Arjuna

class Robot:
    orientation = ["EAST", "WEST", "NORTH", "SOUTH"]

    def __init__(self):
        #Initially declare the variables of the Toy Robot
        self.x_position = None
        self.y_position = None
        self.width = 5
        self.height = 5
        self.facing = None
        self.placed = False

    def place(self, x, y, facing):
        #Initially checking to ensure that coordinates are in the 5x5 Square Top
        if self.coordinates_in_boundry(x, y) is False:
            return

        #Check if the orientation is valid
        if facing not in self.orientation:
            print("Toy robot not placed due to unknown orientation!")
            return

        #Robot placed if robot inside the square top and orientation is valid
        self.placed = True
        self.x_position = x
        self.y_position = y
        self.facing = facing
        print("Toy robot has been placed")

    def move(self):
        if self.placed is False:
            print("Toy robot has not been placed!")

        if self.facing == "EAST":
            x, y = self.x_position + 1, self.y_position
        elif self.facing == "WEST":
            x, y = self.x_position - 1, self.y_position
        elif self.facing == "NORTH":
            x, y = self.x_position, self.y_position + 1
        elif self.facing == "SOUTH":
            x, y = self.x_position, self.y_position - 1
        else:
            print("Toy Robot placed in unknown orientation and cannot be moved")

        if self.coordinates_in_boundry(x,y) is True:
            #Move the Toy Robot
            self.x_position = x
            self.y_position = y
            print("Toy Robot has moved")

    def left(self):
        if self.placed is False:
            print("Toy robot has not been placed!")
            return

        turn_left = \
            [
                # current facing, left of current facing
                ("EAST", "NORTH"),
                ("WEST", "SOUTH"),
                ("SOUTH", "EAST"),
                ("NORTH", "WEST"),
            ]

        #Facing, Left
        for (f, l) in turn_left:
            if self.facing == f:
                self.facing = l
                print("Toy robot has turned left")
                break

    def right(self):
        if self.placed is False:
            print("Toy robot has not been placed!")
            return

        turn_right = \
            [
                # current facing, left of current facing
                ("EAST", "SOUTH"),
                ("WEST", "NORTH"),
                ("SOUTH", "WEST"),
                ("NORTH", "EAST"),
            ]

        # Facing, Right
        for (f, r) in turn_right:
            if self.facing == f:
                self.facing = r
                print("Toy robot has turned right")
                break

    def report(self):
        if self.placed is False:
            print("Toy robot has not been placed!")
            return


        info = "({0}, {1}, {2})".format(self.x_position, self.y_position, self.facing)
        print(info)
        return info

    def coordinates_in_boundry(self, x, y):
        if x < 0 or x >= self.width: #Maximum self.width is 5
            print("Toy Robot's X position is out of bounds!")
            return False

        if y < 0 or y >= self.height: #Maximum self.height is 5
            print("Toy Robot's Y position is out of bounds!")
            return False

        return True

# Code by Niroo Arjuna


