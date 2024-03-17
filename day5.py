import random

char = ['q','w','e','r','t','y','u','i','o','p','l','k','j','h','g','f','d','s','a','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','L','K','J','H','G','F','D','S','A','Z','X','C','V','B','N','M']
nums = ['1','2','3','4','5','6','7','8','9','0']
special_chars = ['!', '@', '#', '$', '%', '^', '&', '&', '*', '_', '+', '-', '=', ':', ';', '<', '>', '.', '?', '/', '|']

n = int(input("How many letters do you want? "))
m = int(input("How many digits do you want? "))
s = int(input("How many special characters do you want? "))

password = []

for i in range(n):
    password.append(random.choice(char))

for j in range(m):
    password.append(random.choice(nums))

for k in range(s):
    password.append(random.choice(special_chars))

random.shuffle(password)
password = ''.join(password)
print(password)
