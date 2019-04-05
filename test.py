import Fighter
import Warrior

fighterA = Fighter.Fighter({'spear':7, 'unarmed_combat':7, 'mace':7, 'broadsword':7}, "John", 19, 20)
fighterB = Fighter.Fighter({'spear':9, 'unarmed_combat':2, 'mace':8, 'broadsword':6}, "Ben", 25, 37)
warriorA = Warrior.Warrior({'spear':8, 'unarmed_combat':9, 'mace':9, 'broadsword':9}, "Will", 55, 55)

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

#Case 6: Warrior accepts random challenge
print(fighterA)
print(fighterB)
print(warriorA)
warriorA.accept_random()
print(fighterA)
print(fighterB)
print(warriorA)