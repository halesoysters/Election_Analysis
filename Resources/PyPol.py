import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("bootcamp/class folder/week 3/Election_Analysis/Resources/election_results.csv")
# Create a filename variable to a direct opath to the file.
file_to_save = os.path.join("bootcamp/class folder/week 3/Election_Analysis/Resources/Analysis/election_analysis.txt")

# 1. Initialize total vote counter
total_votes = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and Print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
            #2. Add to the total vote count
            total_votes += 1

    # 3. 
    print(total_votes)




