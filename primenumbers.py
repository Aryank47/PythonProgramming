#program to print prime numbers till 100
for x in range(2,101):
   for y in range(2,int(x/2)+1):
       if (x%y)==0:
           break
   else:
       print(x)
