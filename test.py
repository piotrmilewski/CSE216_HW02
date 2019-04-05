import Fighter
import Warrior
import KnightErrant

fighterA = Fighter.Fighter({'spear':7, 'unarmed_combat':7, 'mace':7, 'broadsword':7}, "John", 19, 50)
fighterB = Fighter.Fighter({'spear':9, 'unarmed_combat':2, 'mace':8, 'broadsword':6}, "Ben", 25, 37)
warriorA = Warrior.Warrior({'spear':8, 'unarmed_combat':2, 'mace':9, 'broadsword':9}, "Will", 55, 55)
warriorB = Warrior.Warrior({'spear':4, 'unarmed_combat':3, 'mace':2, 'broadsword':1}, "Mario", 17, 121)
keA = KnightErrant.KnightErrant({'spear':2, 'unarmed_combat':4, 'mace':9, 'broadsword':1}, "Dio", 34, 250)
keB = KnightErrant.KnightErrant({'spear':8, 'unarmed_combat':6, 'mace':1, 'broadsword':9}, "Peter", 34, 200)

#Case 1: Fighter vs another Fighter
print(fighterA)
print(fighterB)
fighterA.challenge(fighterB, 'spear')
print(fighterA)
print(fighterB)

print("------------------------------------------------------------------------")

#Case 2: Fighter vs Self
print(fighterA)
fighterA.challenge(fighterA, 'spear')
print(fighterA)

print("------------------------------------------------------------------------")

#Case 3: Fighter challenges Warrior
print(fighterB)
print(warriorA)
fighterB.challenge(warriorA, 'mace')
print(fighterB)
print(warriorA)

print("------------------------------------------------------------------------")

#Case 4: Fighter2 challenges Warrior
print(fighterA)
print(warriorA)
fighterA.challenge(warriorA, 'broadsword')
print(fighterA)
print(warriorA)

print("------------------------------------------------------------------------")

#Case 5: Fighter2 tries challenging Warrior again (doesn't challenge cause no repeats)
print(fighterA)
print(warriorA)
fighterA.challenge(warriorA, 'broadsword')
print(fighterA)
print(warriorA)

print("------------------------------------------------------------------------")

#Case 6: Warrior declines random challenge
print(fighterA)
print(fighterB)
print(warriorA)
warriorA.decline_random()
print(fighterA)
print(fighterB)
print(warriorA)

print("------------------------------------------------------------------------")

#Case 7: Warrior accepts random challenge
print(fighterA)
print(fighterB)
print(warriorA)
warriorA.accept_random()
print(fighterA)
print(fighterB)
print(warriorA)

print("------------------------------------------------------------------------")

#Case 8: Warrior accepts random challenge (but there are no challenges)
print(warriorA)
warriorA.accept_random()
print(warriorA)

print("------------------------------------------------------------------------")

#Case 9: Test skill level up guarantee
print(fighterA)
print(warriorA)
fighterA.challenge(warriorA, "unarmed_combat")
warriorA.accept_random()
print(fighterA)
print(warriorA)

print("------------------------------------------------------------------------")

#Case 10: Test withdrawing a challenge
print(warriorA)
fighterA.challenge(warriorA, "spear")
print(warriorA)
fighterA.withdraw(warriorA)
print(warriorA)

print("------------------------------------------------------------------------")

#Case 11: KnightErrant challenges KnightErrant
print(keA)
print(keB)
keA.challenge(keB, "unarmed_combat")
print(keA)
print(keB)

print("------------------------------------------------------------------------")

#Case 12: KnightErrant accepts random challenge
fighterB.challenge(keB, "spear")
warriorB.challenge(keB, "mace")
warriorA.challenge(keB, "unarmed_combat")
print(keB)
keB.accept_random()
print(keB)

print("------------------------------------------------------------------------")

#Case 13: KnightErrant declines random challenge
print(keB)
keB.decline_random()
print(keB)

print("------------------------------------------------------------------------")

#Case 14: Withdraw challenges from KnightErrant
print(keB)
fighterB.withdraw(keB)
keA.withdraw(keB)
warriorB.withdraw(keB)
warriorA.withdraw(keB)
fighterB.withdraw(keB)
print(keB)

print("------------------------------------------------------------------------")

#Case 15: KnightErrant starts traveling
print(keA)
keA.travel()
fighterB.challenge(keA, "spear")
warriorB.challenge(keA, "mace")
warriorA.challenge(keA, "unarmed_combat")
keA.accept_random()
keA.decline_random()
print(keA)

print("------------------------------------------------------------------------")

#Case 16: KnightErrant stops traveling
print(keA)
keA.return_from_travel()
print(keA)