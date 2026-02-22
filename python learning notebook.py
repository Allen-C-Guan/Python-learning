# 依据python公开文档，自行学习的笔记上传
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
        # else的主要用途，还是在for没有被break的时候，能向try catch一样，发现没有被break，并进行处理，例如for循环的查找，如果i==1没有被找到，则会被else所捕获

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
'''
**************************   循环的技巧   **********************
'''
import time

from package_test_mod.private import private_test


def for_tips_test():
    # 对dict的遍历，如果只是单纯的遍历，只会把key拿出来
    dic_test = {"1": 20, "2": 30, "3": 40}
    for item in dic_test:
        print(item)

    # items()的使用, items 会把key和val对都拿出来,并以tuple的形式返回
    for key, value in dic_test.items():
        print(key, value)

    for pair in dic_test.items():
        print(pair)
    # enumerate()的使用，enumerate可以遍历所有可迭代的内容，同时启动计数器，计数，返回计数与对应的元素
    for index, (key, val) in enumerate(dic_test.items()):
        print(index, key, val)

    l = [1,2,3,4,5]
    for i, val in enumerate(l[2:4]):  # 这里就可以证明，是从零计数的，3对应的计数是0
        print(i,val)

    # zip
    # 第i个iterater，返回的是所有由所有被迭代对象的第i个对象组成的tuple
    l1 = [1,2,3,4,5]
    l2 = {"A":1,"B":2,"C":3,"D":4,"E":5}
    l3 = (1,2,3,4,5)
    print(*zip(l1, l2, l3))  # zip 返回的是迭代器，只有解包才会打印内容，解包的实现就是遍历迭代器，放到list里然后返回

    for i1, i2, i3 in zip(l1, l2, l3):
        print(i1, i2, i3)

'''
***************************  比较运算符  *************************
in, not in:  表示一个items是否在一个容器内
is, is not： is表示两个对象是否是同一个对象
'''
def cmp_op_test():
    l = [1,2,3,4,5]
    print(2 in l)
    print(3 not in l)

    l2 = l
    print(l is l2)

    a = 1
    b = 2
    c = 2
    print(a < b == c)  # 等于 a < b && b == c，并且如果b是个表达式，b只会被调用一次，但是如果是拆分开些，b会被调用2次

    l1 = [1,2,3,4,5]
    l2 = [1,2,3,4]
    print (l1 < l2) # 对于list比较，逐个元素对比，直到找到第一个不同的元素，输出比较结果。那如果如上l2是l1的子集，则短的序列小

    ll1= [l1,l2]
    ll2 = [l2,l2]
    print(ll1 < ll2)  # 对比会递归进行，既会把每个item再打开，对比item内的每个元素，直到找到一个不一样的进行比较
'''
***************************  模块  **********************************
通过import + 模块名称，可以将模块加到当前name space下，
这里注意，不会污染全局作用域，添加的是模块，如果要使用模块下的内容，需要mod_name.val_name的形式来使用
这样做的好处是，import的名称不会对当前作用域产生命名污染，import的内容，必须显示.形式的调用

注意：每个模块都会有自己的私有符号表，该表将所有本模块的函数，都定义为全局变量，可以放心使用，而另一个模块的必须要用modname.itemname
的形式来使用

***** 污染全局作用域的导入方法 ******
好处：不用总点点点
坏处：污染作用域
from modname import itemsname
这里，会把itemsname直接放到本mod下的全局作用域去，这可能会导致和本mod的命名冲突

from modname import *
这里是把有非 _items都放到本mod下的全局作用域去了

****** 脚本运行  *********
当mod有main函数的时候，既 __name__ == "__main__"的时候，可以直接执行该脚本
但是作为mod import的时候，又不会被import进来，这样一个py文件，既可以被import，又可以被当做脚本来使用
python fibo.py 50

'''


# from fib import fib1  # 这里是吧fib中的fib1直接拿过来，放到全局作用域里去了，这和本mod中的同名func混合了，作用域冲突了
# def fib1(n):
#     """Write Fibonacci series up to n."""
#     print("this is main mod fib func")
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()


g_num = 100
def mod_test():
    fib1(10)  # 如果使用 from modname import funcname, 那就会作用域污染了，
    print(g_num)   # 这里是全局作用域
    # print(fib.g_num)  # 必须显示的调用，否则就是当前作用域的全局变量

'''
**************************  模块的搜索顺序 *******************
Python 按以下顺序搜索模块：
1.搜索优先级（从高到低）：
2. 内置模块（Built-in modules）
3. 当前脚本所在目录
4. PYTHONPATH 环境变量指定的目录
5. 标准库目录
6. 第三方包目录（site-packages）

也就是说，如果当前目录下有与标准库同名的mod，将会掩盖标准库




***************************** 标准模块 *****************************
例如sys 模块, 存在于所有解释器下的


'''


'''
************************ dir() **************************
用来查找模块内定义的所有的名称（func，var等）
'''
def dir_test():
    import fib
    print(dir(fib))
    print(dir(sys))
    print(fib.__name__)
    print(fib.__file__)
    print(fib.__cached__)  # 编译后的文件，被缓存了


'''
**************************** 包 *********************************
包指的是利用“.”的方式来构造命名空间的一种方式
其解包的机制如下：
from package import item
1. 先用item匹配函数，变量等
2. 如果未找到，则假定是模块，按照模块去import，失败则抛出异常

包的使用方法如下几种
import A.B.C 
A.B.C.func()  # 此时必须用全名去使用
等价于：
from A.B import C
C.func()  # 这时，把C已经加到了全局作用域了，可以忽略A和B的前缀来直接使用了
等价于
from A.B.C import func()
func()  #这时已经把func给加入到全局作用域了，可以忽略A B C来使用了

*************** 通过 __init__ 组织package *************
如下层级架构
package_test_mod（文件夹）
    |
    |__  __init__.py
    |__  package_test.py
    |__ private.py
    |__ public.py

其中init是用来组织 package_test_mod 这个文件夹的，一个文件夹下，有了init后，就会被认为是一个package整体
当import package_test_mod发生时，调用__init__的__name__函数并执行

注意此时文件夹名称就是最外层包的根节点，使用时候，要以文件夹名字作为解包的起始，平级之间也要用文件夹起始解包

'''
def package_test():
    import package_test_mod
    package_test_mod.public.public_test()  # 可以使用不停的.操作，逐步拆包，直到拆到内层
    from package_test_mod import public
    public.public_test() # 这里就不用再带package_test_mod了
    private_test()  # private 在 import package_test_mod被引用了

'''
************************  输入和输出 ***************************

'''
def format_print_test():
    dic = {"a":1,"b":2,"c":3,"d":4,"e":5}
    for key, val in dic.items():
        print(f"the key is {key}, the value is {val}") # 在“”前+f，并用{val}中，将变量放到括号内

    # str.format的用法,{pos},{key}表示pos或者key，用来match后面的入参的
    print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))

'''
************************  with ***************************
with 可以用在任何实现了 __enter__和 __exit__的接口类上。

with expression [as var]:
    # 使用资源
    # 代码块

执行顺序：
1. with 先调用expression，返回实例给var
2. 执行var的__enter__
3. 执行代码段（正常或异常）
4. 执行var的__exit__
5. 离开with，结束

f = expression
等于try f.open():  #获取资源
    # 代码段   #使用资源
    finally：
        f.close()  # 需要手动清理
'''

class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        print(self.start)
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        print(self.end)
        return self

def with_test():
    with Timer() as t:
        time.sleep(1)

'''
*********************** open **********************
open("file name","type",encoding="utf-8")
其中 file name是文件的内容，type w(写）,r（读）,r+（读写）,a（打开并追加，修改都在后面）
'''
def open_test():
    with open("read file test.txt","r+") as f:   #配合 with使用
        print(f.readline())  # 只读取一行
        data = f.read() #返回字符串，以及全部内容，
        print(type(f))
        print(type(data))  # txt 读出来的都是str
        print(data)  # 这里会接着上面的内容继续往后读，也就是读取第二行和第三行，不是从头开始读
        # f.write(",just append")
        print(f.tell())
        f.seek(0)   # 重新将读取的光标移动到开始，index是目标位置
        print(f.read())

'''
************************ exception ***********************
'''
class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass
# 继承关系为： B <- C <- D
# exception的匹配关系中，可以向上匹配，不得向下匹配，既D可以匹配B，但是B不能匹配D
# 因此如果except高优先级的是父类的话，低优先级的子类将永远无法被匹配到
def exception_test():

    '''优先级测试'''
    for cls in [B,C,D]:  #输出BCD
        try:
            raise cls
        except D:
            print("D")
        except C:
            print("C")
        except B:
            print("B")

    for cls in [B,C,D]: #输出 BBB
        try:
            raise cls
        except B:
            print("B")
        except C:
            print("C")
        except D:
            print("D")


    '''raise 主动触发异常测试'''
    try:
        raise Exception("test exception")
    except Exception as my_error:
        print(my_error)
        # raise       # 可以重新把当前异常向外抛。直到这个异常被成功处理
    else:      # else指的是 当try没有触发exception的时候，才会走的，如果走到了except，则else不会走
        print("error end")

    '''异常链'''
    # try:
    #     open("not exist.txt")
    # except OSError as os_error:
        # 这里打印信息会多出from后的信息，体现出当前exception是由哪个exception导致的后果
        # 打印结果 raise TypeError("this is type Error in the Exception") from os_error

        # code
        # raise TypeError("this is type Error in the Exception") from os_error

    '''异常被捕获后的信息添加'''
    try:
        raise Exception("test exception")
    except Exception as my_error:
        my_error.add_note("we have tryed,but not works")  # 可以通过在exception中添加note，来更好的跟踪exception所走过的路
        # raise  # 异常继续抛出


'''
**********************************  类 **************************************
1. python类中，默认权限为public，包括成员变量和成员函数
2. 所有成员函数都是virtual的
3. 基础类型也可以被继承
'''

class MyInt(int):  # int是可以被继承的
    pass

'''
******************************** namespace ***************************
1. 不同命名空间之间是绝对没有关系的
2. 命名空间是不同时刻创建的，且有不同声明周期
    2.1 内置namespace（buildins）解释器启动创建，永远不会删除
    2.2 模块的的全局namespace是在读取模块定义时创建的
    2.3 function的命名空间是被调用时创建，返回时遗忘（无差异）
3. 作用域是静态确定的，确是动态使用的
4. 作用域的搜索顺序：
    1. 最内层作用域，包含局部名称，并首先在其中进行搜索
    2. 中间层（逐步向外）：那些外层闭包函数的作用域，包含“非局部、非全局”的名称，从最靠内层的那个作用域开始，逐层向外搜索。
    3. 倒数第二层作用域，包含当前模块的全局名称
    4. 最外层（最后搜索）的作用域，是内置名称的命名空间

因此外层变量对于局部命名空间是只读的，无法修改指向的对象，但能修改对象内容，不管是入参还是外层变量，或全局变量
如果想要修改，显示声明global或nonlocal，随后可以修改。

这就是python的哲学，拒绝一切隐式操作，必须显示赋值
'''
global_val = [3,1,4,1,5,9]
to_change_val = [1,2,3,4]
def namespace_test(val):
    print(global_val)  # val现在函数里找，找不到，到函数外找到了，既全局作用域
    # global val在局部namespace里是不允许重新指向的，但是可以修改内容
    global_val[0] = 10  # 这个可以，而且全局作用域的对象的内容同时也被修改
    # global_val = [1,2]  #修改指向是非法的，对于全局变量是语法错误
    print("inside global_val in function =", global_val)

    '''
    对于入参，不能重，但是可以修改内容，也无法重定向，
    如果重定向发生，这意味着新建了一个对象，此后的修改，都不影响外面的值。
    '''
    print("inside val value before change",val)
    val[0] = 0
    val = [3, 4]
    print ("inside val value after change", val)
    '''
    因此外层变量对于局部命名空间是只读的，无法修改指向的对象，只能修改对象内容，不管是入参还是全局变量
    '''

    global to_change_val  # 除非你显示的声明这是global变量，你才可以修改，当然如果之前没声明过，这也等于在global层面声明了一个全局变量
    print ("inside change_val after call = ", to_change_val)
    to_change_val= []

def name_space_test_main():
    val = [1,2]
    namespace_test(val)
    print("outside global_val after call =", global_val)
    print("outside val after call =", val)
    print ("outside change_val after call = ", to_change_val)
'''
************************ class ************************
不得不提class的成员变量可以延迟添加
例如
class persion:
    def __init__(self):
        self.name
        self.age
    def add_contact(email, phone):
        self.email = email
        self.phone = phone

只有当add contract被调用后才会添加联系方式，而没有被调用的add contact之前是没有这个成员的

why？
1. 动态：随时相加随时加，运行时可以添加
2. 灵活： 不用先初始化一堆变量，然后不用空着。
3. 支持多种初始化：可以分层分批次逐步初始化
4. 惰性计算：很多计算代价非常大，先不算，用时候再算

为什么python能这么灵活，C++却这么搓？
C++
那是因为C++是编译时候确定的，即使是虚函数，也是虚表，虚表是一个类公用一个，不支持动态添加的
python：
但是python确是运行时查找的，找到自己的dict，看看dict有没有这个属性？（运行到了现场进行字符串匹配），
而且每个instance是由自己的独有的dict！不同的inst可以有不同的dict！这太离谱了

到9.3.3了
'''
class MyClass:
    class_val = 10   # 这是类变量！所有instance共享
    def __init__(self):
        self.instance_val = 20  # 这是成员变量，instance独享的
    def test1(self): # 甚至可以在非__init__函数中声明成员变量
        self.other_function_inst_val1 = 30
    def test2(self):
        self.other_function_inst_val2 = 40

def class_test():
    my_class = MyClass()
    print(my_class.class_val)
    print(my_class.instance_val)
    my_class.test1()
    print(my_class.other_function_inst_val1)
    print("is inst has val2 before call test2",hasattr(my_class,"other_function_inst_val2"))  # 这时还没有val2
    print(dir(my_class))
    my_class.test2()
    print("is inst has val2 after call test2",hasattr(my_class,"other_function_inst_val2")) # 调用test2后，这已经有了val2
    print(my_class.other_function_inst_val2)  # 必须要test2调用后，val2才会被实例化
    print(dir(my_class))
'''
**************************************  类  ********************************
python和C++成员函数差异解析：
1. python中，成员函数就是普通函数，和外部函数一样，储存在类字典中，运行时现绑定
2. C++ 成员函数是真正的成员函数，编译时绑定
python哲学：
1. 显示由于隐式，所以要显示的写出self
2. 一致性：成员函数没什么特殊的，只是普通函数的第一个入参是实例自己罢了


成员函数：
1. python所有成员函数都是virtual的
2. python中多态的实现方式是：
    算法上：MRO算法
    数据上：Class.__bases__(直接父类), Class.__mro__(命名空间解析顺序（编译时确定）), Class.__subclasses__(直接子类)

def get_attribute(obj, attr_name):
    # 1. obj的dict里是否能找到
    # 2. 遍历mro，在遍历当前namespace下的dict是否能找到该内容
    # 3. 如果找到了就返回

所以这里本质上其实是依赖mro的顺序，以及每个mro下的dict，实现动态绑定的，这是运行时现场查找的

'''

# 这里就更反映出了，其实成员函数就是入参是self的函数仅此而已，类内可以去直接通过赋值来复用这个函数。
def out_side_member_func(self, a):  # 如果要被类内引用，必须加上self
    print("this is out side member func with val =", a)



class MyClass:
    def __init__(self):
        self.__private_var = 3.14

    def __private_func(self):
        print("this is private func")

    def f(self): # 成员函数被调用的时候，成员自己作为self的实参，而不需要外部显示的调用
        return "hello world!"

    g = f  #这里是把成员函数赋值给了另一个变量，g和h没有任何区别
    in_side_member_func = out_side_member_func

class Class2:
    func = out_side_member_func  # 两个类共用一个函数，外部定义的函数成了接口了！

class MyDerivedClass(MyClass):
    def f(self):
        return "hello son"
class MyGrandSonClass(MyDerivedClass):
    pass

def ClassTest():
    x = MyClass()
    print(x.f())
    print(x.g())
    x.in_side_member_func(10)
    # x.out_side_member_func(20)   #这是非法的！

    y = Class2()
    y.func(20)
    print(x.__class__)  # 通过__class__可以看到type的类型

    # 继承
    x_son = MyDerivedClass()
    print(x_son.f())  #hello son
    print(x_son.g())  # hello world! 也就是说，父类中的g = f，真的就是等于，及时子类已经重写了f，g也是等于父类的f，这是因为g = f 本质上是g = MyClass.f

    x_grand_son = MyGrandSonClass()
    print(MyGrandSonClass.__bases__)
    print(MyGrandSonClass.__mro__)
    print(MyClass.__subclasses__())
    print(x_grand_son.__dict__)
    print(isinstance(x_son, MyClass))

'''
**************************** 类的private ***************************************
python中，没有真正的private的类，通常情况下我们约定俗成的private有如下两类
1. self._private  #这只是一种命名约定，没有强制要求
2. self.__private #这里解释器会改变__的命名，改成_ClassName__private，在继承体系中，会让不同子类之间，有不同的命名。

__private
用法1：避免子类覆盖父类接口：例如  __overrided_func_others的用法

'''
class Private_Base_Class:
    def __init__(self):
        __private_val = 10
        public_val = 2

    def overrided_func(self):
        print("this is base_func")

    def outside_func(self):
        self.__overrided_func_others()  # 此时这里就没有多态了！

    __overrided_func_others = overrided_func  # 这里对于Private_Base_Class中，overrided_func_others = Private_Base_Class_overrided_func
                                            # 对于Private_Drived_Class中，overrided_func_others == Private_Drived_Class_overrided_func_others
                                            # 由于python所有接口都是虚接口，因此针对想要避免父类行为被子类通过重写其中某个接口而覆盖时，需要这个操作

class Private_Drived_Class(Private_Base_Class):
    def overrided_func(self):
        print("this is overrided func")

class TestNothing:
    def __init__(self):
        self._private = 100
        self.__private = 10

def private_func_test():
    b1 = Private_Base_Class()
    d1 = Private_Drived_Class()
    b1.outside_func()
    d1.outside_func()
    t = TestNothing()
    print(t._TestNothing__private)
    print(t._private)


'''
*************************************** 迭代器 **********************************************
只要类有iter和next， 就可以被迭代
使用迭代器的常用方法：for...in iterater
注意：迭代器中，next接口中，当迭代到终点时，是抛出异常！不是返回异常！
'''

class ReverseIt:
    def __init__(self, data):
        self.index = len(data)
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration   # 这里是抛出异常，不是return 异常！
        self.index -= 1
        return self.data[self.index]

def iteration_test():
    l = [1,2,3,4,5]
    r_it = ReverseIt(l)
    for item in r_it:
        print (item)


'''
############################### 生成器  ####################################
1. 生成器和迭代器最大的不同在于，生成器是惰性生成，迭代器是一次性全部生成的，iteration对于内存的压力非常大
2. yield通过一种优雅的函数形式，实现了next，iter接口，实现了current的存储，断点继续执行等高级用法，体现了python函数编程的核心

def range_generator(start, end):
    current = start
    while current < end:
        # Python自动保存：current的值、程序执行位置(while循环内)
        yield current
        # 恢复执行时自动恢复：current的值、程序位置
        current += 1
'''

def reverse_generator(data):
    current = len(data)-1
    while current >= 0:
        yield data[current]     # yield会将指针，current的值，都记录下来，为了下次断点可以继续执行
        current -= 1            # 下一次调用同一个实例的next的时候，会从这一行开始执行

def generater_test():
    l = [1,2,3,4,5]
    r = reverse_generator(l)
    print(next(r))  # 输出5
    print(next(r))  # 输出4
    for i in r:   # 输出3 2 1，是接着上面输出的，因为是同一个实例
        print(i)

    print(sum([i * i for i in range(5)]))  # 这里是推导式，要把整个数组都生成出来，然后执行sum
    print(sum(i * i for i in range(5)))  # 这里是生成式，元素一个一个生成，然后执行sum，内存要求小


'''
****************************************  标准库  *****************************************
os 模块提供了许多与操作系统交互的函数:
'''
def std_test():
    import os
    print(os.getcwd())  # 返回当前工作目录
    # os.chdir('/server/accesslogs')  # 改变当前工作目录
    import sys
    print(sys.argv)

'''
***************************************  用注释来生成测试用例  **********************
'''
def average(values):
    """计算数字列表的算术平均值

    >>> print(average([20, 30, 70]))      # 这直接把测试用例写注释里了！，这太牛逼了
    40.0
    """
    return sum(values) / len(values)+1

def test_doc():
    import doctest
    doctest.testmod()   # 自动验证嵌入式测试用例

'''
***************************************  python虚拟环境与包  **********************
https://docs.python.org/zh-cn/3/tutorial/venv.html
'''


if __name__ == "__main__":
    private_func_test()
    a = 0.1
    print(3*a == 0.3)
    print("end of main")


