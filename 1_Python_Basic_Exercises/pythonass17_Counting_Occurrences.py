fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = 0
counted = "apple"
x = len(fruits)
for i in range(x):
    if fruits[i] == counted:
        counter += 1
print(f"the {counted} has appeard {counter} times")

