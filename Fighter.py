import Person
import Fight

class Fighter(Person.Person):

    def __init__(self, name:str="", age:int=0, wealth:int=0, **skills:dict):
        super().__init__(self, name, age, wealth)
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
    def skill(self, skill:str) -> int:
        return self.__skills[skill]

    @skill.setter
    def skill(self, skill:str, newValue:int) -> None:
        if skill in self.__skills:
            self.__skills[skill] = newValue
        else:
            print("{} is not a skill".format(skill))

    def challenge(self, challengee:'Fighter', skill:str) -> None:
        if self.id() != challengee.id(): #check so challenger can't fight himself
            print("Excuse me, you can't fight yourself.")
            return None
        if self.wealth <= 0 or challengee.wealth <= 0: #check if both fighters aren't broke
            if self.wealth <= 0:
                print("{} has no money to challenge someone.".format(self.name))
            else:
                print("{} has no money to challenge someone.".format(challengee.name))
            return None
        if not(isinstance(challengee, Fighter)): #check if challenger is of type fighter
            print("Can't challenge this person, they're not a fighter")
            return None
        if not("spear" == skill or "unarmed_combat" == skill or "mace" == skill or "broadsword" == skill): #check if valid skill
            print("Invalid skill to fight with, please select a valid skill and make sure it is lowercase")
            return None
        #if valid challenge
        challengee.acceptChallenge(self, skill)
        return None

    def acceptChallenge(self, challenger:'Fighter', skill:str) -> None:
        Fight.challenger = challenger
        Fight.challengee = self
