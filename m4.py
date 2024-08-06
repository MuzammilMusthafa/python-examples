list1=[1,2,3,4,5,6,7,8,9,10]
sum=0
for value in list1: 
    sum=sum+value
print(sum)
def muzammil(z):
    sum=0
    for value in list1: 
        sum=sum+value
    return sum 

muzammil(list1)



#
list1=[1,2,3,4,5,6,7,8,9,10]
list2=[]
list3=[]
for value in list1:
    if value%2==0:
        list2.append(value) 
    else:
        list3.append(value)


def muzammil(h):
    list2=[]
    list3=[]
    for value in list1:
        if value%2==0:
            list2.append(value)
        else:
            list3.append(value)
    return list2,list3 
muzammil(list1)


input1=input('enter a value')

for value in input1:
    if value.isupper():
        pass
          
        
        print(value)
    else:
        print(value)
print(input1)        

def muzammil(a):
    upper=0
    lower=0
    for value in input1:
        if value.isupper():
            upper=upper+1
        else:
            lower=lower+1
    return upper,lower       
muzammil(input1)


input2=input("enter data")
for value in input2:
    if value.isupper():
        print(value)
    elif value.islower():
        print(value) 
    else:
        print(value)      
def muzammil(h):    
    upper=0
    lower=0
    num=0        
    for value in input2:
        if value.isupper():
            upper=upper+1
        elif value.islower():
            lower=lower+1
        else:
            num=num+1
        return upper,lower,num   
muzammil(input2)


list1=[1,2,3,4,5,6]
def muhammed(n):
    return n*n   
list(map(muhammed,list1))

list2=[1,2,3,4,5]
sum=0
for value in list2:
    sum=sum+value
    print(sum)
def muzammil(a):
      for value in list2:
        sum=sum+value
      return sum

def muzammil(a,b):
    return a+b
import functools
print(functools.reduce(muzammil,list2))     
print(functools.reduce(lambda a,b:a+b,list2))