import shutil
import os

fileName = "ouighour.xml"

file = open(fileName)
newFile = open("tmp.xml", "w")

for line in file:
    if "<meta" in line and not "/>" in line:
        line = line.replace(">","/>")
    newFile.write(line)
   
#shutil.copyfile("tmp.xml",fileName)
#os.remove("tmp.xml")