# list列表中由逗号隔开
# np.ndarray类型数组,中间没有逗号
# np.arange(起始, 终止, 步长, dtype=float)可以设置数据类型


import numpy as np

# 对比range创建列表range(start,stop,step),左闭右开,step默认为1,逗号隔开
a = list(range(1, 10, 2))
print(a, " ,type:", type(a))
# arange创建数组
b = np.arange(1, 10, 2, dtype=float)
print(b, " ,type:", type(b))
