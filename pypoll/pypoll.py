import os
import csv
csvpath = os.path.join('/Users/iqraimam/Desktop/pythonchallenge', 'election_data.csv')


total_votes = 0
ccs = 0
dg = 0
rad = 0
winning_candidate = ""
winning_count = 0
winning_percent = 0
cands = ["Diana DeGette","Charles Casper Stockham","Raymon Anthony Doane"]
votes = [dg, ccs, rad]

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    candidates = []
    csvheader = next(csvreader)
    for row in csvreader:
        total_votes += 1
        if row [2] in candidates:
            a = 1
        else:
            candidates.append (row[2])
        if row [2] == "Charles Casper Stockham":
            ccs +=1
        if row [2] == "Diana DeGette":
            dg +=1
        if row [2] == "Raymon Anthony Doane":
            rad +=1

    dict_cands_and_votes = dict(zip(cands,votes))
    key = max(dict_cands_and_votes, key=dict_cands_and_votes.get)

    print (candidates)
    print (total_votes)
    print ("Charles Casper Stockham", ccs, ((ccs/total_votes)*100))
    print ("Diana DeGette", dg, ((dg/total_votes)*100))
    print ("Raymon Anthony Doane", rad, ((rad/total_votes)*100))
    print (f"Winner: {key}")