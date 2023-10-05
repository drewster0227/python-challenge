import csv

# Specify the path to the CSV file and the output text file
pypoll_csv = 'C:/Users/dreww/Desktop/DataAnalysisWork/Assignments/python-challenge/PyPoll/Resources/election_data.csv'
final_report = 'C:/Users/dreww/Desktop/DataAnalysisWork/Assignments/python-challenge/PyPoll/Analysis/election_analysis.txt'

# Open the CSV file for reading
with open(pypoll_csv) as csv_file:
    pypoll = csv.reader(csv_file)
    next(pypoll)  # Skip the header row
    totalVotes = 0
    
    candidates = []
    candidateVotes = []

    for row in pypoll:
        totalVotes += 1
        candidate_name = row[2]
        
        if candidate_name in candidates:
            # Find the index of the candidate in the list
            candidate_index = candidates.index(candidate_name)
            # Increment the corresponding candidate's vote count
            candidateVotes[candidate_index] += 1
        else:
            # Add the new candidate to the list
            candidates.append(candidate_name)
            # Initialize their vote count to 1
            candidateVotes.append(1)

# Now you have a list of candidates and a corresponding list of their vote counts
# You can proceed to analyze the election results

# For example, you can find the winner by getting the candidate with the most votes
winning_votes = max(candidateVotes)
winner_index = candidateVotes.index(winning_votes)
winner = candidates[winner_index]

print(f"Total Votes: {totalVotes}\n")
print("-------------------------\n")
print("Election Results\n")
for i in range(len(candidates)):
        candidate = candidates[i]
        votes = candidateVotes[i]
        percentage = (votes / totalVotes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})\n")
print(f"Winner: {winner}\n")
# Print and write the results to the output text file
with open(final_report, 'w') as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {totalVotes}\n")
    txt_file.write("-------------------------\n")
    for i in range(len(candidates)):
        candidate = candidates[i]
        votes = candidateVotes[i]
        percentage = (votes / totalVotes) * 100
        txt_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("-------------------------\n")

# Print a message indicating the analysis is complete

print("Election analysis complete. Results written to", final_report)
