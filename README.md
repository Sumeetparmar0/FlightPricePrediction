# Flight Price Analysis

## Overview

This project aims to analyze flight prices using a dataset from Kaggle and build a machine learning model to predict future flight prices. The project involves data cleaning, transformation, visualization using Power BI, and developing predictive models using Python.

## Table of Contents
- [Dataset](##dataset)
- [ETL Operations](#etl-operations)
- [Power BI Dashboards](#power-bi-dashboards)
- [Key Questions and Insights](#key-questions-and-insights)
- [Machine Learning](#machine-learning)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)

## Dataset
The dataset used for this project is sourced from Kaggle and contains information about flight prices.
Link: https://www.kaggle.com/code/varunsaikanuri/flight-fare-prediction-10-ml-models

## ETL Operations
Performed Extract, Transform, and Load (ETL) operations using Power BI to clean and preprocess the data. The steps included:
1. Data Cleaning
2. Data Transformation
3. Loading data into Power BI

## Power BI Dashboards
Created three interactive dashboards in Power BI to visualize the data and explore various combinations of flight price factors. 

## Key Questions and Insights
The project addressed several key questions, including:
1. Does price vary with Airlines?
2. How is the price affected when tickets are bought in just 1 or 2 days before departure?
3. Does ticket price change based on the departure time and arrival time?
4. How the price changes with change in Source and Destination?
5. How does the ticket price vary between Economy and Business class?

## Machine Learning
Developed an end-to-end machine learning pipeline using Python to predict future flight prices. The steps included:
1. Data Cleaning and Preprocessing
2. Exploratory Data Analysis (EDA)
3. Building Predictive Models
4. Model Evaluation and Validation

Link: https://github.com/Sumeetparmar0/FlightPricePrediction

## Technologies Used
- **Power BI**: For data visualization and dashboard creation
- **Python**: For data cleaning, EDA, and machine learning model development

## Getting Started
To get a local copy up and running, follow these steps:
* For PowerBI Visualisation
- Download FlightPrice_analysis.pbix file.
- Download Kaggle dataset and give path of csv file in power Query and load dataset.

* For Python Predictive model
1. Clone the repository to your local machine using the following command:
git clone https://github.com/Sumeetparmar0/FlightPricePrediction

2. Navigate to the project directory:
cd FlightPricePrediction

3. Install the required dependencies using pip:
pip install -r requirements.txt

4.Run training_pipeline.py file:
by this programe will create model.pkl file (Because of size limitation its not placed here)

5. Run the Flask application:
python application.py

6. Open your web browser and go to
http://127.0.0.1:5000/ - to access the home page

http://127.0.0.1:5000/predict - to perform prediction of Flight price on the web application.

