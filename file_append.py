f=open('append.txt','r+')
content=f.read()
c=open('p.txt','a+')
c.write(content)
c.write('\najith')
print('current possistion',c.tell())
c.seek(3)
print('current possition',c.tell())
c.write('LLM')






