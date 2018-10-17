import os
import shutil
import time
import glob

unifiles = [] #List for storing all files picked from the directory .unl files generated at the time the script runs

#Appending files onto unifiles
for file in glob.glob("*.unl"):
    unifiles.append(file)

#Generating the output file format trunvouYYYYMMDD-HHMMSS.txt
filename2 = time.strftime("%Y%m%d-%H%M%S") 
filename1 = "trunvou" +  filename2 + ".txt"

#Opens outputfile for writing
#loop over the list of files in unifiles
#open each file for reading
#loop over each line in the file stripping six zeros of the 11th and 12th column
#write each line into the output file
#close each input file
f= open(filename1,"w+")
for file in unifiles:
    inputfile = open(file,'r')
    for line1 in inputfile:
        line1 = line1.strip().split("|")
        line1[11] = str(line1[11])[:-6]
        line1[12] = str(line1[12])[:-6]
        line2 = "|".join(line1)
        f.write(line2+ "\n")
        #print(line2)
    inputfile.close()
    
#Closing the output file
f.close()

#Moving each file in unifiles to a different folder
for file in unifiles:
    source = 'D:\\vvvvv\\test\\%s' %file
    destination = "D:\\vvvvv\\test\\Destination\\%s" %file
    shutil.move(source, destination)

#clearing the unifiles list
unifiles = []

