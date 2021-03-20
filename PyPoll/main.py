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
percent_votes = []

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

#create a 0 count list
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
        #run throough each candidate
        for x in number_can:
            #if the candidate name appears on the row it will be counted
            if candidates[x] == row[2]:
                #adds one vote to previous value in that candidate's index
                votes_count[x] += 1

    #calcuate percent for each candidate
    for x in number_can:
        #formula for percent being rounded
        percent = round((votes_count[x]*100 / count),2)
        #adding calculated percent to list
        percent_votes.append(percent)

    #calculate the winner
    #set base values in case no one beats the first value
    winner = candidates[0]
    value = votes_count[0]
    #run through all the candidates 
    for x in number_can:
        #compare to the current highest
        if value < votes_count[x]:
            #if the listed votes in the index is higher than the original it replaces it as the new highest
            value = votes_count[x]
            #saves the name of the candidate attached to the new highest votes
            winner = candidates[x]  

#print title of output
print("Election Results")
#print dividing line
print("____________________")
#print out how many votes there are in the data file
print(f'Total Votes: {count}')
#print dividing line
print("____________________")
#run through all candidates
for x in number_can:
    #prints the data for all the candidates
    print(f'{candidates[x]}: {percent_votes[x]}% ({votes_count[x]})')   
#print dividing line
print("____________________")
#print winner
print(f'Winner: {winner}')
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
    