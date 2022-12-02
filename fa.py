import random
faf = open('fa.txt','w')
fa = []
for i in range(31):
    fa.append(random.randint(50,100))

minF = 0
maxF = 0
for szam in fa:
    if maxF < szam:
        szam = maxF
    if minF > szam:
        szam = minF

print(f'Legtöbb kitermelt fa ebben a hónapban {maxF}')
print(f'Legkevesebb kitermelt fa ebben a hónapban {minF}')
faf.write(f'Legtöbb kitermelt fa ebben a hónapban {maxF}\n')
faf.write(f'Legkevesebb kitermelt fa ebben a hónapban {minF}\n')

nap = 0
if fa > 82:
 nap = nap + 1
print(f'Ennyiszer volt nagyobb 82m3-nál : {nap}')
faf.write(f'Ennyiszer volt nagyobb 82 m3-nál: {nap}\n')

print(f'Ennyi volt a fakitermelés 20.-án: {fa[20]}')
faf.write(f'Ennyi volt a fakitermelés 20. -án : {fa[20]}\n')


for szamok in fa:
    ossz = ossz + szamok
atlag = ossz / szamok
print(f'A hőmérséklet átlaga: {atlag:0.2f}')
faf.write(f'A kitermelt fa átlaga: {atlag:0.2f}\n')

faf.close()


