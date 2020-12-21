

def palindrom():
    M = 999**2 #larges possible value
    for i in range(M, 1, -1):
        i = str(i)
        normal = [int(d) for d in i]
        reverse = normal[::-1]
        if reverse == normal:
            return normal
            break

print(palindrom())
#wrong