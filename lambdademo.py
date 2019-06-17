#lambda demo
l1=[1,2,3,4,5,6,7,8,]
l=[x for x in filter(lambda a:a%2==0,l1)]
print(l)