import random

def newPassword ():
        # List out the characters we will use, into groups.
        lowers = "abcdefghijklmnopqrstuvwxyz"
        uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "1234567890"
        symbols = "!@#$%^&*()"

        # Select 4 random characters from each group
        a = random.choices(lowers, k=4)
        lowers2 = a[0]+a[1]+a[2]+a[3]
        b = random.choices(uppers, k=4)
        uppers2 = b[0]+b[1]+b[2]+b[3]
        c = random.choices(numbers, k=4)
        numbers2 = c[0]+c[1]+c[2]+c[3]
        d = random.choices(symbols, k=4)
        symbols2 = d[0]+d[1]+d[2]+d[3]

        # Combine the groups into a string (4 lower, 4 upper, 4 number, 4 symbols)
        combined = lowers2 + uppers2 + numbers2 + symbols2

        # Shuffle the characters in the length of 16 characters.
        shuffled = random.sample(combined, k=16)

        # Join the list of responses into 1 string.
        shuffleCombine = ''.join(shuffled)

        # return the shuffleCombine to the function()
        return shuffleCombine

a = newPassword()
# Print the string
print(a)

print("""
      
      Menu
    1. Refresh
    2. Exit      
      """)



answer = input("Please make a selection:  ")

while answer == ("1"):
     print(newPassword())
     print("""
      
      Menu
    1. Refresh
    2. Exit      
      """)
     answer = input("Please make a selection:  ")
else:
    exit()







