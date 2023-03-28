# Create database

```
create database assignment;
```

# Check if the database is created or not.

```
show databases;
```

# Move to the database created

```
use assignment;
```

# Check the tables in the database

```
show tables;
```

# Create the required table

```
create table sales_order_data_csv_v1(
    ORDERNUMBER int,
    QUANTITYORDERED int,
    PRICEEACH float,
    ORDERLINENUMBER int,
    SALES float,
    STATUS string,
    QTR_ID int,
    MONTH_ID int,
    YEAR_ID int,
    PRODUCTLINE string,
    MSRP int,
    PRODUCTCODE string,
    PHONE string,
    CITY string,
    STATE string,
    POSTALCODE string,
    COUNTRY string,
    TERRITORY string,
    CONTACTLASTNAME string,
    CONTACTFIRSTNAME string,
    DEALSIZE string
)
row format delimited
fields terminated by ','
tblproperties("skip.header.line.count"="1")
;
```

# Loading data to the table

```
load data local inpath 'file:///config/workspace/sales_order_data.csv' into table sales_order_data_csv_v1;

```

set hive.cli.print.header = true;

# Creating a orc table
```
create table sales_order_data_orc
(
ORDERNUMBER int,
QUANTITYORDERED int,
PRICEEACH float,
ORDERLINENUMBER int,
SALES float,
STATUS string,
QTR_ID int,
MONTH_ID int,
YEAR_ID int,
PRODUCTLINE string,
MSRP int,
PRODUCTCODE string,
PHONE string,
CITY string,
STATE string,
POSTALCODE string,
COUNTRY string,
TERRITORY string,
CONTACTLASTNAME string,
CONTACTFIRSTNAME string,
DEALSIZE string
)
stored as orc;

```

# Storing the data from the normal table to orc table

```
from sales_order_data_csv_v1 insert overwrite table sales_order_data_orc select \*;

```

# Run a query to check map-reduce activity

```
select year_id, sum(sales) as total_sales from sales_order_data_orc group by year_id;
```

# b. Find a product for which maximum orders were placed
```
select PRODUCTCODE from sales_order_data_orc order by QUANTITYORDERED DESC limit 1;

```
# c. Calculate the total sales for each quarter
```
select sum(SALES) as total_sales_in_each_quater, QTR_ID from sales_order_data_orc group by QTR_ID;

```

# d. In which quarter sales was minimum

select sum(SALES) as total_sales_in_each_quater, QTR_ID from sales_order_data_orc group by QTR_ID order by total_sales_in_each_quater limit 1;

# e. In which country sales was maximum and in which country sales was minimum

select sum(SALES) as total_sales_in_each_quater, COUNTRY from sales_order_data_orc group by COUNTRY order by total_sales_in_each_quater DESC limit 1;

select sum(SALES) as total_sales_in_each_quater, COUNTRY from sales_order_data_orc group by COUNTRY order by total_sales_in_each_quater limit 1;
