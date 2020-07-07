import csv, os

file = os.path.join('Resources', 'election_data.csv')
file_to_analysisPollSummary = os.path.join('Resources', 'analysisPollSummary.txt')

totalVotes = 0
county = []
candidates = []
candidate_votes = {}
candidate = 0
winner = ['',0]
candidateData = []

with open(file) as readfile:
    csvreader = csv.reader(readfile)
    
    #skip header, but start at first row of data
    next(csvreader, None)

    for row in csvreader:
        totalVotes += 1
        candidate = row[2]

        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        
        candidate_votes[candidate] += 1

    #Analysis Poll Summary
    analysisPollSummary = (
    f"\nElection Results\n"
    f"--------------------\n"
    f"Total Votes: {totalVotes}\n"
    f"--------------------")
    #print
    print(analysisPollSummary)

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        print(f'{candidate}: {(votes/totalVotes)*100:.3f}% ({votes})')
        candidateData.append(f'{candidate}: {(votes/totalVotes)*100:.3f}% ({votes})')
        if votes > int(winner[1]):
            winner[0] = candidate
            winner[1] = votes

    analysisPollSummary2 = (
    f"--------------------\n"
    f"Winner: {winner[0]}\n"
    f"--------------------\n")

    #print
    print(analysisPollSummary2)

# print(analysisPollSummary, candidateData, analysisPollSummary2)

txt_file = open("analysisPollSummary.txt", "w")
txt_file.write(analysisPollSummary)
txt_file.write("\n")
for line in candidateData:
    txt_file.write(line)
    txt_file.write("\n")
txt_file.write(analysisPollSummary2)
txt_file.close()


#analysisSummary to a text file
# with open(file_to_analysisPollSummary, "w") as txt_file:
#     txt_file.write(analysisPollSummary)