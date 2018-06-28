import json
import csv

infile = open("distros1.json","r")
outfile = open("distros2.csv","w")

# writer = csv.writer(outfile)

# print(json.dumps(infile.read()))
# for row in json.load(infile.read()):
# 	print(row)
#writer.writerow(json.dumps(json.loads(infile.read())))

# inputFile = open("distros1.json","r") #open json file
outputFile = open("distros2.csv","w") #load csv file
# data = json.load(inputFile) #load json content
# inputFile.close() #close the input file
# print(data)
output = csv.writer(outputFile) #create a csv.write
# output.writerow(data.keys())# header row
# output.writerow(data.values())
with open("distros1.json") as f:
	# temp = json.loads(each)

	# list_data = [{"name":"siddhu"},{"name":"abc"}]
	# temp = []
	# temp.append(f)\
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
				output.writerow("abcde")


# for row in data:
#     output.writerow(row) #values row