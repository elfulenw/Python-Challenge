import csv,os

file = os.path.join('Resources','budget_data.csv')
file_to_analysisSummary = os.path.join('Resources', 'anaalysisSummary.txt')
months = 0
profit = []
totalProfit = 0
prevValue = 0
netChangelist = []
averageChange = 0
greatestIncrease = 0
greatestDecrease = 0
greatestIncreaseDate = 0
greatestDecreaseDate = 0

with open(file) as readfile:
    csvreader = csv.reader(readfile)

    #skip header and define first row to keep previous values in calculations
    next(csvreader)
    firstrow = next(csvreader)

    months = months + 1
    totalProfit = totalProfit + int(firstrow[1])
    prevValue = int(firstrow[1])
    
    for row in csvreader:
        months = months + 1
        profit.append(row[1])
        totalProfit = totalProfit + int(row[1])
        netChange = int(row[1]) - prevValue
        prevValue = int(row[1])
        netChangelist.append(netChange)
        if netChange > greatestIncrease:
            greatestIncrease = netChange
            greatestIncreaseDate = row[0]
        if netChange < greatestDecrease:
            greatestDecrease = netChange
            greatestDecreaseDate = row[0]
    averageChange = sum(netChangelist)/(months-1)
    prettyamount = f"${averageChange:.2f}\n"        
           

    # #Analysis Summary
    analysisSummary = (
        f"\nFinancial Analysis\n"
        f"----------------------\n"
        f"Total Months: {months}\n"
        f"Total: ${totalProfit}\n"
        f"Average Change: {prettyamount}"
        f"Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncrease})\n"
        f"Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecrease})\n")


    #print
    print(analysisSummary)

    #analysisSummary to a text file
    with open(file_to_analysisSummary, "w") as txt_file:
        txt_file.write(analysisSummary)