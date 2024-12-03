# 获取用户输入
total_cost = float(input("请输入总房价（元）: "))
annual_salary = float(input("请输入年薪（元）: "))
portion_saved = float(input("请输入月存款比例（百分比，例50代表50%）: ")) / 100
semi_annual_raise = float(input("请输入每半年加薪比例（百分比，例7代表7%）: ")) / 100

# 固定参数
portion_down_payment = 0.30  # 首付比例30%
current_savings = 0.0  # 当前存款
monthly_salary = annual_salary / 12  # 每月薪水
r = 0.04  # 年化收益率假设为4%

# 计算目标首付款金额
down_payment = total_cost * portion_down_payment

# 初始化计数器
months = 0

# 模拟存钱过程
while current_savings < down_payment:
    # 每月存款并计入利息收益
    current_savings += current_savings * (r / 12) + portion_saved * monthly_salary
    months += 1
    
    # 每6个月加薪一次
    if months % 6 == 0:
        monthly_salary *= (1 + semi_annual_raise)

# 输出结果
print(f"小王需要 {months} 个月才能攒够首付款。")
