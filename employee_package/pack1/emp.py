class employee:
    def __init__(self,empid,ename,esalary):
        self.empid = empid
        self.ename=ename
        self.esalary=esalary
    def display(self):
        print(self.empid,self.esalary,self.ename)

