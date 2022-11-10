import os
import csv
import statistics 
csvpath = os.path.join('/Users/iqraimam/Desktop/pythonchallenge', 'budget_data.csv')

txt_path = "output.txt"

months = 0
revenue =  0
rev = []
prevrev = 0
month_change = []
revchange = 0
decrease = ["", 9999999]
increase = ["", 0]
rev_change_list = []
avgrev = 0

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print (csvreader)
    csvheader = next(csvreader)
    csvheader = next(csvreader)

    for row in csvreader:
        months += 1 
        revenue = revenue + int(row[1])
        revchange = float(row[1])-prevrev
        prevrev = float(row[1])
        rev_change_list = rev_change_list + [revchange]
        month_change = [month_change] + [row[0]]
        
        if revchange>increase[1]:
            increase[1] = revchange
            increase[0] = row [0]

        if revchange<decrease[1]:
            decrease[1]=revchange
            decrease[0]=row[0]
    avgrev = sum(rev_change_list)/len(rev_change_list)

    print (months)
    print (revenue)
    print (avgrev)
    print(increase)
    print (decrease)


  