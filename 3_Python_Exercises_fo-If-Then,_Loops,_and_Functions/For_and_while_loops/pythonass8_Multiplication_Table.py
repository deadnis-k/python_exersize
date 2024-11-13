fnum= int(input("what is your first number? "))
snum= int(input("what is your second number? "))
x =0
for i in range( 0, fnum+1):
    for j in range(0 , snum+1):
        if j==0:
            print(i, end=" ")
        elif i==0:
            print(j, end=" ")
        else:
            print(i*j, end=" ")
    print(" ")
5

