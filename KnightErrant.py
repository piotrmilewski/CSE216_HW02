import Warrior
import random
import Fight
import Fighter

class KnightErrant(Warrior.Warrior):

    def __init__(self, skills:dict, name:str="", age:int=0, wealth:int=0):
        super().__init__(skills, name, age, wealth)
        self.traveling = False

    #OVERRIDDEN FOR TRAVELING CASE
    #-----------------------------------------------------------------------------------------
    def challenge(self, challengee:'Fighter', skill:str) -> None:
        if not(traveling):
            if id(self) == id(challengee): #check so challenger can't fight himself
                print("Excuse me, you can't fight yourself.\n")
                return None
            if self.wealth <= 0 or challengee.wealth <= 0: #check if both fighters aren't broke
                if self.wealth <= 0:
                    print("{} has no money to challenge someone.\n".format(self.name))
                else:
                    print("{} has no money to challenge someone.\n".format(challengee.name))
                return None
            if not(isinstance(challengee, Fighter)): #check if challenger is of type fighter
                print("Can't challenge this person, they're not a fighter.\n")
                return None
            if not("spear" == skill or "unarmed_combat" == skill or "mace" == skill or "broadsword" == skill): #check if valid skill
                print("Invalid skill to fight with, please select a valid skill and make sure it is lowercase.\n")
                return None
            #if valid challenge
            challengee.sendChallenge(self, skill)
            return None
        else:
            print("Currently traveling.")

    def acceptChallenge(self, challenger:'Fighter', skill:str) -> None:
        fight = Fight.Fight(challenger, self, skill)
        winner = fight.winner()
        if winner == self:
            challenger.lostChallenge(skill, 10, True)
            self.wonChallenge(skill, 10, 1)
        else:
            if (challenger.type == "Fighter"):
                self.lostChallenge(skill, 40, False)
                challenger.wonChallenge(skill, 40, 2)
            elif (challenger.type == "Warrior"):
                self.lostChallenge(skill, 20, False)
                challenger.wonChallenge(skill, 20, 1)
            else:
                self.lostChallenge(skill, 10, True)
                challenger.wonChallenge(skill, 10, 0)

    def accept_random(self) -> None:
        if not(traveling):
            if self.challenges: #check if there is a challenge
                randChallenger = random.choice(self.listOfChallenges)
                self.acceptChallenge(self.challenges[randChallenger][0], self.challenges[randChallenger][1])
                self.challenges.pop(randChallenger)
                self.listOfChallenges.pop(randChallenger)
            else:
                print("There are no challenges to accept.")
        else:
            print("Currently traveling.")

    def decline_random(self):
        if not(traveling):
            if self.challenges: #check if there is a challenge
                randChallenger = random.choice(self.listOfChallenges)
                self.challenges.pop(randChallenger)
                self.listOfChallenges.pop(randChallenger)
            else:
                print("There are no challenges to decline.")
        else:
            print("Currently traveling.")
    
    def accept_first(self):
        if not(traveling):
            if self.challenges: #check if there is a challenge
                accepted = self.listOfChallenges.pop(0)
                self.acceptChallenge(self.challenges[accepted][0], self.challenges[accepted][1])
                self.challenges.pop(accepted)
            else:
                print("There are no challenges to accept.")
        else:
            print("Currently traveling.")
    
    def accept_last(self):
        if not(traveling):
            if self.challenges: #check if there is a chellenge
                accepted = self.listOfChallenges.pop(len(self.listOfChallenges)-1)
                self.acceptChallenge(self.challenges[accepted][0], self.challenges[accepted][1])
                self.challenges.pop(accepted)
            else:
                print("There are no challenges to accept.")
        else:
            print("Currently traveling.")
    #-----------------------------------------------------------------------------------------

    def travel(self) -> None:
        self.traveling = True

    def return_from_travel(self) -> None:
        self.wealth = self.wealth + random.randint(1,101)
        self.traveling = False

    def __str__(self):
        result = ("Name: " + self.name + " | Age: " + str(self.age) + " | Wealth: " + str(self.wealth) + "\n")
        result += ("Skills: " + str(self.skills) + "\n")
        result += ("List of Challenges: " + str(self.challenges) + "\n")
        if (traveling):
            result += "Currently Traveling?: Yes\n"
        else:
            result += "Currently Traveling?: No\n"
        return result