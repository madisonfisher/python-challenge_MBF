#PyBank

#import packages
import os
import csv

#path to get data
bankinfo = os.path.join("resources", "budget_data.csv")

#setting variables to 0
count = 0
profit = 0

#create csv reader
with open(bankinfo, 'r') as csvfile:
    #setting csv reader to be seperated by commas
    csv_reader= csv.reader(csvfile, delimiter=',')
    #skipping reading the top row
    header = next(csv_reader)
    #printing the information in the top row
    print(header)

    #run for each row in the data file
    for row in csv_reader:
        #to count each row aka each month
        count = count + 1
        row_profit = int(row[1])
        profit = row_profit + profit
        
    
    #print title of output
    print("Financial Analysis")
    #print dividing line
    print("____________________")
    #print out how many months there are in the data file
    print(f'Total Months: {count}')
    #print total profit (+/-)
    print(f'Total: ${profit}')