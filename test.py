import json
import csv
import os

infile = open("distros.json","r")
outfile = open("distros0.csv","w")
writer=csv.writer(outfile)

#print(json.dumps(infile.read()))

for row in json.loads(infile.read()):
	print(row)
	#writer.writerow(json.dumps(json.loads(infile.read())))
	writer.writerow(row)
