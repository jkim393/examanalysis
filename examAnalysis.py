#reference: https://www.geeksforgeeks.org/working-csv-files-python/
#importing csv module
import csv

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
 
fields = ["Item ID", "# of Students Answered Correct", "# of Students Answered Incorrect",
          "Mean Scores of Students Answered Correct", "Mean Scores of Students Answered Incorrect",
          "P Values", "r with MC", "r with FR", "r with MC+FR", "KR-20 if Item Omitted", "KR-20"
          ]

#rows
big_data = []



data = dict.fromkeys(fields)

#loop through question by question
for x in questions:
    data["Item ID"] = x
    data["# of Students Answered Correct"] = 50 #function(items, x)
    data["# of Students Answered Incorrect"] = 40 #90 - function(items,x)
    data["Mean Scores of Students Answered Correct"] = 1
    data["Mean Scores of Students Answered Incorrect"] = 1 
    data["P Values"] = 1
    data["r with MC"] = 1
    data["r with FR"] = 1
    data["r with MC+FR"] = 1
    data["KR-20 if Item Omitted"] = "-"
    data["KR-20"] = 1 #variable
    #print (data)
    big_data.append(data.copy())







# # name of csv file
# filename = "Results.csv"
 
# # writing to csv file
# with open(filename, 'w') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames = fields)
     
#     # writing headers (field names)
#     writer.writeheader()
     
#     # writing data rows
#     writer.writerows(big_data)






