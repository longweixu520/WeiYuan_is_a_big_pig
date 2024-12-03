import math
print("YES" if (n := int(input())) == sum(map(lambda x: math.factorial(int(x)), str(n))) else "NO")
