from conversion import Conversion
import numpy as np

exp = input("Your expression here: ")
expression= list(exp)
obj = Conversion(len(expression)).toPostfix(expression)
print(obj)
operandos = []
for i in expression:
    if i.isalpha():
        operandos.append(i)
len = len(operandos)
row = 2**len
List = list(range(0, row))
n = []
for i in List:
    n.append(list(np.binary_repr(i, width=len)))

print(" Operandos: {} and Binary List: {} ".format(operandos, n))