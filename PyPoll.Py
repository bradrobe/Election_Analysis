# The data we need to retreive.
# 1.  The total number of votes cast
# 2.  A complete list of candidates who received votes
# 3.  The percentage of votes each candidates won
# 4.  The total number of botes each candidate won
# 5. The winner of the election based on popular vote.

# Import the datetime class from the datetime module.
import datetime
# use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)

# Import the datetime class from the datetime module.
import datetime as dt
# use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)


# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Open the election resiults and read the file modified with the With statement.

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do analysis.
    print(election_data)

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
    print(election_data)
    
import csv
import os
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() funtion with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Create a filename variable to a direct or indirect path th the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()

# Using a cleaner code: Using the "With"  statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:


    # Write three counties to the file/you can also write code: txt_file.write("Arapahoe, Denver, Jefferson").
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson, ")

    # Use newline escape sequence "\n" to write them on separate lines: 
    
    txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")
    
# My turn, opening the Election Results in CSV to read.

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open teh election resulte and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    # Read the file object  witht the reader funtion.
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    # "for row in file_reader:""
    
    #Read and print the header row.
    headers = next(file_reader)
    print(headers)
    
        

