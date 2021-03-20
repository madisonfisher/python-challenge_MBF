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

#setting change_list
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
    #find greatest increase value
    max_Pchange = max(change_list)
    #find greatest decrease value
    max_Nchange = min(change_list)

#recreating csv reader to run through all the rows again
with open(bankinfo, 'r') as csvfile:
    #setting csv reader to be seperated by commas
    csv_reader= csv.reader(csvfile, delimiter=',')
    #skipping reading the top row
    header = next(csv_reader)

    for row in csv_reader:
        #find the difference between the current row and the previous row
        change = int(row[1]) - pre_value
        #reset the previous row value as the current row
        pre_value = int(row[1])
        #to find the month in which the greatest increase happened
        if change == max_Pchange:
            #set the variable as the month
            month_Pchange = row[0]
        #to find the month in which the greatest decrease happened
        elif change == max_Nchange:
            #set the variable as the month
            month_Nchange = row[0]

    #print title of output
    print("Financial Analysis")
    #print dividing line
    print("--------------------")
    #print out how many months there are in the data file
    print(f'Total Months: {count}')
    #print total profit (+/-)
    print(f'Total: ${profit}')
    #print average change
    print(f'Average Change: ${a_change}')
    #print greatest increase
    print(f'Greatest Increase in Profits: {month_Pchange} (${max_Pchange})')
    #print greatest decrease
    print(f'Greatest Decrease in Profits: {month_Nchange} (${max_Nchange})')

#set up the path for the output file
out_text = os.path.join("analysis","PyBank_results.txt")
#open the txt file to write in it 
with open(out_text, 'w') as file:
    #write title of output
    #+ '\n' to go to new line
    file.write("Financial Analysis" + '\n')
    #write dividing line
    file.write("--------------------" + '\n')
    #write out how many months there are in the data file
    file.write(f'Total Months: {count}' + '\n')
    #write total profit (+/-)
    file.write(f'Total: ${profit}' + '\n')
    #write average change
    file.write(f'Average Change: ${a_change}' + '\n')
    #write greatest increase
    file.write(f'Greatest Increase in Profits: {month_Pchange} (${max_Pchange})' + '\n')
    #write greatest decrease
    file.write(f'Greatest Decrease in Profits: {month_Nchange} (${max_Nchange})' + '\n')
