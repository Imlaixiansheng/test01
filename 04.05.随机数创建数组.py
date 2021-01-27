import numpy as np

# 生成size个[0,1)范围内的随机数(以数组形式返回)
x = np.random.random(size=3)
print(x, type(x))
# 生成一个随机数多维数组
y = np.random.random(size=(3, 4))
print(y, type(y))

# np.random.randint(low,high,size=(3,4))
# 生成一个(3,4)的随机整数矩阵,随机数范围[low,high)
z = np.random.randint(1, 11, size=(2, 3))
print(z, type(z))
# 第六页
