word="Python"
print(word[:3])
print(word[-3:])

y=word[0]
z=1
x=len(word)

while z<x:
    print(y)
    z=z+1
    y=word[z-1] 

print(y)