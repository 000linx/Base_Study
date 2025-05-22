import pandas as pd
import np as np
import random 
'''
创建DataFrame对象
pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
参数说明：
data:数据,可以是列表、字典、数组、Series等
index:行索引,可以是列表、字典、数组等
columns:列索引,可以是列表、字典、数组等
dtype:数据类型
copy:是否复制数据,默认为False
'''

# 创建DataFrame对象
df_01 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 打印DataFrame对象
print(df_01)

data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
# 创建DataFrame
df_02 = pd.DataFrame(data, columns=['Site', 'Age'])

# 使用astype方法设置每列的数据类型
df_02['Site'] = df_02['Site'].astype(str)
df_02['Age'] = df_02['Age'].astype(float)
print(df_02)


# # 创建一个包含网站和年龄的二维ndarray
# ndarray_data = np.array([
#     ['Google', 10],
#     ['Runoob', 12],
#     ['Wiki', 13]
# ])

# # 使用DataFrame构造函数创建数据帧
# df_03 = pd.DataFrame(ndarray_data, columns=['Site', 'Age'])
# # 打印数据帧
# print(df_03)


df = pd.DataFrame(data = random.randint(60, 100), columns=['a', 'b', 'c', 'd', 'e'],)
print(df[3:5]['c','e'])
