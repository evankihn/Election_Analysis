# Election_Analysis

## Project Overview
Colorado board of governors has provided the information needed to determine the following tasks: 

1. Calculate the total number of voters cast.
2. Get a complete list of candidates who recieved votes
3. Calculate the total number of votes each candidate recieved 
4. Calculate the percentage of votes each candidate won 
5. Determine the winner of the election based on popular vote

## Resources 
- Data Source: election_analysis.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary
- There were "x" voters cast in the election
- The candidates were: 
    - Charles Casper Stockham
    - Diana DeGette 
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham recieved 23% of the vote and 85,213 votes
    - Diana DeGette recieved 73.8% of the vote and 272,892 votes
    - Raymon Anthony Doane recieved 3.1% of the vote and 11,606 votes
- Diana DeGette won the election with 73.8% of the vote, totalling 272,892 total votes

## Challenge Overview
The purpose of this analysis is to use different soucres (in our case, Python and Visual Studio Code) to break down the results of a recent election. With so many lines of data, we could find a way to extract the results using excel or other tools, but this code represents the speed and accuracy with which we want this analysis performed.


## Election Audit Results 
- How many votes were cast in this congressional election?
    - We were able to use a count that was able to summarize the total votes made in the election. It all begin with intializing a total vote count, and then defining out variable as we see below: 
        
        "total_votes = 0"
        "total_votes = total_votes + 1"

- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
    - For county votes (including total per county and percentage of final total) we needed to develop a for statement using our variables and f string to display the name of the county, the percentage of votes they won, and the total votes they earned.

        "countyvote_percentage = float(c_votes)/float(total_votes) * 100"
        "county_results = (
        f"{county_name}: {countyvote_percentage:.1f}% ({c_votes:,})\n")"

- Which county had the largest number of votes?
    - Using the formaula above under our third bullet, it was clear that "Denver" had 82.8% of the vote, tallying a total of 306,055 total votes.

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
    - Similiar to the breakdown of the votes/percentage of votes we used for counties, candidates had a similiar code. Using different variable we were able to come up with the code below to represent the candidate data: 

        "votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
        f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")"

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
    - Diana DeGette won the election, with 272,892 total votes accounting for 73.8%.

## Election-Audit Summary
With the adjustment of variables and some of the statements within our code, you can see how it could be used for other future elections. In terms of modifications, my proposal to the election commission would be centered around the ease of access and fleixbility within the code. The small adjustments that would need to be made really would be more within the csv file, in order to make sure we are keeping the rows simple in our language. If there were more rows added, we would just need to clarify what we were after, as we already were able to do presenting "county" and "canbdidate" votes, percentages, and winners. 