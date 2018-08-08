#reference: https://www.geeksforgeeks.org/working-csv-files-python/
#importing csv module
import csv
import numpy as np

# csv file name (maybe pass it in as argument)
filename = "sampleData.csv"
 
# initializing the row list, the key (answer to the question) list and item (question: answer list) dictionary
rows = [] #list for 
keys = [] #list for 
items = {} #dictionary for 
mc = []
fr = []
total = []
questions = []
items_1_0 = {}

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting key through first row
    keys = next(csvreader)
    keys = keys[0: - 2] #remove 2 empty spaces (data format issue)
    numQuestions = len(keys)

    # extracting each data row by row
    for row in csvreader:
        rows.append(row)

    #number of students
    numStudents = csvreader.line_num - 2

    #initializing the items dict with question numbers as keys with empty lists.
    for q in rows[0][0:numQuestions]:
        items[q] = []
        questions.append(q)

#appending answers list to the items dictionary
for row in rows[1:]:
    # parsing each column of a row
    index = 1
    for col in row[0:numQuestions]:
        items["q"+str(index)].append(col)
        index += 1
    mc.append(float(row[numQuestions]))
    fr.append(float(row[numQuestions + 1]))
    total.append(mc[-1] + fr[-1])

for x, y in zip(questions, keys):
	for z in items[x]:
		if z == y:
			items_1_0.[x].append(z)
 
fields = ["Item ID", "# of Students Answered Correct", "# of Students Answered Incorrect",
          "Mean Scores of Students Answered Correct", "Mean Scores of Students Answered Incorrect",
          "P Values", "r with MC", "r with FR", "r with MC+FR", "KR-20 if Item Omitted", "KR-20",
          "Key", "#ofA", "#ofB", "#ofC", "#ofD", "#ofE", "#ofF", "%ofA", "%ofB", "%ofC", "%ofD", "%ofE", "%ofF",
          "rofA", "rofB", "rofC", "rofD", "rofE", "rofF"
          ]

#rows
big_data = []



data = dict.fromkeys(fields)

def correct(id, answer):
	count = 0
	for x in items[id]:
		if x==answer:
			count += 1
	return count




#loop through question by question
for x, y in zip(questions, keys):
    data["Item ID"] = x
    data["# of Students Answered Correct"] = correct(x, y)
    data["# of Students Answered Incorrect"] = numStudents-correct(x, y)
    data["Mean Scores of Students Answered Correct"] = 1
    data["Mean Scores of Students Answered Incorrect"] = 1 
    data["P Values"] = 1
    data["r with MC"] = np.correlate(items_1_0[x], mc)
    data["r with FR"] = np.correlate(items_1_0[x], fr)
    data["r with MC+FR"] = np.correlate(items_1_0[x], total)
    data["KR-20 if Item Omitted"] = "-"
    data["KR-20"] = 1 #variable
    data["Key"] = y
    data["#ofA"] = 1
    data["#ofB"] = 1
    data["#ofC"] = 1
    data["#ofD"] = 1
    data["#ofE"] = 1
    data["#ofF"] = 1
    data["%ofA"] = 1
    data["%ofB"] = 1
    data["%ofC"] = 1
    data["%ofD"] = 1
    data["%ofE"] = 1
    data["%ofF"] = 1
    data["rofA"] = 1
    data["rofB"] = 1
    data["rofC"] = 1
    data["rofD"] = 1
    data["rofE"] = 1
    data["rofF"] = 1

    big_data.append(data.copy())







# name of csv file
filename = "Results.csv"
 
# writing to csv file
with open(filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fields)
     
    # writing headers (field names)
    writer.writeheader()
     
    # writing data rows
    writer.writerows(big_data)











