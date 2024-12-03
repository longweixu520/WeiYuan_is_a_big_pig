head, foot = map(int, input("请输入头数和脚数（空格分隔）: ").split())

if foot % 2 != 0 or foot < 2 * head or foot > 4 * head:
    print("Data Error!")
else:
    # 计算兔子的数量
    rabbit = (foot - 2 * head) // 2
    # 计算鸡的数量
    chicken = head - rabbit
    print(f"鸡有 {chicken} 只，兔有 {rabbit} 只")
