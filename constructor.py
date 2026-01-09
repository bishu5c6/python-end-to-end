class cons:
    def __init__(self):
        print("this is constructor")

    def name(self):
        print('This is normal method')

    def m2(self, x,y):
        return (x+y)

a = cons()
a.name()
print(a.m2(10,20))