
m=open('marks.txt','w')
marks=['arun 80\n','rahul 45\n','meera 90\n','arun 70\n']
m.writelines(marks)
m=open('marks.txt','r')
x=m.readlines()
print(x)
l=open('names.txt','w')
for i in x:
    o=i.split()
    print(o)
    if int(o[1])>75:
       l.writelines(o[0]+'\n')