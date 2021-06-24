## Tanzanian Water Well Prediction 
#### Authors: Ryan Reilley and Kevin McDonough 
![Well Picture](images/HappyKid_well.jpeg)

### Overview
This project analyzes data for over 74,000 water wells that have been installed in Tanzania over the years. The goal of this analysis is to determine what features of a water well provide a good prediction if the well is functional, not functional, or functional but needs repair. This will be done through exploratory data analysis and iterative predictive modeling using classification models.

### Business Problem
The Tanzania Ministry of Water have hired us to predict the operating condition for wells in their country. They will use our analysis to send teams of people out to fix the waterpoints that are currently not functional or need repair. Based on our analysis, we are going to provide reccomendations based on the following.

* Which wells you should start fixing first based on location
* Which funders and installers to focus on when building new wells
* Which type of wells should be used to replace non-functional wells

### Data Understanding 
Each row in this dataset represents a unique water well in Tanzania and surrounding information about the well. There are 59,400 rows in the training data set and 14,850 rows in the test data set. The target feature we will be predicting on is "status_group." Status_group represents the functionality of the well and there are three classes: "functional," "non functional" and "functional needs repair." There are a number of columns related to geo location of the well. There is also a good mix of continuous and categorical variables in the dataset. Each feature and its description is listed below.

### Methods
* Preliminary data cleaning, exploratory data analysis and feature engineering to identify and create features that will generate accurate predictions
* scaling and fitting data to multiple classification models using pipelines  
* Evaluating model performance using selected metrics and tuning hyperparameters to maximize accuracy and micro-precision 
* Selecting final model and creating predictions for testing data

### Exploratory Data Analysis and Feature Engineering 
![Classes]('images/outcome_classes.png')
