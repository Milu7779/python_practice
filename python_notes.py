import time
print("hello Amzsys,")
print(1.3 + 2.5)
print("welcome"+"2")
print(str("2")+"group")
print("hy"*3)
print(len("Amzsys"))
text= """this is milu mathew.
from Amzys
line 3"""
print(text)
print('list...............')
list=['a','b','c']
print(list)
print(len(list))
print(list[1])
print('touple.........')
touple=(2,3,4,4)
print(touple)
print('dictionary.......')
dict={'name':'milu','email':'email@gmail.com'}
print(dict['name'])
print('set......')
set = {1,2,3,3}
print(set)
num=125
print(len(str('125')))
print('functions.........')
def square1(x):
    print(x * x)
square1(5)


x1 = 0
y = 0
def incr(x1):
    y = x1 + 1
    print(x1, y)
incr(5)
print('custom...')
x = 1
def f():
    return x
print(x)
print(f())
x = 1
#rewrite alredy asigned variable value with new value-global
def f():
    global x
    x = 2
    return x
print(x)
print(f())
print(x)
print('prob-5...')
x1 = 1
def f():
        y = x1
        x = 2
        return x + y
print(x)
print(f())
print(x)
x2 = 2
def f(a):
    x2 = a * a
    return x2
y = f(3)
print(x2, y)

def increment(a,amount=1):
    inc = a+amount
    return inc
print(increment(10))

print('lambda function')
a1= lambda a:a*a
print(a1(2))

print('string..........')
string = 'Amzsys'
print(string.upper())
print("string compare...........")

def istrcmp(x,y):
    x=x.lower()
    y=y.lower()
    if x == y :
        return True
    else:
        return False
print('comparison=',istrcmp('python','hello'))

x4=5
print(2< x4)
print(2<= x4)
print(2< x4 and x4>5)

x = 2
if x == 3:
    print(x)
else:
    print(y)
print(time.asctime())
print('.....list....')
list1 = ['hello',22,7,['a','b']]
print(list1)
print(len(list1))
print(list1[0:-2])
print(list1[0:1])
print(list1[::-1])
print(list1[:])
print(list1[1:])
print(22 in list1)
x = [0, 1, [2]]
x[2][0] = 3
print(x)
x[2].append(4)
print(x)
x[2] = 2
print(x)
l1=['a','b']
l2=[1,2,3]

for l1,l2 in zip(l1,l2):
    print(l1,l2)

print('sum of integer list= ',sum([1,2,3]))
def product(p):
    p1 = 1
    for i in p:
        p1=p1*i
    print('product of list of numbers=',p1)
product([1,2,3,4])
def factorial(n):
    fact = 1
    n=6
    for i in range(1,n+1):
        fact= fact *i
    #return fact
    print('factorial=', fact)
f=factorial(5)

print('.....reverse.....')
def reverse(l):
    rev_list = []
    for i in l:
        rev_list.insert(0,i)
    print('reverse list =',rev_list)
reverse(['hello',44,5])
print('list minimum=',min(['apple','ac','kiwi']))
print('list maximum=',max(['apple','kiwi']))
print('....CUMULATIVE SUM...')
def cumulative_sum(cl):
    cum_sum = []
    sum=0
    for i in cl:
        sum=sum+i
        cum_sum.append(sum)
    return cum_sum
cl=[1,2,3,4,5]
print('original list=',cl)
print('cumulative sum=',cumulative_sum(cl))

print('....CUMULATIVE PRODUCT...')

def cumulative_product(cl):
    cum_sum = []
    sum=1
    for i in cl:
        sum=sum*i
        cum_sum.append(sum)
    return cum_sum
cl=[1,2,3,4,5]
print('original list=',cl)
print('cumulative product=',cumulative_product(cl))

def unique(ul):
    unique_list = []
    dup_list = []
    for i in ul:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list
ul1=[1,2,3,3,5]
print('unique=',unique(ul1))


def dup(dl):
    dup_list = []
    or_list =[]
    for i in dl:
        if i not in or_list:

            or_list.append(i)
        else:
            dup_list.append(i)
    print('dup=',dup_list)
ul2=[1,2,3,3,5,5]
dup(ul2)

def group(list,size):
    for i in range(0,len(list),size):
        return list[i:i+size]

list=[1,2,3,66,4,7]
size=2
g=group(list,size)
print('group=',g)

def slice_list(input_list, size):
    return [input_list[i:i + size] for i in range(0, len(input_list), size)]

# Example usage
numbers = [1, 2, 33, 43, 5, 64, 7, 8, 9, 10]
size = 3
sliced_list = slice_list(numbers, size)

print("Original list:", numbers)
print(f"Sliced list (size {size}):", sliced_list)

print('.......tuple.....')
t = (2,3,4,6)
print(t[1])
t1=(1,)
print(t1[0])
print(t[1:])
print(len(t))


print('............set......')


s={1,2,3,5}
s.add(77)
print(s)
if 1 in s:
    print('True')
print('..........string...')
word='amzsys'
print(len(word))
print(word[1:3])
print(word[1:])
print(word[:-2])
print(word[-2:])
print('amzsys world'.split())
print('split=','amzsys.world'.split('.')[-1])
print('amzsys'.strip('mz'))
a='abcdefgh'.strip('abdh')
print(a)
def lensort(ls):
    s=sorted(ls,key=len)
    print(s)
lss=['hello1111111','amzsysy']
lensort(lss)

def extsort(el):
    for i in el:
        s=i.split('.')[-1]
        sr=sorted(s)
        print(sr)
ex=['a.c','hello.py','bb.c']
extsort(ex)

print('....files...')
f=open('hello.c')
r=f.read()
print(r)
def charcount1(filename):
    return len(open(filename).read())
print('character count=',charcount1('hello.c'))
def wordcount(filename):
    return len(open(filename).read().split())
print('word count=',wordcount('hello.c'))
def linecount(filename):
    return len(open(filename).readlines())
print('line count=',linecount('hello.c'))

lines=open('hello.c').readlines()
lines.reverse()
print(lines)

for line in lines:
    rev=line.strip()[::-1]
    print(rev)

print('...string to be search in file....')
def search_string(str,file):
    f=open(file).readlines()
    for line in f:
        if str in line:
            print(f'exist {str} in {file}')
        else:
            pass

str1='amzsys'
file1 = 'hello.c'
search_string(str1,file1)

def head(file,size):
    f=open(file).readlines()
    count=len(f)
    if size <= count:
        for line in range(size):
            #print('s')
            print(line)
f1='hello.c'
size1=1
head(f1,size)

print('list comprehension...')
a1=[1,3,4,5,7,10]
a2=[3,4,5,2,1,8]
new_l = [x for x in a1 if x%2==0]
new1 = [(a1,a2) for a1,a2 in zip(a1,a2)]
print(new_l)
print(new1)
new2 = [(x+y) for x in range(5) for y in range(5) if (x+y)%2==0 ]
print(new2)
#pythogorian triplets - x*x + y*y == z*z
n=25
new3 = [(x,y,z) for x in range(1,n) for y in range(x,n) for z in range(y,n) if x*x + y*y == z*z]
print(new3)
for index,value in  enumerate(['a','b','c']):
    print(index,value)
print('p-29')
def d_array(r,c):
    return [[None for i in range(c)] for j in range(r)]
r=2
c=3
a=d_array(r,c)
for row in a:
    print(row)

print('p-30')
def parse_csv(filename):
    new_file=[]
    f=open(filename).readlines()
    for line in f:
        nl=line.split()
        new_file.append(nl)
    return new_file
file1='file.csv'
print(parse_csv(file1))

print('..dictionarys....')
a={'name':'milu','email':'milu@gmail.com'}
print(a.keys())
print(a.values())
print(a.items())
print(a['name'])

if 'name' in a:
    print('true')
k=a.get('email')
if k is not None:
    print('exist')
add=a.setdefault('age','24')
print(a)
t='hello %(name)s' % {'name': 'python'}
print(t)
t1='welcome %(name)s' % {'name':'Amzsys'}
print(t1)
print('word count')
def word_frequency(words):
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency
print(word_frequency(['this','is','is']))



















