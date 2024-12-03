class Solution:
    # 参数 s: 字符列表, 参数 offset: 整数, 返回值: 无
    def rotateString(self, s, offset):
        if len(s) > 0:
            offset %= len(s)  # 使用取模运算，确保 offset 不超过字符串长度
            temp = (s + s)[len(s) - offset:2 * len(s) - offset]
            for i in range(len(temp)):
                s[i] = temp[i]

# 主函数
if __name__ == '__main__':
    s = ["a", "b", "c", "d", "e", "f", "g"]
    offset = 3
    solution = Solution()
    solution.rotateString(s, offset)
    print("输入：s =", ["a", "b", "c", "d", "e", "f", "g"], " offset =", offset)
    print("输出：s =", s)
