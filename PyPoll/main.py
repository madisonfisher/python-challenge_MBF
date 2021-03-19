#PyPoll

#import packages
import os
import csv

#path to get data
pollinfo = os.path.join("resources", "election_data.csv")

#set variables to 0
count = 0
votes = 0

#set list
candidates = []
votes_count = []

#create csv reader
with open(pollinfo, 'r') as csvfile:
    #setting csv reader to be seperated by commas
    csv_reader= csv.reader(csvfile, delimiter=',')
    #skipping reading the top row
    header = next(csv_reader)

    #run for each row in the data file
    for row in csv_reader:
        #to count each row aka each votes
        count = count + 1
        #find all the names in the file
        #set the variable to the candidate column
        name = row[2]
        #determine if the name is already in the list
        if name not in candidates:
            #if its not then add it to the list 
            candidates.append(name)
        #find how many candidates and put it in a range
        number_can = range(len(candidates))

for x in number_can:
    votes_count.append(0)

#recreate csv reader to run through file from the top
with open(pollinfo, 'r') as csvfile:
    #setting csv reader to be seperated by commas
    csv_reader= csv.reader(csvfile, delimiter=',')
    #skipping reading the top row
    header = next(csv_reader)

    #run for each row in the data file
    for row in csv_reader:
        for x in number_can:
            if candidates[x] == row[2]:
                votes_count[x] += 1
    
    print(candidates)
    print(votes_count)


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
    