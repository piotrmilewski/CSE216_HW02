import Warrior
import random
import Fight
import Fighter

class KnightErrant(Warrior.Warrior):

    def __init__(self, skills:dict, name:str="", age:int=0, wealth:int=0) -> "KnightErrand":
        "Initializes an instance of a KnightErrand with skills, name, age, and wealth attributes."
        super().__init__(skills, name, age, wealth)
        self.traveling = False

    #OVERRIDDEN FOR TRAVELING CASE
    #-----------------------------------------------------------------------------------------
    def challenge(self, challengee:'Fighter', skill:str) -> None:
        "Challenges another fighter and calls the fighter's method to continue algorithm."
        if not(self.traveling):
            if id(self) == id(challengee): #check so challenger can't fight himself
                print("Excuse me, you can't fight yourself.\n")
                return None
            if self.wealth <= 0 or challengee.wealth <= 0: #check if both fighters aren't broke
                if self.wealth <= 0:
                    print("{} has no money to challenge someone.\n".format(self.name))
                else:
                    print("{} has no money to challenge someone.\n".format(challengee.name))
                return None
            if not(isinstance(challengee, Fighter.Fighter)): #check if challenger is of type fighter
                print("Can't challenge this person, they're not a fighter.\n")
                return None
            if not("spear" == skill or "unarmed_combat" == skill or "mace" == skill or "broadsword" == skill): #check if valid skill
                print("Invalid skill to fight with, please select a valid skill and make sure it is lowercase.\n")
                return None
            #if valid challenge
            challengee.sendChallenge(self, skill)
            return None
        else:
            print("Currently traveling.\n")

    def acceptChallenge(self, challenger:'Fighter', skill:str) -> None:
        "Deals with the specifics for accepting a challenge from a Fighter."
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
        "Accepts a random challenge in the list of challenges."
        if not(self.traveling):
            if self.challenges: #check if there is a challenge
                randChallenger = random.choice(self.listOfChallenges)
                self.acceptChallenge(self.challenges[randChallenger][0], self.challenges[randChallenger][1])
                self.challenges.pop(randChallenger)
                self.listOfChallenges.remove(randChallenger)
            else:
                print("There are no challenges to accept.\n")
        else:
            print("Currently traveling.\n")

    def decline_random(self) -> None:
        "Declines a random challenge in the list of challenges."
        if not(self.traveling):
            if self.challenges: #check if there is a challenge
                randChallenger = random.choice(self.listOfChallenges)
                self.challenges.pop(randChallenger)
                self.listOfChallenges.remove(randChallenger)
            else:
                print("There are no challenges to decline.\n")
        else:
            print("Currently traveling.\n")
    
    def accept_first(self) -> None:
        "Accepts the first challenge in the list of challenges."
        if not(self.traveling):
            if self.challenges: #check if there is a challenge
                accepted = self.listOfChallenges.pop(0)
                self.acceptChallenge(self.challenges[accepted][0], self.challenges[accepted][1])
                self.challenges.pop(accepted)
            else:
                print("There are no challenges to accept.\n")
        else:
            print("Currently traveling.\n")
    
    def accept_last(self) -> None:
        "Accepts the last challenge in the list of challenges."
        if not(self.traveling):
            if self.challenges: #check if there is a chellenge
                accepted = self.listOfChallenges.pop(len(self.listOfChallenges)-1)
                self.acceptChallenge(self.challenges[accepted][0], self.challenges[accepted][1])
                self.challenges.pop(accepted)
            else:
                print("There are no challenges to accept.\n")
        else:
            print("Currently traveling.\n")
    #-----------------------------------------------------------------------------------------

    def travel(self) -> None:
        "Sets taveling to 'True' to show that KnightErrant is currently traveling."
        self.traveling = True

    def return_from_travel(self) -> None:
        "Comes back from travels and earns money from travels."
        if (self.traveling):
            earnings = random.randint(1,101)
            self.wealth = self.wealth + earnings
            print("Earned " + str(earnings) + " wealth while traveling.\n")
            self.traveling = False
        else:
            print("Not currently traveling.\n")

    def __str__(self) -> str:
        "Prints string representation of the class' attributes."
        result = ("Name: " + self.name + " | Age: " + str(self.age) + " | Wealth: " + str(self.wealth) + "\n")
        result += ("Skills: " + str(self.skills) + "\n")
        result += ("List of Challenges: " + str(self.challenges) + "\n")
        if (self.traveling):
            result += "Currently Traveling?: Yes\n"
        else:
            result += "Currently Traveling?: No\n"
        return result