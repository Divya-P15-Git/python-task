# List Comperhension:
#myList=[22,3,4,56,87]
#Square=[]
#for i in myList:
 #   Square.append(i**2)
#print("Using method convention method:")
#print(Square)

#Using map function:
#Square=lambda x:x**2
#newlist=list(map(Square,myList))
#print("Using convenstion method :")
#print(newlist)

#Using list Comprehension:
#Square=[x**2 for x in myList]
#print(Square)
#[(element/expression/formate) for element in reference]

#Even : [Element]
#even=[x for x in myList if x%2==0]
#print(even)

# Formate:
# To find x,x**2) list from given list
#myList=[2,3,4,5]
#numAndsqu=[[x,x**2] for x in myList]
#print(numAndsqu)

# Count
#a = [11, 12, 14, 12, 15, 13, 13, 14]
#freq = [(x, a.count(x)) for x in set(a)]
#print(freq)

# We have list of string(word,length)

#words=("Apple","Banana","Cherry","Berry","Date")
#wordlength=[(word,len(word)) for word in words]
#print(wordlength)

#Ex.6: We have of string and get list of words having length > 5

#words=("Apple","Banana","Cherry","Berry","Date")
#mylist=[word for word in words if len(word)>5]
#print(mylist)

#foods=("Vadapav","Panipuri","Modak","Chakali")
#mylist=[word for word in foods if len(word)>6]
#print(mylist)

#books=("Chava","Mahabhart","Geeta")
#mylist=[word for word in books if len(word)>7]
#print(mylist)

#Ex.7 We have to creat list of "string" having "A" as prefix from other list a=[]
#a=["Apple","Ant","Paper","Chair","Airpods","Atul","appu ghar"]
#mylist=[word for word in a if word.startswith("A") ]
#print(mylist)

#ex.8 palindrom no
#a=["1234","456","454","99899","2013","1221"]
#b=[num for num  in a if num == num [::-1]]
#print(b)

#Ex.9:
# We have list of all numbers occured in give string

s="Today at 9:30 we a our python lecture for 1/2 hour"
# o/p : num=[9,3,0,1,2]
num=[int(x) for x in s if x.isdigit()] 
#num=[ n for n  in s if n.isdigit()]
num.sort()
print(num)





