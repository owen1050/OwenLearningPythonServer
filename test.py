f = open("test.txt","r+")
data = f.read()
f.close()
f = open("test.txt", "w")
f.write("WORTKED")
f.close()