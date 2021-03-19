#PyBank

#import packages
import os
import csv

#path to get data
bankinfo = os.path.join("resources", "budget_data.csv")

#setting variables to 0
count = 0
profit = 0
pre_value = 0
change = 0

#setting change list
change_list = []

#create csv reader
with open(bankinfo, 'r') as csvfile:
    #setting csv reader to be seperated by commas
    csv_reader= csv.reader(csvfile, delimiter=',')
    #skipping reading the top row
    header = next(csv_reader)

    #run for each row in the data file
    for row in csv_reader:
        #to count each row aka each month
        count = count + 1
        #calcuate profit change per row
        profit = int(row[1]) + profit
        #calcuate change for every row after the first one
        if pre_value == 0:
            pre_value = int(row[1])
        else:
            #find the difference between the current row and the previous row
            change = int(row[1]) - pre_value
            #reset the previous row value as the current row
            pre_value = int(row[1])
            #add the change to list
            change_list.append(change)
    #find average change   
    a_change = round((sum(change_list)/len(change_list)),2)

    #print title of output
    print("Financial Analysis")
    #print dividing line
    print("____________________")
    #print out how many months there are in the data file
    print(f'Total Months: {count}')
    #print total profit (+/-)
    print(f'Total: ${profit}')
    #print average change
    print(f'Average Change: ${a_change}')