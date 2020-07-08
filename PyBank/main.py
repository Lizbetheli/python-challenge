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

    first_row = (next(csvreader))
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
        average_change_round = round(average_change,2)

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
    print("Total Months:" + str(total_months))
    print(f"Average Change: ${average_change_round}")
    print(f"Greatest Increase in Profits: {max_date} (${max_increase})")
    print(f"Greatest Decrease in Profits: {min_date} (${min_decrease})")

#export a text file
output_path=os.path.join("..", "PyBank","Analysis.txt")
with open(output_path, 'w', newline= '') as text_file:
#contents of text file 
        print(f'Financial Analysis' + '\n', file=text_file)
        print(f'------------------'+ '\n',file=text_file)
        print("Total Months:" + str(total_months),file=text_file)
        print(f"Average Change: ${average_change_round}",file=text_file)
        print(f"Greatest Increase in Profits: {max_date} (${max_increase})",file=text_file)
        print(f"Greatest Decrease in Profits: {min_date} (${min_decrease})",file=text_file)
