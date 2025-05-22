# pandas详解
pandas的数据结构主要由Series （一维数据）与 DataFrame（二维数据）组成
## Series
Series是一种类似于一维数组的对象，由一组数据（各种NumPy数据类型）以及一组与之相关的数据标签（即索引）组成。

## DataFrame
DataFrame是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔型值）。DataFrame既有行索引也有列索引，它可以被看做由Series组成的字典（共用同一个索引）。

## 数据的选取
### 1. 选取列
```python
df['column_name']
df[['column_name1','column_name2']]
```
### 2. 选取行
```python
df.loc['row_name']
df.loc[['row_name1','row_name2']]
df.iloc[0]
df.iloc[[0,1]]
```
### 3. 选取行和列
```python
df.loc['row_name','column_name']
df.loc[['row_name1','row_name2'],['column_name1','column_name2']]
df.iloc[0,0]
df.iloc[[0,1],[0,1]]
```


# 常用的函数
## 1. 读取数据
```python
import pandas as pd
1.pd.read_csv(filename)

2.pd.read_excel(filename)

3.pd.read_sql(query,connection_object)

4.pd.read_json(json_string)

5.pd.read_html(url)
```
## 2. 查看数据
```python
1.df.head(n) # 查看前n行数据，默认为5行

2.df.tail(n) # 查看后n行数据，默认为5行

3.df.shape # 查看数据的行数和列数

4.df.info() # 查看数据的基本信息

5.df.describe() # 查看数据的统计信息
```
## 3. 数据清洗
```python
1.df.dropna() # 删除缺失值

2.df.fillna(value) # 填充缺失值

3.df.drop_duplicates() # 删除重复值

4.df.rename(columns={'old_name':'new_name'}) # 重命名列名

5.df.replace(old_value,new_value) # 替换数据

6.df.apply(func) # 对数据应用函数
```


# 数据可视化

