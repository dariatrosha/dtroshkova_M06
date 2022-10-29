f=open("f.txt","w")
f.write("Last Christmas, I gave you my heart")
f.close()
g=open("g.txt","w")
g.write("But the very next day, you gave it away")
g.close()
h=open("h.txt","w")
with open('f.txt', 'r') as ffile, open("h.txt", 'a') as hfile:
    for i in ffile:
        hfile.write(i)
with open("g.txt", 'r') as gfile, open("h.txt", 'a') as hfile:
    for i in gfile:
        hfile.write(i)
h.close()
something=open("g.txt","r")
smthng=something.read()
number=len(smthng)
print("Количество символов в файле:", number)
