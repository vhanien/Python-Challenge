import os
import csv

# import file path and ensure it is correct also create a path to txt file
os.chdir("C:\\Users\\verin\\Desktop\\Columbia Data Program\\Python-Challenge\\PyPoll")
print(os.getcwd())
filepath = os.path.join(os.getcwd(), "Resources", "election_data.csv")
pathout = os.path.join("Analysis", "election_analysis.txt")
print(filepath)
print(pathout)

#define variables 
khanvotes = 0
correyvotes = 0
livotes = 0
otooleyvotes = 0
totalvotes = 0

# open and read csv.
with open(filepath, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

# create a for loop to go through second column of data for each candidate, retrive the total vote and store votes for each candidate
    for row in reader:
        
        # find total votes cast
        totalvotes += 1
        
        # find total votes won per candidate
        if (row[2] == "Khan"):
            khanvotes += 1
        elif (row[2] == "Correy"):
            correyvotes += 1
        elif (row[2] == "Li"):
            livotes += 1
        else:
            otooleyvotes += 1

#quick check on the vote totals 
print(totalvotes)
print(khanvotes)
print(correyvotes)
print(livotes)
print(otooleyvotes)

#do some quick maths to figure out the winners 
winner = max (khanvotes,correyvotes,livotes,otooleyvotes)

if winner == khanvotes:
    winneris = "Khan"
elif winner == correyvotes:
    winneris = "Correy"
elif winner == livotes:
    winneris = "Li"
else:
    winneris = "O'Tooley"

#quickwinnercheck
print(winneris)

#do some quick maths to get some percents
khanpercent = khanvotes/totalvotes
correypercent = correyvotes/totalvotes
lipercent = livotes/totalvotes
otooleypercent = otooleyvotes/totalvotes

#quick check on the percents 
print(khanpercent)
print(correypercent)
print(lipercent)
print(otooleypercent)

# Print Analysis
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {totalvotes}")
print(f"---------------------------")
print(f"Khan: {khanpercent:.3%}({khanvotes})")
print(f"Correy: {correypercent:.3%}({correyvotes})")
print(f"Li: {lipercent:.3%}({livotes})")
print(f"O'Tooley: {otooleypercent:.3%}({otooleyvotes})")
print(f"---------------------------")
print(f"Winner: {winneris}")
print(f"---------------------------")


#export as txt file 
output = f'''Election Results
------------------------------------
Total Votes:{totalvotes}
------------------------------------
Khan:{khanpercent:.3%} ({khanvotes})
Correy:{correypercent:.3%} ({correyvotes})
Li: {lipercent:.3%} ({livotes})
O'Tooley:{otooleypercent:.3%} ({otooleyvotes})
------------------------------------
Winner:{winneris}
------------------------------------ '''

pathout = os.path.join("Analysis", "election_analysis.txt")

# export the results as a text file
with open(pathout, "w") as txtfile:
    txtfile.write(output)
    
