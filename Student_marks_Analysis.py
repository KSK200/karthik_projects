import pandas as pd
import numpy as np
from matplotlib import pyplot as plt  

student_marks=pd.read_csv("student_marks.csv")
print(student_marks)
print("")
print("Enter your Details to get marks")
usn=int(input("Enter the usn:"))
print("")
#if(student_marks[(student_marks["usn"]==usn)]):

res=student_marks[(student_marks["usn"]==usn)]
name=res["name"]
maths=res["Maths"]
physics=res["Physics"]
chem=res["Chemistry"]
Bilogy=res["Biology"]

names = ['Maths', 'Physics', 'Chemistry','Bilogy']  
marks= [int(maths),int(physics),int(chem),int(Bilogy)]  
print(student_marks[(student_marks["usn"]==usn)])
plt.figure(figsize=(9,3))    
plt.subplot(131)  
plt.bar(names, marks)  
plt.subplot(132)  
plt.scatter(names, marks)  
plt.subplot(133)  
plt.plot(names, marks)  
plt.suptitle('Student performance')  
plt.show()

