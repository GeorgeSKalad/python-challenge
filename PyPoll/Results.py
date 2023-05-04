import csv

# Read the election results from the CSV file
with open('election_data.csv', 'r') as f:
  reader = csv.reader(f)
  header = next(reader)
  election_data = list(reader)

# Get the total number of votes 
total_votes = len(election_data)

# Get a list of candidates votes
candidates = set()
    
for result in election_data:
    candidate = result[2]
    candidates.add(candidate)
   
# Calculate the number of votes each candidate won
candidate_votes = {}
for candidate in candidates:
  candidate_votes[candidate] = sum(1 for row in election_data if row[2] == candidate)

# Calculate the percentage of votes each candidate won
candidate_percentage = {}
for candidate in candidates:
  candidate_percentage[candidate] = candidate_votes[candidate] / total_votes * 100

# Determine the winner of the election based on votes
winner = max(candidate_percentage, key=candidate_percentage.get)

# Print the election results 
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')
for candidate in candidates:
    print(f'{candidate}: {candidate_percentage[candidate]:.3f}% ({candidate_votes[candidate]})')
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')

# Write the election results to a text file
with open('election_results.txt', 'w') as f:
    f.write('Election Results\n')
    f.write('-------------------------\n')
    f.write(f'Total Votes: {total_votes}\n')
    f.write('-------------------------\n')
    for candidate in candidates:
        f.write(f'{candidate}: {candidate_percentage[candidate]:.3f}% ({candidate_votes[candidate]})\n')
    f.write('-------------------------\n')
    f.write(f'Winner: {winner}\n')
    f.write('-------------------------\n')
