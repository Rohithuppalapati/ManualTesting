# importing python debugger
import pdb

def divide(a,b):
    pdb.set_trace()
    dummy=6*7
    return a//b

print(divide(24,4))


