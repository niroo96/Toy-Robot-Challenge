# Code by Niroo Arjuna

from unittest import TestCase
from classes.robot import Robot

class Test(TestCase):

    #Test to ensure that toy robot is placed within the board boundaries
    def test_placetest(self):
        robot = Robot()

        robot.place(2, 2, "EAST")
        self.assertEqual(robot.report(), "(2, 2, EAST)")

        # more than board bounds
        robot.place(1, 6, "NORTH")
        self.assertNotEqual(robot.report(), "(1, 6, NORTH)")

        robot.place(0, 0, "NORTH")
        self.assertEqual(robot.report(), "(0, 0, NORTH)")

    #Enusre that the toy robot doesn't not move out of bounds
    def test_movetest(self):
        robot = Robot()

        robot.place(1, 2, "WEST")

        robot.move()
        self.assertEqual(robot.report(), "(0, 2, WEST)")

        # shouldn't go more in west direction
        robot.move()
        self.assertEqual(robot.report(), "(0, 2, WEST)")

    #Ensure that the toy robot turns right
    def test_righttest(self):
        robot = Robot()

        robot.place(0, 3, "EAST")

        # turn around full circle
        robot.right()
        self.assertEqual(robot.report(), "(0, 3, SOUTH)")

        robot.right()
        self.assertEqual(robot.report(), "(0, 3, WEST)")

        robot.right()
        self.assertEqual(robot.report(), "(0, 3, NORTH)")

        robot.right()
        self.assertEqual(robot.report(), "(0, 3, EAST)")


    #Esnures that the toy robot turns left
    def test_lefttest(self):
        robot = Robot()

        robot.place(4, 4, "EAST")

        # turn around full circle
        robot.left()
        self.assertEqual(robot.report(), "(4, 4, NORTH)")

        robot.left()
        self.assertEqual(robot.report(), "(4, 4, WEST)")

        robot.left()
        self.assertEqual(robot.report(), "(4, 4, SOUTH)")

        robot.left()
        self.assertEqual(robot.report(), "(4, 4, EAST)")

    #Testing example case 1
    def test_example1(self):
        robot = Robot()

        robot.place(0, 0, "NORTH")
        self.assertEqual(robot.report(), "(0, 0, NORTH)")

        robot.move()
        self.assertEqual(robot.report(), "(0, 1, NORTH)")

        robot.report()
        self.assertEqual(robot.report(), "(0, 1, NORTH)")

    #Testing example case 2
    def test_example2(self):
        robot = Robot()

        robot.place(0, 0, "NORTH")
        self.assertEqual(robot.report(), "(0, 0, NORTH)")

        robot.left()
        self.assertEqual(robot.report(), "(0, 0, WEST)")

        robot.report()
        self.assertEqual(robot.report(), "(0, 0, WEST)")

    #Testing example case 3
    def test_example3(self):
        robot = Robot()

        robot.place(1, 2, "EAST")
        self.assertEqual(robot.report(), "(1, 2, EAST)")

        robot.move()
        self.assertEqual(robot.report(), "(2, 2, EAST)")

        robot.move()
        self.assertEqual(robot.report(), "(3, 2, EAST)")

        robot.left()
        self.assertEqual(robot.report(), "(3, 2, NORTH)")

        robot.report()
        self.assertEqual(robot.report(), "(3, 2, NORTH)")


# Code by Niroo Arjuna