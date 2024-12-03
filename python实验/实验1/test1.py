import math

def calculate_segment_area(ab, cd):
    # 根据弦AB和高CD计算半径 r
    r = (cd**2 + (ab/2)**2) / (2 * cd)
    
    # 计算圆心角 θ（弧度制）
    theta = 2 * math.asin(ab / (2 * r))
    
    # 计算扇形面积
    sector_area = 0.5 * r**2 * theta
    
    # 计算三角形面积
    triangle_area = 0.5 * ab * cd
    
    # 计算弓形面积
    segment_area = sector_area - triangle_area
    
    return round(segment_area, 2)

# 输入AB和CD的长度
ab = float(input("请输入AB的长度: "))
cd = float(input("请输入CD的长度: "))

# 计算并输出结果
area = calculate_segment_area(ab, cd)
print("弓形的面积为:", area)
