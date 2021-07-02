import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# Read and Print Header Row
    headers = next(file_reader)
    print(headers)
    
# To do: perform analysis
    print(election_data)

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write three counties to the file.
    txt_file.write("Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson")



