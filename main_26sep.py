# file handling using python method:

filename="itProjects.txt"

#fp = open(filename, "x")  # "x"---> create a file
fp = open(filename,"w")

data='''
Project name 1:

Weather forecasting system

As a software engineer, there’s nothing more satisfying than working on a rewarding project.
Projects can help build your experience, boost your portfolio, and drive innovation forward.
They can even lead to a public launch.
However, whether you’re a beginner in software engineering projects or highly
experienced in product development, it can be challenging to come up with new ideas.

 Project name 2 :
Age Calculator Application
Address the need for a convenient and user-friendly solution to calculate 
age by developing an Age Calculator Application,
simplifying the process of determining age based on birthdate.

'''
fp.write(data)
fp.close()

fp= open(filename,"a")

newData='''
project 3
 Online Chat Application
Problem Statement: Address the need for real-time communication and collaboration
 by developing an Online Chat Application, 
providing users with an interactive and efficient platform for communication.
'''
fp.write(newData)
fp.close()

filename="itprojects.txt"
fp=open(filename)
details=fp.read
print(fp.read())  # read the file

print(details)
fp.close


file_name="recipe.txt"
fp=open(file_name,"w")

data='''


'''






