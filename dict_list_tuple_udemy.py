names=["aaa","bbb","ccc"]
print(names[1])
#2.replace 2nd item with another sport
sports=["chess","cricket","Base ball"]
sports[1]= "foot ball"
print(sports)

#3.delete 3rd num in the arrray
num=[1,2,3,4,5]
del num[3]
print(num)

#4.2 lists and merge
A=[1,2,3,4,5]
B=[2,5,6,"anu"]
print(A+B)         #[1, 2, 3, 4, 5, 2, 5, 6, 'anu']

#5.length ,min and max of list
numbers=[2,3,4,6,8,9]
len =print(len(numbers))
min=print(min(numbers))
max=print(max(numbers))        #6,2,9

#6.students and their score using dictory object(key value)
students={"lava":80,"Avi":90}
print(students)
print(students["lava"])

#7delete 2nd person from dictionary obj
data={"lava":40 ,"tej":20,"sai":18,"ven":46}
del data["tej"]
print(data)    #{'lava': 40, 'sai': 18, 'ven': 46}

#9.create a tuple of ur favourite movies
movies=("hary potter" ,"dora","barney","dora")
print(movies)   #('hary potter', 'dora', 'barney', 'dora')

#10.tuple and print all the items from 1st to 3rd index
index=(1,2,3,4)
print(index[0:3])   #(1, 2, 3)

