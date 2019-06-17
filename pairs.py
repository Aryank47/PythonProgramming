#program to find the no. of pairs in an array
a=[10,20,10,20,20,30,10,20,15,12]
count=i=0
x=len(a)
print(x)
for i in range(0,x):
    if a[i]!=-1:
        for j in range(i+1,x):
            if a[i]==a[j]:
                count +=1
                a[i]=a[j]=-1
        
print(count)    
print(a)
