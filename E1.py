sum = 0
for i in range (1,1000):
    if i%3 == 0:
        sum += i
    elif i%5 == 0:
        sum += i
print(sum)
"""
233168
"""
#python -m pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org --upgrade pip