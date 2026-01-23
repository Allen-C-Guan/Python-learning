import sys

# 赋值与表达式之间的关系
def fib():
    a, b = 0, 1
    while a < 10:
        print(a)
        a, b = b, a + b  # 等号右边的所有表达式的执行，都在赋值之前完成！不会存在右边表达式之间互相影响的情况，执行顺序从左到右

def copy_test():
    a = [1, 2, 3]
    b = a # 在python中，所有的赋值都是copy，除了字面值
    print(id(a), ",", id(b))

def for_test():
    users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
    # 策略：迭代一个副本
    for user, status in users.copy().items(): # 遍历copy，但是del原来的内容
        if status == 'inactive':
            del users[user]  # del删除的是引用计数器--，shara_ptr的计数--的作用，不是直接干掉内存。

def ref_count_test():
    a = "this is allen"
    print(sys.getrefcount(a))
    b = a                       # 计数器++
    print(sys.getrefcount(a))
    print(sys.getrefcount(b))
    c = b                       # 计数器++
    print(sys.getrefcount(a))
    print(sys.getrefcount(b))
    del b                       # 计数器--
    print(sys.getrefcount(a))
    print(sys.getrefcount(c))

def range_test():
    print(list(range(-10, -100, -30)))  # start,end,step,step默认是1
    print(range(-10, -100, -30))  # range只有再被迭代的时候，才会展现出期望的列表项，实际上range没有生成过含有全部项的列表，为了节省空间,range和list是两个不同的class

def for_else_test():
    print ("start end without break")
    for i in range(3):
        print(i)
    else:
        print("end of for without break") # 在这里else会被无脑执行, else会在for循环结束后执行
    print("start end with break")
    for i in range(3):
        print(i)
        if i == 1:
            break
    else:
        print("end of with break")   # 这里else是不会被执行到的，for前有break
        # 从语法上看，else是for的一部分，break或者return的时候，也会跳过else。
        # else的主要用途，还是在for有break的时候，能向try catch一样，抓住break，并进行处理

# pass的主要作用是：语法占位，从而让编码的过程中，头脑始终保持在抽象的层次思考。
def pass_test():
    pass  #记得实现

    class MyEmptyClass:
        pass  # 类里

    for i in range(10):
        pass  #循环里

"""
**********************    function   *******************************
概念1：实参和形参
例如对于函数中
def func(a):
    pass
a 就是形参
当调用函数时 func(1) 或者 func(score)的时候，1和score就是实参
在call时，编译器将score的地址，绑定给了形参“a”，并且在function结束时，这种绑定关系结束。

概念2：局部变量符号表
当函数call的时候，所有函数变量都在局部符号表中，而实参也被引入到该函数的局部符号表中

概念3：对于没有返回值的函数，python仍然提供一个返回值，None！
"""
def func_test(a):
    a += 1




'''
****************************  形参表述   ***************************
当函数的形参的默认值是个mutable时，多次调用会有风险
'''
def f(a, L=[]):
    L.append(a)
    return L
'''
多次调用的时候，会发生如下情况，
print(f(1)) # [1]
print(f(2)) # [1,2]
print(f(3)) # [1,2,3]

这是因为默认值只在函数定义时，被创建了一次，而不是每次调用都创建：
​生命周期: 默认参数列表的生命周期与函数对象相同，从函数定义开始，直到程序结束或函数被重新定义。
​创建时机: 默认参数在函数定义时创建一次，而不是每次调用时创建。
​最佳实践: 使用 None 作为可变类型（列表、字典、集合）的默认值，在函数内部创建新对象。

def f(a, L=[]):
    """
    这个默认参数列表在函数定义时创建，
    并且在整个程序运行期间都存在
    """
    L.append(a)
    return L

# 相当于：
_default_L = []  # 在函数定义时创建

def f(a, L=_default_L):  # 引用 到完全相同的list
    L.append(a)
    return L
'''




'''
*************************  关键字参数  ********************************
关键字的顺序可以颠倒，顺序不重要，也可以不使用关键字（位置参数）（顺序按照形参定义顺序）
但是关键字参数后不能有位置参数
'''

def key_word_param_test(a, b = 1, c = 2, d = 3):
    print (a,b,c,d)

'''
特殊参数
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):  # 3.7不支持

      -----------    ----------     ----------
        |             |                  |
        |        位置或关键字   |
        |                                - 仅限关键字
         -- 仅限位置
def standard_arg(arg):
def pos_only_arg(arg, /):
def kwd_only_arg(*, arg):
def combined_example(pos_only, /, standard, *, kwd_only):

'''
### 任意实参列表 #####
def test_multiple_items(a, b, *args,  c = 0):  #args后面只能跟关键字参数，不允许pos 参数
    print(type(args))
    print(*args)
'''
test_multiple_items(1, 2,3,4,5,6,7,10) # 输出：3 4 5 6 7 10。 针对关键字参数，如果显示指定，args不会把最后一个参数分给关键字参数的
test_multiple_items(1, 2,3,4,5,6,7,c =10) # 输出 3 4 5 6 7
'''




'''
 ***************************  解包 **********************************
什么是解包：就是把可以“可迭代的对象”进行切片就是解包
'''
def unpacking_test():
    a, b, c = [1,2,4] # 这就是把list里的对象切片为3个对象，并进行赋值
    e,f = "la" # 字符串也可以解包
    k1,k2 = {"a":1, "b":2}  # dict解包之后，就把val给丢了！
    print(k1,k2)

    g,*h, i = [1,2,3,4,5]  # * arg 语法可以放任意个变来拿个，当每个元素都匹配一个的时候，剩下的就是args的了, 当然不能有两个 *args存在，此时语法有二义性
    print(g, h, i)
'''
可以使用 * 显示解包序列容器，用** 解包映射容器
'''
def unpacking_params_test(a,b,c):
    print(a,b,c)
'''
unpacking_params_test(*[1,2,3]) # 输出1,2，3 这里把1,2,3拆分成三个，按照顺序解包给了入参a，b，c
unpacking_params_test(**{"b":2, "a":1,"c":3}) # 输出1,2,3，这里把每一对字典对，key作为关键字参数，val作为对应的形参的值
'''
def multiple_unpacking_test():
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    print([*l1, l2])  # [1, 2, 3, [4, 5, 6]]，这里把*l1解包放在外面，l2是个嵌套的内层list
    print([*l1, *l2])  # [1, 2, 3, 4, 5, 6] 这里包都解开了

'''
**************************** lambda *****************************************
lambda arguments: expression
其中arguments可以省略
expression的结果就是返回值
l_func = lambda a : a+10
print(l_func(10))
'''

'''
************************ 文档字符串  ***********************
'''

def doc_str_test():
    """do nothing, just document it

        lalalala
    """
    pass
# 可以通过  print(doc_str_test.__doc__) 打印这段内容

'''
************************ list ***************************
'''

def list_test():
    '''list的 function'''
    l1 = [1, 2, 3]
    l2 = [3, 4, 5]
    l1.extend(l2)
    print(l1)
    print(l1+l2)
    print(l1.index(3,3,6))  #index 查找首个元素对应的索引,(key, start, end)
    # print(l1.index(10))    # index如果找不到是会报错的！！抛出异常的
    l1.reverse()
    print(l1)
    l1.pop(3)  # pop 的入参是index，对应index的内容从list里删除
    l1.remove(5)  #remove的入参是 值，找到第一个是该值的内容，并移除
    print(l1)

    '''
    列表推导式
    列表推导指的是：对序列，或者可迭代对象中的每个元素操作后，生成新的序列的过程
    
    '''
    # 1. 可迭代
    squares = [x**2 for x in range(10)]  # 这里，list可以通过 内置for循环来优雅的创建
    print(squares)
    l3 = [1,2,3,4,5,6]
    l4 = [x**2 for x in l3]
    print(l4)

    # 2. 可迭代+表达式，当表达式成立时，新增元素
    print([(x, y) for x in range(10) for y in range(10,1,-1) if x == y])

    #等价于
    combs = []
    for x in range (10):
        for y in range(10,1,-1):
            if x == y:
                combs.append((x,y))
    '''
    嵌套列表推导式
    '''
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    print([[row[i] for row in matrix] for i in range(4)])
    # 这里[row[i] for row in matrix]（内层）是 for i in range(4)（外层）的初始表达式，等于
    transports = []
    for i in range(4):  #这是外层的
        transports.append([row[i] for row in matrix])  #这是内层表达式
'''
************************** del ****************************
何时是修改，何时是修改指向？
函数1：
def test_del_func(dt):
    dt.a = 2  
函数2：
def test_del_func(dt):
    dt = DelTest(2) 
    
这里函数1是修改，函数2不是修改！这是因为针对函数1，
'''

class DelTest:
    def __init__(self, i):
        self.a = i
        print("constructed")
    def __del__(self):
        print("destructed")

def test_del_func(dt):
    print(id(dt))
    dt.a = 2

'''
************************** 形参与实参的关系 ****************************
何时是修改，何时是修改指向？
函数1：
def test_del_func(dt):
    dt.a = 2  
函数2：
def test_del_func(dt):
    dt = DelTest(2) 

这里函数1是修改，函数2不是修改！这是因为针对函数1，显示的使用了”."的操作，此时形参依旧绑定在了实参上，因此修改了外层实参的内容，既产生了副作用
而函数2中，本来传入的时候，形参是绑定在实参上，随后形参又指向了一个新的内容为2的实例，此时形参和实参没有绑定在同一个对象上。


**************** python 为什么要设计成共享传递 **************************
python中的传递，既不是引用传递，又不是值传递，是两者的折中。
共享传递：将对象的引用*副本*传递给函数形参，也就是形参只是拿到了地址的副本，因此如果你对地址解引用（使用.)，则可以访问和修改内容。
但是如果你发生复制操作 a = A() 则你只是修改了副本地址，此后a就指向了一个新的内容了，对a的访问和修改，都不影响实参的内容



1. 一致性原理：明确优于隐晦，函数的调用导致外部无预期，是隐晦的
例如
x = 5
y = x
some_function(x)
# 现在x还是5吗？不确定！ 如果要明确应该：x = some_function(x)

2. 避免副作用原则：上述例子，函数调用对外部产生了副作用，且不是明显的，是隐晦的
3.​ 函数式编程的考虑（不依赖继承关系）：Python支持函数式编程范式，其中一个重要原则是纯函数​：
    给定相同输入，总是返回相同输出
    没有副作用（不改变外部状态）
当前的参数传递方式使得编写纯函数变得容易。
4. ​与不可变对象的一致性: 如果可以引用，那入参是可变的，和不可变的没法用相同的方式调用。（不依赖继承的函数式编程）
5. 允许改变可变对象的内容，但是不能改变实参的引用！（上面的例子就违反了这个条款）

从而达成，在一个函数里，只有对形参进行"."的显示操作（说明显示的获取了内容），才有可能有副作用
'''



if __name__ == "__main__":
    dt = DelTest(1)
    print(id(dt))
    test_del_func(dt)
    print("end of main")


