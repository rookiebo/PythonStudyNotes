"""Python 高级特性示例：切片、迭代、列表生成式、生成器和迭代器。"""


from collections.abc import Iterator


def demonstrate_slicing() -> None:
    """展示切片：从序列中取得一部分元素。"""
    numbers = list(range(1, 11))
    print("1. 切片")
    print(f"原列表：{numbers}")
    print(f"前 3 个元素：{numbers[:3]}")
    print(f"每隔 2 个取一个：{numbers[::2]}")
    print(f"倒序列表：{numbers[::-1]}")


def demonstrate_iteration() -> None:
    """展示迭代：依次访问可迭代对象中的元素。"""
    student_scores = {"小明": 92, "小红": 95, "小刚": 88}
    print("\n2. 迭代")
    for name, score in student_scores.items():
        print(f"{name} 的成绩：{score}")


def demonstrate_list_comprehension() -> None:
    """展示列表生成式：用简洁语法创建列表。"""
    squares_of_even_numbers = [number**2 for number in range(1, 11) if number % 2 == 0]
    print("\n3. 列表生成式")
    print(f"1 到 10 中偶数的平方：{squares_of_even_numbers}")


def fibonacci(limit: int):
    """生成器函数：按需产生斐波那契数列。"""
    first, second = 0, 1
    for _ in range(limit):
        yield first
        first, second = second, first + second


def demonstrate_generator() -> None:
    """展示生成器：不会一次性创建所有结果。"""
    print("\n4. 生成器")
    generator_expression = (number**2 for number in range(1, 6))
    print(f"生成器表达式产生的平方数：{list(generator_expression)}")
    print(f"斐波那契数列前 8 项：{list(fibonacci(8))}")


def demonstrate_iterator() -> None:
    """展示迭代器：通过 next() 逐个获取元素。"""
    colors = ["红", "绿", "蓝"]
    color_iterator: Iterator[str] = iter(colors)
    print("\n5. 迭代器")
    print(f"iter(colors) 是迭代器：{isinstance(color_iterator, Iterator)}")
    print(f"依次调用 next()：{next(color_iterator)}、{next(color_iterator)}、{next(color_iterator)}")


if __name__ == "__main__":
    demonstrate_slicing()
    demonstrate_iteration()
    demonstrate_list_comprehension()
    demonstrate_generator()
    demonstrate_iterator()
