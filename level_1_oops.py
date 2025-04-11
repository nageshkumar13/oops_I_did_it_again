"""Blue Print of Robot"""

class Robot:                            # class Robot = defines a class(blueprint)
    def __init__(self, name, task):     # __init__  = The constructor method, it runs when you create an object.
        self.name = name
        self.task = task                # self -> refers to the current object

    def introduce(self):
        print(f"Hi I am {self.name} and I {self.task} !")

robot_1 = Robot("Robo_cleaner", "clean floors")  # robot 1 and 2 are instances of the class
robot_2 = Robot("Chef_bot", "cook food")

robot_1.introduce()
robot_2.introduce()
