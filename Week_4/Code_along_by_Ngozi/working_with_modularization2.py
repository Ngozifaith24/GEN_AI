#different ways to import Modules
#1. Import the whole module
import math

#putting it into use
print(math.sqrt(9))
#- Note you must specify the module name when calling a function name 


# 2. import as an alias
import math as a
# lets put
print(a.sqrt(25))

#This shorthens the module name, this is common with libaries likenumpy, pandas, etc

#3. Import specific functions or variables
from math import sqrt, pi
print(sqrt(36))
print(round(pi, 2))


# - here you dont need the prefix 'math.' anymore

#4. Import everything from the module
from math import *

print(sqrt(49))
print(pi)
print(log)

# - This is usually not recommended because it can cause name conflits if two modules have functions with the same name
