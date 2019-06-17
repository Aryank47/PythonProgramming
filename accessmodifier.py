# access modifier demo
class test:
    x=10
    __y=100;#private variable declaration
    def disp(self):
        print("hrllo")
        
t=test()
print(t.x)
#print(t.y)# illegal access