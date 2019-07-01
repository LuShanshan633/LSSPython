#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
print("hello,world");
# print("请输入数字a：");
# a = input();
# print("请输入数字b：");
# b = input();
# print("a * b =",int(a)*int(b));
# print('b的长度',len(b));

### 字符串编码
# print('%2d-%02d' % (3, 1))
# print('%.2f' % 3.1415926)
# s1 = 72
# s2 = 85
# r = (s2-s1)/72*100
# print('%.1f' % r)

### 数组
studentsList = ['赵','钱','孙','李']
# print(studentsList)
# print(studentsList[0],studentsList[-1])
# print(len(studentsList))
# studentsList.append('周')
# print(studentsList)
# studentsList.insert(2,'吴')
# print(studentsList)
# studentsList.pop()
# print(studentsList)
# studentsList.pop(2)
# print(studentsList)
# studentsList[0] = '郑'
# print(studentsList)

# glas = [1,'ddd',studentsList]
# print(glas)

### 判断
# age = input('请输入年龄')

# if int(age) >= 60:
# 	print('已经退休啦')
# elif int(age) >= 18:
# 	print('已经成年啦')
# else:
# 	print('未成年')

# height = input('请输入身高')
# width = input('请输入体重')
# s =  (float(height)/100) ** 2
# print(float(height)/100)

# bmi = int(width)/s
# bmi = float('%.1f' % bmi)
# print(bmi)

# if bmi > 32:
# 	print('严重肥胖')	
# elif bmi >= 28:
# 	print('肥胖')
# elif bmi >= 25:
# 	print('过重')
# elif bmi >= 18.5:
# 	print('正常')
# else:
# 	print('过轻')
	
### 循环
# for name in studentsList:
# 	print(name)

# count = list(range(101))
# sum = 0
# for x in count:
# 	sum = sum + x

# 	if x % 2 > 0:
# 		continue
# 	if x > 50:
# 		break
# 	print(x)
# print(sum)

# # num = 0
# # n = 99
# # while n > 0:
# # 	num = n + num
# # 	n = n - 2

# # print(num)


# dic = {'a':1,'b':123,'c':423}
# print(dic['b'])

# n1 = 123
# print(hex(n1))


# def prix():
# 	print('22')

# prix()

# def my_abs(x):
# 	if x > 0:
# 		return x;
# 	else:
# 		return -x;

# print('绝对值：',my_abs(int(input('请输入数字'))))

# print(math.sqrt(2))


# def power(x,n):
# 	return x**n


# print(power(5,3));

# def enroll(name,gender,age = 4,city = 'changsha'):
# 	print('name:',name,'gender:',gender,'age:',age,'city:',city)


# enroll('ac','5',city = 'henan')

# def cals(*numbers):
# 	sum = 0
# 	for n in numbers:
# 		sum = sum + n
# 	return sum

# names = [3,1,23,5]
# print(cals(*names))

extra = {'city':'beinjing','job':'ios'}
# def person(name,age,**other):
# 	if 'city' in other :
# 		print('包含city')
# 		pass
# 	if 'job' in other :
# 		print('包含job')
# 		pass
# 	if 'id' in other:
# 		print('包含id')
# 		pass
# 	print('name=',name,'age=',age,'other=',other)
# print(person('hh',3,**extra))

# def personname(name,age,*,city,job):
# 	print(name,age,city,job)

# print(personname('hh',3,city = 'rr',job = 'ddd'))

# def product(*cheng):
# 	sum = 1
# 	for n in cheng:
# 		sum = sum * n
# 	return sum

# print(product(1,3,5,4,2))


# L = list(range(100))

# print(L[::3])

str = 'hello  '
# def trim(s):
# 	sum = ''
# 	for x in range(len(s)):
# 		if x < len(s):
# 			st = s[x:x+1]
# 			if st != ' ':
# 				sum = sum + st
# 	print(sum)

# trim(str)


def trim(s):
    if s[:1] != ' ' and s[-1:] != ' ':
        print(s + '1')
        return s
    elif s[:1] == ' ':
        print(s + '2')
        return trim(s[1:])
    else:
        print(s + '3')
        return trim(s[:-1])
if trim('hello  ') != 'hello':
    print('测试失败!1')
elif trim('  hello') != 'hello':
    print('测试失败!2')
elif trim('  hello  ') != 'hello':
    print('测试失败!3')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!4')
elif trim('') != '':
    print('测试失败!5')
elif trim('    ') != '':
    print('测试失败!6')
else:
    print('测试成功!') 	










