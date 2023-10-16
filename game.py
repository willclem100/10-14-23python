import random

weapons = ['copper shortsword', 'iron broadsword', 'tungston bow']
weapon = random.choice(weapons)

if weapon == 'copper shortsword':
    weapon_p = random.randint(3,5)
    
elif weapon == 'iron broadsword':
    weapon_p = random.randint(8,12)
    
else:
    weapon_p = random.randint(12,15)
    
crit = 3
damage = weapon_p + crit
print(f"Your {weapon} did {damage} damage.")

