list = [9,2,3,5,7,1,6,4,8,10]
temp_list = [0]
x=list[0]
for i in range(len(list)):
    if x>list[i]:
        x=list[i]
    "print(list[i],x)"

y=0
block=0
while len(list)>1:
    while y<len(list) and len(list)!=1 and y!=len(list):
        if x==list[y]:
            temp_list.append(list[y])
            if block==0:
                temp_list.pop(0)
                block=1
            list.pop(y)
            y=-1
        y=y+1
        """
        print(x,"x")
        print(y,"y")
        print(list,"list")
        print(temp_list,"templist")
        """
    y=0
    x=x+1
temp_list.append(list[0])
print(temp_list,"final temp")
