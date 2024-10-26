import numpy as np
data_type=[('name','S15'),('class',int),('height',float)]
student_details=[('Ali',3,80),('Naila',9,170),('Umaima',10,120)]
students=np.array(student_details,dtype=data_type)
print(students)
print(np.sort(students,order='height'))