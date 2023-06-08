students = ['Renat','Troy','Dane','Edward','MJ','Nick','Ousama','Paul']

from random import randint

group1 = randint(1,3)

groups={}

for i in students:
    groups[i] = randint(1,3)
print(groups)

