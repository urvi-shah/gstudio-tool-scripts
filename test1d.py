import json
import csv
import os


outputFile = open("distros4.csv","w")
output = csv.writer(outputFile)
with open("distros1.json") as f:
	temp = json.load(f)
	print(temp)
	for each in temp:
		count = 0
		print("+++++++++++++++++++++++")
		print(each)
		print("+++++++++++++++++++++++")
		for key, value in each.items():
			print("=========================")
			print(key)
			print(value)
			if isinstance(key,str):
				print("string---------------------")
			print("=========================")

			if key == "appData":
				print("0000000000000000000000")
				print(dict(value)["language"])
				print("0000000000000000000000")
			
			if key == "language" or key == "userId":
				print("if block")
				print(key)
				#output.writerow("abcde")

