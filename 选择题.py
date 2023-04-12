q='''1.对于以下代码段：
Code1:
if number % 2 == 0:
    even = True
else:
    even = False
Code 2:
even = True
if number % 2 == 0
else:
    False
Code3:
even = number % 2 == 0
（	）是正确的。
A.Code 2有错误
B.Code 3有错误
C.Code 1、Code 2和code 3都是正确的，但Code 1更好
D.Code 1、Code 2和code 3都是正确的，但Code 2更好
E.Code 1、Code 2和code 3都是正确的，但Code 3更好

参考答案：
E'''

 

w='''2.若年龄（age）小于16岁，显示“Cannot get a driver's license”；若年龄
（age）大于或等于16岁，显示“Can get a driver's license”，以下代码段最佳的是（	）。

I:
if age < 16:
    print("Cannot get a driver's license")
if age >= 16:
    print("Can get a driver's license")
II:
if age < 16:
    print("Cannot get a driver's license") 
else:
    print("Can get a driver's license")
III:
if age < 16:
    print("Cannot get a driver's license")
elif age >= 16:
    print("Can get a driver's license")
IV:
if age < 16:
    print("Cannot get a driver's license")
elif age == 16:
    print("Can get a driver's license")
elif age > 16:
    print("Can get a driver's license")   
A.I
B.II
C.III
D.IV

参考答案：
B'''

 

e='''3.下面的语句读取两个数据，正确的输入格式是（	）。
x, y = eval(input("Enter two numbers: "))
A.1 2
B."1 2"
C.1, 2
D.1, 2,

参考答案：
C'''


r='''4.“小于或等于”比较运算符是（	）。
A.<
B.<=
C.=<
D.<<
E.!=

参考答案：
B'''

 

t='''5.可以在一行的结尾处放置一个行继续符号（	）来告诉解释器这条语句将继续到下一行。
A./
B.\
C.#
D.*
E.&

参考答案：
B'''


y='''6.format函数的返回值是（	）。
A.一个整数
B.一个浮点数
C.一个字符串

参考答案：
C'''

 
u='''7.以下程序的输出结果是（	）。
y = 0
for i in range(10, 1, -2):
    y += i
print(y)
A.10
B.40
C.30
D.20

参考答案：
C'''


i='''8.下面（	）应该被定义为一个无返回值函数。
A.编写一个函数，打印从1到100的整数
B.编写一个函数，返回一个1到100之间的随机整数
C.编写一个函数，检查当前秒数是否是一个1到100之间的整数
D.编写一个函数，将一个大写字母转换为小写字母

参考答案：
A'''

 
o='''9.执行下列语句，输出的结果是（	）。
j = i = 1
i += j + j * 5 print(i)
A.1
B.5
C.6
D.7

参考答案：
D'''

 
p='''10.以下程序的输出结果是（	）。
for i in range(1,11):
print(i, end = " ")
A. 1 2 3 4 5 6 7 8 9
B. 1 2 3 4 5 6 7 8 9 10
C. 1 2 3 4 5		
D. 1 3 5 7 9		
E. 2 4 6 8 10		

参考答案：
B'''
 


 


a='''11.假设x的值为4、y的值为5，以下表达式的值为真（true）的是（	）。
A.x < 5 and y < 5
B.x < 5 or y < 5
C.x > 5 and y > 5
D.x > 5 or y > 5

参考答案：
B'''


s='''12.以下程序的输出结果是（	）。
x=0
while x<4:
    x=x+1
print(x)
A.0
B.1
C.2
D.3
E.4

参考答案：
E'''


d='''13.以下运算符右结合的是（	）。
A.*
B.**
C.%
D.and
E. =

参考答案：
E'''

 

f='''14.下列（	）是正确的。
(A)x-=x+4
(B)x=x+4-x
(C)x=x-(x+4)
A.(A)和(B)是相同的
B.(A)和(C)是相同的
C.(B)和(C)是相同的
D.(A)、(B)和(C)是相同的

参考答案：
B'''

 
g='''15.下列代码段的输出结果是（	）。
print("A", end = ' ')
print("B", end = ' ')
print("C", end = ' ')
print("D", end = ' ')
A.ABCD
B.A, B, C, D
C.A B C D
D.A B C D

参考答案：
C'''
 
h='''16.random.randint(0, 1)的返回值是（	）。
A.0
B.1
C.0或1
D.2

参考答案：
C'''

 
j='''17.以下程序的输出结果是（	）。
y = 0
for i in range(0, 10, 2):
    y+=i
    print(y)
A.9
B.10
C.11
D.20

参考答案：
D'''

 
k='''18.	以下程序输出“Welcome to Python”（	）次。 count = 0
while count <10:
print("Welcome to Python")
 

（2分）
 

A.	8
B.	9
C.	10
D.	11
E.	无数次

参考答案：
E'''

 

l='''19.	给定以下四种图案：
图案A	图案B	图案C	图案D
1					1	2	3	4	5	6				1	1	2	3	4	5	6
1	2				1	2	3	4	5				2	1		1	2	3	4	5
1	2	3			1	2	3	4				3	2	1			1	2	3	4
1	2	3	4		1	2	3				4	3	2	1				1	2	3
1	2	3	4	5	1	2					5 4	3	2	1					1	2
1	2	3	4	5 6	1						6 5 4	3	2	1						1
（	）是由如下程序生成的。 for i in range(1, 6 + 1):
for j in range(6, 0, -1):
print(j if j <= i else " ", end = " ") print()
 

（2分）
 

A.	图案A
B.	图案B
C.	图案C
D.	图案D
 
参考答案：
C'''


z='''20.	下列（	）函数的返回值是4。	（2分）
A.	int(3.4)
B.	int(3.9)
C.	round(3.4)
D.	round(3.9)

参考答案：
D'''


x="""21.	Python的段落注释的语法格式是（	）。	（2分）
A.	//comments //
B.	/* comments */
C.	'''comments '''
D.	/# comments #/

参考答案：
C"""

 
c='''22.	以下程序的输出结果是（	）。 number = 25
isPrime = True
for i in range(2,number): if number % i == 0:
isPrime = False break
print("i is", i, "isPrime is", isPrime)
 

（2分）
 

A.	i is 5 isPrime is True
B.	i is 5 isPrime is False
C.	i is 6 isPrime is True
D.	i is 6 isPrime is False

参考答案：
B'''

 

v='''23.	下列代码段的输出结果是（	）（注意：?表示空格）。
print(format("Welcome", "10s"), end = '#')
print(format(111,"4d"), end = '#')
print(format(924.656, "3.2f"))
 

（2分）
 

A. ???Welcome#?111#924.66
B. Welcome#111#924.66
C. Welcome#111#.66
D. Welcome???#?111#924.66

参考答案：
D'''


b='''24.	执行下列语句，输出的结果是（	）。	（2分）
 
x = 1
x = x + 2.5
print(x)

A.	1
B.	2
C.	3
D. 3.5

参考答案：
D'''


n='''25. 45 / 4的计算结果是（	）。	（2分）
A.	10
B.	11
C. 11.25
D. 12

参考答案：
C'''


m='''26.	假设s = "Welcome"，s.upper()结果是（	）。	（2分）
A.	welcome
B.	WELCOME
C.	Welcome

参考答案：
B'''

 

q1='''27.	编写Python程序，输出“Hello World”，要求将这两个单词分两行输出，以下错误的是（	）。
 

（2分）
 

A.	print("Hello\nWorld")

B.	print('Hello\nWorld')

C.	print('Hello World')

D.	print('Hello') print('World')

参考答案：
C'''


qq='''28.	“等于”比较运算符是（	）。	（2分）
A.	<>
B.	!=
C. ==
D. =

参考答案：
C'''
 
qw='''29.	下列程序的输出结果是（	）。
x = 1
def f1():
global x x = x + 2 print(x)
f1()
print(x)
 
（2分）
 

A.	1 3
B.	3 1
C.	程序有运行时错误，因为x未定义
D.	1 1
E.	3 3

参考答案：
E'''


qe='''30.	将x的值格式化为小数点后三位小数，使用（	）。	（2分）
A.	format(x, "5.3f")
B.	format("5.3f", x)
C.	format(x, "5.3%")
D.	format("3d", x)

参考答案：
A'''


qr='''31.	下列表达式计算结果为1的是（	）。	（2分） A. 2 % 1
B. 15 % 4
C. 25 % 5
D. 37 % 6

参考答案：
D'''


qt='''32.	对象5.6的类型是（	）。	（2分）
A.	int
B.	float
C.	str

参考答案：
B'''

 
qy='''33.	如下语句执行后，x的值是（	）。 x = 1
x *= x + 1
 

（2分）
 

A.	1
B.	2
C.	3
D.	4

参考答案：
 
B'''


qu='''34. 2 ** 3.0的计算结果是（	）。	（2分）
A.	9
B.	8
C. 9.0
D. 8.0

参考答案：
D'''


qi='''35.	表达式"Good " + 1 + 2 + 3的计算结果是（	）。	（2分）
A.	Good123
B.	Good6
C.	Good 123
D.	非法的表达式

参考答案：
D'''


qo='''36.	下列（	）语句的输出结果是smith\exam1\test.txt。	（2分）
A.	print("smith\exam1\test.txt")
B.	print("smith\\exam1\\test.txt")
C.	print("smith\"exam1\"test.txt")
D.	print("smith"\exam1"\test.txt")

参考答案：
B'''

 
qp='''37.	执行以下代码段后，y的值是（	）。 x = 0
y = 10 if x > 0 else -10
 

（2分）
 

A. -10
B.	0
C.	10
D.	20
E.	非法的表达式

参考答案：
A'''

 
qa='''38.	执行下面程序后，x的值是（	）。 a = 1
b = 3
c = 5
d = 4
if a < b:
if c < d:
x = 1
 

（2分）
 
else:
 

if a < c:
if b < d:
 




else:
 

else: x = 7
 

else: x = 6
 
x = 2

x = 3
 

A.	4
B.	1
C.	3
D.	2

参考答案：
D'''

 
qs='''39.	以下程序的输出结果是（	）。 number = 6
while number > 0:
number -= 3 print(number, end = ' ')
 

（2分）
 

A. 6 3 0
B. 6 3
C. 3 0
D. 3 0 -3
E. 0 -3

参考答案：
C'''

 
qd='''40.	下列程序的输出结果是（	）。 x = 1
def f1():
x = x + 2 print(x)
f1()
print(x)
 

（2分）
 

A.	1 3
B.	3 1
C.	程序有运行时错误，因为x未定义
D.	1 1
E.	3 3

参考答案：
C'''


qf='''41.	假设x的值为4、y的值为5，以下表达式的值为真（true）的是（	）。	（2分）
A.	not (x == 4)
B.	x != 4
C.	x == 5
D.	x != 5

参考答案：
D'''
 
qg='''42.	下列程序的输出结果是（	）。

def f1(x = 1, y =2): return x + y, x - y

x, y = f1(y = 2, x= 1) print(x, y)
 
（2分）
 

A.	1 3
B.	3 1
C.	程序有运行时错误，因为函数返回多个值
D. 3 -1
E. -1 3

参考答案：
D'''

 
qh='''43.	下列程序的输出结果是（	）。 def f1(x = 1, y =2):
x = x + y y += 1
print(x, y)
f1()
 

（2分）
 

A.	1 3
B.	3 1
C.	程序有运行时错误，因为x和y未定义
D.	1 1
E.	3 3

参考答案：
E'''


qj='''44.	range(5)返回序列（	）。	（2分）

A. 1,	2,	3,	4,	5
B. 0,	1,	2,	3,	4, 5
C. 1,	2,	3,	4	
D. 0,	1,	2,	3,	4

参考答案：
D'''

 

qk='''45.	对于下列函数：

def nPrint(message,n): while n > 0:
print(message, end = '') n -= 1
调用nPrint('a',4)，输出结果是（	）。
 

（2分）
 

A.	aaaaa
B.	aaaa
C.	aaa
D.	无效的函数调用
E.	无限循环

参考答案：
B'''
 
ql='''46.	以下程序的输出结果是（	）。
ch = 'F'
if ch >= 'A' and ch <= 'Z': print(ch)
 
（2分）
 

A.	F
B.	f
C.	无输出
D.	F f

参考答案：
A'''


qz='''47.	假设s = "Welcome"，type(s)结果是（	）。	（2分）
A.	<class 'int'>
B.	<class 'float'>
C.	<class 'str'>
D.	<class 'String'>

参考答案：
C'''

 

qx='''48.	假设x是一个字符变量，其值为'b'。语句print(chr(ord(x) + 1))的输出结果是（	）。
 

（2分）
 

A.	a
B.	b
C.	c
D.	d

参考答案：
C'''

 
qc='''49.	以下程序的输出结果是（	）。 x = 0
if x < 4:
x = x + 1 print(x)
 

（2分）
 

A.	0
B.	1
C.	2
D.	3

参考答案：
B'''


qv='''50.	random.random()的返回值是（	）。	（2分）
A.	一个浮点数i，0 < i < 1.0
B.	一个浮点数i，0 <= i< 1.0
C.	一个浮点数i，0 <= i<= 1.0
D.	一个浮点数i，0 < i < 2.0

参考答案：
 
B'''

 

qb='''51.	算法是一个计算过程，是程序设计的基础和精髓。一个有效的算法应该具有如下特点，其中错误的是（	）。
 

（2分）
 

A.	零个或多个输入及一个或多个输出
B.	无穷性
C.	可行性
D.	确定性

参考答案：
B'''

 
qn='''52.	执行下列语句，输出的结果是（	）。 x = 1
x = 2 * x + 1 print(x)
 

（2分）
 

A.	1
B.	2
C.	3
D.	4

参考答案：
C'''


qm='''53. 45 // 4的计算结果是（	）。	（2分）
A.	10
B.	11
C. 11.25
D. 12

参考答案：
B'''


w1='''54.	Python语言被称为高级程序设计语言，（	）。	（2分）
A.	因为它比低级语言功能强大
B.	因为它是编译型语言
C.	因为它是解释型语言
D.	因为它比低级语言更贴近人类的思维

参考答案：
D'''

 
wq='''55.	下列程序的输出结果是（	）。 def f1(x = 1, y = 2):
x = x + y y += 1
print(x, y)
f1(y = 2, x = 1)
 

（2分）
 

A.	1 3
B.	2 3
C.	程序有运行时错误，因为x和y未定义
 
D.	3 2
E.	3 3

参考答案：
E'''


ww='''56.	关于Python程序的执行过程，正确的是（	）。	（2分）
A.	由解释器一条语句一条语句地执行
B.	由编译器将源程序转化为机器语言，然后执行
C.	可以同时执行多条语句
D.	执行过的语句将不会再被执行

参考答案：
A'''

 
we='''57.	假设income的值为4001，以下代码段的输出结果是（	）。 if income > 3000:
print("Income is greater than 3000") elif income > 4000:
print("Income is greater than 4000")
 

（2分）
 
A.	无输出
B.	Income is greater than 3000
C.	先输出Income is greater than 3000，接着输出Income is greater than 4000
D.	Income is greater than 4000
E.	先输出Income is greater than 4000，接着输出Income is greater than 3000

参考答案：
B'''

 
wr='''58.	对于下面不完整的程序： def f(number):
# 缺失的函数体 print(f(5))
缺失的函数体应该是（	）。
 

（2分）
 

A.	return "number"
B.	print(number)
C.	print("number")
D.	return number

参考答案：
D'''

 
wt='''59.	以下程序的输出结果是（	）。 y = 0
for i in range(0, 10): y += i
print(y)
 

（2分）
 
A.	10
B.	11
C.	12
D.	13
E.	45
 
参考答案：
E'''


wy='''60.	给定|x-2|≤4，以下表达式正确的是（	）。	（2分） A. x - 2 <= 4 and x - 2 >= 4
B. x - 2 <= 4 and x - 2 > -4
C. x - 2 <= 4 and x - 2 >= -4
D. x - 2 <=4 or x - 2 >= -4

参考答案：
C'''

 
wu='''61.	下列程序的输出结果是（	）。 x = 1
def f1():
x = 3 print(x)
f1()
print(x)
 

（2分）
 

A.	1 3
B.	3 1
C.	程序有运行时错误，因为x未定义
D.	1 1
E.	3 3

参考答案：
B'''


wi='''62.	若一个函数没有返回值，默认情况下，该函数返回（	）。	（2分）
A.	None
B.	int
C.	double
D.	public
E.	null

参考答案：
A'''


wo='''63.	Python的行注释以（	）开头。	（2分）
A.	//
B.	/*
C.	#
D.	$$

参考答案：
C'''

 
wp='''64.	对于以下程序： total = 0
for d in range(0,10, 0.1):
 

（2分）
 
total += total + d
（	）是正确的。

A.	程序有语法错误，因为range函数不能有三个参数
B.	程序有语法错误，因为range函数的参数必须是整数
C.	程序无限循环运行
D.	程序运行正常

参考答案：
B'''


wa='''65.	time.time()的返回值是（	）。	（2分）
A.	当前时间
B.	以毫秒为单位的当前时间
C.	从午夜开始以毫秒为单位的当前时间
D.	从1970年1月1日午夜开始以毫秒为单位的当前时间
E.	从格林威治标准时间（GMT）1970年1月1日午夜开始以毫秒为单位的当前时间（UNIX时间）

参考答案：
E'''


ws='''66.	（	）函数立即终止程序。	（2分）
A.	sys.terminate()
B.	sys.halt()
C.	sys.exit()
D.	sys.stop()

参考答案：
C'''

 
wd='''67.	以下（	）程序输出“Welcome to Python”10次。 A:
for count in range(1, 10): print("Welcome to Python")
B:
for count in range(0, 10): print("Welcome to Python")
C:
for count in range(1, 11): print("Welcome to Python")

D:
for count in range(1, 12): print("Welcome to Python")
 

（2分）
 

A.	BD
B.	ABC
C.	AC
D.	BC
E.	AB

参考答案：
D'''
 
wf='''68.	以下程序的输出结果是（	）。
total = 0
item = 0
while item < 5:
item += 1 total += item
if total > 4: break print(total)
 
（2分）
 

A.	5
B.	6
C.	7
D.	8

参考答案：
B'''

 

wg='''69.	若年龄（age）小于16岁，显示“Cannot get a driver's license”；若年龄
（age）大于或等于16岁，显示“Can get a driver's license”，以下代码段正确的是（	）。

I:
if age < 16:
print("Cannot get a driver's license") if age >= 16:
print("Can get a driver's license")
II:
if age < 16:
print("Cannot get a driver's license")
 

（2分）
 
else:
print("Can get a driver's license")

III:
if age < 16:
print("Cannot get a driver's license") elif age >= 16:
print("Can get a driver's license")
IV:
if age < 16:
print("Cannot get a driver's license") elif age == 16:
print("Can get a driver's license") elif age > 16:
print("Can get a driver's license")

A.	I和II
B.	II和III
C.	I、II和III
D.	III和IV
E.	以上都是

参考答案：
E'''


wh='''70.	一个函数（	）。	（2分）
A.	必须至少有一个参数
B.	可以没有参数
C.	必须有一个return语句返回一个值
D.	必须有一个return语句返回一个值
 
参考答案：
B'''

 
wj='''71.	以下程序输出“Welcometo Python”（	）次。 count = 0
while count <10:
print("Welcome to Python") count += 1
 

（2分）
 

A.	8
B.	9
C.	10
D.	11
E.	0

参考答案：
C'''

 

wk='''72.	下列表达式的计算结果是（	）。 eval("1 + 3 * 2")
 

（2分）
 
A. "1 + 3 * 2"
B. 7
C. 8
D. "1 + 6"

参考答案：
B'''

 
wl='''73.	以下程序，print语句执行了（	）次。 for i in range(10):
for j in range(i):
print(i * j)
 

（2分）
 

A. 100
B.	20
C.	10
D.	45

参考答案：
D'''

 

wz='''74.	下列程序的输出结果是（	）。
number1, number2,number3 = eval(input("Enter three numbers: ")) # Compute average
average = (number1+ number2 + number3) / 3

# Display result print(average)

程序运行时，输入（↙表示回车）： 1, 2, 3↙
 

（2分）
 

A. 1.0
B. 2.0
 
C. 3.0
D. 4.0

参考答案：
B'''

 
wx='''75.	如下语句执行后，x的值是（	）。 x = 2
y = 1
x *= y + 1
 

（2分）
 

A.	1
B.	2
C.	3
D.	4

参考答案：
D'''


wc='''76.	若半径是正数，下面（	）代码段输出一个圆的面积。	（2分）
A.	if radius != 0:
print(radius *radius * 3.14159)
B.	if radius >= 0:
print(radius *radius * 3.14159)
C.	if radius > 0:
print(radius *radius * 3.14159)
D.	if radius <= 0:
print(radius *radius * 3.14159)

参考答案：
C'''

 
wv='''77.	执行下列语句，输出的结果是（	）。 x = 1
y = x = x + 1 print(y)
 

（2分）
 

A.	0
B.	1
C.	2
D.	3

参考答案：
C'''

 

wb='''78.	下列程序的输出结果是（	）。

print("Enter three numbers: ") number1 = eval(input()) number2 = eval(input()) number3 = eval(input())
# Compute average
average = (number1+ number2 + number3) / 3

# Display result print(average)
 

（2分）
 
程序运行时，输入（↙表示回车）： 1 2 3↙

A. 1.0
B. 2.0
C. 3.0
D. 4.0
E.	输入数据时，程序发生运行时错误

参考答案：
E'''

 

wn='''79.	对于下列函数：

def nPrint(message,n): while n > 0:
print(message, end = '') n -= 1
调用nPrint("A message", k)后，k的值是（	）。 k = 2
nPrint("A message", k)
 

（2分）
 

A.	0
B.	1
C.	2
D.	3

参考答案：
C'''

 

wm='''80.	能实现下面功能的语句是（	）。
接收用户输入的一个整数。如果输入的是偶数，则输出“True”，否则输出 “False”。
 

（2分）
 

A.	print(not bool(input() % 2))
B.	print(int(input()) % 2 != 0)
C.	print(int(input()) % 2 == 1)
D.	print(not bool(int(input()) % 2))

参考答案：
D'''


e1='''81.	假设s = "Welcome"，s.lower()结果是（	）。	（2分）
A.	welcome
B.	WELCOME
C.	Welcome

参考答案：
A'''


eq='''82.	下列函数头，正确的是（	）。	（2分）
A.	def f(a = 1, b):
B.	def f(a = 1, b, c = 2):
C. def f(a = 1, b =1, c = 2):
D. def f(a = 1, b =1, c = 2, d):
 
参考答案：
C'''

 
ew='''83.	对于下列函数，错误的函数调用是（	）。 def foo(arg1, arg2 = 'test', arg3 = 100):
print(arg1, arg2, arg3)
 

（2分）
 

A.	foo('where','what')
B.	foo(arg1 = 'where', arg2 = 'what')
C.	foo(arg = 'where')
D.	foo('where')

参考答案：
C'''


ee='''84.	给定|x-2|≥4，以下表达式正确的是（	）。	（2分） A. x - 2 >= 4 and x - 2 <= -4
B. x - 2 >= 4 or x - 2 <= -4
C. x - 2 >= 4 and x - 2 < -4
D. x - 2 >=4 or x - 2 < -4

参考答案：
B'''

 

er='''85.	下列代码段的输出结果是（	）（注意：?表示空格）。
print(format("Welcome",">10s"), end = '#')
print(format(111,"<4d"), end = '#') print(format(924.656, ">10.2f"))
 

（2分）
 

A. ???Welcome#?111#924.66
B. ???Welcome#?111#????924.66
C. ???Welcome#111?#????924.66
D. Welcome???#111?#????924.66

参考答案：
C'''

 
et='''86.	下列Python程序，正确的是（	）。 A.
print("Programmingis fun") print("Python is fun")
B.
print("Programmingis fun") print("Pythonis fun")

C.
print("Programmingis fun) print("Pythonis fun")
 

（2分）
 

D.
print("Programmingis fun")
print("Pythonis fun")

A.	A
B.	B
 
C.	C
D.	D

参考答案：
B'''

 
ey='''87.	以下程序，print语句执行了（	）次。 for i in range(10):
for j in range(10):
print(i * j)
 

（2分）
 

A. 100
B.	20
C.	10
D.	45

参考答案：
A'''

 
eu='''88.	执行下列语句，输出的结果是（	）。 x = 7.0
y = 5 print(x % y)
 

（2分）
 

A. 2.0
B. 1.0
C. 2
D. 1

参考答案：
A'''

 

ei='''89.	对于以下程序：

even = False if even:
print("It is even!")
（	）是正确的。
 

（2分）
 

A.	程序正常运行，显示It is even!
B.	程序正常运行，但不显示任何信息
C.	程序有错误，if even:应该替换成if even ==True:
D.	程序有错误，if even:应该替换成if even =True:

参考答案：
B'''

 

eo='''90.	每次调用一个函数时,系统将参数和局部变量存储在一个称为
（	）的内存区域中，该内存区域以后进先出的形式存储元素。
 

（2分）
 

A.	堆
B.	数组
C.	存储区
D.	栈

参考答案：
 
D'''

 
ep='''91.	以下程序的输出结果是（	）。 temperature = 50
if temperature>= 100: print("too hot")
elif temperature<= 40: print("too cold")
 

（2分）
 
else:
print("just right")

A.	too hot
B.	too cold
C.	just right
D.	too hot too cold just right

参考答案：
C'''

 
ea='''92.	下列程序的输出结果是（	）。 x = 1
def f1():
y = x + 2
print(y, end = ' ')

f1()
print(x)
 

（2分）
 

A.	1 3
B.	3 1
C.	程序有运行时错误，因为x未定义
D.	1 1
E.	3 3

参考答案：
B'''


es='''93.	函数的参数总是出现在（	）中。	（2分）
A.	方括号
B.	双引号
C.	圆括号
D.	花括号

参考答案：
C'''

 
ed='''94.	下列程序的输出结果是（	）。 def f1(x = 1, y =2):
x = x + y y += 1
print(x, y)
f1(2, 1)
 

（2分）
 

A.	1 3
B.	2 3
C.	程序有运行时错误，因为x和y未定义
 
D.	3 2
E.	3 3

参考答案：
D'''

 

ef='''95.	下列程序的输出结果是（	）。

print("Enter three numbers: ") number1 = eval(input()) number2 = eval(input()) number3 = eval(input())
# Compute average
average = (number1+ number2 + number3) / 3

# Display result print(average)

程序运行时，输入（↙表示回车）： 1↙
2↙
3↙
 

（2分）
 

A. 1.0
B. 2.0
C. 3.0
D. 4.0

参考答案：
B'''

 
eg='''96.	以下程序的输出结果是（	）。 isCorrect = False
print("Correct" if isCorrect else "Incorrect")
 

（2分）
 

A.	Correct
B.	Incorrect
C.	无输出
D.	Correct Incorrect

参考答案：
B'''

 
eh='''97.	下列Python程序，正确的是（	）。 I:
print("Programmingis fun") print("Python")
print("ComputerScience")
II:
print("Programmingis fun") print("Python")
print("ComputerScience")
 

（2分）
 

III:
print("Programmingis fun")
print("Python") print("ComputerScience")
 
IV:
print("Programmingis fun") print("Python") print("ComputerScience")

A.	I
B.	II
C.	III
D.	IV

参考答案：
D'''


ej='''98.	下列（	）是对算法的正确描述。	（2分）
A.	解决一个问题只有一种算法
B.	对于所有问题都可以找到最好的算法
C.	算法所包含的语句数量越少，算法越先进
D.	解决一个问题可以有多种算法

参考答案：
D'''


ek='''99.	函数头由（	）组成。	（2分）
A.	def关键字、函数名和冒号
B.	def关键字、函数名、参数表和冒号
C.	函数名和参数表
D.	函数名、参数表和冒号

参考答案：
B'''

 

el='''100. 以下（	）程序正确计算了“1/2 + 2/3 + 3/4 + ... +
99/100”的值。
A:
total = 0
for i in range(1,99): total += i / (i + 1)
print("Total is", total)
B:
total = 0
for i in range(1,100): total += i / (i + 1)
print("Total is", total)
C:
total = 0
for i in range(1.0,99.0): total += i / (i + 1)
print("Total is", total)
D:
total = 0
for i in range(1.0,100.0): total += i / (i + 1)
print("Total is", total)
 

（2分）
 

A.	BCD
B.	ABCD
 
C.	B
D.	CDE
E.	CD

参考答案：
C'''

 
ez='''101. 以下程序的输出结果是（	）。 number = 30
if number % 2 == 0: print(number, 'is even')
elif number % 3 == 0:
print(number, 'is multiple of 3')
 

（2分）
 
A.	30 is even
B.	程序出错
C.	30 is multiple of 3 D.
30 is even
30 is multiple of 3

参考答案：
A'''

 

ex='''102. 假设x的值为345.3546，format(x, "10.3f")结果是（	）（注意：b表示空格）。
 

（2分）
 

A. bb345.355
B. bbb345.355
C. bbbb345.355
D. bbb345.354
E. bbbb345.354

参考答案：
B'''


ec='''103. 2 + 2 ** 3 / 2的计算结果是（	）。	（2分）
A.	4
B.	6
C. 4.0
D. 6.0

参考答案：
D'''


ev='''104.	下面（	）是一个有效的标识符。	（2分）
A. $343
B.	9X
C.	import
D.	max_radius
E.	"red"

参考答案：
D'''
 
eb='''105.	以下程序的输出结果是（	）。

number = 25 isPrime = True i = 2
while i < number and isPrime: if number % i == 0:
isPrime = False i += 1
print("i is", i, "isPrime is", isPrime)
 
（2分）
 
A.	i is 5 isPrime is True
B.	i is 5 isPrime is False
C.	i is 6 isPrime is True
D.	i is 6 isPrime is False

参考答案：
D'''

 

eb='''106.	以下程序的输出结果是（	）。

x	=	1
y	=	-1
z	=	1
if	x	> 0:
if y > 0:
print("x > 0 and y >0")
 

（2分）
 
elif z > 0:
print("x < 0 and z > 0")

A.	x > 0 and y > 0
B.	x < 0 and z > 0
C.	x < 0 and z <0
D.	无输出

参考答案：
D'''


en='''107.	math.degrees(math.pi / 2)的返回值是（	）。	（2分） A. 0.0
B. 90.0
C. 45.0
D. 30.0

参考答案：
B'''

 

em='''108.	以下程序的输出结果是（	）。

x	=	1	
y	=	-1	
z	=	1	
if	x	>	0:
		if	y > 0:
print('AAA') elif z > 0:
print('BBB')
 

（2分）
 

A.	语法错误
B.	BBB
 
C.	无输出
D.	AAA

参考答案：
C'''


r1='''109.	假设number的值为4，下列语句错误的是（	）。	（2分）
A.	print(format(number, "2d"), format(number ** 1.5, "4.2d"))
B.	print(format(number, "2d"), format(number ** 1.5,"4.2f"))
C.	print(format(number, "2f"), format(number ** 1.5,"4.2f"))
D.	print(format(number, "2.1f"), format(number ** 1.5,"4.2f"))

参考答案：
A'''


rq='''110.	使用下列（	）函数读取一个字符串。	（2分）
A.	input("Enter a string")
B.	eval(input("Enter a string"))
C.	enter("Enter a string")
D.	eval(enter("Enter a string"))

参考答案：
A'''


rw='''111.	下列Python程序，正确的是（	）。	（2分）
A.	print("Hello, I'm Tom.")
B.	print('Hello, ' print 'World!')
C.	print('Hello, this's Tom.')
D.	Print('Hello, World!')

参考答案：
A'''


re='''112.	运算符+、*、and、or的优先级（从高到低）是（	）。	（2分）
A.	and、or、*、+
B.	*、+、or、and
C.	*、+、and、or
D.	or、and、*、+

参考答案：
C'''


rr='''113.	math.radians(30) * 6的返回值是（	）。	（2分） A. 0.0
B. 1.3434343
C. 3.141592653589793
D. 5.565656

参考答案：
C'''
 
rt='''114.	执行下列语句，输出的结果是（	）。
x, y = 1, 2
x, y = y, x print(x, y)
 
（2分）
 

A.	1 1
B.	2 2
C.	1 2
D.	2 1

参考答案：
D'''

 
ry='''115.	对于以下代码段： Code1:
if number % 2 == 0:
even = True
 

（2分）
 
else:
even = False

Code2:
even = number % 2== 0
（	）是正确的。

A.	Code 1有错误
B.	Code 2有错误
C.	Code 1和Code 2都有错误
D.	Code 1和Code 2都是正确的，但Code 2更好

参考答案：
D'''

 
ru='''116.	对于以下程序： even = False
if even = True:
print("It is even!")
（	）是正确的。
 

（2分）
 

A.	在行1（even = False），程序有语法错误
B.	在行2，程序有语法错误，if even = True:不是一个正确的条件，它应该替换成if even
== True:或if even:
C.	程序正常运行，但不显示任何信息
D.	程序正常运行，显示It is even!

参考答案：
B'''

 

ri='''117.	假设isPrime是一个布尔类型的变量，为了测试isPrime是否为真（true），下列（	）语句是正确且最佳的。
 

（2分）
 

A.	if isPrime = True:
B.	if isPrime == True:
C.	if isPrime:
D.	if not isPrime = False:
E.	if not isPrime == False:

参考答案：
 
C'''

 

ro='''118.	对于下列函数：

def nPrint(message,n): while n > 0:
print(message, end = '') n -= 1
调用nPrint(n = k, message = "A message")后，k的值是
（	）。
k = 2
nPrint(n = k,message = "A message")
 

（2分）
 

A.	0
B.	1
C.	2
D.	3

参考答案：
C'''

 
rp='''119.	以下程序的输出结果是（	）。 total = 0
item = 0
while item < 5:
item += 1 total += item
if total > 4: continue print(total)
 

（2分）
 

A.	15
B.	16
C.	17
D.	18

参考答案：
A'''

key_word=input("关键词：")
line=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,q1,qq,qw,qe,qr,qt,qy,qu,qi,qo,qp,qa,qs,qd,qf,qg,qh,qj,qk,ql,qz,qx,qc,qv,qb,qn,qm,w1,wq,ww,we,wr,wt,wy,wu,wi,wo,wp,wa,ws,wd,wf,wg,wh,wj,wk,wl,wz,wx,wc,wv,wb,wn,wm,e1,eq,ew,ee,er,et,ey,eu,ei,eo,ep,ea,es,ed,ef,eg,eh,ej,ek,el,ez,ex,ec,ev,eb,en,em,r1,rq,rw,re,rr,rt,ry,ru,ri,ro,rp]
for index,answer in enumerate(line):
    if key_word in answer:
        print(answer)
