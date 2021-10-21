'''when this is executed it displays
    
    'Traceback (most recent call last):
  File "D:\PythonCodes\function_ops\recurrsion_error.py", line 4, in <module>
    recurr()
  File "D:\PythonCodes\function_ops\recurrsion_error.py", line 2, in recurr  
    recurr()
  File "D:\PythonCodes\function_ops\recurrsion_error.py", line 2, in recurr  
    recurr()
  File "D:\PythonCodes\function_ops\recurrsion_error.py", line 2, in recurr  
    recurr()
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded'

 hence PVM allow us to make only 1000 calls with respect to recurrsion beyond
 which we face stackover flow error.
'''

def recurr() :
    recurr()

recurr()