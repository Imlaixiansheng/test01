# array如何将列表转换成数组(一维二维三维)
# 转换成数组之后的数据类型为:np.ndarray
# np.array(d, dtype=float, ndmin=5)两形参的用法
# a.shape查看数组维度

import numpy as np

# array创建一维数组(将列表转换为数组)
a = [1, 2, 3, 4]
a = np.array(a)
print(a, " ,type:", type(a))

# array创建二维数组
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = np.array(b)
print(b, " ,type:", type(b), b.shape)

# array创建三维数组
c = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
c = np.array(c)
print(c, " ,type:", type(c), c.shape)

# array(p_object, dtype=None, ndmin=0)
# p_object:列表对象, dtype:列表中的变量类型, ndmin:数组维数
d = [1, 2, 3]
d = np.array(d, dtype=float, ndmin=5)
print(d, d.shape)
