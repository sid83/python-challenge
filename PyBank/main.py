import csv
import os

# csv file to read, change CSV file name to process other similar structured dataset
csvfile=os.path.join("budget_data_2.csv")
# Empty lists
month=[]
revenue=[]
change=[]
# Open File and instantiating as object of class csv.reader
with open(csvfile,newline="") as data:
    budgetdata=csv.reader(data,delimiter=",")
    #skip header
    next(budgetdata,None)
    # applying conditionals to object (budgetdata) of csv.reader class
    for row in budgetdata:
        # date=row[0].split('-')
        month.append(row[0])
        revenue.append(row[1])

#Calculation of total number of months and total revenue
number_months=len(month)
total_revenue=sum(int(i) for i in revenue)

# Revenue Change Calculation
for j in range(len(revenue)-1):
    revenue_change=int(revenue[j+1])-int(revenue[j])
    change.append(revenue_change)

#calculation of mean, greatest incr and greatest decrease
mean_revch=round(float(sum(change)/len(change)))
max_increase=max(change)
indx_maxincr=change.index(max_increase)
max_decrease=min(change)
indx_maxdecr=change.index(max_decrease)

#Printing Final Answers
"""revenue change array has one less element than the month array. Add one to the indx_maxincr"""
print("\n Financial Analysis \n -------------------------------------------")
print(f"Total Months: {str(number_months)}")
print(f"Total Revenue: ${total_revenue}")
print(f'Average Revenue Change: ${mean_revch}')
print(f"Greatest Increase in Revenue: {month[indx_maxincr+1]} (${max_increase})")
print(f"Greatest Decrease in Revenue: {month[indx_maxdecr+1]} (${max_decrease})")

#Printing answers in a text file
import sys
sys.stdout=open('Results.txt','w')
print("\n Financial Analysis \n -------------------------------------------")
print(f"Total Months: {str(number_months)}")
print(f"Total Revenue: ${total_revenue}")
print(f'Average Revenue Change: ${mean_revch}')
print(f"Greatest Increase in Revenue: {month[indx_maxincr+1]} (${max_increase})")
print(f"Greatest Decrease in Revenue: {month[indx_maxdecr+1]} (${max_decrease})")
