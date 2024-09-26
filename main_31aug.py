# Function:
#defination:

#Ex.1(No para no return)
'''
def greet():#Function declearation
    print("Good Morning!") #Function(body/defination)
    print("Have nice day")
    print("Welcome")


greet()#function
greet()
greet()
greet()


#Ex.2:
def add():
    a=int(input("Enter a first number :"))
    b=int(input("Enter a second no :"))
    print(a+b)

add()
add()
add()
add()


#Ex.3
def AreaOfCuboid():
    l=int(input("Enter length :"))
    b=int(input("Enter breadth :"))
    h=int(input("Enter a height :"))
    Area=2*(l*b+b*h+h*l)
    print(f"The Area of Cuboid :{Area} cu.cm")

#AreaOfCuboid()
#AreaOfCuboid()
#AreaOfCuboid()
for i in range(5):
    AreaOfCuboid()
   

#Ex.3:
def evenOdd():
    n=int(input("Enter a number :"))
    if(n%2==0):
     print("The number is even")
    else:
       print("The number is odd")

evenOdd()
evenOdd()
evenOdd()
 ''' 
#Ex.4:
def calculateBill():
    item=input("Enter a item name :")
    price=float(input("Enter a price of the item :"))
    tax=float(input("Enter the tax percetage :"))
    tax_amount = (price * tax)/100
    total_bill = (price + tax_amount)
    print(f"Your total bill is :{item}:{total_bill} Rs")

calculateBill()
