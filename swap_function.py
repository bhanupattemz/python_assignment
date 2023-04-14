def swap(a,b):
    c=a
    a=b
    b=c
    return a,b
a=int(input('enter value of a:'))
b=int(input('enter value of b:'))
print('before swap: a=',a,'b=',b)
a,b=swap(a,b)
print('after swap: a=',a,'b=',b)
    