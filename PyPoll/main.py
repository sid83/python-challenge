import csv
import os

# Datafile to open. Change file name to read similarly structured datafiles
datafile=os.path.join("raw_data","election_data_2.csv")
#Creating empty list
votes=[]
# Open and read in a csv.reader's object
with open(datafile,newline='') as csvfile:
    readerfile=csv.reader(csvfile,delimiter=",")
    next(readerfile,None) #removing header row
    for row in readerfile:
        votes.append(row[2])

#Total Number of votes case
total_votes=len(votes)
#Creating Dictionary to count votes of each candidate
votes_eachcandidate={}
for element in votes:
    if element in votes_eachcandidate:
        votes_eachcandidate[element]+=1
    else:
        votes_eachcandidate[element]=1
#Creating Dictionary to calculate vote % of each candidate
votepercent={}
for key in votes_eachcandidate:
    votepercent[key]=votes_eachcandidate[key]/total_votes*100

# Figuring the winner!
winner=max(votes_eachcandidate, key=lambda key: votes_eachcandidate[key])

# Printing Election Results to the terminal
print("Election Results\n------------------------")
print(f'Total Votes: {total_votes}\n------------------------')
for keys in votes_eachcandidate:
    print(f"{keys}: {round(votepercent[keys],0)}% ({votes_eachcandidate[keys]})")
print("------------------------")
print(f"Winner: {winner}")
print("------------------------")

import sys
sys.stdout=open('Results.txt','w')
# Printing Election Results to Results.txt file
print("Election Results\n------------------------")
print(f'Total Votes: {total_votes}\n------------------------')
for keys in votes_eachcandidate:
    print(f"{keys}: {round(votepercent[keys],0)}% ({votes_eachcandidate[keys]})")
print("------------------------")
print(f"Winner: {winner}")
print("------------------------")
