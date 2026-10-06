# #1 reverse the lines
# u=open('p.txt','r')
# content=u.readlines()
#
# rev=content[::-1]
# u=open('p.txt','w')
# u.writelines(rev)
#
# u.close()
#
# #2 A file totalstudents.txt contains the names of all students in a class,
# # and a file passedstudents.txt contains the names of students who passed.txt the exam.
# # Write a Python program to:
# # Read the names from both files.
# # # Find the students who did not pass.
# # # Write their names to a new file named failedstudents.txt, one name per line.
#
# f=open('total_students.txt','r')
# total=f.readlines()
#
# u=open('passed_students.txt','r')
# passed=u.readlines()
#
# failed=open('failed.txt','w')
# for i in total:
#     if i not in passed:
#         failed.write(i)
#
# #3 # Two files, swiggy.txt and zomato.txt.txt, contain the names of food items ordered from each platform.
# # # Write a Python program to read words from swiggy.txt and zomato.txt.txt, combine them, and count how many
# # times each word appears. Store the result in a dictionary and print it
#
# z=open('zomato.txt','r')
# f1=z.read().split()
#
# s=open('swiggy.txt','r')
# f2=s.read().split()
#
# items=f1+f2
#
# d={}
# for i in items:
#     d[i]=items.count(i)
# print(d)

# A file marks.txt.txt contains the names and marks.txt of students as shown below:
# Anu 80
# Rahul 65
# Meera 90
# Arun 70
# Write a Python program to read the file and write the
# names of students who scored more than 75 marks.txt into a file named names.txt.
f=open('marks.txt','w')
marks=['Anu 80\n','Rahul 65\n','Meera 90\n','Arun 70\n']
f.writelines(marks)
f=open('marks.txt','r')
m=f.readlines()
print(m)

for i in m:
    l=i.split()
    print(l)
    if int(l[1])>75:
        f.write(l[0])



