s=input("enter a string:")
sl=len(s)
i=sl-1
n=0
p=0
while n<sl:
    if s[n]!=s[i-n]:
       print('given string is not a palindrome')
       break
    else: 
       p += 1
    n += 1
    
if p==(sl) :
   print('given string is palindrome')