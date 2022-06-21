from dinosaur import Dinosaur
from robot import Robot 


class Battlefield:

    def __init__(self):
        self.robot = Robot("Bender")
        self.dinosaur = Dinosaur("Charizard", 20)

    def run_game(self):
        self.print_display_welcome()
        self.battle_phase()


    def print_display_welcome(self):
        print("welcome to an epic battle the ages!")
        print("Only one side can win!")
    
    def battle_phase(self):
        robo_player = self.robot
        dino_player = self.dinosaur
        while self.robot.health > 0:
            self.robot.attack(dino_player)
            dino_remaining_health = self.robot.health
            print (f"Robot {self.robot.name} attacked {self.dinosaur.name}. {self.dinosaur.name} has blank {dino_remaining_health} remaining")
        if self.dinosaur.health > 0:
            self.dinosaur.attack(robo_player)
            print (f"Dinosaue {self.dinosaur.name} attacked {self.robot.name}.")
            print (f"{self.robot.name} has blank health remaining")

    def display_winner(self):
        self.winner = ""

