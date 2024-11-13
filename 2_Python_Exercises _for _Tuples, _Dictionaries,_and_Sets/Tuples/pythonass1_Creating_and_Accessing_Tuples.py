my_tuple = (1,2,3,)
print(my_tuple)
print(my_tuple[1])
x=list(my_tuple)
x[0]= 10
my_tuple=tuple(x)
print(my_tuple)