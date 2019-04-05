class Person:

    def __init__(self, name:str="", age:int=0, wealth:int=0):
        "Sets attributes for name, age, wealth, and whether or not the person is an adult."
        self.name = name
        if (age < 0):
            print("Age cannot be lower than 0, setting age to 0")
            self.age = 0
        else:
            self.age = age
        self.wealth = wealth
        if (self.age >= 18):
            self.adult = True
        else:
            self.adult = False

    def equals(self, person:'Person') -> bool:
        "Checks whether or not two person instances are equal."
        return (self.name == person.name) and (self.age == person.age)