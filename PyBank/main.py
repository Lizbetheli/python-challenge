#dependancies
import os
import csv

csvpath= os.path.join("Resources","budget_data.csv")

print(csvpath)
with open(csvpath,newline='') as csvfile:
    #to read the file as a CSV file
    csvreader=csv.reader(csvfile,delimiter=',')
    csv_header=next(csvreader)

    #variables
    total_months = 0
    total_net = 0
    date = []
    net_change_list = []
    first_row = next(csvreader) 
    total_net += int(first_row[1])
    prev_net=int(first_row[1])
    
    #loop for going through page for months, average
    for row in csvreader:
        total_months += 1
        total_net += int(row[1])
        net_change = int(row[1])- prev_net 
        prev_net = int(row[1])
        net_change_list += [net_change]    
        average_change = sum(net_change_list) / len(net_change_list)    

#for max and min numbers
        date.append(row[0])
        max_increase = max(net_change_list)
        min_decrease = min(net_change_list)
#for max and min date 
        max_date = date[net_change_list.index(max_increase)]
        min_date = date[net_change_list.index(min_decrease)]
    
#print statements
    print(f'Financial Analysis' + '\n')
    print(f'------------------'+ '\n')
    print("Total:" + str(total_months))
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {max_date} (${max_increase})")
    print(f"Greatest Decrease in Profits: {min_date} (${min_decrease})")
    