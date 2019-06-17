#program to check if a given number is armstrong number or not
for x in range(1000):
   p=x
   y=z=0
   while (p>0):
       y=p%10
       z+=y**3
       p//=10

   if(z==x):
       print(x,"Armstrong number")




