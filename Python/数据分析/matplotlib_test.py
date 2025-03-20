import pandas as pd
import matplotlib.pyplot as plt

# data = {'Year': [2015, 2016, 2017, 2018, 2019, 2020],
#         'Sales': [100, 150, 200, 250, 300, 350]}
# df = pd.DataFrame(data)

# # 折线图
# df.plot(kind='line', x='Year', y='Sales', title='Sales Over Years', xlabel='Year', ylabel='Sales', figsize=(10, 6))
# plt.show()



# # 示例数据
# data = {'Category': ['A', 'B', 'C', 'D'],
#         'Value': [10, 15, 7, 12]}
# df = pd.DataFrame(data)

# # 绘制柱状图
# df.plot(kind='bar', x='Category', y='Value', title='Category Values', xlabel='Category', ylabel='Value', figsize=(8, 5))
# plt.show()


# 示例数据
data = {'Height': [150, 160, 170, 180, 190],
        'Weight': [50, 60, 70, 80, 90]}
df = pd.DataFrame(data)

# 绘制散点图
df.plot(kind='scatter', x='Height', y='Weight', title='Height vs Weight', xlabel='Height (cm)', ylabel='Weight (kg)', figsize=(8, 5))
plt.show()