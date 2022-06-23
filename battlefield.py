from dinosaur import Dinosaur
from robot import Robot 


class Battlefield:

    def __init__(self):
        self.robot = Robot("Bender")
        self.dinosaur = Dinosaur("Charizard", 20)

    def run_game(self):
        self.print_display_welcome()
        print(" ")
        self.battle_phase()
        print(" ")
        self.display_winner()

    def print_display_welcome(self):
        print("welcome to an epic battle the ages!")
        print(" ")
        print("Only one side can win!")
    
    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:  
            if self.robot.health > 0:
                self.robot.attack(self.dinosaur)
            if self.dinosaur.health > 0:
                self.dinosaur.attack(self.robot)

    def display_winner(self):
        if self.dinosaur.health > 0:
            print(f"{self.dinosaur.name} has been declared the winner!" )
            print(" ")
        elif self.robot.health > 0:
            print(f"{self.robot.name} has been declared the winner!" )
            print(" ")
        
        


