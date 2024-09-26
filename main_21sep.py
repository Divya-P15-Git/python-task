

# Ex.1
#myList=[2,4,3,9,8]
#newList=[]
#for i in myList:
 #   newList.append(i*2)
#print(newList)


#myList=[2,3,4,5,11]
#newlist=list(map(lambda x:x*2,myList))    (by using map function)
#print(newlist)

#Ex.2

# i/p: myList=[2,4,7,9,8]
#o/p:newlist=[2,4,8]

#myList=[2,3,4,5,6,7]
#newList=[]
#for i in myList:
 #   if i % 2 == 0:
  #      newList.append(i)
#print(newList)        

#myList=[2,3,4,5,6,7,8]
#newList=list(filter(lambda x:x %2==0,myList))     (by using filter function)  
#print(newList)

#from functools import reduce
#myList=[2,3,4,5,6]
#sum=reduce(lambda a,b:a+b,myList)    (by using reduce function)
#print(sum)