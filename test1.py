import json 
import csv
import os



inputFile = open("distros1.json","r")      #opened json file
outputFile = open("distros3.json", "w")    #load csv file
data = json.load(inputFile)                #load json content
inputFile.close()                          #close the input file
output = csv.writer(outputFile)            #create a csv.write
output.writerow(data.keys())               #header row
output.writerow(data.values())            
  #  for row in data:
   #     output.writerow(row.values()) #values row
