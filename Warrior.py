import Fighter
import random
import Fight

class Warrior(Fighter.Fighter):

    def __init__(self, skills:dict, name:str="", age:int=0, wealth:int=0) -> "Warrior":
        "Initializes an instance of a Warrior with skills, name, age, and wealth attributes."
        super().__init__(skills, name, age, wealth)
        self.type = "Warrior"
        self.listOfChallenges = []
        self.currChallenge = 1
        self.challenges = dict()

    def sendChallenge(self, challenger:'Fighter', skill:str) -> None:
        "Deals with processing a sent challenge from a Fighter"
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
        "Deals with the specifics for accepting a challenge from a Fighter."
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
        "Accepts a random challenge in the list of challenges."
        if self.challenges: #check if there is a challenge
            randChallenger = random.choice(self.listOfChallenges)
            self.acceptChallenge(self.challenges[randChallenger][0], self.challenges[randChallenger][1])
            self.challenges.pop(randChallenger)
            self.listOfChallenges.remove(randChallenger)
        else:
            print("There are no challenges to accept.\n")

    def decline_random(self) -> None:
        "Declines a random challenge in the list of challenges."
        if self.challenges: #check if there is a challenge
            randChallenger = random.choice(self.listOfChallenges)
            self.challenges.pop(randChallenger)
            self.listOfChallenges.remove(randChallenger)
        else:
            print("There are no challenges to decline.\n")
    
    def accept_first(self) -> None:
        "Accepts the first challenge in the list of challenges."
        if self.challenges: #check if there is a challenge
            accepted = self.listOfChallenges.pop(0)
            self.acceptChallenge(self.challenges[accepted][0], self.challenges[accepted][1])
            self.challenges.pop(accepted)
        else:
            print("There are no challenges to accept.\n")
    
    def accept_last(self) -> None:
        "Accepts the last challenge in the list of challenges."
        if self.challenges: #check if there is a chellenge
            accepted = self.listOfChallenges.pop(len(self.listOfChallenges)-1)
            self.acceptChallenge(self.challenges[accepted][0], self.challenges[accepted][1])
            self.challenges.pop(accepted)
        else:
            print("There are no challenges to accept.\n")

    def removeChallenge(self, fighter:'Fighter') -> None:
        "Removes a challenge issues by a Fighter if one exists."
        if (self.challenge):
            for challenge in list(self.challenges):
                if self.challenges[challenge][0] == fighter:
                    self.challenges.pop(challenge)
                    self.listOfChallenges.remove(challenge)
            print("All challenges by " + fighter.name + " withdrawed.\n")
        else:
            print("There are no challenges to withdraw")

    def __str__(self) -> str:
        "Prints string representation of the class' attributes."
        result = ("Name: " + self.name + " | Age: " + str(self.age) + " | Wealth: " + str(self.wealth) + "\n")
        result += ("Skills: " + str(self.skills) + "\n")
        result += ("List of Challenges: " + str(self.challenges) + "\n")
        return result