#when different functions nad classes have same method is called method overiridng

#ex
class a:
    def m1(self):
        print('thisis method for class a')

class b(a):
    def m1(self):
        print("this is method for class b")
        super().m1()
o =b()
o.m1()









