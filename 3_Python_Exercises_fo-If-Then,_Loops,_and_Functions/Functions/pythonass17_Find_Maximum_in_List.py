def find_max(lst):
    x=lst[0]
    for i in range(0 ,len(lst)):
        if lst[i] > x :
            x=lst[i]
    return x


flst = [1, 5, 3, 9, 2]
x = find_max(flst)
print(x)
