import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams['axes.unicode_minus'] = False

# 1. 读取CSV文件
data = pd.read_csv('mtcars.csv')

# 2. 查看数据的维度、大小、占用内存空间、类型等信息
print("数据维度:", data.shape)  # 行数和列数
print("数据大小:", data.size)  # 总元素个数
print("数据占用内存空间:", data.memory_usage(deep=True).sum(), "bytes")  # 内存占用
print("数据类型:\n", data.dtypes)  # 每列的数据类型

# 3. 获得各属性的若干统计信息
print("\n各属性的统计信息：")
print(data.describe())  # 数值列的统计信息

# 4. 按cyl属性进行分组，并计算每组disp、hp、drat、wt、qsec等属性的统计信息
grouped_data = data.groupby('cyl')[['disp', 'hp', 'drat', 'wt', 'qsec']].describe()
print("\n按cyl分组后的统计信息：")
print(grouped_data)

# 5. 可视化统计信息：柱状图和饼图
# a. 各车型的平均马力（hp）柱状图
mean_hp = data.groupby('cyl')['hp'].mean()
mean_hp.plot(kind='bar', title='平均马力（hp）按cyl分组', color='skyblue')
plt.ylabel('平均马力')
plt.xlabel('cyl')
plt.show()

# b. 按cyl属性显示各类别的数量（饼图）
cyl_counts = data['cyl'].value_counts()
cyl_counts.plot(kind='pie', autopct='%1.1f%%', title='cyl分布饼图')
plt.ylabel('')  # 不显示y标签
plt.show()

# c. 柱状图：各车型的平均重量（wt）
mean_wt = data.groupby('cyl')['wt'].mean()
mean_wt.plot(kind='bar', title='平均重量（wt）按cyl分组', color='lightgreen')
plt.ylabel('平均重量')
plt.xlabel('cyl')
plt.show()

# d. 计算各属性的相关性，生成相关系数矩阵
correlation_matrix = data.corr()
print("\n相关系数矩阵：")
print(correlation_matrix)

# e. 可视化相关系数矩阵（热图）
import seaborn as sns
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title("属性相关系数矩阵")
plt.show()
