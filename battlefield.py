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
        robo_player = self.robot
        dino_player = self.dinosaur

        while robo_player == self.robot and dino_player == self.dinosaur:  
            if self.robot.health > 0:
                self.robot.attack(dino_player)
                dinosaur_remaining_health = self.dinosaur.health
                print (f"Robot {self.robot.name} attacked {self.dinosaur.name} for {self.robot.active_weapon.attack_power} damage. {self.dinosaur.name} has {dinosaur_remaining_health} health remaining.")
                print(" ")
            if self.dinosaur.health > 0:
                self.dinosaur.attack(robo_player)
                robot_remaining_health = self.robot.health
                print (f"Dinosaur {self.dinosaur.name} attacked {self.robot.name} for {self.dinosaur.attack_power} damage. {self.robot.name} has {robot_remaining_health} health remaining.")
                print(" ")
            elif dinosaur_remaining_health == 0:
                self.winner = robo_player.name
                break
            elif robot_remaining_health == 0:
                self.winner = dino_player.name
                break

    def display_winner(self):
        self.winner == self.winner
        print(f"{self.winner} has been declared the winner!" )
        print(" ")
        


