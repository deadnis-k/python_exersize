def remove_all (list,value):
    while value in list:
        list.remove(value)
    return list





numbers = [1, 2, 2, 3, 4, 2]
print(numbers)
rnum = 2
remove_all(numbers,rnum)
print(numbers)
