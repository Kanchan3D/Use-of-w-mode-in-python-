f=open("text.txt",'w+')

f.write("Hello Learner")
f.seek(2)
print(f.tell())
text=f.read()
print(text)
f.close

