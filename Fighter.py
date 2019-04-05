import Person
import Fight
import random

class Fighter(Person.Person):

    def __init__(self, skills:dict, name:str="", age:int=0, wealth:int=0):
        super().__init__(name, age, wealth)
        self.type = "Fighter"
        if not(self.adult):
            print("This Fighter is not an adult, using growth serum to make this Fighter an adult.")
            self.adult = True
        self.__skills = skills 
        #check if proper skills are set with proper value
        for skill in self.__skills:
            if self.__skills[skill] < 0:
                print("Skill cannot have a level lower than 0, setting skill level to 0")
                self.__skills[skill] = 0
            elif self.__skills[skill] > 10:
                print("Skill cannot have a level higher than 10, setting skill level to 10")
                self.__skills[skill] = 10
            else:
                pass
        if not("spear" in self.__skills):
            print("Spear skill wasn't initialized by user. Initializing spear skill with value of 0")
            self.__skills["spear"] = 0
        if not("unarmed_combat" in self.__skills):
            print("Unarmed_combat skill wasn't initialized by user. Initializing unarmed_combat skill with value of 0")
            self.__skills["unarmed_combat"] = 0
        if not("mace" in self.__skills):
            print("Mace skill wasn't initialized by user. Initializing mace skill with value of 0")
            self.__skills["mace"] = 0
        if not("broadsword" in self.__skills):
            print("Broadsword skill wasn't initialized by user. Initializing broadsword skill with value of 0")
            self.__skills["broadsword"] = 0

    @property
    def skills(self) -> dict:
        return self.__skills

    @skills.setter
    def skills(self, skill:str, newValue:int) -> None:
        if skill in self.__skills:
            self.__skills[skill] = newValue
        else:
            print("{} is not a skill".format(skill))

    def get_skill(self, skill:str) -> int:
        return self.__skills[skill]

    def challenge(self, challengee:'Fighter', skill:str) -> None:
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

    def sendChallenge(self, challenger:'Fighter', skill:str) -> None:
        fight = Fight.Fight(challenger, self, skill)
        winner = fight.winner()
        if winner == self:
            if (challenger.type == "Fighter"):
                challenger.lostChallenge(skill, 10, True)
                self.wonChallenge(skill, 10, 0)
            elif (challenger.type == "Warrior"):
                challenger.lostChallenge(skill, 25, False)
                self.wonChallenge(skill, 25, 1)
            else:
                challenger.lostChallenge(skill, 40, False)
                self.wonChallenge(skill, 40, 2)
        else:
            self.lostChallenge(skill, 10, True)
            challenger.wonChallenge(skill, 10, 0)

    def wonChallenge(self, skill:str, money:int, lvlup:int) -> None:
        self.wealth = self.wealth + money
        if (self.__skills[skill] < 10):
            if (lvlup == 2):
                self.__skills[skill] = self.__skills[skill] + 2
            elif (lvlup == 1):
                self.__skills[skill] = self.__skills[skill] + 1
            else:
                if (random.choice([1,2]) == 1): #50% chance to rank up skill
                    self.__skills[skill] = self.__skills[skill] + 1
        else:
            print("Skill can't level up, already at max level.")
    
    def lostChallenge(self, skill:str, money:int, lvlup:bool) -> None:
        if ((self.wealth - money) < 0):
            self.wealth = 0
        else:
            self.wealth = self.wealth - money
        if (self.__skills[skill] < 10):
            if (lvlup):
                if (random.choice([1,2]) == 1): #50% chance to rank up skill
                    self.__skills[skill] = self.__skills[skill] + 1

    def __str__(self):
        result = ("Name: " + self.name + " | Age: " + str(self.age) + " | Wealth: " + str(self.wealth) + "\n")
        result += ("Skills: " + str(self.skills) + "\n")
        return result
