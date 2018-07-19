# is instance of dict ni method use karine app data nu reference layine eni andar na contents jevu kai check karine jovaye

import json
import csv
import os 
import sys

program_name=sys.argv[0]
# arg1=sys.argv[1]
# arg2=sys.argv[2]

arg1="/home/urvi/Downloads/samplenestedjson/"
arg2="1.csv"

# arg1=sys.argv[1]
# arg2=sys.argv[2]


json_list=[]

if os.path.exists(arg1):

	l=os.listdir(arg1)
	for each_file in l:
		if each_file.endswith(".json"):
			print("Iteration")
			json_list.append(each_file)

else:
	print("Not found")
	sys.exit()

var=0


	# with open(arg1,"r") as file1:
	# 	data1 = json.load(file1)

with open(arg2, "a") as file:
	for i in json_list:
		with open(i,'r') as file1:
			
			data1 = json.load(file1)

		if var==0:
			csv_file = csv.writer(file)
			y=data1[0].keys()
			iterate_till= len(y)
			# print (y)
			csv_file.writerow(y)

			var=1

		l=[]
		for counter in range(0,iterate_till,1):
			l.append('')

		for item in data1:
			# l = ['','','','','','','']
			for k,v in item.items():
				p = y.index(k)
				l[p] = item[k]
				# print l  #agar list nu display jou hoye values sathe toh aane uncomment kar

			csv_file.writerow(l)


file1.close()
file.close()