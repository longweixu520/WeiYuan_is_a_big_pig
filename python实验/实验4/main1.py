import numpy as np

# 1. 创建一维数组、二维数组、三维数组
# 方法1：使用 np.array
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# 方法2：使用 np.arange 和 np.reshape
array_1d_method2 = np.arange(5)
array_2d_method2 = np.arange(9).reshape(3, 3)
array_3d_method2 = np.arange(12).reshape(2, 2, 3)

# 2. 生成一个三维随机数组，并显示其所有属性
random_3d_array = np.random.rand(2, 3, 4)
print("三维随机数组:\n", random_3d_array)
print("数组形状:", random_3d_array.shape)
print("数组维度:", random_3d_array.ndim)
print("数组元素总数:", random_3d_array.size)
print("数组数据类型:", random_3d_array.dtype)

# 3. 生成一个随机数组，找出符合某个条件（自给）的所有元素
random_array = np.random.randint(1, 10, size=(5, 5))
print("随机数组:\n", random_array)
condition_elements = random_array[random_array > 5]
print("符合条件的元素:", condition_elements)

# 4. 生成多个随机数组，实现数组的不同轴上的合并
random_array1 = np.random.randint(1, 10, size=(3, 4))
random_array2 = np.random.randint(1, 10, size=(3, 4))
concatenated_array = np.concatenate((random_array1, random_array2), axis=0)  # 沿着第一维拼接
print("合并后的数组:\n", concatenated_array)

# 5. 生成一个随机数组，实现数组的不同轴上的分割
split_array = np.random.randint(1, 10, size=(4, 4))
split_result = np.split(split_array, 2, axis=1)  # 沿着第二维分割
print("分割后的数组:")
for i, sub_array in enumerate(split_result):
    print(f"子数组{i}:\n", sub_array)

# 6. 生成一个随机数组，实现数组的不同轴上的排序
sort_array = np.random.randint(1, 100, size=(3, 4))
sorted_array = np.sort(sort_array, axis=1)  # 沿着第二维排序
print("排序后的数组:\n", sorted_array)

# 7. 生成一个1000*4的随机数组，描述其一些统计属性
large_random_array = np.random.rand(1000, 4)
print("数组的统计属性：")
print("平均值:", np.mean(large_random_array, axis=0))
print("标准差:", np.std(large_random_array, axis=0))
print("最小值:", np.min(large_random_array, axis=0))
print("最大值:", np.max(large_random_array, axis=0))
print("中位数:", np.median(large_random_array, axis=0))
