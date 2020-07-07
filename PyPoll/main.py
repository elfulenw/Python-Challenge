import csv, os

file = os.path.join('Resources', 'election_data.csv')

votes = []
totalVotes = 0
county = []
candidates = []
candidate = 0
Khan = []
Correy = []
Li = []
Otooley = []

with open(file) as readfile:
    csvreader = csv.reader(readfile)
    
    #skip header, but start at first row of data
    next(csvreader, None)

    for row in csvreader:
        totalVotes = totalVotes + 1
        votes.append(row[0])
        candidates.append(row[2])
    
    #total vote count
    # totalVotes = (len(votes))
    print(totalVotes)

    #votes by candidate
    for candidate in candidates:
        if candidate == "Khan":
            Khan.append(candidates)
            KhanVotes = len(Khan)
        elif candidate == "Correy":
            Correy.append(candidates)
            CorreyVotes = len(Correy)
        elif candidate == "Li":
            Li.append(candidates)
            LiVotes = len(Li)
        else:
            Otooley.append(candidates)
            OtooleyVotes = len(Otooley)
    print(KhanVotes)
    print(CorreyVotes)
    print(LiVotes)
    print(OtooleyVotes)

    # #candidate percentages
    # KhanPercentage = round((KhanVotes/totalVotes)*100)
    # print(KhanPercentage)

    


   #Analysis Summary
#    analysisSummary = (
#     f"\nElection Results\n"
#     f"--------------------\n"
#     f"Total Votes: {}\n"
#     f"--------------------\n"
#     f"Khan: {}\n"
#     f"Correy: {}\n"
#     f"Li: {}\n"
#     f"O'Tooley: {}\n"
#     f"--------------------\n"
#     f"Winner: {}\n"
#     f"--------------------\n")

# #print
# print(analysisSummary)

# #analysisSummary to a text file
# with open(file_to_analysisSummary, "w")_ as txt_file:
#     txt_file.write(analysisSummary)
