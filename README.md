# Project Introduction

This project is part of the Data Engineering Nanodegree by Udacity
It is an introduction to modelling with Postgres using python and PostgreSQL

The purpose of the project is to build a star schema and an ETL to fill it. 
It uses data from logs and songs of a fictitious music streaming app called Sparkify
(all can be found it the data directory)


## Star Schema

This is the schema that was built

![alt text](https://github.com/abiais/Data-Engineering-Nanodegree-Program-Data-Modeling-with-Postgres/blob/master/Start%20Schema.png?raw=true)

All the queries used to create and fill these tables can be found in the sql_queries.py file and create_tables.py runs these queries after connecting to a database.

At different steps of the project test.ipynb can be used to test if the different statements work as expected.

## ETL

The ETL file is etl.py and was built progressively using the etl.ipynb jupyter notebook supplied for the project.

## Running the project

To run this project, you simply need to run create_tables.py and etl.py in your terminal.