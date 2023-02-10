# datafun-05-data-at-rest

Task 1
Read and work through Chapter 9 - Files & Exceptions - understand the examples. 

9.1 Introduction
9.2 Files
9.3 Text-File Processing
9.3.1 Writing to a Text File: Introducing the with Statement
9.3.2 Reading Data from a Text File
9.4 Updating Text Files
9.5 Serialization with JSON
9.6 Focus on Security: pickle Serialization and Deserialization
9.7 Additional Notes Regarding Files
9.8 Handling Exceptions
9.8.1 Division by Zero and Invalid Input
9.8.2 try Statements
9.8.3 Catching Multiple Exceptions in One except Clause
9.8.4 What Exceptions Does a Function or Method Raise?
9.8.5 What Code Should Be Placed in a try Suite?
9.9 finally Clause
9.10 Explicitly Raising an Exception
9.11 (Optional) Stack Unwinding and Tracebacks
9.12 Intro to Data Science: Working with CSV Files
9.12.1 Python Standard Library Module csv
9.12.2 Reading CSV Files into Pandas DataFrames
9.12.3 Reading the Titanic Disaster Dataset
9.12.4 Simple Data Analysis with the Titanic Disaster Dataset
9.12.5 Passenger Age Histogram
Task 2
Read and work through Chapter 17 - Big Data - understand the examples. 

17.1 Introduction
17.2 Relational Databases and Structured Query Language (SQL)
17.2.1 A books Database
17.2.2 SELECT Queries
17.2.3 WHERE Clause
17.2.4 ORDER BY Clause
17.2.5 Merging Data from Multiple Tables: INNER JOIN
17.2.6 INSERT INTO Statement
17.2.7 UPDATE Statement
17.2.8 DELETE FROM Statement
 

Task 3 - Titanic (from 9.12 above)
Follow the instructions in 9.12.3 (starting pg. 346).
Don't work in interactive mode!
Instead complete the exercise in a notebook. 
1-Load: Use pandas to read in the Titanic Disaster dataset csv file.
2-View: Set the precision to 2 decimal places. View the head and tail of the file.
3-Headings: customize the column headings.
4-Describe: Use the DataFrame describe() function to calculate basic descriptive statistics for all numeric columns. 
5-Survivors: Follow instructions to describe statistics for those who survived (titanic.survived == 'yes') - see the example. 
Notice that describe provides different results for non-numeric data (e.g., unique, top, freq)
Enable matplotlib. If it doesn't work (e.g., in a notebook), try 
%matplotlib inline
6-Histogram: Use the DataFrame's hist() function to create a histogram for each numerical column.
Required: Use Section headings in your Markdown to make it clear that each of these 6 sections are shown in your notebook. They should be numbered 1-6 and include the keyword shown above.
Required: Include the title of the notebook, and your name and date at the top.
Do these consistently. A heading and section titles is required in every notebook. 
 

Task 3 Output
Document your results.

execute the completed notebook 
export to html
include the html in your repo
 

Task 4 - SQL (from 17.2 above)
Follow the instructions in 17.2.1 (starting pg 730) 
Don't work in interactive mode - use a notebook.
IMPORTANT: create the table using the books.sql script provided with the author files.  See https://github.com/pdeitel/IntroToPython/blob/master/examples/ch17/sql/books.sql Links to an external site.
Import the sqlite3 module and use the connect function to create a connection to your database.
After running the script, there should be 3 tables: authors, author_ISBN, and titles. 
Import pandas as pd
Use pd options.display to set the max_columns to 10
Use pd read_sql fuction to select everything (*) from the authors table, then the titles table, then the author_ISBN table.
Complete 17.2.2 SELECT (1 query)
Complete 17.2.3 WHERE (3 queries)
Complete 17.2.4 ORDER BY (4 queries)
Complete 17.2.5 INNER JOIN (1 query)
Complete 17.2.6 INSERT INTO (2 queries)
Complete 17.2.7 UPDATE (2 queries)
Complete 17.2.8 DELETE FROM (2 queries)
Final Results, SELECT * from each table and display the final state of each of the 3 tables.
Required: Use Section headings in your Markdown to make it clear that each of these 8 sections are shown in your notebook. They should be numbered 1-8 and include the SQL keyword shown above. Use a heading before your the final results showing all 3 tables as well. 
Required: Include the title of the notebook, and your name and date at the top.
Do these consistently. A heading and section titles is required in every notebook. 
 

Task 4 Output
Document your results.

execute the completed notebook 
export to html
include the html in your repo
Task 5. Push Repo to GitHub
Use VS Code to commit and sync (push) your repo to GitHub - or in Git Bash or terminal, do the following. 

git add .
git commit -m "added code"
git push origin main
Optional Task 6. Bonus
Start a new notebook.
Locate a unique csv dataset. 
Use pandas to import the csv dataset into a DataFrame.
Use the DataFrame commands to clean the data as needed and/or rename the columns.
Use the DataFrame describe() function to calculate basic descriptive statistics. 
Use the DataFrame hist() function to generate histograms for all numeric columns. 
Include the required heading at the top, and use section headings to tell your story with data. 
Execute the entire, professionally presented file and output to html. 
Git add, git commit, and git push the new content to your GitHub repo. 
