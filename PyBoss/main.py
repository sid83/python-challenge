import csv
import os
import us_state_abbrev
#empty lists
empid=[];name=[];dob=[];ssn=[];state=[]
first_name=[];last_name=[];dob_for=[];ssn_for=[];abbr_state=[]
#csv files to open
file1=os.path.join("raw_data","employee_data1.csv")
file2=os.path.join("raw_data","employee_data2.csv")

# Opening and instantiating csv.reader object
with open(file1,newline='') as csvfile1, open(file2,newline='') as csvfile2:
    csvreader1=csv.reader(csvfile1,delimiter=",")
    csvreader2=csv.reader(csvfile2,delimiter=",")
    # Remove Header
    next(csvreader1,None)
    next(csvreader2,None)
    #reading data
    for row in csvreader1:
        empid.append(row[0])
        name.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])
    for line in csvreader2:
        empid.append(line[0])
        name.append(line[1])
        dob.append(line[2])
        ssn.append(line[3])
        state.append(line[4])

# Splitting name in first and last
for element in name:
    first_name.append(element.split(" ")[0])
    last_name.append(element.split(" ")[1])

# Changing DOB format
for number in dob:
    year=str(number.split("-")[0])
    month=str(number.split("-")[1])
    day=str(number.split("-")[2])
    dob_for.append(f'{month}\{day}\{year}')

# Formatting SSN Field
for x in ssn:
    ssn_for.append(f'***-**-{x.split("-")[2]}')

# Changing state name to abbreviation
for state in state:
    abbr_state.append(us_state_abbrev.us_state_abbrev[state])

# zipping formatted data into tuples
formatted_data=zip(empid,first_name,last_name,dob_for,ssn_for,abbr_state)

# Write formatted output to csv file
file=os.path.join("formatted_data","FormattedData.csv")
# open csv file as write only and write data
with open(file,'w',newline='') as opcsvfile:
    opfile=csv.writer(opcsvfile,delimiter=",")
    opfile.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])
    opfile.writerows(formatted_data)