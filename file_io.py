f = open('A.txt', 'w')
f.write('Welcome to A.txt')
f.write('\nHello')
f.close()


f=open('A.txt','r')
print(f.read())

