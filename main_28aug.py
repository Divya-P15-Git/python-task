# String:
# Defination:
#String is a sequence of characters,such a word or a sentence.

# Ex.1:

#str1="Hello,Good Morning"
#str2='Hello,Good Morning'
#str3='''Hello,Good Morning'''
#str4="""Hello Good Morning"""
#print(str1)
#print(str2)
#print(str3)
#print(str4)
'''
#Ex.2:(Escape Sequence Character \",\'),\n,\t)
str1="hello,Good,Morning!"

d1='Remaesh Said,"I want apple".'
print(d1)
#Remaesh Said,"I want apple".
d2="Ramesh Said,\"I want apple\"."
print(d2)
#Ramesh Said,"I want apple".
d3="Ramesh Say's,\"I want apple\"."
print(d3)
#Ramesh Say's,"I want apple".
d4='Ramesh Say\'s,"I want apple".'
print(d3)
#Ramesh Say's,"I want apple".

d5='Ramesh Say\'s,"Hello ji\nkese ho".'
print(d5)

d6='Ramesh Say\'s,"Hello ji\tkese ho".'
print(d6)

#Ex.3
#String Concatenation
str1="hello"
str2="Good morning"
str3=str1 + " " +str2
print(str3)
#hello Good morning

#Ex.4
#Formated String:(f-String):
#f-String is a feature i python that allows you to embed expression inside string literals,using
# F prefix before the String. This is a,more readable and effiecent way to format String

a=30 
b=40
ans1="Addition of ",a,"and",b,"is",a+b
print(ans1)
#('Addition of ', 30, 'and', 40, 'is', 70)
ans2="Addition of a and b is a+b"
#Addition of a and b is a+b
print(ans2)

ans3=(f"Addition of {a} and {b} is {a+b})"
print(ans3)
#Addition of 30 and 40 is 70
ans4=("Addition of {} and {} is {}".format(a,b,a+b))
print(ans4)
#Addition of 30 and 40 is 70
print("Addition of %d and %d is %d"%(a,b,a+b))


s="hello, Good morning!"

#print("length :",len(s))

for i in range(len(s)):
    print(s[i],end="")

    print("\n")

    for ch in s:
        print(ch,end="")
        print("\n")
        print(s[0:9])
'''
