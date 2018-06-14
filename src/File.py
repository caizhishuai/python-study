import codecs

f = codecs.open("D://1.txt", "rb")
print(f.read())
print(f.mode)

print(f.name)

with open("D://1.txt", "rb") as t:
    content=t.read()
    print(content)
    print("-----------------")
    print(content.rstrip())

filename="D://3.txt"
c = open(filename, "a") # w a
with open("D://1.txt","rb") as t:
    for line in t:
        c.write(str(line.rstrip()))

c.close()
t.close()


