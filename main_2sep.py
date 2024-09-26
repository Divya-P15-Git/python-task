#Function
#(With para with return)
#ex.1
'''
def percentage():
    marks=[89,76,89,67,87,90]
    count=len(marks)
    total=0
    for mark in marks:
        total = total + mark
    print(f"Total Obtained marks:{total}")
    print(f" Percentage:{round(total/count,2)}")

percentage()

#Method:2
def percentage():
    marks=[89,76,89,67,87,90]
    print(f" Percentage:{round(sum(marks)/len(marks),2)}")

percentage()


#Ex:2

def Percentage():
 ravi ={
        "Maths":89,
        "Science":83,
        "English":78,
        "Histroy":90,
        "Geography":97,
        "Marathi":88
    }
total=0
for subject in ravi:
    print(subject + ":" +str(ravi[subject]))
    total +=ravi[subject]
    print(f"ravi hava total{total}marks")
    print(f"ravi hava{round(total/len(ravi),2)}")

Percentage()'''

#Ex:3
def Percentage(student,name):
    total=0
    for subject in student:
        print(subject + ":" +str(student[subject]))
        total += student [subject]

    print(f"{name} have total{total}marks")
    return round(total/len(subject),2)  
name=input("Enter Student name :")
student={
    "Maths":int(input("Enter marks of Maths :")),
    "English":int(input("Enter marks of Englisg :")),
    "Histrory":int(input("Enter marks of History :")),
    "Geography":int(input("Enter marks of Geography :")),
    "Marathi":int(input("Enter marks of Marathi :")),
    "Science":int(input("Enter marks of Science :"))
}
result=Percentage(student,name)
print(f"{name} have percentage of { Percentage (student , name)}")




