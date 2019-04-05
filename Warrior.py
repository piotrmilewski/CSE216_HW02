import Fighter
import random
import Fight

class Warrior(Fighter.Fighter):

    def __init__(self, skills:dict, name:str="", age:int=0, wealth:int=0):
        super().__init__(skills, name, age, wealth)
        self.type = "Warrior"
        self.listOfChallenges = []
        self.currChallenge = 1
        self.challenges = dict()

    def sendChallenge(self, challenger:'Fighter', skill:str) -> None:
        found = False
        for challenge in self.challenges:
            if self.challenges[challenge][0] == challenger:
                found = True
        if (found):
            print("Fighter has already issued a challenge.\n")
        else:
            self.listOfChallenges.append(self.currChallenge)
            self.challenges[self.currChallenge] = (challenger, skill)
            self.currChallenge = self.currChallenge + 1

    def acceptChallenge(self, challenger:'Fighter', skill:str) -> None:
        fight = Fight.Fight(challenger, self, skill)
        winner = fight.winner()
        if winner == self:
            if (challenger.type == "Fighter" or challenger.type == "Warrior"):
                challenger.lostChallenge(skill, 10, True)
                self.wonChallenge(skill, 10, 0)
            else:
                challenger.lostChallenge(skill, 20, False)
                self.wonChallenge(skill, 20, 1)
        else:
            if (challenger.type == "Fighter"):
                self.lostChallenge(skill, 25, False)
                challenger.wonChallenge(skill, 10, 1)
            else:
                self.lostChallenge(skill, 10, True)
                challenger.wonChallenge(skill, 10, 0)

    def accept_random(self) -> None:
        if self.challenges: #check if there is a challenge
            randChallenger = random.choice(self.listOfChallenges)
            self.acceptChallenge(self.challenges[randChallenger][0], self.challenges[randChallenger][1])
            self.challenges.pop(randChallenger)
            self.listOfChallenges.remove(randChallenger)
        else:
            print("There are no challenges to accept.")

    def decline_random(self):
        if self.challenges: #check if there is a challenge
            randChallenger = random.choice(self.listOfChallenges)
            self.challenges.pop(randChallenger)
            self.listOfChallenges.remove(randChallenger)
        else:
            print("There are no challenges to decline.")
    
    def accept_first(self):
        if self.challenges: #check if there is a challenge
            accepted = self.listOfChallenges.pop(0)
            self.acceptChallenge(self.challenges[accepted][0], self.challenges[accepted][1])
            self.challenges.pop(accepted)
        else:
            print("There are no challenges to accept.")
    
    def accept_last(self):
        if self.challenges: #check if there is a chellenge
            accepted = self.listOfChallenges.pop(len(self.listOfChallenges)-1)
            self.acceptChallenge(self.challenges[accepted][0], self.challenges[accepted][1])
            self.challenges.pop(accepted)
        else:
            print("There are no challenges to accept.")

    def __str__(self):
        result = ("Name: " + self.name + " | Age: " + str(self.age) + " | Wealth: " + str(self.wealth) + "\n")
        result += ("Skills: " + str(self.skills) + "\n")
        result += ("List of Challenges: " + str(self.challenges) + "\n")
        return result