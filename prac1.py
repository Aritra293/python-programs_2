#tuple1=(1,2,3,4,5,6)
#print(tuple1)
#months = set(["january","february","March","April","May","June"])
#print("\nprinting the original set..")
#print(months)
#print("\nremoving some months from the set..")
#months.discard("January");
#months.discard("May");
#for i in months:
#    print(i)

#months =set(["January","February","March","April","May","june"])
#print("\nprinting the original set...")
#print(months)
#print("\nremoving some months from the set...")
#months.remove("January");
#months.remove("May");
#print("\nPrinting the modified set");
#print(months)

#Months =set(["January","February","March","April","May","june"])
#print("\nprinting the original set ... ") 
#print(Months) 
#print("\nRemoving some months from the set..."); 
#Months.pop(); 
#Months.pop(); 
#print("\nPrinting the modified set..."); 
#print(Months)

#Months =set(["January","February","March","April","May","june"])
#print("\nprinting the original set ... ") 
#print(Months) 
#print("\nRemoving some months from the set..."); 
#Months.clear(); 
#Months.clear(); 
#print("\nPrinting the modified set..."); 
#print(Months)

#Months =set(["January","February","March","April","May","june"])
#print("\nprinting the original set ... ") 
#print(Months) 
#print("\nRemoving some months from the set..."); 
#Months.discard("january"); 
#Months.discard("March"); 
#print("\nPrinting the modified set..."); 
#print(Months)

#days1 ={"Monday","Tuesday","Wednesday","Thursday"}
#days2 ={"Friday","Saturday","Sunday"}
#print(days1|days2)

#days1 ={"Monday","Tuesday","Wednesday","Thursday"}
#days2 ={"Friday","Saturday","Sunday"}
#print(days1.union(days2))

#days1 ={"Monday","Tuesday","Wednesday","Thursday"}
#days2 ={"Monday","Tuesday","Sunday","Friday"}
#print(days1&days2)

#set1 ={"Devansh","John","David","Martin"}
#set2 ={"Steve","Milan","David","Martin"}
#print(set1.intersection(set2))

#set1 = {1,2,3,4,5,6,7}
#set2 = {1,2,20,32,5,9}
#set3 =set1.intersection(set2)
#print(set3)

#a = {"devansh","bob","castle"}
#b = {"castle","dude","emyway"}
#c = {"fuson","gaurav","castle"}
#a.intersection_update(b,c)
#print(a)

#days1 ={"Monday","Tuseday","Wednesday","Thursday"}
#days2 ={"Monday","Tuseday","Sunday"}
#print(days1-days2)

#days1 ={"Monday","Tuesday","Wednesday","Thursday"}
#days2 ={"Monday","Tuesday","Sunday"}
#print(days1.difference(days2))

#a = {1,2,3,4,5,6}
#b = {1,2,9,8,10}
#c = a.symmetric_difference(b)
#print(c)

#days1 = {"Monday","Tuesday","Wednesday","Thursday"}
#days2 = {"Monday","Tuesday"}
#days3 = {"Monday","Tuesday","Friday"}

#print(days1>days2)

#print(days1>days2)

#print(days2==days3)

#Frozenset =frozen([1,2,3,4,5])
#print(type(Frozenset))
#print("\nprinting the content of frozen set..")
#for i in Frozenset:
#    print(i)
#Frozenset.add(6)

#dictionary = {"Name":"John","Country":"USA","ID":101}
#print(type(dictionary))
#Frozenset = frozenset(dictionary);
#print(type(Frozenset))
#for i in Frozenset:
#    print(i)

##Write a program to remove the given number from the set.

#my_set = {1,2,3,4,5,6,12,24}
#n = int(input("enter the number you want to remove"))
#my_set.discard(n)
#print("After Removing:",my_set)

## Write a program to add multiple elements to the set
#set1 = set([1,2,4,"john","CS"])
#set1.update(["Apple","Mango","Grapes"])
#print(set1)

#Write a program to find the union between two set.
#set1 = set(["peter","joseph",65,59,96])
#set2 = set(["peter",1,2,"joseph"])
#set3 = set1.union(set2)
#print(set3)

#Write a program to find the intersection between two sets
#set1 = {23,44,56,67,90,45,"javatpoint"}
#set2 = {13,23,56,76,"Sachin"}
#set3 = set1.intersection(set2)
#print(set3)

#writeaprogram to find 
#set1 = set(["Peter","James","Camroon","Ricky","Donald"])
#set2 = set(["Camroon","Washington","Peter"])
#set3 = set(["Peter"])

#issubset=set1 >= set2
#print(issubset)
#issuperset = set1 <=set2
#print(issuperset)
#issubset= set3<= set2
#print(issubset)
#issuperset= set2>= set3
#print(issuperset)

#create_dictionary

#Employee = {"Name":"Tom","Age":22}
#print(type(Employee))
#print("printing Employee data")
#print(Employee)


#Employee = {"Name":"John","Age":29,"salary":25000,"Company":"GOOGLE"}
#print(type(Employee))
#print("Name:%s" %Employee["Name"])
#print("Age:%d" %Employee["Age"])
#print("Salary:%d"%Employee["salary"])
#print("Company:%s"%Employee["Company"])

#Dict = {}
#print("Empty Dictionary:")
#print(Dict)

#Dict[0]='peter'
#Dict[2]='Joseph'
#Dict[3]='Ricky'
#print("\nDictiionary after adding 3 elements:")
#print(Dict)

#Dict['Emp_ages']=20,33,24
#print("\nDictionary after adding 3 elements:")
#print(Dict)

#Dict[3]='JavaTpoint'
#print("\nUpdated key value:")
#print(Dict)

#Dict={1:'Javatpoint',2:'Peter',3:'Thomas'}
#pop_ele=Dict.pop(3)
#print(Dict)

# for loop to print all the keys of a dictionary
#for loop to print all the values of the dictionary
#Employee = {"Name":"John","Age":29,"salary":25000,"Company":"GOOGLE"}
#for x in Employee:
 #   print(x)
  #  print(Employee[x])

#for loop to print the values of the dictionary by using values() method
#Employee = {"Name":"John","Age":29,"salary":25000,"Company":"GOOGLE"}
#for x in Employee.values():
#    print(x)

#for loop to print the items of the dictionary by using items() method.

#Employee = {"Name":"John","Age":29,"salary":25000,"Company":"GOOGLE"}
#for x in Employee.items():
#    print(x)


#Employee = {"Name":"John","Age":29,"salary":25000,"Company":"GOOGLE"}
#for x,y in Employee.items():
#    print(x,y)

#function
#def hello_world():
#    print("hello world")
#hello_world()

#def sum():
#    a=10
#    b=20
#    c=a+b
#    return c
#print("The sum is:",sum());

#def func(name):
#    print("Hi",name)
#func("Devansh")

#def sum(a,b):
#    return a+b;
#a=int(input("enter a:"))
#b=int(input("enter b:"))
#print("Sum=",sum(a,b))

#def change_list(list1):
   # list1.append(20)
   # list1.append(30)
#   print("list inside function=",list1)
#    list1 =[10,30,40,50]
#    change_list(list1)
#    print("list outside function=",list1)

#def change_list(list1): 
#    list1.append(20) 
#    list1.append(30) 
#    print("list inside function = ",list1) 
 
#defining the list 
#list1 = [10,30,40,50]
#calling the function 
#change_list(list1) 
#print("list outside function = ",list1)

#def change_string(str):
#    str=str+"hows you"
#    print("printing the string inside function:",str)
#    string1 = "Hi I am there"
#    change_string(string1)
#    print("Printing the string outside function:",string1)
    
#def func(name):
#    message ="Hi" + name
#    return message
#name = input("Enter the name:")
#print(func(name))

#def printme(name,age=22):
#    print("My name is",name,"and age is",age)
#printme(name="john")
#printme(age=10,name="David")

#def printme(*names):
#    print("type of passed argument is",type(names))
#    print("printing the passed arguments...")
#    #for name is names:
#    print(name)
#printme("john","David","smith","nick")    

#C=a<<2;#240=111100000
#print("line 5-value of C is",C)

#list =["Godavari","Kaveri","Krishna"]
#list.append("Narmada")
#print(list)
#list[0]="Tapti"
#print(list)

#def food(**kwargs):
#    print(kwargs)
#food(a="Apple")
#food(fruits="Orange",vegetables="Carrot")

#def calculate(*args):
#    sum=0
#    for arg in args:
#        sum=sum +arg
#    print("The sum is",sum)
#sum=0
#calculate(10,20,30)
#print("value of sum outside the function:",sum)

#integer = -20
#print('Absolute value of -40 is:',abs(integer))

#floating =-20.83
#print('Absolute value of -40.83 is:',abs(floating))

#k = [1,3,4,6]
#print(all(k))

#k=[0,False]
#print(all(k))

#k=[1,3,7,0]
#print(all(k))

#k=[0,false,5]
#print(all(k))

#x = 10
#y = bin(x)
#print(y)

#test1 = []
#print(test1,'is',bool(test1))
#test1 = [0]
#print(test1,'is',bool(test1))
#test1 = 0.0
#print(test1,'is',bool(test1))
#test1 = None
#print(test1,'is',bool(test1))

#string = "Hello World."
#array = bytes(string,'utf-8')
#print(array)


#x= 8
#print(callable(x))

#str="hello world"
#print(str[::-1])


#s= sum([1,2,4])
#print(s)

#s= sum([1,2,4],10)
#print(s)

#I=[4,3,2,0]
#print(any(I))

#I = [0,False]
#print(any(I))

#I=[0,False,5]
#print(any(I))

#I=[]
#print(any(I))

#string = "python is a programming language"
#arr = bytearray(string,'utf-8')
#print(arr)

#x=8
#print(eval('x+1'))

#print(float(9))

#print(float(8.19))

#print(format(123,"d"))

#class details:
#    age=22
#    name="phill"

#details = details()
#print('The age is:',getattr(details,"age"))
#print('The age is:',details.age)

#age=22

#globals()['age'] = 22
#print('the age is:',age)

#list = [1,2,3,4,5] 
#print(list[::-1])

#tuple1 = (1, 2, 3, 4, 5) 
#print(tuple1[::-1])

#def times(x,y):
#    return x*y
#print(times(6,3))
#print(times(3.14,6))
#print(times('HNY',3))

#def list_modify(seq):
#    seq.append('3')
#l=['1','2']
#list_modify(l[:])
#print(l)

#def test_func(y):
 #       x=int(input("Enter value:"))
#        x=x+y
#        y=9
#        return x
#        z=test_func(y)
#        print(z)

x=['1','2','3','4']
y=['A','B','C','D']
zipped=zip(x,y)
list_result=list(zipped)
tuple_result=tuple(zipped)
#print(list_result)
#print(tuple_result)

#for pair in zip(x,y):
       # print(pair)

#for a, b in zip(x,y):
      #  print(a,b)

#[(a,b) for a,b in zip(x, y)]

#[(a,b) for a,b in sorted(zip(x, y))]

x=['1', '2', '3', '4']
y=['A', 'B', 'C', 'D']
zipped = zip(x, y)
list_result = list(zipped)
#print(list_result)
a, b = zip(*list_result)
#print("a= ",a)
#print("b= ",b)

string = "Hello Python"
#(list(reversed(seq_string)))
tuple_input = ('H', 'e', 'l', 'l', 'o', ' ', 'P', 'y', 't', 'h', 'o', 'n')
print(list(reversed(tuple_input)))
range_input = range(2, 50, 5)
print(list(reversed(range_input)))

#components = ['RAM', 'ROM', 'Graphics Card', 'HDD', 'SSD']
#enu_comp = enumerate(components)
#print(type(enu_comp))

#enu_comp = enumerate(components)
#print(list(enu_comp))

value=input("Enter Some Values separated by space : ")
print(value.split())

def calculateAddition(n): 
return n+n  
numbers = (1, 2, 3, 4) 
result = map(calculateAddition, numbers) 
print(result) 




