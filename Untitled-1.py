for row in range(1,6):
    for col in range (6,row,-1):
        print(' ',end='')

    for col in range(0,row*2-1):
        print('*',end='')
    print()    