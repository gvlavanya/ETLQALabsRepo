address="banglore"
size=len(address)
print(address[0])
print (address[size-1])      #b,e
#2.upper case
name="lavanya"
print(name.upper())j

# substring = s[start:stop:step]
#3.substring
s="Hello world"
#substring=s[0:5]
print(s[0:7])  #Hello w

#4.omitting
print(s[:3])  #Hel
print(s[3:]) #lo world
print(s[:])   #Hello world
print(s[-7:-1])   #o worl

#5for
for i in range(1,10,2):      #1,3,5,7,9
    print(i)
 # for string
for ch in "Lavanya":    #l,a,v,a,n,y,a
    print(ch)
#6.add
num1="10"
num2="2010"
print(num1+num2)  #102010
print(int(num1)+int(num2))  #2020
print(float(num1))   #10.0

num3=1010
con_str=str(num3)
print(con_str)    #1010
print(num3)
print(type(con_str))

# variable naming convention
# camel case
numberOfStudent = 10
#Pascal case
NumberOfStudent = 10
# snake case
number_of_student = 10
#7.wrong
name="etlqalabs"
l=len(name)
print(l)  #9
for i in range(l):
    item=name[i]
  #  print(item,":",type(item))

#List:not cmg
    '''
 students=[1,2,3,4,5]
l=len(students)
sum=0
for x in range(l):
sum=sum+students[x] '''

#8.tuple ->(immutable ) not change values once its assigned,accepts dups,
#set:immutable and no dups
#list:accepts dups and can change values
students_list=[1,2,3,4,5,6,6]
students_tuple=(1,2,3,4,5,6,5)
students_set={1,2,3,4,5,6,2}
print(type(students_tuple))
print(type(students_list))
print(type(students_set))
print("before list:", students_list)   #before list: [1, 2, 3, 4, 5, 6, 6]
students_list[0]=10
print("after list:", students_list)    #after list: [10, 2, 3, 4, 5, 6, 6]
print("before tuple:" ,students_tuple)  #before tuple: (1, 2, 3, 4, 5, 6)
#students_tuple[0]=11
#print("after tuple:" ,students_tuple)   #error
print("before set:", students_set)   #before set: {1, 2, 3, 4, 5, 6}
#students_set[1]=12
#print("after set:", students_set)

#10.dictionary:key-map
emp_dict={1:"ram","2":"sam"}
print(emp_dict["2"])  #sam

#11.str
str = "etlqalabs"
print(str)   #etlqalabs
result = str[0]+str[1]+str[2]+str[4]
print(result)  #etla
l=len(str)
result_slice = str[0:l:2]    # 0->starting index,l->length of the string ,2->intravel(skip one letter)
print(result_slice)  #elaas

#home work:
#1.reverse sting
city="ETLQALabs"
reverse_city=city[::-1]
print(reverse_city)   #sbaLAQLTE
#2.sub string
city = "ETLQALabs"
print(city[3:8])    #QALab

#4.How would you use slicing to create a new list containing only the odd-indexed elements of a given list?
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l=len(list)   #9
print(list[1:l:2])  #[1, 3, 5, 7, 9]

#5.the even-indexed elements of a given list?
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l=len(list)
print(list[0:l:2])   #[0, 2, 4, 6, 8]

#3.Write a python code to check if the given list contains duplicate elements and print yes or no as per input
list1 =[1,2,3,4,3]
print(len(list1))  #5
print(list1)    #[1, 2, 3, 4, 3]
print(set(list1))   #{1, 2, 3, 4}
#chk dups:
if len(list1)!=len(set(list1)):
    print("yes")
else:
    print("no")
