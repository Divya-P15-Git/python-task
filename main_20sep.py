# args and kwargs
'''
Ex.1
def add(*digits):
    print(digits)
    sum = 0
    for i in digits:
        sum +=i
    print(sum)

add(2,4,567,899,67)

#Ex.2

def percentage(**marks):
    total=0
    for sub in marks:
        total += marks[sub]
    print(f"Total marks :{total} outoff 600")

    per=(total/600)*100
    print(f"Percentage:{round(per,2)}%")

percentage(math=99,Eng=87,sci=98,marathi=71,hindi=81,socialSci=86)
percentage(maths=99,Eng=85,sci=98,it=180,evs=98)
'''
 
 #lambda Expression:
#Ex.1
#sqr =lambda x: x**2

#print(sqr(8))
#print(sqr(25))

#Ex.2 
#sqr=lambda x: x**2
#isEven =lambda x:"Even" if(x%2==0) else "odd"
#print(isEven(36))

