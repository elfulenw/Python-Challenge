import csv,os

file = os.path.join('Resources','budget_data.csv')

with open(file) as readfile:
    csvreader = csv.reader(readfile)

    next(csvreader)

    months = 0

    for row in csvreader:
        months = months + 1
    
    print('\n\nFinancial Analysis')
    print('----------------------------')
    print('Total Months: ' + str(months))