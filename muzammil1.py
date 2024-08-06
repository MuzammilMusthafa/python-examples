'''*****
   *****
   *****
   *****
   *****
   '''
for value in range (0,5):
    print('*****') 

''' 12345
    12345
    12345
    12345
    12345'''
for value in range (0,5):
    print('12345') 

input6=int(input('enter a value'))
for value in range(input6):
    print('12345')
    
'''
   *****
   ****
   ***
   **
   *   '''   

list(range(5,0,-2))
4*'*'
1*'*'
for value in range(5,0,-1):
    print(value*'*')

'''
   54321
   54321
   54321
   54321
   54321 '''
for value in range(0,5):
    print('54321')

input6=int(input('enter a value'))    
for value in range(input6):
    print('54321')

''' 
   *
   **
   ***
   ****
   ***** '''
list(range(5,0,-1))    
5*'*'
for value in range(0,7):
    print(value*'*')

'''
   1
   12
   123
   1234
   12345'''

for value in range(0,7):
    print(value*'*',end =' ')


    for row in range(1,7):
    for col in range(1,row):
        print(col,end='') 
    print()        

for row in range(7,1,-1):
    for col in range(1,row):
        print(col,end='')
    print()    

'''
   *
   **
   ***
   ****
   *****
   ****** '''
for row in range(1,8):
    for col in range(1,row):
        print('*',end='')
    print()    

'''                 
    *
   ***
  *****
 *******
*********'''
for row in range(1,6):
    for col in range(6,row,-1):
        print(' ',end=' ')
      
    for col in range(0,row*2-1):
        print('*',end=' ')
    print()

for row in range(6,0,-1):
    for col in range (6,row,-1):
        print(' ',end='')

    for col in range(0,row*2-1):
        print('*',end='')
    print()  
    