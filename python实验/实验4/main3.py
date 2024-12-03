import pandas as pd

# 读取数据
data = pd.read_csv('missing_data.csv', header=None)

# 查看原数据
print("原数据：")
print(data)

# 填充缺失值
# 1. 对于数值列，我们使用均值填充缺失值
data_filled_mean = data.fillna(data.mean())

# 2. 如果我们认为数据可能有极端值，可以选择使用中位数填充
# data_filled_median = data.fillna(data.median())

# 3. 如果数据的缺失是随机且前后数据相关，可以使用前向填充（ffill）或后向填充（bfill）
# data_filled_ffill = data.fillna(method='ffill')
# data_filled_bfill = data.fillna(method='bfill')

# 4. 如果有更复杂的插值需求，可以使用插值法
# data_filled_interpolate = data.interpolate(method='linear')

# 输出填充后的数据
print("\n填充后的数据（使用均值填充）：")
print(data_filled_mean)

# 保存填充后的数据（如果需要）
# data_filled_mean.to_csv('filled_data.csv', index=False)
