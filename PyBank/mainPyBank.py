import os
import csv

# import file path and ensure it is correct also create a path to txt file
os.chdir("C:\\Users\\verin\\Desktop\\Columbia Data Program\\Python-Challenge\\PyBank")
print(os.getcwd())
filepath = os.path.join(os.getcwd(), "Resources", "budget_data.csv")

# define my variables
budget = {}
months = []
net_profit_losses = []
change = []
meanchange = 0
maxchange = 0
minchange = 0

# open and read csv. create two new lists, one that holds months and the other profit/losses
with open(filepath, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in reader:
        months.append(row[0])
        net_profit_losses.append(int(row[1]))


# find the total number of months
no_of_months = len(months)

# find the net total amount
net_total = 0
for number in net_profit_losses:
    net_total += number
print("Total: ${}".format(net_total))

# find the monthly change to base calculations off 
monthly_changes = []
for i in range(len(net_profit_losses)):
    print(net_profit_losses[i])
    if i > 0:
        print(net_profit_losses[i-1])
        monthly_change = net_profit_losses[i] - net_profit_losses[i-1]
        monthly_changes.append(monthly_change)

# do some stats stuff; find average change, max change, and min change and set them as variables
from statistics import mean
meanchange = round(mean(monthly_changes),2)
maxchange = max(monthly_changes)
minchange = min(monthly_changes)

# create a list that holds all the months and matches the changes 
change_months = months[1:]

# create a dictionary to combine both the change in months and the monthly changes

budget_dict = dict(zip(change_months,monthly_changes))
key_list = list(budget_dict.keys())
val_list = list(budget_dict.values())

# use the dictionary to find the corresponding values for the max change and the min change

monthyearmax = key_list[val_list.index(maxchange)]
monthyearmin = key_list[val_list.index(minchange)]
print(monthyearmax)
print(monthyearmin)


#print the final output
print('Financial Analysis')
print('----------------------------')
print("Total Months: {}".format(no_of_months))
print("Total: ${}".format(net_total))
print("Average Change: ${}".format(meanchange))
print("Greatest Increase in Profits: {}".format(monthyearmax) + " ($" + (str(maxchange)) + ")")
print("Greatest Decrease in Profits: {}".format(monthyearmin) + " ($" + (str(minchange)) + ")")

#export as txt file 
output = f'''Financial Analysis
------------------------------------
Total Months:{no_of_months}
Total:${net_total}
Average Change:${meanchange}
Greatest Increase in Profits: {monthyearmax} (${maxchange})
Greatest Decrease in Profits: {monthyearmin} (${minchange})'''

pathout = os.path.join("Analysis", "budget_analysis.txt")

# export the results as a text file
with open(pathout, "w") as txtfile:
    txtfile.write(output)
    
