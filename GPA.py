grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
my_list=list(students)
my_list.sort()
students=my_list
d1=sum(grades[0])/len(grades[0])
d2=sum(grades[1])/len(grades[1])
d3=sum(grades[2])/len(grades[2])
d4=sum(grades[3])/len(grades[3])
d5=sum(grades[4])/len(grades[4])
my_list= [d1, d2, d3, d4, d5]
grades=my_list
GPA=dict(zip(students,grades))
print (GPA)
