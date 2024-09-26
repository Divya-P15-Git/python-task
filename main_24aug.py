#List is a collection of items that can be of any data type

# -List are denoted by sequence brackets[] and are ordered, meaning that items
#have specific position in the list.

# lists are mutable,meaning that can be modified after creation

#---------------------------------------------------------------

#Ex.1
#nums=[1,2,3,4,0]
#print(type(nums))

#Ex.2
#mylist=[23,4.23,True,"Divya Pawar "]
#print(mylist)

#Ex.3
#  0 1  2  3  4
#a=[1,2,33,44,55]
# -5  -4 -3 -2  -1
#print("List :",a)
#print(a[2])
#print(a[-2])

# Ex.4 
# Sorting od list in A/d order
'''
b=[11,22,88.,34]
print("List :",b)
print("Sorted List :",b.sort())   #(Asdding order)
print("List :",b)
print("Sorted List :",b.sort(reverse=True)) #(disendding order)
print("List :",b)

#Ex.5:
# Romoving of element
mylist=[2,4,3,6,7]
print("orignal list : ",mylist)
mylist[2]=8
print("list after modify :" ,mylist)
mylist.remove(6)
mylist.remove(7)
print("list after remove : ",mylist)

#Ex.6:
# To insert the new element in list :

mylist=[1,2,3,4,5]
print("list :",mylist)

#append:

mylist.append(9)
print("List after append :",mylist)

#insert:

mylist.insert(2,0)
print("List after insert :",mylist)

#Ex.7:

#To find the index of element in list :

mylist=[2,3,4,5,6,7,8,9,0,345,56]
print("Index of 9 :",mylist.index(8))

#Ex.8:

#To find the count of element in the list

mylist=[1,2,3,4,5,1,2,4,5,61,2,4,556,]
print("count of 4 :",mylist.count(4))

#Ex.9:

#to find max and min

mylist=[1,2,3,4,56]
print("Max element : ",max(mylist))
print("Min element : ",min(mylist))


#Ex.10:

#to find the sum of all element in the list 
mylist=[1,2,3,4,5,6]
print("sum of element : ", sum(mylist))

#reverse:

mylist=[2,4,6,8,10]
print("Orignal list :",mylist)
mylist.reverse()
print("After reverse list : ",mylist)'''
