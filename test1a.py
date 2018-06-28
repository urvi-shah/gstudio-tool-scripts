import json
import csv
import os

infile = open("distros1.json","r")
outfile = open("distros2.csv","w")
writer=csv.writer(outfile)

#print(json.dumps(infile.read()))

for row in json.loads(infile.read()):
	print(row)
	#writer.writerow(json.dumps(json.loads(infile.read())))
	writer.writerow(row)
