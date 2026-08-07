import math

# 使用条件判断来判断人物的BMI指数
def CalculateBMI():
    height = float(input('height:'))
    weight = float(input('weight:'))
    bmi = weight/height/height
    print(f'BMI:{bmi:.1f}')
    if bmi < 18.5:
        print("过轻")
    elif 18.5 <= bmi <25:
        print("正常")
    elif 25 <= bmi < 28:
        print("过重")
    elif 28 <= bmi < 32:
        print("肥胖") 
    else:
        print("严重肥胖")

# 定义quadratic(a, b, c)，计算一元二次方程的两个解
def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b**2 - 4*a*c))/2*a
    x2 = (-b - math.sqrt(b**2 - 4*a*c))/2*a
    return x1, x2

# 定义一个函数mul()计算一个或多个数的乘积
def mul(*numbers):
    if not numbers or len(numbers) == 0:
        raise TypeError
    sum = 1
    for n in numbers:
        sum = sum * n
    return sum

# 定义move()，解决汉诺塔问题
def move(n, a, b, c):
    if n == 1:
        # 如果只有1个盘子，直接从起点移到终点
        print(f"{a} --> {c}")
    else:
        # 1. 把上面 n-1 个盘子从 a 借助 c 移到 b
        move(n - 1, a, c, b)
        # 2. 把最大的盘子从 a 移到 c
        move(1, a, b, c)
        # 3. 把 n-1 个盘子从 b 借助 a 移到 c
        move(n - 1, b, a, c)

if __name__ == "__main__":
    CalculateBMI()

    # 利用循环打印出集合中的每个名字，Hello, xxx!
    L = ['Bart', 'Lisa', 'Adam']
    for n in L:
        print(f"Hello, {n}!")

    print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
    print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
    if quadratic(2, 3, 1) != (-0.5, -1.0):
        print('测试失败')
    elif quadratic(1, 3, -4) != (1.0, -4.0):
        print('测试失败')
    else:
        print('测试成功')

    print('mul(5) =', mul(5))
    print('mul(5, 6) =', mul(5, 6))
    print('mul(5, 6, 7) =', mul(5, 6, 7))
    print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
    if mul(5) != 5:
        print('mul(5)测试失败!')
    elif mul(5, 6) != 30:
        print('mul(5, 6)测试失败!')
    elif mul(5, 6, 7) != 210:
        print('mul(5, 6, 7)测试失败!')
    elif mul(5, 6, 7, 9) != 1890:
        print('mul(5, 6, 7, 9)测试失败!')
    else:
        try:
            mul()
            print('mul()测试失败!')
        except TypeError:
            print('测试成功!')
    
    # 测试：假设有3个盘子，从A借助B移到C
    move(3, 'A', 'B', 'C')