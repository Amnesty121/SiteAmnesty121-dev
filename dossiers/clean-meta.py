import shutil
import os

fileName = "index-data.xml"

file = open(fileName)
newFile = open("tmp.xml", "w")

for line in file:
    if "<meta" in line:
        line = line.replace(">","/>")
    newFile.write(line)
   
#shutil.copyfile("tmp.xml",fileName)
#os.remove("tmp.xml")