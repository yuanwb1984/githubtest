import time
import math
import numpy as np

x = [i * 0.001 for i in range(1000000)] # 初始化数组0.000~999.999 
start = time.clock()
for i, t in enumerate(x):                # 用循环计算正弦值
    x[i] = math.sin(t)                
print("math.sin:", time.clock() - start)

x = [i * 0.001 for i in range(1000000)]
x = np.array(x)                          # 初始化矩阵（这里是一维）
start = time.clock()
np.sin(x,x)                              # numpy的广播计算（代替循环）
print("numpy.sin:", time.clock() - start)

