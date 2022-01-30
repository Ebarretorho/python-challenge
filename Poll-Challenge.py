#Poll-Challenge

import os
import csv
from random import randrange


poll_data_path = os.path.join("Resources","election_data.csv")


candidates = []

with open(poll_data_path,'r') as votesfile:
    election_data = csv.reader(votesfile,delimiter=',')

    header = next(election_data)

    for row in election_data:

        candidates.append(row[2])

sortedcandidates = sorted(candidates)

uniquecandidates = []

for i in range(len(sortedcandidates)):

    if sortedcandidates[i] != sortedcandidates[i-1]:
        
        uniquecandidates.append(sortedcandidates[i-1])

votes = 0
pct = 0

totalvotes = []
votepct = []

for candidate in uniquecandidates:

    for i in range(len(candidates)):

        if candidates[i] == candidate:
            votes = votes+1

    totalvotes.append(votes)
    pct = float(float(votes)/float(len(sortedcandidates)))*100
    votepct.append(f'{pct:.2f}%')
    votes = 0

mostvotes_index = 0

for i in range(len(totalvotes)):
    if totalvotes[i] > totalvotes[i-1]:
        mostvotes_index = i

resultslist = []
print(F'---------------------Election Results---------------------')
print(f'--------------------------------------------------------------')
print(f'                TOTAL VOTES: {len(sortedcandidates)}            ')
print(f'--------------------------------------------------------------')
for i in range(len(uniquecandidates)):
    results = (f'{uniquecandidates[i]} obtained {votepct[i]} of the votes; for a total of {totalvotes[i]}')
    resultslist.append(results)
    print(results)
print(f'----------------------******----------------------')
print(f'------------  Winner : {uniquecandidates[int(mostvotes_index)]}  ------------------')


output_path = os.path.join( "output", "ElectionResults.txt")

with open(output_path, 'a') as txtfile:

    txtfile.writelines(F'---------------------Election Results---------------------')
    txtfile.writelines('\n')
    txtfile.writelines(f'--------------------------------------------------------------')
    txtfile.writelines('\n')
    txtfile.writelines(f'                TOTAL VOTES: {len(sortedcandidates)}            ')
    txtfile.writelines('\n')
    txtfile.writelines(f'--------------------------------------------------------------')
    txtfile.writelines('\n')

    for lines in resultslist:
        txtfile.writelines(lines)
        txtfile.writelines('\n')

    txtfile.writelines(f'----------------------******----------------------')
    txtfile.writelines('\n')
    txtfile.writelines(f'------------  Winner : {uniquecandidates[int(mostvotes_index)]}  ------------------')