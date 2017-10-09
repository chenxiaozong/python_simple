Python简明教程

- [项目一 外星人入侵](./alien_invasion/README.md)
- [项目二 数据可视化](matplot/md/readme.md)
- 项目三 PythonWeb



# 基础部分

----

<!-- MarkdownTOC -->

- [1.起步](#1%E8%B5%B7%E6%AD%A5)
- [2.字符串](#2%E5%AD%97%E7%AC%A6%E4%B8%B2)
    - [1.字符串](#1%E5%AD%97%E7%AC%A6%E4%B8%B2)
    - [2.数字运算](#2%E6%95%B0%E5%AD%97%E8%BF%90%E7%AE%97)
- [3.列表](#3%E5%88%97%E8%A1%A8)
- [4.元组](#4%E5%85%83%E7%BB%84)
    - [条件语句if](#%E6%9D%A1%E4%BB%B6%E8%AF%AD%E5%8F%A5if)
- [5.字典](#5%E5%AD%97%E5%85%B8)
- [6.用户输入和while](#6%E7%94%A8%E6%88%B7%E8%BE%93%E5%85%A5%E5%92%8Cwhile)
- [7.函数](#7%E5%87%BD%E6%95%B0)
    - [1.定义函数](#1%E5%AE%9A%E4%B9%89%E5%87%BD%E6%95%B0)
    - [2.定义有参函数](#2%E5%AE%9A%E4%B9%89%E6%9C%89%E5%8F%82%E5%87%BD%E6%95%B0)
    - [3.带返回值函数](#3%E5%B8%A6%E8%BF%94%E5%9B%9E%E5%80%BC%E5%87%BD%E6%95%B0)
    - [4.可变参函数](#4%E5%8F%AF%E5%8F%98%E5%8F%82%E5%87%BD%E6%95%B0)
    - [5.任意个数的参数](#5%E4%BB%BB%E6%84%8F%E4%B8%AA%E6%95%B0%E7%9A%84%E5%8F%82%E6%95%B0)
    - [6.使用任意数量的关键字实参](#6%E4%BD%BF%E7%94%A8%E4%BB%BB%E6%84%8F%E6%95%B0%E9%87%8F%E7%9A%84%E5%85%B3%E9%94%AE%E5%AD%97%E5%AE%9E%E5%8F%82)
    - [7.将函数存储在模块中](#7%E5%B0%86%E5%87%BD%E6%95%B0%E5%AD%98%E5%82%A8%E5%9C%A8%E6%A8%A1%E5%9D%97%E4%B8%AD)
    - [8.使用 as 给函数指定别名](#8%E4%BD%BF%E7%94%A8-as-%E7%BB%99%E5%87%BD%E6%95%B0%E6%8C%87%E5%AE%9A%E5%88%AB%E5%90%8D)
    - [9.导入模块中所有方法](#9%E5%AF%BC%E5%85%A5%E6%A8%A1%E5%9D%97%E4%B8%AD%E6%89%80%E6%9C%89%E6%96%B9%E6%B3%95)
- [9.类](#9%E7%B1%BB)
    - [9.1创建和使用类](#91%E5%88%9B%E5%BB%BA%E5%92%8C%E4%BD%BF%E7%94%A8%E7%B1%BB)
    - [9.2继承](#92%E7%BB%A7%E6%89%BF)
    - [9.3导入类](#93%E5%AF%BC%E5%85%A5%E7%B1%BB)
    - [9.4python 标准库](#94python-%E6%A0%87%E5%87%86%E5%BA%93)
    - [9.5类编码风格](#95%E7%B1%BB%E7%BC%96%E7%A0%81%E9%A3%8E%E6%A0%BC)
- [10.文件和异常](#10%E6%96%87%E4%BB%B6%E5%92%8C%E5%BC%82%E5%B8%B8)
    - [1.从文件中读取数据](#1%E4%BB%8E%E6%96%87%E4%BB%B6%E4%B8%AD%E8%AF%BB%E5%8F%96%E6%95%B0%E6%8D%AE)
        - [1.1 读取整个文件](#11-%E8%AF%BB%E5%8F%96%E6%95%B4%E4%B8%AA%E6%96%87%E4%BB%B6)
        - [1.2 逐行读取文件](#12-%E9%80%90%E8%A1%8C%E8%AF%BB%E5%8F%96%E6%96%87%E4%BB%B6)
        - [1.3 创建一个包含文件各行内容的列表](#13-%E5%88%9B%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%8C%85%E5%90%AB%E6%96%87%E4%BB%B6%E5%90%84%E8%A1%8C%E5%86%85%E5%AE%B9%E7%9A%84%E5%88%97%E8%A1%A8)
        - [1.4 使用文件中的数据](#14-%E4%BD%BF%E7%94%A8%E6%96%87%E4%BB%B6%E4%B8%AD%E7%9A%84%E6%95%B0%E6%8D%AE)
    - [2.写入文件](#2%E5%86%99%E5%85%A5%E6%96%87%E4%BB%B6)
        - [2.1 向空文件写入数据](#21-%E5%90%91%E7%A9%BA%E6%96%87%E4%BB%B6%E5%86%99%E5%85%A5%E6%95%B0%E6%8D%AE)
        - [2.2 写入多行文件](#22-%E5%86%99%E5%85%A5%E5%A4%9A%E8%A1%8C%E6%96%87%E4%BB%B6)
    - [3.异常](#3%E5%BC%82%E5%B8%B8)
        - [3.1处理ZeroDivisionError](#31%E5%A4%84%E7%90%86zerodivisionerror)
        - [3.2else代码块](#32else%E4%BB%A3%E7%A0%81%E5%9D%97)
        - [3.3 FileNotFoundError](#33-filenotfounderror)
    - [4.存储数据](#4%E5%AD%98%E5%82%A8%E6%95%B0%E6%8D%AE)
        - [1.使用json.dump\(\) 和 json.load\(\)](#1%E4%BD%BF%E7%94%A8jsondump-%E5%92%8C-jsonload)
        - [2.重构](#2%E9%87%8D%E6%9E%84)
- [11.测试代码](#11%E6%B5%8B%E8%AF%95%E4%BB%A3%E7%A0%81)
        - [1.测试函数](#1%E6%B5%8B%E8%AF%95%E5%87%BD%E6%95%B0)

<!-- /MarkdownTOC -->




# 1.起步

> mac 使用 brew 安装python3

- home brew 的安装 `https://brew.sh/`

- 安装homebrew `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"` 

- 使用brew 安装python3

```
brew help
brew update
brew -v
brew install python3 //安装python3 
brew upgrade python3 //升级python3
history
```


# 2.字符串

## 1.字符串

- 修改字符串大小写
```python3

name = "add lovelace"
print(name)
# title方法
print(name+"->"+name.title())


```

> 大小写转换

- string.upper()
- string.lower()


> 常用空白符: 

- 制表符(\t) 
- 换行符(\n)


> 去除空格

- 删除两侧空格
string.strip()
- 删除左侧空格
string.lstrip()
- 删除右侧空格
sting.rstrip()

## 2.数字运算

> 基本运算

- 加
- 减
- 乘
- 除
- 幂运算 `a**b`

# 3.列表

> 常用方法


方法| 作用
---|---
name.append() |列表末尾添加
name.count()   |记录
name.insert(index,elem) |指定位置添加
name.reverse() |倒序
name.clear() |清空
name.extend(list)|尾部添加list所有元素
name.pop(index)|弹出index索引对应的元素,index为空,弹出末尾元素
name.sort() |永久排序① 默认从小到大排序 ② 添加参数:name.sort(reverse=True) 从大到小排序
name.copy()| 返回name列表的一个映射,创建一个新的list ` li2 = li.copy()`
name.index(elm)| 返回指定元素的索引值
name.remove(elm)|按元素移除;如果有多个相同元素,移除第一的
sorted(name)|对name进行临时排序,不改变list中元素的位置
len(list) | 返回列表长度
tyep(list) | 返回元素类型
id(obj)| 返回obj对应id

> 获取列表最后一个元素

- `li[len(li)-1]`
- `li[-1] //获取最后一个元素,仅当li不为空时有效`



---
> 列表操作

- 遍历列表


```
In [46]: for elm in li:
    ...:     print(elm)
    ...:     
//结果
bb
cc
dd
bb
cc
dd


```

> 数字列表

- `range()`


```
//打印1到9的数字
In [62]: for value in range(1,10):#(1,10):左闭右开
    ...:     print(value)
    ...:     
1
2
3
4
5
6
7
8
9

```

- 使用list() 和range() 生成数字链表

```
>>> numbers = list(range(1,6))
>>> numbers
[1, 2, 3, 4, 5]
```

- 生成平方数
```
In [8]: square = []
   ...: for val in range(1,11):
   ...:     print(val**2)
   ...:     square.append(val**2)
   ...:     
In [9]: square
Out[9]: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
   
```


- 数字列表统计

```
datas = []

for x in range(1,11):
    x = x**2
    datas.append(x)
print(datas)


min = min(datas)
max = max(datas)
sum = sum(datas, 0)

print("min="+str(min))
print("max="+str(max))
print("sum="+str(sum))

//结果
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
min=1
max=100
sum=385
```

- 列表解析(使用一行for语句,生成列表)

```python
# 列表解析
datas = [values**2 for values in range(1,10)]
print(datas)

//结果
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```


- 列表切片:取列表一部分

```
# 列表解析

datas = [values  for values in range(0,11)]
print(datas)

print(datas[0:3])#不包含下标为3的元素
print(datas[1:3])#不包含下标为3的元素
print(datas[1:])#1:到最后的元素
print(datas[:5])#开头:到下标为5-1的元素
print(datas[-3:])#最后3个元素

//结果
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[0, 1, 2]
[1, 2]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[0, 1, 2, 3, 4]
[8, 9, 10]
```

- 遍历部分元素(切片)

```
datas = [values  for values in range(0,11)]
print(datas)

for num in datas[1:5]:
    print(num)

```


- 列表复制

```
# 列表解析

data1 = [values  for values in range(0,11)]

data2 = data1

print("data1_id:"+str(id(data1))) #id相同,指向同一块内存
print("data2_id:"+str(id(data2)))

data1.append(23)



print("data1:"+str(data1))
print("data2:"+str(data2))



#使用复制

data3 = data1.copy();
print("data3_id:"+str(id(data3)))
print("data3:"+str(data3))


#复制
data4 = data1[:]

print("data4_id:"+str(id(data4)))
print("data4:"+str(data4))

# 拓展data
data5=[]
data5.extend(data1)

print("data5_id:"+str(id(data5)))
print("data5:"+str(data5))

//结果
data1_id:4411185032
data2_id:4411185032

data1:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 23]
data2:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 23]

data3_id:4408819464
data3:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 23]

data4_id:4411390728
data4:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 23]

data5_id:4411376776
data5:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 23]
[Finished in 0.0s]
```


# 4.元组
>  Python将不能修改的值称为**不可变**的，而不可变的列表被称为元组。

- 定义元组

元组看起来犹如列表，但使用圆括号而不是方括号来标识。
定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样。

```
# 元组


dem = (200,400) #定义一个长宽不能改变的矩形,长:200 宽:400

lon = dem[0]
width = dem[1]

print("long:"+str(lon))
print("width:"+str(width))

# 改变值
dem[0] = 12     #报错:'tuple' object does not support item assignment

```

> 遍历元组

```python

dem = (200,400) #定义一个长宽不能改变的矩形,长:200 宽:400
# 遍历元组
for de in dem:
    print("dem:"+str(de))
```



## 条件语句if

```
cars = ['audi', 'bmw', 'subaru', 'toyota']

#将bmw以全部大写方式打印
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```


- 普通条件检查
  - ==
  - \>=
  - <=
  - !=

- 多个条件检查
  - and
  - or

- 包含检查
  - elm in list
  - elm not in list

> 测试:

```
>>> age1=12
>>> age2=20
>>> age1>age2
False
>>> age1<=age2
True
>>> age1<age2 and age1>0
True

>>> age1>20 or age2<40
True
>>> 

```

> 检查特定值是否在列表中

```pyton
 datas=list(range(1,5))
  datas
[1, 2, 3, 4]
3 in datas
True
6 in datas
False

# 特定值不在列表中

>>> 6 not in datas
True
```


- if-elif-else

```
# -*- coding: utf-8 -*-
age = 12


if age<4:
    print("fee five")
elif age<60:
    print("fee15")
else:
    print("old free")


```

- 判断列表是否为空

```python
data=[]
data.append(12)

if data:#列表不为空时返回True
    print("list is not null")
    print("len:"+str(len(data)))
else:
    print("list is null")

#结果
list is not null
len:1
[Finished in 0.1s]
```




- 判断列表1中的元素是否在列表2中

```python
# -*- coding: utf-8 -*-

data1=[val for val in range(1,6)]
data2=list(range(1,11))
print(data1)
print(data2)

# 判断data1中的数据是否在data2中存在

for val in data1:
    if val in data2:
        print(str(val)+" in data2")
    else:
        print(str(val)+" is not in data2")  

# 判断是否data1 中的数字都在data2中
count=0
for val in data1:
    if val in data2:
        count = count+1

if count==len(data1):
    print("data1 in data2")

```


# 5.字典

> 使用字典

- 在Python中，字典是一系列**键—值**对。每个键都与一个值相关联，你可以使用键来访问与之相关联的值。与键相关联的值可以是数字、字符串、列表乃至字典。事实上，可将任何Python对象用作字典中的值。

- 在Python中，字典用放在花括号{}中的一系列键—值对表示


> 字典创建,基本使用

- 创建字典
- 添加元素
- 查看元素
- 修改元素
- 删除元素


```
# -*- coding: utf-8 -*-
# python 字典

person={'name':'chen','age':23,'id':'001'}

print(person)

print("name:"+person['name'])
print("id:"+person['name'])
print("age:"+person['name'])


# 添加 字典元素
person['desc']="haoren"
print(person)


#修改字典中的元素

person['desc']="dahaoren".title()
print(person)

# 删除键-值对

del person['desc']
print(person)
```



> 字典遍历

- 遍历**键-值**对 (排序可能与输入顺序不一致,python不关系字典的顺序)
- 遍历键
- 遍历值


```
# python 字典
person={'name':'chen','age':23,'id':'001'}

# 遍历 key-value
for key,value in person.items():
    print("key:"+str(key)+" value:"+str(value))

print()

# 遍历所有键
for key in person.keys():
    print("key:"+str(key))


print()
# 遍历所有value

for value in person.values():
    print("Value:"+str(value))


```

> 遍历不重复元素:使用set() 去重

```
# python 字典
ages = {"chen":23,"tom":22,"lucy":22}
print(ages)
for age in ages.values():
    print(str(age))

print()
#遍历字典中所有不重复元素
for age in set(ages.values()):
    print(age)
```

 > 嵌套字典
 
 
```python
 # 嵌套字典
person1 = {'name':'chen','age':11}
person2 = {'name':'wang','age':22}
person3 = {'name':'zhang','age':33}

#列表中嵌套字典
persons = [person1,person2,person3]

for p in  persons:
    print(p)

print()

# 字典中嵌套字典
perDic = {'person1':person1,"person2":person2,"person3":person3}

for pName,pInfo in perDic.items():
    print(pName+":"+str(pInfo))


print()
# 字典中嵌套列表
list1 = list(range(1,6))
list2 = list(range(11,16))
list3 = list(range(21,26))

listDic = {'list1':list1,'list2':list2,'list3':list3}

for li in listDic.values():
    print(li)

```

> 结果

```
{'name': 'chen', 'age': 11}
{'name': 'wang', 'age': 22}
{'name': 'zhang', 'age': 33}

person1:{'name': 'chen', 'age': 11}
person2:{'name': 'wang', 'age': 22}
person3:{'name': 'zhang', 'age': 33}

[1, 2, 3, 4, 5]
[11, 12, 13, 14, 15]
[21, 22, 23, 24, 25]
[Finished in 0.0s]
```

# 6.用户输入和while

```python
# 用户输入
input = input("input what you want to say:")
print(input)
```

> 类型转换

```
age = input("input how old are you?")
print("age:"+age)

age = int(age)      #使用int 转换类型
print("age > 20?"+ str(age>20))
```



- while使用


```
num = 1
while num <=10:
    print("num is "+str(num))
    num +=1
```



- while 用户输入


```
# 用户输入
# -*- coding: utf-8 -*-
msg ="input somethin and outprint in screen:"
msg+="\n 'quit' to exit"

string = ''
while string!='quit':
    string=input("input yout want to say,and 'quit' to exit:")
    if string!='quit':
        print("out:"+str(string))
```


> 使用标志位结束循环

```
# 使用 falg 标志结束循环
flage= True
while flage:
    inString = input("input what you want to say :")
    if inString == 'quit':
        flage = False
    else:
        print("out:"+str(inString))
    pass
```

> 使用break 结束循环


```
# 使用break 结束循环  
while True:
    inString = input("input what you want to say :")
    if inString == 'quit':
        break;
    else:
        print("out:"+str(inString))
    pass

```



- `continue` 跳过当次循环


```
num = 0

while True:
    num += 1
    inNum = input("input a num,input 'quit' to exit, "+
        "input 'next' to continue: ")
    if inNum=='quit':
        break
    elif inNum=='next':
        continue
    else:
        print("the num is "+ str(num))
    pass
```




> 使用 while 循环来处理列表和字典


```
# -*- coding: utf-8 -*-
# 使用while 循环处理 字典/列表
# 处理列表:将列表a 中的元素的每个字符串第一个单词改为大写,放到b列表
la = list(range(1,10))
lb=[]


while len(la)>0:# 使用la的长度判断
    lb.append(la.pop())
    print("la:"+str(la))
    print("lb:"+str(lb))


```


```
la = list(range(1,10))
lb=[]
while la: #使用la是否为空判断
    lb.append(la.pop())
    print("lb:"+str(lb))

```


> 删除列表中指定元素

```
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
    print(pets)
    pass
```


> 打印三角形

```python
# 打印三角形
coun = 15
i=coun
while i>=1:
    ll=rr=int((coun-i)/2)
    print(' '*ll + '*'*i+ ' '*rr)
    i -=2


#结果
***************
 ************* 
  ***********  
   *********   
    *******    
     *****     
      ***      
       *   
```


> 右三角

```python
#效果
                    *
                 ****
              *******
           **********
        *************
     ****************
  *******************
```



> 使用用户输入来填充字典


```
//使用用户输入填充词典
personInfo = {} # 存放不同name对应的年龄

flag = True

while flag:
    personName = input("input person name:")

    personAge = input("input person age:")

    #将personName 对应的年龄存放到词典中
    personInfo[personName]=personAge

    stataust = input("input 0 exit and 1 continue")

    if stataust=='0':
        #flag=False
        break


print(personInfo)
```

-----

# 7.函数

> 函数是带名字的代码块，用于完成具体的工作。要执行函数定义的特定任务，可调用该函数。需要在程序中多次执行同一项任务时，你无需反复编写完成该任务的代码，而只需调用执行该任务的函数，让Python运行其中的代码。你将发现，通过使用函数，程序的编写、阅读、测试和修复都将更容易


## 1.定义函数

- def 定义函数
- say_hello() 函数名
- `"""xxxx"""` 使用3引号包裹,用于生成


```python
 #定义函数
def say_hello():
    """ this function is used to print hello on the screen"""
    print("hello python world")
    pass

 #调用函数
say_hello()
```

> 效果

```
chendeMacBook-Air:python chen$ py test.py 
hello python world
```



## 2.定义有参函数

```python
# 定义有参函数

def say_hello(userName):
    """ this function is used to print hello on the screen"""
    print("hello python"+userName.title()+" world")
    pass

# 调用函数
userName = input("input person name: ")

say_hello(userName) 
```


## 3.带返回值函数


```python
#带返回值的函数

def personInfo(firstName,lastName):
     person ={}
     person['firstName']=firstName.title()
     person['lastName']= lastName.title()
     return person


firstName = input("input firstName: ")
lastName = input("input lastName:")

p = personInfo(firstName, lastName)

print("full name is :"+str(p))
```



## 4.可变参函数

```
#可变参函数
def fullName(fName,lName,mName=""):
    """分别代表 firstName lastName midleName"""

    person = {}
    person["firstName"]=fName;
    person["midleName"]=mName;
    person["lastName"]=lName;

    return person



firstName = 'chen'
midleName = 'xiao'
lastName = 'zong'

person = fullName(firstName,lastName,midleName)
person = fullName(firstName,lastName)# 省略参数调用

print(person)
```


## 5.任意个数的参数


```
#可变参函数
def fullName(*name):
    print(name)
fullName('wang','li','chen','zhang')

```

## 6.使用任意数量的关键字实参

```
##使用任意数量的关键字实参: 传入的参数为key-value格式

def func(**infos):
    print(infos)
    for info in infos.items():
        print(info)
        pass
func(name='chen',age='23',id='001')
```

## 7.将函数存储在模块中

- 定义函数,并封装到模块中
- 在主调代码文件中导入模块
- 使用导入模块的方法


> 封装模块:保存到 func.py


```
# -*- coding: utf-8 -*-

#将函数存储在模块中

def say(info):
    print(info)
    pass
```

> 导入模块

- 新建test.py
- 导入模块

```python
import func                 #导入模块
func.say("hello world")     #调用模块的方法
```



> 使用

```
chendeMacBook-Air-2:python_simple chen$ py test.py 
hello world
```


--- 

> 导入模块中特定的函数

- 语法: ` form module improt function`

```
from func import say,info
say("hello python ")
info()
```



## 8.使用 as 给函数指定别名

- 语法 `from module import func as newfunc`



```
##使用as 别名导入模块中的方法

from func import say as func_say,info
func_say("hello")
```


## 9.导入模块中所有方法

> func.py

```python
#将函数存储在模块中

def say(info):
    print(info)
    pass


def info():
    print("this is info function ")
    pass
```

> test.py 主调

```python
# 导入模块总所有函数
from func import *
say("say what you want to say")
info()
```




# 9.类

> 简介

- 面向对象编程是最有效的软件编写方法之一。
- 在面向对象编程中，你编写表示现实世界中的事物和情景的类，并基于这些类来创建对象。
- 编写类时，你定义一大类对象都有的通用行为。
- 基于类创建对象时，每个对象都自动具备这种通用行为，然后可根据需要赋予每个对象独特的个性。
- 使用面向对象编程可模拟现实情景，其逼真程度达到了令你惊讶的地步。
- 根据类来创建对象被称为实例化，这让你能够使用类的实例。




## 9.1创建和使用类

> python3

- 声明一个类 `class  Dog():`
- 构造方法:`def __init__(self, name,age):`
- 成员方法: `def  sit(self):`

- 创建实例  `mydog = Dog("lionDog", 12)` 
- 使用属性  `mydog.age)`
- 使用方法  `mydog.sit()`

```python
# -*- coding: utf-8 -*-
# 定义一个dog类
class  Dog():
    """docstring for  Dog"""
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def  sit(self):
        print("the dog is sit ....")
    def roll_over(self):
        print("the dag is roll_over ....")
# 使用Dog类创建一个实例
mydog = Dog("lionDog", 12)
# 输出my_dog信息
print("mydog info:"+"name:"+mydog.name.title()+" age:"+str(mydog.age))
#使用方法
mydog.sit()
```

## 9.2继承
> 创建子类的实例时， Python首先需要完成的任务是给父类的所有属性赋值。
为此，子类的方法__init__()需要父类施以援手。




```python
# -*- coding: utf-8 -*-
# 使用类的继承
class Car( ):
    """一次模拟汽车类的尝试"""
    def __init__(self, make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make+" "+ self.model
        return long_name
    def  read_odometer(self):
        print("this car has "+ str(self.odometer_reading)+" miles on it")
    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer ")
    def increment_odometer(self,miles):
        self.odometer_reading +=miles


# 创建一个父类
my_car = Car("china", "bmw", "2012")
print(str(my_car.make.title()+" "+my_car.model+" "+ my_car.year))
print(str(my_car.get_descriptive_name()))

# 使用Car 定义一个子类
class  ElectricCar(Car):
    """定义一个汽车的子类"""
    def __init__(self, make,model,year):
        super().__init__(make,model,year)

#创建子类
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())      

```



> 子类设置属性和方法


```python
# -*- coding: utf-8 -*-
# 使用类的继承
class Car( ):
 ... ....
# 使用Car 定义一个子类
class  ElectricCar(Car):
    """定义一个汽车的子类"""
    def __init__(self, make,model,year):
        super().__init__(make,model,year)
        #定义子类自己的属性
        self.battery_size = 70
        
    def describ_battery(self):
        """ 打印一条描述电池容量的信息"""
        print("This car has a "+ str(self.battery_size)+ " -Kwh battery..")

#创建子类
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())      

#调用子类的 方法
my_tesla.describ_battery()
```

> 重写父类方法



```
# -*- coding: utf-8 -*-
# 使用类的继承
class Car( ):
    """一次模拟汽车类的尝试"""
    def __init__(self, make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make+" "+ self.model
        return long_name
    def  read_odometer(self):
        print("this car has "+ str(self.odometer_reading)+" miles on it")
    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer ")
    def increment_odometer(self,miles):
        self.odometer_reading +=miles
    def fill_gas(self):
        print("fill gas....")
        pass

my_car = Car("china", "bmw", "2012")
print(str(my_car.make.title()+" "+my_car.model+" "+ my_car.year))
print(str(my_car.get_descriptive_name()))
my_car.fill_gas()


print("------------")

# 使用Car 定义一个子类
class  ElectricCar(Car):
    """定义一个汽车的子类"""
    def __init__(self, make,model,year):
        super().__init__(make,model,year)
        #定义子类自己的属性
        self.battery_size = 70
    def describ_battery(self):
        """ 打印一条描述电池容量的信息"""
        print("This car has a "+ str(self.battery_size)+ " -Kwh battery..")
    def fill_gas(self):
        print("the electric car dong has gas ")

#创建子类
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())      

#调用子类的 方法
my_tesla.describ_battery()
my_tesla.fill_gas()
```

## 9.3导入类

```
from car import Car

my_car = Car("china", "bmw", 2017)

des_name = my_car.get_descriptive_name()

print(des_name)
```


> 一个模块定义多个类

```
# -*- coding: utf-8 -*-

class  Person():
    """定义一个Person类"""
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def  info(self):
        print("[Person ]name:"+self.name+" age:"+str(self.age))
        pass

# 定义一个Studen 类
class  Student(Person):
    """定义一个Student类继承Person类"""
    def __init__(self, name,age,studenId):
        super().__init__(name,age)
        self.studenId = studenId

    def info(self):
        print("[Student] name:"+self.name+" age:"+str(self.age)+" id:"+self.studenId)

# 定义一个Teacher类

class Teacher(Person):
    """定义一个Teacher类继承Person"""
    def __init__(self, name,age,teacherID):
        super(Teacher, self).__init__(name,age)
        self.teacherID = teacherID

    def info(self):
        print("[Teacher] name:"+self.name+" age:"+str(self.age )+" id:"+self.teacherID)

```


> 导入一个模块的多个类

- `from person import Person`

```
from person import Person
from person import Teacher
from person import Student


p = Person("chen", 27)
p.info()



# student

stu = Student("xiaoming", 12, "001")
stu.info()


# teacher 

teacher = Teacher("Mr wang", 33, "100")
teacher.info()
```

> 导入模块

- `import person`
- `person.Person`

```
import person
p =  person.Person("personname", 23)
p.info()
```

> 导入一个模块所有关的类

- `from person import *`

```
from person import *
p = Person("chen", 23)
p.info()
```

> 一个模块导入另一个模块

- person 中导入car 

` from car import Car`

- 直接使用

```

from person import *
p = Person("chen", 23)
p.info()


#使用person 中的car
mycar = Car("hello", "bmw", "2017")
print(mycar.get_descriptive_name())
```


## 9.4python 标准库

> Python标准库是一组模块，安装的Python都包含它。  


你现在对类的工作原理已有大致的了解，可以开始使用其他程序员编写好的模块了。可使用标准库中的任何函数和类，为此只需在程序开头包含一条简单的import语句。下面来看模块collections中的一个类——OrderedDict。字典让你能够将信息关联起来，但它们不记录你添加键—值对的顺序。要创建字典并记录其中的键—值对的添加顺序，可使用模块collections中的OrderedDict类。 OrderedDict实例的行为几乎与字典相同，区别只在于记录了键—值对的添加顺序


> 使用有序词典


```
# 记录键值对添加的顺序
from collections import OrderedDict


# 使用 有序词典
persons = OrderedDict()


##定义字典
# persons = {}
persons['zhang'] = 89
persons['li'] = 11
persons['chen']=23

for name,age in persons.items():
    print("name:"+name.title()+" age:"+ str(age))

```

## 9.5类编码风格

你必须熟悉有些与类相关的编码风格问题，在你编写的程序较复杂时尤其如此。
类名应采用驼峰命名法，即将类名中的每个单词的首字母都大写，而不使用下划线。实例名
和模块名都采用小写格式，并在单词之间加上下划线。
对于每个类，都应紧跟在类定义后面包含一个文档字符串。这种文档字符串简要地描述类的
功能，并遵循编写函数的文档字符串时采用的格式约定。每个模块也都应包含一个文档字符串，
对其中的类可用于做什么进行描述。
可使用空行来组织代码，但不要滥用。在类中，可使用一个空行来分隔方法；而在模块中，
可使用两个空行来分隔类。
需要同时导入标准库中的模块和你编写的模块时，先编写导入标准库模块的import语句，再
添加一个空行，然后编写导入你自己编写的模块的import语句。在包含多条import语句的程序中，
这种做法让人更容易明白程序使用的各个模块都来自何方。




# 10.文件和异常

## 1.从文件中读取数据
### 1.1 读取整个文件 

> 数据文件 pi_digist.txt

```
3.1415926535
8979323846
2643383279
```


> 测试代码

- `with open('文件名') as file_obj:` 读取文件,生成一个file_obj对象
- `file_obj.read()` : 返回文件内容

- 使用上述结构,会自动在合适时间关闭文件

```python
# 读取文件 pi_digits.txt

with open('pi_digits.txt') as file_object:
    content = file_object.read()
    print(content)

```


> 显示效果

```
chendeMacBook-Air-2:python_simple chen$ py test.py 
3.1415926535
8979323846
2643383279
```


### 1.2 逐行读取文件

```python
file = 'pi_digits.txt'
with open(file) as file_obj:
    for line in file_obj:
        print(line.rstrip())
```


### 1.3 创建一个包含文件各行内容的列表

```python
# 读取文件各行内容到 list
file = 'pi_digits.txt'
with open(file) as file_obj:
    lines = file_obj.readlines()
# print(str(lines))
# 输出列表
for line in lines:
    print(line.rstrip())
```


### 1.4 使用文件中的数据

```python
file = 'pi_digits.txt'
with open(file) as file_obj:
    lines = file_obj.readlines()
# print(str(lines))
# 输出列表
pi_str=''
for line in lines:
    pi_str +=line.strip()
print(pi_str)   
print(len(pi_str))
```


> 效果

```python
chendeMacBook-Air-2:python_simple chen$ py test.py 
3.141592653589793238462643383279
32
```






## 2.写入文件

> 保存数据的最简单的方式之一是将其写入到文件中。通过将输出写入文件，即便关闭包含程

序输出的终端窗口，这些输出也依然存在：你可以在程序结束运行后查看这些输出，可与别人分
享输出文件，还可编写程序来将这些输出读取到内存中并进行处理。

### 2.1 向空文件写入数据

- 'w' : 打开并写入文件, 若文件不存在,则创建文件,若文件存在,则清空内容重新写入
- 'r' : 只读方式打开文件(省略参数时,默认为只读方式)
- 'a' : 追加方式打开文件
- 'r+': 读写方式打开文件

```python

file = 'info.txt'

#写入文件
with open(file,'w') as file_obj:
    file_obj.write("i love python.....") 


# 读取方式打开文件
with open (file,'r') as file_obj:
    content = file_obj.readlines()
    print(content)


# 'a' 追加方式打开文件

with open(file,'a') as file_obj:
    file_obj.write("i love programming...")




# 使用读写方式打开文件
with open(file,'r+') as file_obj:
    content = file_obj.read()

    content = str(content).strip()
    file_obj.write(content)


# 默认使用制只读方式打开文件
with open(file) as file_obj:
    content = file_obj.readlines()
    print(content)
```


### 2.2 写入多行文件
- 使用"\n"

```python
# 写入多行文件

file = 'info.txt'
with open(file,'w') as file_obj:
    file_obj.write("i love java. \n")
    file_obj.write("i love python. \n")

```



## 3.异常
Python使用被称为异常的特殊对象来管理程序执行期间发生的错误。每当发生让Python不知
所措的错误时，它都会创建一个异常对象。如果你编写了处理该异常的代码，程序将继续运行；
如果你未对异常进行处理，程序将停止，并显示一个traceback，其中包含有关异常的报告。
异常是使用try-except代码块处理的。 try-except代码块让Python执行指定的操作，同时告
诉Python发生异常时怎么办。使用了try-except代码块时，即便出现异常，程序也将继续运行：
显示你编写的友好的错误消息，而不是令用户迷惑的traceback。



### 3.1处理ZeroDivisionError

> 捕获异常

``` 
# 异常

try:
    print(4 / 0)
except ZeroDivisionError :
    print("you can not divide by zero "

```


### 3.2else代码块
通过将可能引发错误的代码放在try-except代码块中，可提高这个程序抵御错误的能力。错
误是执行除法运算的代码行导致的，因此我们需要将它放到try-except代码块中。这个示例还包
含一个else代码块；依赖于try代码块成功执行的代码都应放到else代码块中：

> 测试

```python
# 异常

try:
    answer = 5/3
except Exception as e:
    print("can not divide by 0")
    # raise e
else:
    print("answer:"+str(answer))
    pass
```

> 结果: `answer:1.6666666666666667`


### 3.3 FileNotFoundError

> 打开不存在文件时,抛出文件不存在异常

```python
# FileNotFound异常


file_name = 'test.txt'
content = ""
try:
    with open(file_name) as file_obj:
        content = file_obj.read()

        print(content)
        pass
except FileNotFoundError:
    print("file  not  found ")
    # raise e


if content!="":
    words = content.split()
    print(words)
```



## 4.存储数据

很多程序都要求用户输入某种信息，如让用户存储游戏首选项或提供要可视化的数据。不管
专注的是什么，程序都把用户提供的信息存储在列表和字典等数据结构中。用户关闭程序时，你
几乎总是要保存他们提供的信息；一种简单的方式是使用模块json来存储数据。
模块json让你能够将简单的Python数据结构转储到文件中，并在程序再次运行时加载该文件
中的数据。你还可以使用json在Python程序之间分享数据。更重要的是，JSON数据格式并非Python
专用的，这让你能够将以JSON格式存储的数据与使用其他编程语言的人分享。这是一种轻便格
式，很有用，也易于学习。

> JSON（JavaScript Object Notation）格式最初是为JavaScript开发的，但随后成了一种常见
格式，被包括Python在内的众多语言采用



### 1.使用json.dump() 和 json.load() 

> 使用 

- json.dump() : 存储数据
- json.load() : 加载数据




> 数据的保存和读取

```python
# 数据存储

import json

numbers = [2,3,5,7,11,13]

file_name = 'numbers.json'

with open(file_name,'w') as file_obj:
    json.dump(numbers, file_obj)



# 从文件中加载数据  
with open(file_name) as fobj:
    numbers2 = json.load(fobj)
print("加载数据:"+str(numbers2))    

```




> 保存和读取用户生成的塑胶

- 用户首次运行程序时被提示输入自己的名字，这样再次运行程序时就记住他了。


```python
# 用户数据保存
import json
user_name = input("inut user name:")
file_name = 'user_name.json'
with open(file_name,'w') as fobj:
    json.dump(user_name, fobj)
    print("have save username to file :"+str(file_name))
# 读取用户信息
print("-------read names in file-----")
with open(file_name) as fobj:
    uname = json.load(fobj)
    print("username is :"+str(uname))
```



### 2.重构

> 你经常会遇到这样的情况：代码能够正确地运行，但可做进一步的改进——将代码划分为
一系列完成具体工作的函数。这样的过程被称为重构。重构让代码更清晰、更易于理解、更容
易扩展

```python
# 定义重构函数
import json

file_name = 'user_name.json'

# 定义函数,保存用户数据 
def get_stored_username():
    """如果保存了用户名,则读取用户名"""
    try:
        with open(file_name) as fobj:
            uname = json.load(fobj) #读取用户名
    except FileNotFoundError:
        return None
    else:
        return uname

def gree_user():
    """问候用户,并指出其名字"""
    user_name = get_stored_username()
    if user_name:
        print("Welcom back, "+user_name + "!!!")
    else:
        user_name = input("input your name:")
        with open(file_name,'w') as fobj:
            json.dump(user_name, fobj)
            print("Save your name into file ")


gree_user()         
```




# 11.测试代码
编写函数或类时，还可为其编写测试。通过测试，可确定代码面对各种输入都能够按要求的那样工作。测试让你信心满满，深信即便有更多的人使用你的程序，它也能正确地工作。在程序中添加新代码时，你也可以对其进行测试，确认它们不会破坏程序既有的行为。程序员都会犯错，因此每个程序员都必须经常测试其代码，在用户发现问题前找出它们。在本章中， 你将学习如何使用Python模块unittest中的工具来测试代码。你将学习编写测试用例，核实一系列输入都将得到预期的输出。你将看到测试通过了是什么样子，测试未通过又是什么样子，还将知道测试未通过如何有助于改进代码。你将学习如何测试函数和类，并将知道该为项目编写多少个测试。

### 1.测试函数

> 待测试函数: 根据firs last 返回全名 `name_function.py`

```python
# -*- coding: utf-8 -*-
# 测试 

def  get_full_name(firstname,lastname):
    """Generate a neatly formatted full name """
    full_name = firstname +' '+ lastname
    return full_name.title()

```

> 主调函数 `names.py`

```python
import name_function
# from name_function import get_full_name

print("Enter 'q' at any time to quit:")

while True:
    first_name = input("input first name:")
    if first_name == 'q':
        break

    last_name = input("input last name: ")
    if last_name=='q':
        break

    full_name = name_function.get_full_name(first_name,last_name)
    print("Full name is :"+full_name)
    
```



> 测试函数 `test_name_function.py`

```python
# -*- coding: utf-8 -*-

import unittest

from name_function import get_full_name

class  NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    def test_first_last_name(self):
        """ 能够正确处理像 Janis Joplin 这样的名字吗? """
        full_name = get_full_name('janis', 'joplin')
        self.assertEqual(full_name,'Janis Jplin')

unittest.main()     
```

































