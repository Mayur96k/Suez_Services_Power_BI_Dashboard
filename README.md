# Suez_Services_Dashboard (Australia & New Zealand)

## Overview

Suez help businesses, governments and communities across Australia and New Zealand to protect, access and optimise the use of natural resources and create new resources through reuse and recycling of water and waste.

This project focuses on scraping all the service locations across Australia & New Zealand and their associated attributes from Suez, performing exploratory data analysis to generate insights and visualize them with the help of Power BI.

The repository directory structure is as follows:

Analyzing-Suez-Services

 01_WEBSCRAPING
 
 02_ETL
 
 03_DATA
 
 04_ANALYSIS
 
 05_DASHBOARD
 
 06_RESOURCES

The type of content present in the directories is as follows:

### 01_WEBSCRAPING

This directory contains the python script to scrape data from the website along with flat file that has the scraped data.

### 02_ETL

This directory contains the ETL script that takes the scraped dataset as input, transforms it and exports an analysis-ready dataset into the 03_DATA directory.

### 03_DATA

This directory contains the data that can be directly used for exploratory data analysis and data visualization purposes.

### 04_ANALYSIS

This directory contains the python notebooks that analyzes the clean dataset to generate insights

### 05_DASHBOARD

This directory contains the python notebook with an embedded Power BI report that visualizes the data. The Power BI dashboard contains slicers, cross-filtering and other advance capabilities that end user can play with to visualize a specific facet of the data or, to get additional insights.


This directory contains images, icons, layouts, etc. that are used in this project

### Prerequisites

The major skills that are required as prerequisite to fully understand this project are as follows:

    Basics of Python & Web Scraping
    Basics of HTML
    Basics of Python Notebooks
    Basics of Power BI

In order to complete the project, I've used the following applications and libraries

    Python
    Python libraries mentioned in Notebook
    Jupyter Notebook
    Visual Studio Code
    Microsoft Power BI

    The choice of applications & their installation might vary based on individual preferences & system settings.


# Architecture

The project architecture is quite straight forward and can be explained through the below image:

![PA](https://github.com/Mayur96k/Suez_Services_Power_BI_Dashboard/assets/114133429/537877a5-ca76-4a9d-a69a-ace4ea0ca3c0)






As per the above workflow suggests; we are first scraping the data from the website using the Python script and collecting the same in a flat file which is then processed and cleaned with another ETL specific Python script.

Finally; we leverage the clean & analysis-ready dataset for some exploratory data analysis (EDA) using Jupyter Notebook and creating an insightful report using Power BI


## Power BI Dashboard




![Screenshot from 2023-08-19 19-24-11](https://github.com/Mayur96k/Suez_Services_Power_BI_Dashboard/assets/114133429/6293f2f4-9cb0-4369-8f94-36445cc54d16)







## Author

- Mayur Jagtap (mayurjagtap96k@gmail.com)

## Bug Reporting

For bug reports or any issues encountered while using repository code, please contact me at mayurjagtap96k@gmail.com. Please include detailed information about the problem and steps to reproduce it.

## License

"Copyright: 2023 Mayur Jagtap. All rights reserved."




