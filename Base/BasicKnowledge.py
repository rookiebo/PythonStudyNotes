# 转义字符 \，\n表示换行，\t表示制表符，\\可以把\输出
print('I \'m Bangor.')
print('I \'m learning \nPython.\\')
# Python还规定使用r''的字符串默认不转义
print('\\\t\\')
print(r'\\\t\\')
# Python的与或非是and、or、not，空值是None，无限大是inf
print(10/3) # 结果是3.3333333333333335
print(9/3) # 结果是3.0
print(10//3) # 结果是3
print(10%3) # 结果是1
# Python提供ord()来获取字符的整数表示，chr()把编码转换成对应的字符
print(ord('A')) # 结果是65
print(chr(65)) # 结果是A
# 通过encode()把字符串转换成指定编码的bytes类型
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# Python对bytes类型的数据用b前缀表示
x = b'ABC'
# len()可以计算字符串的字符数，如果是bytes类型则是字节数
print(len('ABCDE')) # 结果是5
print(len('中文')) # 结果是2
print(len('中文'.encode('utf-8'))) # 结果是6

# %还可以用来格式化字符串，如果只有一个占位符，括号可以省略
# %s 用字符串替换，%d 用整数替换，%f 用浮点数替换，%x 用十六进制整数替换
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
# 第二张格式化方法是fotmat()，:后面的.1f指定了格式化参数，f表示不使用科学计数法
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', (85-72)/72))
# 第三种是在字符串开头加f
r = 2.5
s = 3.14 * r ** 2
print(f'半径是{r}的圆面积为{s:.2f}')

# list是一种有序的集合，随时可以增删改查其中的元素，用[]表示
# list里的元素可以是不同数据类型，也可以是另一个list
l = ['A', 'B', 'C']
# 在Python中可以使用负数来获取元素，-1则是最后一个元素
print(l[-2])
# append()在末尾添加元素，insert()在指定位置插入元素，pop()删除末尾元素，要删除指定位置的元素可以输入索引i
l.append('D')
l.insert(1, 'E')
l.pop()

# 另一个中有序集合叫元组：tuple，区别是tuple一旦初始化就不能修改，用()表示
t = ('A', 'B', 'C')
# 如果定义一个元素的tuple，需要这样写，为了不发生歧义
t = (1,)
# tuple其中可以添加list，即‘可变的’tuple，同时list可以进行修改
t = ('a', 'b', ['A', 'B'])

# 展示Python的条件判断
score = 'B'
if score == 'A':
    print('score is A.')
elif score == 'B':
    print('score is B.')
elif score == 'C':
    print('score is C.')
else:
    print('invalid score.')

match score:
    case 'A':
        print('score is A.')
    case 'B':
        print('score is B.')
    case 'C':
        print('score is C.')
    case _: # _表示匹配到其他任何情况
        print('score is ???.')


args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']
match args: # match还可以匹配列表
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')

# Python提供range()函数来生成一个整数序列，再通过list()转换成集合
print(list(range(5)))

# Python中的字典使用{}表示，dict的key必须是不可变对象
d = {'A': 1, 'B': 2, 'C': 3}
# 要避免key不存在的错误，一是通过in判断，二是通过dict的get()方法
print('D' in d)
print(d.get('D')) # 不存在则返回None
print(d.get('D'), -1) # 不存在则返回-1
d.pop('A') # 通过pop()方法删除dict的数据

# Python中还有一种集合set，它是一组key的集合，不存储value。由于key不能重复，所以set中没有重复数据
s = {1, 1, 2, 2, 3, 3}
print(s) # 重复数据会被过滤
s.add(4)
s.remove(4)

# 在定义函数的默认参数时，默认参数必须指向不变对象
# 如果把L定义为[]，重复执行则会出现多个'END'
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# 定义函数的可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 定义函数的关键字参数，可变参数在函数调用时自动组装为一个tuple
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra) # **extra表示把extra的所有key-value用关键字参数传入函数

# 如果要限制关键字参数的名字，就可以用命名关键字参数，*后面的参数被视为命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
# 命名关键字参数可以有默认值，调用时可以不传入city参数
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
# 如果五种参数都要使用，顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b=0, *c,  d, **e):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'e =', e)