import json
import csv
import os 
import sys
import pandas
from pandas.io.json import json_normalize
import pandas.io.json

arg1="/home/urvi/Downloads/samplenestedjson/"

file_list=[]

if os.path.exists(arg1):

	l=os.listdir(arg1)
	for each_file in l:
		if each_file.endswith(".json"):
			print("Iteration")
			file_list.append(each_file)

else:
	print("Not found")
	sys.exit()


head = []
with open("22combine.json", "w") as outfile:
    for f in file_list:
        with open(f, 'rb') as infile:
            file_data = json.load(infile)
            head += file_data
    json.dump(head, outfile)

outfile.close()

with open("22combine.json",'r') as file1:
		
		data1 = json.load(file1)
		data2 = json_normalize(data1)

		data2.to_csv("22result.csv", mode="a", index=False)

file1.close() 

