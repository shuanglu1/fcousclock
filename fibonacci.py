# 定义一个函数，用递归的方式生成一个斐波那契数列
def fibonacci(n):
  # 如果n为0或1，返回n
  if n == 0 or n == 1:
    return n
  # 否则，返回前两项的和
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

# 输入一个正整数
n = int(input("请输入一个正整数："))

# 打印斐波那契数列的前n项
print("斐波那契数列的前", n, "项是：")
for i in range(n):
  print(fibonacci(i), end=" ")
print()
