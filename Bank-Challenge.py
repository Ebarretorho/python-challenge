#Import modules

import os
import csv
from sre_constants import RANGE_UNI_IGNORE
from statistics import mean
from tkinter.tix import INTEGER

#Define file path

budget_data_path = os.path.join("Resources","budget_data.csv")

#Buil list for all months, results, and MoM changes

report_month = []
results = []
MoM_change = []


with open(budget_data_path,'r') as budgetfile:
    budget_data = csv.reader(budgetfile,delimiter=',')

    header = next(budget_data)

    for row in budget_data:

        report_month.append(row[0])
        results.append(int(row[1]))

    for i in range(int(len(results))-1):

        MoM_change.append( int(results[i+1]) - int(results[i]))


#With our lists set, we can now loop throug indexes and find the variables we are looking for

#Find highest month change.

highest_change = int(max(MoM_change))
lowest_change = int(min(MoM_change))

for i in range(len(MoM_change)):
    if MoM_change[i] == highest_change:
        highest_change_index = (i+1)

for i in range(len(MoM_change)):
    if MoM_change[i] == lowest_change:
        lowest_change_index = (i+1)


print(f'------------ Financial Analysis ------------')
print(f'* - * - * - * - * - * - * - * - * - * - * - *')
print(f'Total Months:{len(report_month)}')
print(f'Total: ${int(sum(results))}')
print(f'Average Change: ${float(int(sum(MoM_change))/int(len(MoM_change))):.2f}')
print(f"Greatest increase in profits: {report_month[highest_change_index]} (${highest_change})")
print(f"Greatest Decrease in Profits: {report_month[lowest_change_index]} (${lowest_change})")


output_path = os.path.join( "output", "Bank.txt")

with open(output_path, 'a') as txtfile:
    txtfile.writelines(f'------------ Financial Analysis ------------')
    txtfile.writelines('\n')
    txtfile.writelines(f'* - * - * - * - * - * - * - * - * - * - * - *')
    txtfile.writelines('\n')
    txtfile.writelines(f'Total Months:{len(report_month)}')
    txtfile.writelines('\n')
    txtfile.writelines(f'Total: ${int(sum(results))}')
    txtfile.writelines('\n')
    txtfile.writelines(f'Average Change: ${float(int(sum(MoM_change))/int(len(MoM_change))):.2f}')
    txtfile.writelines('\n')
    txtfile.writelines(f"Greatest increase in profits: {report_month[highest_change_index]} (${highest_change})")
    txtfile.writelines('\n')
    txtfile.writelines(f"Greatest Decrease in Profits: {report_month[lowest_change_index]} (${lowest_change})")