#PyPoll

#import packages
import os
import csv

#path to get data
pollinfo = os.path.join("resources", "election_data.csv")

#set variables to 0
count = 0

#create csv reader
with open(pollinfo, 'r') as csvfile:
    #setting csv reader to be seperated by commas
    csv_reader= csv.reader(csvfile, delimiter=',')
    #skipping reading the top row
    header = next(csv_reader)
    print(header)

    #run for each row in the data file
    for row in csv_reader:
        #to count each row aka each votes
        count = count + 1
        
        



    #print title of output
    print("Election Results")
    #print dividing line
    print("____________________")
    #print out how many votes there are in the data file
    print(f'Total Votes: {count}')
    #print dividing line
    print("____________________")
    
    
    

#set up the path for the output file
out_text = os.path.join("analysis","PyPoll_results.txt")
#open the txt file to write in it 
with open(out_text, 'w') as file:
    #write title of output
    #+ '\n' to go to new line
    file.write("Election Results" + '\n')
    #write dividing line
    file.write("____________________" + '\n')
    #write out how many votes there are in the data file
    file.write(f'Total Votes: {count}' + '\n')
    #write dividing line
    file.write("____________________" + '\n')
    