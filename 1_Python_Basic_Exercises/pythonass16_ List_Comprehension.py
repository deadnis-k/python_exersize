num=[1,2,3,4,5]
x = 0
y=len(num)

while x<y:
    num[x]= num[x]**2
    x += 1

print(num)