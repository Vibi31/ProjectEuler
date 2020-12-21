sum = 2 #starting with t2 added
t1 = 1
t2 = 2

while t2 < 4000000:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    if t3%2 == 0:
        sum += t3

print(sum)

