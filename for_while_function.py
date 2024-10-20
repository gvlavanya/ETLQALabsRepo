#1. for loop from 1 to 11 and 2 intravels
for i in range(1,11,2):
    print (i)   #1,3,5,7,9

#2.
for i in range(5,51,5):
    print(i)   #5,10,15....50

 #3.
'''
for k in range(0, 5):
 for j in range(0, 3):
  print (k * j)
'''
#4.intro while loops
c=0
while c<5:
    c=c+1
    if c==4:
       # break
        continue
    print(c)   #1 2 3(break)            for continue #1 2 3 5

#5.try-catch
try:
    name=[1,2,3,4]
    if name >3:
        print ("hello")
except:
    print("error was detected in the code")   #error was detected in the code

#6Functions :print hello world
def hello1():
    print("hello world")

hello1()  #hello world

#7.
def greetings(name1):
 print("hi "+name1 +"!")jupyter notebook

greetings("lava")   #hi lava!

#8.add 2 numbers
def add(num1 ,num2):
    return num1+num2

print(add(2,4))  #6

def mul(num1 ,num2):
    return num1*num2
print(mul(add(1,2),add(3,4)))   #21

#9.built in python functions
print(dir('hello'))  #['__add__', '__class__', '__contains__',..

#10
print("hello "+str(100))  #hello 100