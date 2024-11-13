def is_prime(number):
    for i in range(2,number//2 +1):
        if number%i ==0:
            return False
    return True

num = 13
x=is_prime(num)
if x== True:
    print("the numbe is prime")
else:
    print("the number is not prime")

