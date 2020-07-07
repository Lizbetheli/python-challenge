import os 
import csv

csvpath= os.path.join("Resources", "election_data.csv")

#set path and open file
#print(csvpath)
with open (csvpath, newline = '') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csv_header=next(csvreader)
    #first_row = next(csvreader) 


    #dictionary
    candidates = {}
    candidate_list = []
    total_votes = 0
    max_votes = []
    #loop
    for row in csvreader:
        total_votes = total_votes + 1
        candidate_name = row[2]

        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidates[candidate_name] = 0

        candidates[candidate_name] = candidates[candidate_name] + 1
    
    #winner = candidates[candidatesCount.index(max(candidate_list))]
    '''for x in range(len(candidate_name)):       
 
        if candidate_name[x] > max_votes :
           max_votes = candidate_name[x]
           max_index = x
    election_winner = candidate_name[max_index]  
print(election_winner)
print(max(int(s) for s in candidates))'''
#print statements 
print("Election Results")
print("-------------- ")
print(f"Total Votes: {total_votes}")
print("--------------")
for key, value in candidates.items():
    print(key, ' : ', value)
print("-------------- ")
print("Winner: {winner}")
print("-------------- ")