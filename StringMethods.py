#---------------------------------------------------
#-------String Methods------------------------
#--------------------------------------------
print("Hello World!")

import matplotlib.pyplot as plt

fig = plt.figure()
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
fig.savefig("plot.png")
a="I Love Python and c#"

d="I-Love-Python-and-c#"

print (a.lower())
print (a.rsplit())

print (d.rsplit("-",2))

#index(sub,start,end) search for character in text and bring the index but if the charachter not found give not found error
print(a.index("P"))

#found(sub,start,end) search for character in text and bring the index but if the charachter not found give -1

print(d.find("p"))

#rjust(width,character) & ljust(width,character)

c="Hassan" 
print(c.rjust(5,'#'))

print(c.ljust(5,'#'))

#splitlines() return each line in list 

f= """first line
second line
third line"""

print(f.splitlines())
#expandtabs() controle tabs size between words

g="i\tlove\tpython"
print(g.expandtabs(2))

print(g.expandtabs(20))

#istitle() all words start with capital letter and chracters after numbers is capital
#isspace()
#islower()all words start with lower charachter 
 #isidentifier() check the text can be variable or not 
 
three="hassan_Gabr100"
four="hassan--gabr"
 
print(three.isidentifier())
print(four.isidentifier())

#isalpha() check ifthe text is alphabitic only 

x="ASDHhdhfdfgdfg"
y="Ahshssggagag100"

print(x.isalpha())
print(y.isalpha())

#isalnum() check if the text alphabitic and numbers tgether or not 

print(x.isalnum())
print(y.isalnum())


#replace("old Value", "new Value", count) replace exissting text with new one any count 

d="Hello one two three one one one"

print(d.replace("one","1",2))

print(d.replace("one","1"))

#join("seperator", itterable) return list or tuble to norml string

mylist=["Hassan","Ahmed","ismail","gabr"]

print("-".join(mylist))


#---------------------------------------------------
#-------String Formating------------------------
#--------------------------------------------
#Old formating %s ==> string , %d==> decimel , %f ==> float

name="Hassan"
age=38
rank=10

print("my name is: %s , my age is %d and my rank is %d" %(name,age,rank))

print("my name is: %s , my age is %d and my rank is %.2f" %(name,age,rank))

#new formating {} ==> PLace hholder and .format function



print("my name is:{} , my age is {} and my rank is {}" .format(name,age,rank))

print("my name is: {:s} , my age is {:d} and my rank is {:f}" .format(name,age,rank))



#	Money Format

MyMoney = 500030399383377

print("My Bacnk account have: {:d}" .format(MyMoney))

print("My Bacnk account have: {:,d}" .format(MyMoney)) #formating money by , after each 3 number and take care it's only working with , and _


# ReArrange Items

a,b,c = "One","two", "Three"

print("Hello {} {} {}" .format(a,b,c))

print("Hello {2} {1} {0}" .format(a,b,c)) #print Hello Three two one 


#-----------Python 3.6+-----------
#New formating way

print("My Name is: {name} and my age is {age}")

print(f"My Name is: {name} and my age is {age}")

#PyFORMAT WEBSITE ONLY FOR python format.info

#----------------------------------------------
#---------Numbering----------------------------
#----------------------------------------------

#Complex Numbers for engineering

MyComplex=5+6j

print(type(MyComplex))

print("my real number is {}" .format(MyComplex.real))

print("my imaganairy number is {}" .format(MyComplex.imag))


#----------------------------------------------
#---------Arithmetice Operation----------------------------
#----------------------------------------------
#[+] Addetion 
#[-] Subtruction
#[*] Multiplication
#[/] Devision
#[%] Modulus 
#[**]Eponent
#[//]Floor Devision
#----------------------------------------------

print (10 % 3)

print (22 % 5)

print (2 ** 5) #==> print(2 * 2 * 2 * 2 * 2)==32 

print(100//20) # =5
print(119//20) # =5
print(120//20) # =6


#----------------------------------------------
#---------Lists--------
#----------------------------------------------
# [1] List Items Enclosed in square Brackets
# [2] List Are Ordered, To Use Index Access items
# [3] List Are Mutble ==> Add, Delete, Update
# [4] List Items is not Unique.
# [5] List can have Different Data Type
# ---------------------------------------------

MyAwsomeList = ["One", "Two", "One", 1,100.5, True]
print(MyAwsomeList)
MyAwsomeList[1:3] = [2,1] # update 
print(MyAwsomeList)

MyAwsomeList[1:3] = [] # Delete 
print(MyAwsomeList)



#----------------------------------------------
#---------Lists Methods--------
#----------------------------------------------
# Append()

MyFriends = ["Hassan","Omar", "Malika"]
MyBrothers = ["Walid", "Khalid", "Asmaa"]


MyFriends.append("Dina")
print(MyFriends)

MyBrothers.append(MyFriends)

print(MyBrothers)

print(MyBrothers[3][3]) # Bring 4th element from the 3rd element which is List

#Extend() extend the list by another list items 

a = [1,2,3,4]
b = ["A", "B", "C"]
a.extend(b)
print(a)

#Remove()

d = [1,2,3,"Hassan", "Omar", "Hassan" , "Hassan", "Hassan"]

d.remove("Hassan")

print(d)

#Sort() sort the list elements 

y=[1,20,-10,50,150,75,90]

y.sort()
print(y)

y.sort(reverse=True)
print(y)

#Reverse() bring and reorder the list items from last item to the first 

z=[20,3,5,"Hassan",100,80]

z.reverse()
print(z)

#clearr() remove all list items but keep the list exit

z.clear()
print(z)

#copy()

b=[1,2,3,4]
c=b.copy()

print(b)
print(c)

b.append(5)
print(b) #Main List
print(c) #Coppied List not related to main list if any change to main list not reflected to the coppied list.

#count()
d =[1,2,3,4,1,9,10,2,1]
print(d.count(1))

#index()
e = ["Hassan","Omar","Malika" ,"Khalid"]
print(e.index("Hassan"))


#insert(index, object) insert object before index 

f = [1,2,3,4,5,"A", "B"]

f.insert(0,"Test")
print(f)
f.insert(-1, "Test")
print(f)

#pop(index)
#index Remove and return item at index (default last)
#Raises IndexEroor if list is empty or index is out of range.

g = [1,2,3,4,5]
print(g.pop(2))
print(g) 

print("#" * 100)
#----------------------------------------------
#---------TYPE Conversion--------
#----------------------------------------------
#str() ==>convert to string

#tuple()

c="Hassan"					#String
d = [1,2,3,4,5]          #list
e = {"A", "B", "C"}      #SET
f = {"A": 1, "B":2}		#Dictionary

print(tuple(c))

print(tuple(d))

print(tuple(e))

print(tuple(f))

print("#" * 50)

#List()

c = "Hassan"				#String
d = (1,2,3,4,5)          #Tuble
e = {"A", "B", "C"}      #SET
f = {"A": 1, "B":2}		#Dictionary

print(list(c))

print(list(d))

print(list(e))

print(list(f))

print("#" * 50)


#set()

c = "Hassan"				#String
d = (1,2,3,4,5)          #Tuble
e = ["A", "B", "C"]      #List
f = {"A": 1, "B":2}		#Dictionary

print(set(c))

print(set(d))

print(set(e))

print(set(f))

print("#" * 50)

#Dict() 

#cannot convert from strig to dict
#cannot connvert from set to dict "unhashable type:set"
#can convert from tuple & list to dict if nested tuble and nested list

d = (("A",1),("B",2),("C",3))  			#Nested Tuple
e = [["One",1],["Two", 2],["Three",3]] #nexsted List

print(dict(d))
print(dict(e))

Print("#"*100)
#----------------------------------------------
#---------User Input--------
#----------------------------------------------

#input()

fName = input('What\'s your First name')

mName = input('What\'s your Second name')

lName = input('What\'s your Last name')

fName= fName.strip().capitalize()

mName= fName.strip().capitalize()

lName= fName.strip().capitalize()


print(f	"Hello {fName) {mName} {lName} Happy To See You.")