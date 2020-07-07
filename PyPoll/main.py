import os 
import csv

csvpath= os.path.join("Resources", "election_data.csv")

#set path and open file
#print(csvpath)
with open (csvpath, newline = '') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csv_header=next(csvreader)
    


    #variables
    candidates = {} 
    candidate_list = [] 
    total_votes = 0 
    max_votes = []
    percent = [] 

    #loop to find votes / person
    for row in csvreader:
        total_votes = total_votes + 1
        candidate_name = row[2]

        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidates[candidate_name] = 0

        candidates[candidate_name] = candidates[candidate_name] + 1

#find winner
    max_votes = max(candidates.values())
    winner = [name for name, votes in candidates.items() if votes == max_votes][0]
  
#print statements
print("Election Results")
print("-------------- ")
print(f"Total Votes: {total_votes}")
print("--------------")
for candidate, num_votes in candidates.items():
    print(candidate, ': ', num_votes, " (", str(round(100*num_votes/total_votes)), "%)")
print("-------------- ")
print(f"Winner: {winner}")
print("-------------- ")