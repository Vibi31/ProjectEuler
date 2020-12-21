number = 600851475143
def find_prime(number):
    for i in range (number-1,2,-1):
        if number%i == 0:
            print(i) 
            break
find_prime(number)
"""
not an effective code
"""



