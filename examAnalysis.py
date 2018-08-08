#reference: https://www.geeksforgeeks.org/working-csv-files-python/
#importing csv module
import numpy as np
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
        items_1_0[q] = []
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
                items_1_0[x].append(1)
            else:
                items_1_0[x].append(0)

 
fields = ["Item ID", "# of Students Answered Correct", "# of Students Answered Incorrect",
          "Mean MC Scores of Students Answered Correct", "Mean MC Scores of Students Answered Incorrect", 
          "Mean FR Scores of Students Answered Correct", "Mean FR Scores of Students Answered Incorrect",
          "Mean Total Scores of Students Answered Correct", "Mean Total Scores of Students Answered Incorrect",
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

def meanCorrect(itemsID, answer, listTestScores):
    sum = 0
    count = 0
    for response, score in zip(items[itemsID], listTestScores):
        if response == answer:
            sum += score
            count += 1
    return sum/count

def meanIncorrect(itemsID, answer, listTestScores):
    sum = 0
    count = 0
    for response, score in zip(items[itemsID], listTestScores):
        if response != answer:
            sum += score
            count += 1
    if count != 0:
        return sum/count
    else:
        return "-"

def countAnswerChosen(itemsID, answer):
    count = 0
    for response in items[itemsID]:
        if response == answer:
            count += 1
    return count

def r(id, score):
    if numStudents == correct(questions, keys):
        return "-"
    else:
        return np.corrcoef(items_1_0[id],score)[1,0]

#loop through question by question
for x, y in zip(questions, keys):
    data["Item ID"] = x
    data["# of Students Answered Correct"] = correct(x, y)
    data["# of Students Answered Incorrect"] = numStudents-data["# of Students Answered Correct"]
    data["Mean MC Scores of Students Answered Correct"] = meanCorrect(x,y,mc)
    data["Mean MC Scores of Students Answered Incorrect"] = meanIncorrect(x,y,mc)
    data["Mean FR Scores of Students Answered Correct"] = meanCorrect(x,y,fr)
    data["Mean FR Scores of Students Answered Incorrect"] = meanIncorrect(x,y,fr)
    data["Mean Total Scores of Students Answered Correct"] = meanCorrect(x,y,total)
    data["Mean Total Scores of Students Answered Incorrect"] = meanIncorrect(x,y,total)
    data["P Values"] = data["# of Students Answered Correct"]/numStudents
    data["r with MC"] = r(x, mc)
    data["r with FR"] = r(x, fr)
    data["r with MC+FR"] = r(x, total)
    data["KR-20 if Item Omitted"] = "-"
    data["Key"] = y
    data["#ofA"] = countAnswerChosen(x, "a")
    data["#ofB"] = countAnswerChosen(x, "b")
    data["#ofC"] = countAnswerChosen(x, "c")
    data["#ofD"] = countAnswerChosen(x, "d")
    data["#ofE"] = countAnswerChosen(x, "e")
    data["#ofF"] = countAnswerChosen(x, "f")
    sum = data["#ofA"]+data["#ofB"]+data["#ofC"]+data["#ofD"]+data["#ofE"]+data["#ofF"]
    data["%ofA"] = data['#ofA']/sum
    data["%ofB"] = data['#ofB']/sum
    data["%ofC"] = data['#ofC']/sum
    data["%ofD"] = data['#ofD']/sum
    data["%ofE"] = data['#ofE']/sum
    data["%ofF"] = data['#ofF']/sum
    data["rofA"] = 1
    data["rofB"] = 1
    data["rofC"] = 1
    data["rofD"] = 1
    data["rofE"] = 1
    data["rofF"] = 1

    big_data.append(data.copy())


PQ = []
	
for x in big_data:
	p = x["P Values"]
	q = 1 - x["P Values"]
	mulval = p*q
	PQ.append(mulval)

pqSum = sum(PQ) 
variance = np.var(mc)

kr20 = (numQuestions/(numQuestions-1))*(1-pqSum/variance)
print(kr20)







# name of csv file
filename = "Results.csv"
 
# writing to csv file
with open(filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fields)
     
    # writing headers (field names)
    writer.writeheader()
     
    # writing data rows
    writer.writerows(big_data)






