import numpy as np

a = np.arange(10)
print(a)
print(type(a))  # numpy的多维数组类型
print(a[1])  # 也支持单个元素读取
a[0] = 9  # 也支持单个元素修改
print(a)

# 通过"遍历"对列表(ndarray)中每个元素进行开方
import math

b = [3, 6, 9]
c = []
for i in b:
    i = math.sqrt(i)
    c.append(i)
    print(i)
print(c)

# 直接对列表(ndarray)元素进行开方(对ndarray进行向量处理)
d=[3,6,9]
e = np.arange(10)
print(np.sqrt(d))
print(np.sqrt(e))
