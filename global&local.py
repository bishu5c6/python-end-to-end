globalaa =10
def func(b):
    print(globalaa*b)

func(20)

print()
print(globalaa)

xy=100
def cal():
    global xy
    xy=1000 #now it become global variable
    print(xy)
cal()
#here xy becomes the new global variable


xy=100
def cal():
   # global xy=1000 invalid syntax
    xy=1000 #now it become global variable
    print(xy)
cal()
