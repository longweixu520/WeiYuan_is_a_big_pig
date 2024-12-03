class Solution:
    # 参数 nums: 整数数组
    # 参数 target: 要查找的目标数字
    # 返回值：目标数字的第一个位置，从0开始
    def binarySearch(self, nums, target):
        return self.search(nums, 0, len(nums) - 1, target)
    
    def search(self, nums, start, end, target):
        # 如果起始位置超过结束位置，说明未找到目标数字
        if start > end:
            return -1
        
        mid = (start + end) // 2  # 计算中间位置
        
        if nums[mid] > target:
            return self.search(nums, start, mid - 1, target)  # 搜索左半部分
        elif nums[mid] == target:
            return mid  # 找到目标，返回位置
        else:
            return self.search(nums, mid + 1, end, target)  # 搜索右半部分

# 主函数
if __name__ == '__main__':
    my_solution = Solution()
    nums = [1, 2, 3, 4, 5, 6]
    target = 3
    targetIndex = my_solution.binarySearch(nums, target)
    
    print("输入：nums =", nums, "target =", target)
    print("输出：", targetIndex)
