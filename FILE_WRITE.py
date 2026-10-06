f=open('total_students.txt','w')

students_list=['aadhila\n','akhilesh\n','snehal\n','ajith\n','vinayak\n','sachin\n']
f.writelines(students_list)

u=open('passed_students.txt','w')
passed_students=['aadhila\n','akhilesh\n','snehal\n']
u.writelines(passed_students)


content=['python\n','java\n','php']
u.writelines(content)