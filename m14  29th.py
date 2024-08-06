list1=[1,2,3,4,5,6,7,8,9,10,10]
list2=[]
for value in list1:
    if list1.count(value)==1:
        list2.append(value)
print(list2)        


list3=[1,2,1,2,1,3,4,5,4,6,8,7,9,10,11]
list4=[]
for value in list3:
    if list3.count(value) in [1,2]:
        list4.append(value)
print(set[list4])        