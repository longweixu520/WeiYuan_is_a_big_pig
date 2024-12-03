import math

def earth_calculations(radius):
    # (1) 地球表面积
    surface_area = 4 * math.pi * radius**2

    # (2) 地球体积
    volume = (4/3) * math.pi * radius**3

    # (3) 地球赤道的周长
    circumference = 2 * math.pi * radius

    # (4) 绳子延长后的空隙大小
    new_circumference = circumference + 1  # 延长1米
    new_radius = new_circumference / (2 * math.pi)
    gap = new_radius - radius

    # (5) 判断老鼠是否能通过
    mouse_diameter = 0.1  # 老鼠直径为10cm，即0.1m
    can_mouse_pass = gap > mouse_diameter
    mouse_result = "老鼠可以从空隙中钻过" if can_mouse_pass else "老鼠无法通过空隙"

    # 输出结果
    print(f"(1) 地球表面积: {surface_area:.2f} 平方公里")
    print(f"(2) 地球体积: {volume:.2f} 立方公里")
    print(f"(3) 地球赤道的周长: {circumference:.2f} 公里")
    print(f"(4) 绳子与地球之间的空隙大小: {gap:.2f} 米")
    print(f"(5) {mouse_result}")

# 地球半径
earth_radius = 6371  # 单位为公里
earth_calculations(earth_radius)
