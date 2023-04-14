n=int(input('enter no.of digit want to print:'))
a,b,i=0,1,0
if n==0:
    print('enter a valid number')
elif n==1:
    print(a)
else:   
    for i in range(0,n) :
        print(a)
        sum=a+b
        a=b
        b=sum