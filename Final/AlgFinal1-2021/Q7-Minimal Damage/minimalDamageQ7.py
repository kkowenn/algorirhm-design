'''
[20 Marks] Minimal damage

Ironman is fighting the Chitauri forces (the villain army in The Avengers 2012). N attacking
aircrafts of the Chitauri form a circle around Ironman. In each aircraft, there are a number of
Chitauri soldiers. Ironman’s repulsor can destroy three adjacent aircrafts per one shoot,
which immediately kills all the soldiers in those aircrafts. However, after the shoot, the
survival Chitauri soldiers also fire back at Ironman causing some damage to him — one unit
per soldier. Ironman will further follow with new shoot and so on until all aircrafts are
destroyed. It is required to define the minimum amount of damage, which can be dangerous
to Tony Stark.

INPUT: N integers, amount of soliders on each consecutive aircraft (not less than 1 and no
more than 100 on each). 3 ≤ N ≤ 20.

OUTPUT: The minimum amount of damage.

EXAMPLE

INPUT
3 4 2 2 1 4 1
OUTPUT
9

Elaboration:
1) Shoot the 2nd aircraft destroys 3+4+2, 
    damage = 2+1+4+1 = 8
2) Shoot the 5th aircraft destroys 2+1+4, 
    damage += 1 = 9


'''
airCraft = list(map(int, input().split()))

def damage(x):
    if len(x) <= 3:
        return 0
    else:
        tempsum = []
        tempdam = []
        for i in range(len(x)):
            re = 0
            dam = []

            if i == len(x) - 2: # 23
                dam = x[1:i]

            elif i == len(x) - 1: # 50
                dam = x[2:i]

            else:
                dam = x[:i] + x[i+3:]

            tempsum.append(sum(dam))
            tempdam.append(dam)

         # find minimum
        xmin = min(tempsum)
        indexmin = tempsum.index(xmin)
        xdam = tempdam[indexmin]

        return xmin + damage(xdam)


print(damage(airCraft))

