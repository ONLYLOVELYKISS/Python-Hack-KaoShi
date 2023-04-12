a='''1.下列程序的输出结果是	（注意：不要有任何多余的空格）。
def f(x, y):
	return x + y, x - y, x * y, x / y

t1, t2, t3, t4 = f(9, 5)
print(t1, t2, t3,t4)
 参考答案：
14 4 45 1.8'''

 
b='''2.以下程序的输出结果是	 。
x = 15;
while x > 10 and x < 50: 
	x += 1
	if x // 3:
		x+=1
		break
 	else: 
	continue
print(x)
 参考答案：
17'''

 
c='''3.下面程序的输出结果是	（注意：不要有任何多余的空格） 。 
def main():
	print(function(6, 2))

def function(i,num): 
	line = ""
	for j in range(1, i):
		line += str(num) + " "
		num *= 2
	return line
main()
参考答案：
2 4 8 16 32'''

 
d='''4.阅读下面代码，输出结果是	.
x = 5
if 8 % 4:
	x = x - 1 
elif 3 < 4 / 2:
	x = x - 2 
elif "t":
	x = x - 3
else:
	x = x - 4
print(x)
参考答案：
2'''

 

e='''5.阅读下面代码，x的值是	。

a=3
b=2
x=a if a > b else b
参考答案：
3'''


f='''6.下面代码段的输出结果是	（注意：不要有任何多余的空格）。 
print("hello", 5)
参考答案：
hello 5'''
 
g='''7.下面代码段的输出结果是	。 
print(5 // 4)
参考答案：
1'''

h='''8.print(chr(ord('B')))的输出结果是	 。
参考答案：
B'''

 
i='''9.阅读下面代码，输出结果是	。 
x = 100
if x > 10:
	x = x + 10
if x > 20:
	x = x + 50
print(x)
 参考答案：
160'''

 
j='''10.阅读下面代码，输出结果是	。 
if 6 < 5:
	print('one') 
elif 7 == 9:
	print('two') print("three")
参考答案：
three'''

 
k='''11.如果输入4、-1、6、9、8、3、0，以下程序的输出结果是	 。 
number = int(input('Enter an integer: '))
max = number
while number != 0:
	number = int(input('Enter an integer: ')) 
if number > max:
	max = number
print(max)
参考答案：
9'''

l='''12.round(6.5)的返回值是	 。
参考答案：
6'''
 
m='''13.阅读下面代码，输出结果是	。
a = 14 // 3
b = 4 > 5
print(a and b)
参考答案：
False'''

 
n='''14.以下代码段的输出结果是	。
number = 15292
if number == 0:
	print("0")
else:
	while number:
		right_digit = number % 10
		print(right_digit, end='')
		number //= 10
参考答案：
29251'''

 
o='''15.下面程序的输出结果是	 。 
def main():
	print(min(5, 6))

def min(n1, n2):
	smallest = n1
	if n2 < smallest:
		smallest = n2

main()
参考答案：
None'''

 

p='''16.在程序中空格             处填上恰当的成分，完成题目要求的功能。注意不需要任何空格。
从键盘输入20个整数，输出它们的和。
total = 0
for i in range(1,21): 
	a= eval(input())
	total =__________
print("Total=", total)
参考答案：
total+a'''

 

q='''17.下面代码段的输出结果是	。
print(format(57.467657, ".2f"))
参考答案：
57.47'''

r='''18.print("Chapter " + str(1))的输出结果是	 （注意：不要有任何多余的空格）。
参考答案：
Chapter 1'''

 

s='''19.下面代码段的输出结果是	。 
print((15 / 5) * 2)
参考答案：
6.0'''

key_word=input("关键词：")
line=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s]
for index,answer in enumerate(line):
    if key_word in answer:
        print(answer)

