import random

class Fight:

    def __init__(self, challenger:'Fighter', challengee:'Fighter', skill:'str'):
        self.challenger = challenger
        self.challengee = challengee
        self.skill = skill

    def winner(self) -> 'Fighter':
        challenger = self.challenger
        challengee = self.challengee
        skill = self.skill
        if (challenger.get_skill(skill) > challengee.get_skill(skill)):
            winner = challenger
        elif (challenger.get_skill(skill) < challengee.get_skill(skill)):
            winner = challengee
        else:
            randWinner = random.choice([1,2])
            if randWinner == 1:
                winner = challenger
            else:
                winner = challengee
        return winner