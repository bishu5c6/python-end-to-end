import c1
import c2

obj1=c1.animal()
obj1.display()

obj2=c2.bird()
obj2.display()


#2 approach
from c1 import animal
from c2 import bird
obj1 = animal()
obj1.display()
obj2=bird()
obj2.display()