import random

def newPassword ():
        # List out the characters we will use, into groups.
        lowers = "abcdefghijklmnopqrstuvwxyz"
        uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "1234567890"
        symbols = "!@#$%^&*()"

        # Select 3 random characters from each group
        a = random.choices(lowers, k=3)
        lowers2 = a[0]+a[1]+a[2]
        b = random.choices(uppers, k=3)
        uppers2 = b[0]+b[1]+b[2]
        c = random.choices(numbers, k=3)
        numbers2 = c[0]+c[1]+c[2]
        d = random.choices(symbols, k=3)
        symbols2 = d[0]+d[1]+d[2]

        # Combine the groups into a string 3 lower, 3 upper, 3 number, 3 symbols)
        combined = lowers2 + uppers2 + numbers2 + symbols2

        # Shuffle the characters in the length of 12 characters.
        shuffled = random.sample(combined, k=12)

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







