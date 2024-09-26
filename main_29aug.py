#Formulation:

#(a + b)^2=a*a + b*b+2*a*b
'''
a=int(input("Enter a first number : "))
b=int(input("Enter a second number : "))

ans = (a*a) + (b*b) + (2*a*b)
print("(a + b)^2 :",ans)


#Area of circle:

r=int(input("Enter Radius of circle : "))
ans=3.14*r*r
print("Area of Circle :",ans,"sq.cm.")
print(f"Area of circle :{ans} sq.cm.")


# Volume of Sphere:

r=int(input("Enter radius of Shpere: " ))

ans=(4/3)*3.14*r*r*r
print("Volume of Sphere : ",ans)
print("Volume of sphere : {ans} cu.cm.")

from math import*
r=int(input("enter a Radius of Sphere :"))
ans=(4/3)*3.14*r*r*r
print(f"Volume of Sphere : {round(ans,4)} cu.cm")
num=int(input("Enter a number : "))
flag=1
for i in range(2,(num//2)+1):
    if(num%1==0):
        flag=0
        break
    if(flag==1):
        print(f"{num} is prime")
    else:
        print(f"{num} not prime")


num=int(input("Enter a number : "))
temp=str(num)
rev=int(int(temp[::-1]))
print(f"Num :{num}")
print(f"rev:{rev}")
if(num==rev):{
    print(f"{num} is palindrom number ")
}
else:{
    print(f"{num} is  not palindrom number ")
}
'''