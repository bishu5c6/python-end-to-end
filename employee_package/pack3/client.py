import sys
# sys.path.append("E:\python-end-to-end\employee_package\pack3\client.py")
sys.path.append("E:\python-end-to-end\employee_package\pack2")
sys.path.append("E:\python-end-to-end\employee_package\pack1")

import emp
obj=emp.employee(101,"njj",6789)
obj.display()

import stu
obj1=stu.stud(102,10233,"hjh")
obj1.display()

#approach 2
from emp import employee
obj=employee(102,"bishu,",987654)
obj.display()