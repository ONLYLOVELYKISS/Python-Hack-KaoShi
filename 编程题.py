a="""21、实验2-5
【描述】
编写程序，读入一个在100和999之间的整数，然后输出按位逆序后的数。当输入的整数含有结尾的0时，输出不应带有前导的0。比如输入100，输出应该是1。
【输入】
在一行中给出一个在100和999之间的整数。
【输出】
在一行中输出按位逆序后的数。
【输入示例】
123
【输出示例】
321
【参考答案】
import math
a,b,c=eval(input())
d=a*math.pow((1+b/1200),c*12)
print(format(d,".2f"))"""

b="""5、实验2-6
【描述】
编写程序，根据火车的出发时间和到达时间计算整个旅途所用的时间。
【输入】
在一行中给出两个正整数，其间以逗号分隔，分别表示火车的出发时间和到达时间。每个时间的格式为两位小时数（00～23）和两位分钟数（00～59），假设出发和到达在同一天内。
【输出】
在一行中输出该旅途所用的时间，格式为“hh:mm”，其中hh为两位小时数、mm为两位分钟数。
【输入示例】
1201,1530
【输出示例】
03:29
【参考答案】
import math
a,b,c=eval(input())
d=a*math.pow((1+b/1200),c*12)
print(format(d,".2f"))"""

c="""27、实验2-8
【描述】
一只大象口渴了，要喝20升水才能解渴，但现在只有一个深h厘米，底面半径为r厘米的小圆桶（h和r都是整数）。问大象至少要喝多少桶水才会解渴。
【输入】
一行中给出小圆桶的深h和底面半径r，其间以逗号分隔，单位厘米。
【输出】
一行中输出大象至少要喝多少桶水。（整数）
【输入示例】
23,11
【输出示例】
3
【提示】
π取math.pi。
1升等于1000立方厘米。向上取整可以使用数学函数ceil(x)。例如，ceil(2.1)，取整结果为3.0；ceil(-2.1)，取整结果为-2.0。
【参考答案】
import math
a,b,c=eval(input())
d=a*math.pow((1+b/1200),c*12)
print(format(d,".2f"))"""


d="""1、实验2-9
【描述】
编写程序，读取投资总额、年利率和年数，然后使用如下公式计算未来投资金额。
 
【输入】
一行中给出投资总额、年利率和年数，其间以逗号分隔。
【输出】
一行中输出未来投资金额，结果保留2位小数。
【输入示例】
1000,3.25,1
【输出示例】
1032.99
【提示】
可以使用数学函数pow(a, b)方法来计算a的b次幂。
年利率转换为月利率，年数转换为月数。
【参考答案】
import math
a,b,c=eval(input())
d=a*math.pow((1+b/1200),c*12)
print(format(d,".2f"))"""

e="""13、实验2-10
【描述】
假设你每月往银行账户中1000元钱，银行的年利率为5%，月利率是0.05/12=0.00417。
第一个月后，你的账户余额为：1000 * ( 1 + 0.00417) = 1004.17 元
第二个月后，账户上钱就变成：(1000 + 1004.17) * ( 1 + 0.00417) = 2012.53 元
以此类推，第六个月后，你的账户上有多少余额？
【输入】
没有输入。
【输出】
第六个月后，账户上的余额数，精确到小数点后2位。
【参考答案】
l=1+0.00417
x = 1000 *l
x = (x + 1000) * l
x = (x + 1000) *l
x = (x + 1000) *l
x = (x + 1000) *l
x = (x + 1000) *l
print('%.2f'%(x))
'''
L=1+0.00417
m=1000*L
i=0
while i<5:
    m=(1000+m)*L
    i+=1
print("%.2f"%(m))

L=1+0.00417
m=1000*L
for i in range(5):
    m=(1000+m)*L
print("%.2f"%(m))'''"""

f="""1、实验3-2
【描述】
编写程序，输入一个整数，检查它是否能被5和6整除，是否被5或6整除，是否被5或6整除但是不能同时被它们整除。
【输入】
一行中给出一个整数。
【输出】
分行输出检查结果，见【输出示例】。
【输入示例】
10
【输出示例】
10 divisible by 5 and 6? False
10 divisible by 5 or 6? True
10 divisible by 5 or 6, but not both? True
【参考答案】
a=eval(input())
print(a,"divisible by 5 and 6?",a%5==0 and a%6==0)
print(a,"divisible by 5 or 6?",a%5==0 or a%6==0)
#print(a,"divisible by 5 or 6,but not both?",(a%5==0 or a%6==0) and a%30!=0)
#print(a,"divisible by 5 or 6,but not both?",a%5!=0 and a%6==0 or a%5==0 and a%6!=0)
print(a,"divisible by 5 or 6,but not both?",(a%5==0 and a%6==0) and not(a%5==0 or a%6==0))"""

g="""14、实验3-4
【描述】
编写程序，求三个整数中的中间数。
【输入】
一行中给出三个整数，其间以逗号分隔。
【输出】
一行中输出三个整数中大小位于中间的数。
【输入示例】
12,6,18
【输出示例】
12
【参考答案】
a,b,c=eval(input())
if a<b:
    a,b=b,a
if a<c:
    a,c=c,a
if b<c:
    b,c=c,b
print(b)
'''
a,b,c=eval(input())
if a<=b<=c or c<=b<=a:
    print(b)
elif b<=a<=c or c<=a<=b:
    print(a)
elif a<=c<=b or b<=c<=a:
    print(c)

a,b,c=eval(input())
if a<b<c:
    print(b)
if a<c<b:
    print(c)
if b<a<c:
    print(a)
if b<c<a:
    print(c)
if c<a<b:
    print(a)
if c<b<a:
    print(b)
if a==b or a==c:
    print(a)
elif b==c:
    print(b)
'''"""

h="""15、实验3-5
【描述】
你买了一箱n个苹果，很不幸的是买完时箱子里混进了一条虫子。虫子每x小时能吃掉一个苹果，假设虫子在吃完一个苹果之前不会吃另一个，那么经过y小时你还有多少个完整的苹果？
【输入】
一行中给出n，x和y（均为整数），其间以逗号间隔。
【输出】
一行中输出剩下的苹果数（完整的苹果数）。
【输入示例】
10,4,9
【输出示例】
7
【参考答案】
n,x,y=eval(input())
m=int(n-y/x)
if m>0 :
    print(m)
else :
    print(0)"""

i="""12、实验3-8
【描述】
编写程序，求解如下的2×2的线性方程：
 
注意：若ad-bc为0，方程无解。
【输入】
一行中给出给出a、b、c、d、e、f的值，其间以逗号分隔。
【输出】
输出方程的解，其间以空格分隔。结果保留2位小数。
如果方程无解，则输出“The equation has no solution”。
【输入示例】
9.0,4.0,3.0,-5.0,-6.0,-21.0
【输出示例】
-2.00 3.00
【参考答案】
a,b,c,d,e,f=eval(input())
m=a*d-b*c
if m==0:
    print("The equation has no solution")
else:
    x=(e*d-b*f)/m
    y=(a*f-e*c)/m
    print("%.2f %.2f"%(x,y))"""

j="""10、实验3-6
【描述】
编写一个简单计算器程序，可根据输入的运算符，对2个整数进行加、减、乘、除或求余运算。题目保证输入和输出均不超过整型范围。
【输入】
在一行中依次给出操作数1、运算符、操作数2，其间以空格分隔。操作数的数据类型为整型，且保证除法和求余的分母非零。
【输出】
 当运算符为+、-、*、/、%时，在一行中输出相应的运算结果。若输入是非法符号（即除了加、减、乘、除和求余五种运算符以外的其他符号）则输出“ERROR”。
【输入示例】
-7 / 2
【输出示例】
-4
【参考答案】
line=input().split()
a=eval(line[0])
op=line[1]
b=eval(line[2])
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)    
elif op=="*":
    print(a*b)
elif op=="/":
    print(a//b)
elif op=="%":
    print(a%b)
else :
    print("ERROR") """

k="""23、实验3-7
【描述】
UTC是世界协调时，BJT是北京时间，UTC时间相当于BJT减去8。编写程序，读入一个整数，表示BJT的时和分。整数的个位和十位表示分，百位和千位表示小时。如果小时小于10，则没有千位部分；如果小时是0，则没有百位部分；如果分小于10分，需要保留十位上的0。如1124表示11点24分，而905表示9点5分，36表示0点36分，7表示0点7分。
有效的输入范围是0到2359，即不可能是0到2359以外的数据。
输出这个时间对应的UTC时间，输出的格式和输入的相同，即输出一个整数，表示UTC的时和分。整数的个位和十位表示分，百位和千位表示小时。如果小时小于10，则没有千位部分；如果小时是0，则没有百位部分；如果分小于10分，需要保留十位上的0。
【输入】
一行中给出一个整数，表示BJT的时和分。整数的个位和十位表示分，百位和千位表示小时。如果小时小于10，则没有千位部分；如果小时是0，则没有百位部分；如果分小于10分，需要保留十位上的0。
【输出】
一行中输出一个整数，表示UTC的时和分。整数的个位和十位表示分，百位和千位表示小时。如果小时小于10，则没有千位部分；如果小时是0，则没有百位部分；如果分小于10分，需要保留十位上的0。
【输入示例】
903
【输出示例】
103
【提示】
要小心跨日的换算。
【参考答案】
b=eval(input())
h=b//100
m=b%100
u=h-8
if u<0:
    u=u+24
if u==0:
    print(m)
else:
    print("%d%02d"%(u,m))"""

l="""20、实验4-2
【描述】
编写程序，输入若干个整数，如果输入0，输入即终止。判定读入的整数中有多少个正整数、多少个负整数，并计算这些整数的总和和平均值（0不计算在内）。平均值结果保留2位小数。
【输入】
一行中给出若干个整数，其间以空格分隔。如果输入0，输入即终止。
【输出】
分行输出这些整数中的正整数个数、负整数个数、总和、平均值（0不计算在内，结果保留2位小数）。
若只输入0，则输出：No input。
【输入示例】
-1 -2 -3 -4 -5 6 7 8 9 0
【输出示例】
4
5
15
1.67
【参考答案】
line=input().split()
z=0
f=0
s=0
i=0
n=len(line)
while i<n:
    x=eval(line[i])
    if x>0:
        z+=1
    elif x<0:
        f+=1
    else:
        break
    s+=x
    i+=1
if i==0:
    print("No input")
else:
    print(z)
    print(f)
    print(s)
    print(format(s/i,".2f"))
'''
line=input().split()
z=0
f=0
s=0
n=len(line)
for i in range(n):
    x=eval(line[i])
    if x>0:
        z+=1
    elif x<0:
        f+=1
    else:
        break
    s+=x
if i==0:
    print("No input")
else:
    print(z)
    print(f)
    print(s)
    print(format(s/i,".2f"))"""


m="""3、实验4-4
【描述】
编写程序，计算序列 1 - 1/4 + 1/7 - 1/10 + ... 的前n项之和。
【输入】
一行中给出一个正整数n。
【输出】
一行中按照“sum = S”的格式输出部分和的值S，精确到小数点后3位。题目保证计算结果不超过双精度范围。
【输入示例】
10
【输出示例】
sum = 0.819
【参考答案】
k=eval(input())
i=0
s=0
f=-1
while i<k:
    f=-f
    i+=1
    s+=f/(3*i-2)
print("sum = %.3f"%(s))
'''
k=eval(input())
s=0
f=-1
for i in range(1,k+1):
    f=-f
    s+=f/(3*i-2)
print("sum = %.3f"%(s))"""


n="""18、实验5-3
【描述】
有形如AB×C+A=y的方程，其中ABC均可以取0～9的数字，y由输入给出，求可以使方程成立的ABC各是多少。ABC可以相同，但A不可为0。若答案不唯一，只输出首先匹配的答案。若不存在匹配的答案，则输出“No solution”。
以A=1，B=1，C=1为例，上式变为11*1+1=12，所以y=12时，A=B=C=1是使方程成立的一个解。
【输入】
y（y≤900）
【输出】
依次输出A、B、C，其间以空格分隔。
【输入示例】
12
【输出示例】
1 1 1
【参考答案】
y=int(input())
a=1
f=False
while a<=9:
    b=0
    while b<=9:
        c=0
        while c<=9:
            if (a*10+b)*c+a==y:
                print(a,b,c)
                f=True
                break
            c+=1
        if f:
            break
        b+=1
    if f:
        break
    a+=1
if not f:
    print("No solution")
'''
y=int(input())
f=False
for a in range(1,10):
    for b in range(10):
        for c in range(10):
            if (a*10+b)*c+a==y:
                print(a,b,c)
                f=True
                break
        if f:
            break
    if f:
        break
if not f:
    print("No solution")'''"""

o="""19、实验5-5
【描述】
编写程序，输入若干个整数，找出它们的最大数，然后计算该数的出现次数。假设输入是以0结束的。
【输入】
一行中给出若干个整数，其间以空格间隔，最后以0结尾。
【输出】
一行中输出它们的最大数以及最大数出现次数，其间以空格间隔。
若只输入0，则输出：No input。
【输入示例】
3 5 2 5 5 5 0
【输出示例】
5 4
【参考答案】
'''line=input().split()
n=len(line)
max1=eval(line[0])
i=0
while i<n:
    x=eval(line[i])
    if x==0:
        break
    if x>max1:
        max1=x
    i+=1
if i==0:
    print("No input")
else:
    c=0
    while i<n:
        x=eval(line[i])
        if x==max1:
            c+=1
        c+=1
    print(max1,c)'''
line=input().split()
n=len(line)
max1=eval(line[0])
for i in range(n):
    x=eval(line[i])
    if x==0:
        break
    if x>max1:
        max1=x
if i==0:
    print("No input")
else: 
    c=0
    for i in range(n):
        x=eval(line[i])
        if x==max1:
            c+=1
    print(max1,c)"""

p="""26、实验6-2
【描述】
求一个整数各位数字之和。定义函数：def sumDigits(n)，该函数返回一个整数各位数字之和。
编写一个main函数，输入一个整数，调用sumDigits函数，显示该整数各位数字之和。
【输入】
一行中给出一个整数。
【输出】
一行中输出该整数各位数字之和。
【输入示例】
3456
【输出示例】
18
【参考答案】
def sumDigits(n):
    '''s=0
    while n!=0:
        s+=n%10
        n//=10
    return s'''
    n=str(n)
    s=0
    for x in n:
        s+=eval(x)
    return s"""

q="""4、实验6-3
【描述】
求一个整数的逆序数。定义函数：def reverse(n)，该函数返回一个整数的逆序数。
编写一个main函数，输入一个整数，调用reverse函数，显示该整数的逆序数。
【输入】
一行中给出一个整数。
【输出】
一行中输出该整数的逆序数。
【输入示例】
-123
【输出示例】
-321
【参考答案】
def reverse(n): 
    if n>=0:
        f=1
    else:
        f=-1
    '''n=abs(n)
    s=0
    while n!=0:
        m=n%10
        s=s*10+m
        n//=10
    return f*s'''
    n=str(abs(n))
    s=n[::-1]
    return f*eval(s)"""

r="""24、实验6-4
【描述】
输入一个整数，判断它是否是回文整数。如果一个整数的逆序数和原数一样，这个整数就称为回文整数
定义函数：def isPalindrome(n)，如果n是回文数，返回True，否则返回False。
编写一个main函数，输入一个整数，调用isPalindrome函数，判断该整数是否为回文整数。如果该整数是回文数，输出true，否则输出false。
【输入】
一行中给出一个整数。
【输出】
如果该整数是回文数，输出True，否则输出False。
【输入示例】
616
【输出示例】
True
【参考答案】
def isPalindrome(n):
    s=str(n) 
    return s==s[::-1]"""

s="""25、实验6-8
【描述】
定义sum函数，返回若干个整数的和，体会函数默认参数的使用。
 【输入】
没有输入。
【输出】
100
106
16
36
【提示】
根据sum函数调用时实参的使用和结果的输出，推测sum函数的定义。
【参考答案】
def sum(a=0,b=100,c=0):
    return a+b+c"""

t="""22、实验7-1
【描述】
已知f(n, 0) = 1, f(n, n) = 1
当n>m>0时，f(n, m) = f(n-1, m-1) + f(n-1, m)
求f(a, b)的值。
【输入】
多行输入，每一行输入两个正整数a、b（1≤b≤a≤10)），a、b以空格分隔。
【输出】
每一行输出f(a, b)值
【输入示例】
2 2
3 2
【输出示例】
1
3
【参考答案】
def f(n,m):
    if m==0 or m==n:
        return 1
    else:
        return f(n-1,m-1)+f(n-1,m)
def main():
    for x in iter(input,""):
        line=x.split()
        n=eval(line[0])
        m=eval(line[1])
        print(f(n,m))"""

u="""16、实验7-2
【描述】
按如下公式：
 
求出数列的前n项（n≤20）并输出，要求每行输出5项。定义和调用函数：def sequence(n)，计算数列第n项的值。
【输入】
输入一个正整数n。
【输出】
输出数列的前n项。每行输出5项。每项宽度为6。
【输入示例】
20
【输出示例】
     0     1     2     3     6
    11    20    37    68   125
   230   423   778  1431  2632
  4841  8904 16377 30122 55403
【参考答案】
def y(n):
    if n<=2:
        return n
    else:
        return y(n-1)+y(n-2)+y(n-3)
def main():
    n=eval(input())
    if n>2:
        for i in range(n):
            print(format(y(i),"6d"),end='')
            if (i+1)%5==0:
                print()
    else:
        print("%6d"%y(n))
main()"""

v="""8、实验7-3
【描述】
编写程序，计算Hermite多项式值。Hermite多项式定义如下：            
 
【输入】
从键盘随机输入一个非负整数和一个实数，作为n和x的值。
【输出】
Hn(x)的值，精确到小数点后2位。
【输入示例】
0 1.5
【输出示例】
1.00
【参考答案】
def Hn(n,x):
    if n==0:
        return 1
    elif n==1:
        return 2*x
    elif n>1:
        return 2*x*Hn(n-1,x)-2*(n-1)*Hn(n-2,x)
def main():
    line=input().split()
    n=eval(line[0])
    x=eval(line[1])
    print("%.2f"%(Hn(n,x)))
main()"""

w="""6、实验7-4
【描述】
编写程序，计算Ackerman函数值。Ackerman函数定义如下：
 
【输入】
从键盘随机输入两个非负整数，分别作为m和n的值。
【输出】
Ack(m,n)的值。
【输入示例】
2 3
【输出示例】
9
【参考答案】
def main():
    line=input().split()
    m=eval(line[0])
    n=eval(line[1])
    print(a(m,n))
def a(m,n):
    if m==0:
        s=n+1
    elif n==0:
        s=a(m-1,1)
    elif m>0 and n>0:
        s=a(m-1,a(m,n-1))
    return s
main()"""

x="""7、实验7-5
【描述】
编写程序，求最大公约数。
要求定义和调用递归函数：def gcd(m, n)，该函数返回m和n的最大公约数。
递归定义如下：
若m % n为0，那么gcd(m, n)的值为n；否则，gcd(m, n)的值为gcd(n, m % n)。
【输入】
输入两个数m、n（均为正整数），其间以空格分隔。
【输出】
输出m、n的最大公约数
【输入示例】
10 15
【输出示例】
5
【参考答案】
def gcd(m,n):
    if m%n==0:
        return n
    else:
        return gcd(n,m%n)"""

y="""2、实验7-7
【描述】
对于任意一个正整数，如果是奇数，则乘3加1，如果是偶数，则除以2，得到的结果再按照上述规则重复处理，最终总能够得到1。例如，假定初始正整数为5，计算过程分别为16、8、4、2、1。要求定义和调用递归函数：def guess(n)，输出计算过程。
【输入】
输入一个正整数。
【输出】
从输入整数到1的步骤，每一步为一行，每一步中描述计算过程，最后一行输出“End”。如果输入为1，直接输出“End”。
【输入示例】
5
【输出示例】
5*3+1=16
16/2=8
8/2=4
4/2=2
2/2=1
End
【参考答案】
def g(n):
    if n==1:
        print("End")
    elif n%2==0:
        print("%d/2=%d"%(n,n//2))
        return g(n//2)
    elif n%2==1:
        print("%d*3+1=%d"%(n,n*3+1))
        return g(n*3+1)
def main():
    n=eval(input())
    g(n)
main()"""

z="""7. 【描述】 求一个整数的逆序数。定义函数：def reverse(n)，该函数返回一个整数的逆 序数。 编写一个main函数，输入一个整数，调用reverse函数，显示该整数的逆序数。 
【输入】 一行中给出一个整数。 
【输出】 一行中输出该整数的逆序数。 
【输入示例】 -123
【输出示例】 -321
【参考答案】
def reverse(n): 
sign = 1
result = 0 
if n < 0:
n = -n
sign = -1
while n != 0:
remainder = n % 10
result = result * 10 + remainder
n //= 10
return sign * result
def main():
value = eval(input())
print(reverse(value))
main()"""

aa="""11. 【描述】 编写程序，求解如下的2×2的线性方程： 注意：若ad-bc为0，方程无解.
【输入】 一行中给出给出a、b、c、d、e、f的值，其间以逗号分隔。
【输出】 输出方程的解，其间以空格分隔。结果保留2位小数。 如果方程无解，则输出“The equation has no solution”。
【输入示例】 9.0,4.0,3.0,-5.0,-6.0,-21.0
【输出示例】 -2.00 3.00
【参考答案】
a,b,c,d,e,f = eval(input())
if (a * d - b * c) != 0:
x = (e * d - b * f) / (a * d - b * c)
y = (a * f - e * c) / (a * d - b * c)
print(format(x, ".2f"), format(y, ".2f"))
else:
print("The equation has no solution")"""

key_word=input("关键词：")
line=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa]
for index,answer in enumerate(line):
    if key_word in answer:
        print(answer)
