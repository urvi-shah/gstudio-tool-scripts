import os
import sys
import csv
import pandas as pd
import datetime
import time

Path_ProgressCSV=raw_input("Enter the path of the folder containing the Progress CSVs:")

headers=['Date','Day','Month','Year','unit_code','server_id','school_name','school_code','module_name','unit_name','username','user_id','first_name','last_name','roll_no','grade',
		'enrollment_status','buddy_userids','buddy_usernames','total_lessons','lessons_visited','percentage_lessons_visited','total_activities',
		'activities_visited','percentage_activities_visited','total_quizitems''visited_quizitems','attempted_quizitems','unattempted_quizitems',
		'correct_attempted_quizitems','notapplicable_quizitems','incorrect_attempted_quizitems','user_files','total_files_viewed_by_user',
		'other_viewing_my_files','unique_users_commented_on_user_files','total_rating_rcvd_on_files','commented_on_others_files','cmts_on_user_files',
		'total_cmnts_by_user','user_notes','others_reading_my_notes','cmts_on_user_notes','cmnts_rcvd_by_user','total_notes_read_by_user',
		'commented_on_others_notes','total_rating_rcvd_on_notes','correct_attempted_assessments','unattempted_assessments','visited_assessments',
		'notapplicable_assessments','incorrect_attempted_assessments','attempted_assessments','total_assessment_items']

file_list=[]

if os.path.exists(Path_ProgressCSV):
	l= os.listdir(Path_ProgressCSV)
	for each_name in l:
		joined_path=os.path.join(Path_ProgressCSV,each_name)
		file_list.append(joined_path)

else:
	print("Path of the folder not found.")
	sys.exit()

os.mkdir(Path_ProgressCSV+"/Date_ModifiedCSV",0755)

for each_file in file_list:
	
	date_string= each_file.split("-")[-2]
	date_object=datetime.datetime.strptime(date_string,'%Y%m%d')
	set_date= date_object.date().strftime("%d %B %Y")
	day = set_date.split(" ")[0]
	month = set_date.split(" ")[1]
	year = set_date.split(" ")[2]
	
	csv_data=pd.read_csv(each_file,delimiter=',')
	csv_data['Date']=set_date
	csv_data['Day']=day
	csv_data['Month']=month
	csv_data['Year']=year
	
	individual=each_file.split("/")[-1]
	new_path= Path_ProgressCSV+"/Date_ModifiedCSV/"+individual

	csv_data.to_csv(new_path, sep=',', index= False, columns=headers)

csvlist=[]

folder_path=Path_ProgressCSV+"/Date_ModifiedCSV/"

j=os.listdir(folder_path)
for each_csvfile in j:
	csvlist.append(each_csvfile)

collation=pd.concat([pd.read_csv(folder_path+c) for c in csvlist])
collation.to_csv(Path_ProgressCSV+"/Collated_CSV.csv",index = False)
print "Collated CSV successsfully created!"




