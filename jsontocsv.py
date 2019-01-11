'''
When this script is run, two inputs are expected from the user:
-The tool name (example: AstRoamer_Element_Hunt_Activity)
-The absolute path of the folder containing the json files(of a single tool) to be converted to csv

This script checks whether or not the path exists
The files having '.json' extension are picked and are collated into a single json file
This collated json is now converted into an output csv file
The csv file is generated with the foldername and the current timestamp

'''

import json
import unicodecsv as csv
import os 
import sys
import pandas
from pandas.io.json import json_normalize
from datetime import datetime

def convert_to_string(s):
    '''
    This function converts unicode to string format

    '''
    try:
        return str(s)
    except:
        return s

def reduce_to_key_value(key,value):
    
    k1= key[len(tool_name)+1:]
    reduced[convert_to_string(k1)] =  convert_to_string(value)   
 
def reduce_the_item(key, value):

    '''
    It normalises the json to granular key value

    Converts 
    {
        a:b
        c:d
        e:[f,g]
        h:{
            i:j
        }

    }

    To
    {
        a:b
        c:d
        e.0:f
        e.1:g
        h.i:j
    }

    '''
    global reduced
    if type(value) is list:                                 # if value is a list
        i=0 
        for sub_item in value:                              # looping for each item in the list
            reduce_the_item(key+'.'+convert_to_string(i), sub_item)
            i=i+1
           
    if type(value) is dict:                                 # if value is a dictionary
        sub_keys = value.keys()                             # fetch all keys 
        for sub_key in sub_keys:                            # looping for each key
            reduce_the_item(key+'.'+convert_to_string(sub_key), value[sub_key])
    
    else:
        flg = True
        if type(value) is list:
            flg = False
        if flg:    
            reduce_to_key_value(key,value)

tool_name=raw_input("Enter the tool name:")                 #input of tool name

folder_path = raw_input ("Enter the path of the folder:")   #input of absolute path of folder

folder_name=folder_path.split("/")[-1:]                     #splitting the path to obtain the folder name

file_list=[]
'''
Checks whether the entered path exists
If path exists, then the json files present in that folder are appended in a list
'''
if os.path.exists(folder_path):

	l=os.listdir(folder_path)
	for each_file in l:
		if each_file.endswith(".json"):
			file_list.append(each_file)

else:
	print("Not found")
	sys.exit()


tstamp=datetime.now().strftime('-%Y-%m-%d-%H-%M-%S')        #current timestamp obtained

jsonfilename=folder_name[0]+tstamp+'.json'                  #current timestamp appended to folder name to jsonfilename

csvfilename=folder_name[0]+tstamp+'.csv'                    #current timestamp appended to folder name to give csvfilename


head = []
'''
Each json file present in the list is collated to give a single json file.
'''
with open(jsonfilename, "w") as fpointer1:
    for f in file_list:
        with open(os.path.join(folder_path,f), 'rb') as fpointer2:
            file_data = json.load(fpointer2)
            head = head+file_data
    json.dump(head, fpointer1)

fpointer1.close()

with open(jsonfilename,'r') as fpointer3:

    json_value = fpointer3.read()
    json_data = json.loads(json_value)

    try:
        process = json_data[tool_name]
    except:
        process = json_data

    final_data = []
    header_name = []
    for each_data in process:
        reduced = {}
        
        reduce_the_item(tool_name, each_data)

        header_name += reduced.keys()

        final_data.append(reduced)

    header_name = list(set(header_name))
    header_name.sort()

fpointer3.close()
'''
The contents of the collated json file are written into a csv file 
'''
with open(csvfilename, 'a+') as fpointer4:
    w = csv.DictWriter(fpointer4, header_name, quoting=csv.QUOTE_ALL, encoding = 'utf-8')
    w.writeheader()
    for each_line in final_data:
        w.writerow(each_line)

'''
Success message is printed 
'''
print ("The csv and the collated json are successfully generated !")
