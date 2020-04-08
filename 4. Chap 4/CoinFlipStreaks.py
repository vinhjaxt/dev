import random
h = 'H'
t = 'T'
count = 0
round = 0

while round < 10000:
    set = []
    for i in range(1, 101):
        flip = random.randint(0,1)
        if flip == 0:
            set.append(h)
        else:
            set.append(t)
            
    for s in range(len(set)-6):
        if set[s] == set[s+1] == set[s+2] == set[s+3] == set[s+4] == set[s+5] != set[s+6]:
            count += 1
    round += 1

a = str(count / round * 100)
print("Co " + a + " % Ti le 6 mat cung up hoac cung ngua dong thoi trong 100 lan lat dong xu dua tren 10K lan tung")