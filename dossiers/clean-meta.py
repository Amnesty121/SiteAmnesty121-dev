file = open("ouighour.xml")
newFile = open("tmp.xml", "w")

for line in file:
    if "<meta" in line:
        line = line.replace(">","/>")
    newFile.write(line)
   