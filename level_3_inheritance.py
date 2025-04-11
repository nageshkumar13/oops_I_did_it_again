##########################################################################################
#                       Inheritance – Like Parent, Like Child
##########################################################################################

class Robot:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello master, {self.name} is at your service.")    

class CleanerBot(Robot):
    def clean(self):
        print(f"{self.name} is cleaning.")


class SecurityBot(Robot):
    def patrol(self):
        print(f"{self.name} is patrolling the area.")        

class ChefBot(Robot):
    def cook(self):
        print(f"{self.name} is cooking meal.")        

cleaner = CleanerBot("Dusty")
cleaner.greet()
cleaner.clean()

security = SecurityBot('Guardian')
security.greet()
security.patrol()

chef = ChefBot('Pasco')
chef.greet()
chef.cook()