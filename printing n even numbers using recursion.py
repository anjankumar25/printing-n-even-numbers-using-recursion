def aa(a):
    if  a == 0:
        return
    if a % 2 ==0:
        print(a)
    aa(a-1)
aa(25)