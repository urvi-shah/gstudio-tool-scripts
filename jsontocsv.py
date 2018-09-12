import json
import csv
import os 
import sys
import pandas
from pandas.io.json import json_normalize
from datetime import datetime

arg1 = raw_input ("Enter the path of the folder:")
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

jsonfilename = datetime.now().strftime('%Y-%m-%d-%H-%M.json')


head = []
with open(jsonfilename, "w") as outfile:
    for f in file_list:
        with open(os.path.join(arg1,f), 'rb') as infile:
            file_data = json.load(infile)
            head += file_data
    json.dump(head, outfile)

outfile.close()



csvfilename = datetime.now().strftime('%Y-%m-%d-%H-%M.csv')

with open(jsonfilename,'r') as file1:
		
		data1 = json.load(file1)
		data2 = json_normalize(data1)

		data2.to_csv(csvfilename, mode="a", index=False)

file1.close() 