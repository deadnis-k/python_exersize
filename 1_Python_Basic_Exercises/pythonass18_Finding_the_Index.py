colors = ['red', 'blue', 'green', 'yellow', 'blue']
test1 = "blue"
exit1 = 0
test = len(colors)
exit2 = 0
while exit1 == 0 and exit2 < test:
    if test1 == colors[exit2]:
        exit1 = exit2
    exit2 += 1
        

print(exit1)