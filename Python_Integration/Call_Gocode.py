import os
import ctypes

# Reference Article
# https://savorywatt.com/2015/09/18/calling-go-code-from-python-code/
# https://medium.com/analytics-vidhya/running-go-code-from-python-a65b3ae34a2d

lib = ctypes.cdll.LoadLibrary('libaddnum.so')
print("Loaded go code generated - so library")
result = lib.add(10, 20)
print("type(result) --> ", type(result))
print("result --> ", result)

################################
##### Executing PythonCode #####
################################
# (base) rocks-Air:Python_Integration rock$ /usr/bin/python3 /Users/rock/Git_Repo/Go_Codes/Python_Integration/Call_Gocode.py 
# Loaded go code generated - so library
# 2022/03/30 11:04:02 Given var1 -->  10
# 2022/03/30 11:04:02 Given var2 -->  20
# type(result) -->  <class 'int'>
# result -->  30
# (base) rocks-Air:Python_Integration rock$ 