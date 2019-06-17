
def myfunc():
    i = 1;
    while 1:
        yield i;
        i += 1


for x in myfunc():
    if x > 100:
        break
    else:
        print(x)
