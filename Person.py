class Person:

    #sets attributes for name, age, wealth, and whether or not the person is an adult
    def __init__(self, name:str="", age:int=0, wealth:int=0):
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

    #checks whether or not two person instances are equal
    def equals(self, person:'Person') -> bool:
        return (self.name == person.name) and (self.age == person.age)