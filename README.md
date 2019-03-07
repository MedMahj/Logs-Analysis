# Logs Analysis Project - Udacity FSWD Nanodegree

## Description 

For this project, we have to create a reporting tool that prints out reports( in plain text) based on the data in the given database. This reporting tool is a Python program using the psycopg2 module to connect to the database. This project sets up a mock PostgreSQL database for a fictional news website. 
The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:

* _What are the most popular three articles of all time?_
* _Who are the most popular article authors of all time?_
* _On which days did more than 1% of requests lead to errors?_

## Project contents :

This project consists of the following files :

* _README.md_ : This readme file.
* _logs_analysis_tool.py_ : The Python program that connects to the PostgreSQL database, executes the SQL queries and displays the results.
* _example_output.txt_ : An example of program's output.

## Getting Started


### Prerequisites

The project code requires the following software:

* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/)
* [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
* Python version 2 or 3



### Installing

1. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](https://www.vagrantup.com/)
2. Clone the [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
3. Launch the Vagrant VM with `vagrant up`
4. Log into Vagrant VM with `vagrant ssh`
5. Install **Psycopg2** module  with `sudo pip install psycopg2` or `sudo pip3 install psycopg2` (Python 3)
6. Download the data provided by **Udacity** [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip the file in order to extract _newsdata.sql_. This file should be inside the _Vagrant_ folder.

7. Clone this repo into the vagrant directory


## Running the program

Follow the steps below to run the program :

* Load the database using `psql -d news -f newsdata.sql`.

* Connect to the database using `psql -d news`.

* Create the **Views** given below. Then `exit` psql.

* Now execute the Python file  - `python logs_analysis_tool.py`.

## Views Definition :
* **View 1** :
```sql
CREATE VIEW viewstab AS 
SELECT title, views, author 
FROM articles ,(SELECT SUBSTRING(path FROM 10) AS slug , count(*) AS views 
                FROM log 
                WHERE path 
                LIKE '%article%' AND status LIKE '2%' 
                GROUP BY path ) AS viewtab 
WHERE articles.slug = viewtab.slug ;
```
* **View 2**
```sql
CREATE VIEW errortab AS 
SELECT DATE(time) AS date, count(*) AS error 
FROM log 
WHERE status LIKE '4%' 
GROUP BY DATE(time), status 
ORDER BY Date(time);
```
* **View 3**
```sql
CREATE VIEW totaltab AS 
SELECT DATE(time) AS date, count(*) AS total 
FROM log 
GROUP BY DATE(time);
```

## Authors

* **Mohamed BOUSETTA MAHJOUB** - *Initial work* - [MedMahj](https://github.com/MedMahj/)





