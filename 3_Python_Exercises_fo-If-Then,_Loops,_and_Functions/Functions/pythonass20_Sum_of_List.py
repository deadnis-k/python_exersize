def sum_list(lst):
    sum =0
    for i in range(0,len(lst)):
        sum += lst[i]
    return sum

lst = [10, 20, 30, 40]
x= sum_list(lst)
print(x)
