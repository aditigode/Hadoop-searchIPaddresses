# Hadoop-searchIPaddresses
A short assignment of using Hadoop streaming to filter and analyze log files of users visiting a website      
A detailed explanation of my code is given in the pdf file "assignment1_report_adigode"
## The goal to perform the following tasks for the problem statement mentioned below:                           
1. Set up a cluster with Hadoop Distributed File System and run examples.
2. On top of HDFS, set up the cluster with MapReduce programming framework.    
3. Run examples of MapReduce programs.          

Based on our examples, we will develop our own MapReduce program to analysis a simple log file.           
Each line is a record of visit, which consists of IP Address, Time, Type of HTTP Request, Requested File, HTTP Version and Status, etc.        


We have provided two examples that related to this lab.         
• logstat: It counts the number of visits for each IP address in the log file.        
• logstat2: It counts the number of visits for each IP address in the same hour.         
As discussed in the lectures, MapReduce programming framework seperates the data and operation     
(two stages). It uses Hadoop Stream, which represents by sys.stdin in Python.          
### Assignment:            
Part 1:             
1. Output the top-3 IP addresses with the granularity of an hour          
• You should read the two examples.             
• Develop your code based on examples. The program may take more than one round of MapReduce.     

Part 2:                          
2. Make your program like a database search
• Your program should be able to accept parameters from users, such as 0-1, which means from time 00:00 to 01:00, and output the top-3 IP addresses in the given time period.             
• Run it along with three other examples, WordCount, Sort, Grep, at the same time, and test fair and capacity schedulers.           

