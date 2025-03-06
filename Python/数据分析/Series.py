import pandas as pd

'''
创建Series对象
pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
参数说明：
data:数据,可以是列表、字典、数组等
index:索引,可以是列表、字典、数组等
dtype:数据类型
name:Series对象的名称
copy:是否复制数据,默认为False
fastpath:是否使用快速路径,默认为False
'''

# 创建Series对象
series_01 = pd.Series([1, 2, 3, 4, 5])
# 打印Series对象
print(series_01)

# 自定义Series对象的索引
series_02 = pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"])
print(series_02)

# 自定义Series对象的名称
series_03 = pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"], name="example")
print(series_03)

# 创建两个Series对象
series_apple = pd.Series([3, 2, 0, 1])
series_orange = pd.Series([0, 3, 7, 2])
# 将两个Series对象合并为一个DataFrame对象,并且通过index参数指定行索引
df_01 = pd.DataFrame([series_apple, series_orange], index=["apple", "orange"])
print(df_01)
# 将两个Series对象合并为一个DataFrame对象,并且通过columns参数指定列索引
df_02 = pd.DataFrame({"apple": series_apple, "orange": series_orange})
print(df_02)


# 创建 Series
data = [1, 2, 3, 4, 5, 6]
index = ['a', 'b', 'c', 'd', 'e', 'f']
s = pd.Series(data, index=index)

# 查看基本信息
print("索引：", s.index)
print("数据：", s.values)
print("数据类型：", s.dtype)
print("前两行数据：", s.head(2))

# 使用 map 函数将每个元素加倍
s_doubled = s.map(lambda x: x * 2)
print("元素加倍后：", s_doubled)

# 计算累计和
cumsum_s = s.cumsum()
print("累计求和：", cumsum_s)

# 查找缺失值（这里没有缺失值，所以返回的全是 False）
print("缺失值判断：", s.isnull())

# 排序
sorted_s = s.sort_values()
print("排序后的 Series：", sorted_s)

