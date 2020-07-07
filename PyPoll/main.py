import csv, os

file = os.path.join('Resources', 'election_data.csv')

totalVotes = 0
county = []
candidates = []
candidate_votes = {}
candidate = 0
winner = ['',0]

with open(file) as readfile:
    csvreader = csv.reader(readfile)
    
    #skip header, but start at first row of data
    next(csvreader, None)

    for row in csvreader:
        totalVotes += 1


        # candidates.append(row[2])

        candidate = row[2]

        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        
        candidate_votes[candidate] += 1
    
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        # print(f'{candidate}: {(votes/totalVotes)*100:.3f}% ({votes})')

        if votes > int(winner[1]):
            winner[0] = candidate
            winner[1] = votes
    
    # print(winner[0])

    #total vote count
    # totalVotes = (len(votes))
    # print(totalVotes)

    # #votes by candidate
    # for candidate in candidates:
    #     if candidate == "Khan":
    #         Khan.append(candidates)
    #         KhanVotes = len(Khan)
    #     elif candidate == "Correy":
    #         Correy.append(candidates)
    #         CorreyVotes = len(Correy)
    #     elif candidate == "Li":
    #         Li.append(candidates)
    #         LiVotes = len(Li)
    #     else:
    #         Otooley.append(candidates)
    #         OtooleyVotes = len(Otooley)
    # print(KhanVotes)
    # print(CorreyVotes)
    # print(LiVotes)
    # print(OtooleyVotes)

    # candidate percentages
    # KhanPercentage = (KhanVotes/totalVotes)*100
    # print(f'{KhanPercentage:.3f}%')

    


   #Analysis Summary
analysisSummary = (
    f"\nElection Results\n"
    f"--------------------\n"
    f"Total Votes: {totalVotes}\n"
    f"--------------------\n"
    f"'{candidate}: {(votes/totalVotes)*100:.3f}% ({votes})'\n"
    # f"Khan: {}\n"
    # f"Correy: {}\n"
    # f"Li: {}\n"
    # f"O'Tooley: {}\n"
    f"--------------------\n"
    "Winner":[0],
    f"--------------------\n")

#print
print(analysisSummary)

# #analysisSummary to a text file
# with open(file_to_analysisSummary, "w")_ as txt_file:
#     txt_file.write(analysisSummary)
