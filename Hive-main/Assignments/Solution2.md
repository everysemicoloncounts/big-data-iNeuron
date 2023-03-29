# Scenario Based questions:

`1. Will the reducer work or not if you use “Limit 1” in any HiveQL query?`

`2. Suppose I have installed Apache Hive on top of my Hadoop cluster using default metastore configuration. Then, what will happen if we have multiple clients trying to access Hive at the same time?`

`4. How can you add a new partition for the month December in the above partitioned table?`

`5. I am inserting data into a table based on partitions dynamically. But, I received an error – FAILED ERROR IN SEMANTIC ANALYSIS: Dynamic partition strict mode requires at least one static partition column. How will you remove this error?`

`6. Suppose, I have a CSV file – "sample.csv" present in "/temp" directory with the following entries\-
id first_name last_name email gender ip_address
How will you consume this CSV file into the Hive warehouse using built-in SerDe?`


`7. Suppose, I have a lot of small CSV files present in the input directory in HDFS and I want to create a single Hive table corresponding to these files. The data in these files are in the format: {id, name, e-mail, country}. Now, as we know, Hadoop performance degrades when we use lots of small files.
So, how will you solve this problem where we want to create a single Hive table for lots of small files without degrading the performance of the system?`