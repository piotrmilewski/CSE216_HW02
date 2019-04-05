import random

class Fight:

    def __init__(self, challenger:'Fighter', challengee:'Fighter', skill:'str'):
        "Initializes instances of the Fight class with challenger, challengee, and skill attributes."
        self.challenger = challenger
        self.challengee = challengee
        self.skill = skill

    def winner(self) -> 'Fighter':
        "Determines the winner of a fight between two Fighters."
        challenger = self.challenger
        challengee = self.challengee
        skill = self.skill
        if (challenger.get_skill(skill) > challengee.get_skill(skill)):
            print(challenger.name + " won the battle!\n")
            winner = challenger
        elif (challenger.get_skill(skill) < challengee.get_skill(skill)):
            print(challengee.name + " won the battle!\n")
            winner = challengee
        else:
            randWinner = random.choice([1,2])
            if randWinner == 1:
                print(challenger.name + " won the battle!\n")
                winner = challenger
            else:
                print(challengee.name + " won the battle!\n")
                winner = challengee
        return winner