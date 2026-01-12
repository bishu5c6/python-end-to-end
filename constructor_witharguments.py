# class myclaa:
#     name = "john"
#     def __init__(self, name):
#         print(name)
#         print(self.name)
#
# mc=myclaa("biswanth")

#example 9
#re emp name id, salary inside constructor
#display() - print eid, ename,esalrt

# class employee:
#     def __init__(self, ename, eid, esalary):
#         self.ename = ename
#         self.eid = eid
#         self.esalary = esalary
#
#     def display(self):
#         print(self.ename)
#         print(self.eid)
#         print(self.esalary)
#
#
# obj = employee("bishy",101,'2000')
# obj.display()
# obj1 = employee("nj",102,'3789')
# obj1.display()







class employee:
    def __init__(self, ename, eid, esalary):
        self.ename = ename
        self.eid = eid
        self.esalary = esalary

    def __str__(self):
        return self.ename


obj = employee("bishy",101,'2000')
print(obj)

#only used for string data types















#


