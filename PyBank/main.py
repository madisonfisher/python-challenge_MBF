#PyBank

#import packages
import os
import csv

#path to get data
bankinfo = os.path.join("resources", "budget_data.csv")

#setting count to 0
count = 0

#create csv reader
with open(bankinfo, 'r') as csvfile:
    #setting csv reader to be seperated by commas
    csv_reader= csv.reader(csvfile, delimiter=',')
    #skipping reading the top row
    header = next(csv_reader)
    #printing the information in the top row
    print(header)

    for row in csvfile:
        count = count + 1
    print(f'Total Months: {count}')