# 定义一个函数，用欧几里得算法求两个数的最大公约数
def gcd(a, b):
  # 如果b为0，返回a
  if b == 0:
    return a
  # 否则，用b和a除以b的余数递归调用函数
  else:
    return gcd(b, a % b)

# 输入两个正整数
a = int(input("请输入第一个正整数："))
b = int(input("请输入第二个正整数："))

# 调用函数并打印结果
print("两个数的最大公约数是：", gcd(a, b))
