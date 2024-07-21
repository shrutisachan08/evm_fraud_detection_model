Deployment URL : https://evmfrauddetectionmodel-xcj7d6ggnxpjec4x4rmpy9.streamlit.app/
### EVM Fraud Detection Streamlit App
This repository contains a Streamlit application designed to detect fraudulent voting records in Electronic Voting Machines (EVM). The app allows users to input details such as machine ID, vote choice, location, and voting duration, and then predicts whether the record is fraudulent or not.
### Suggestion: To reduce time for making various combinations and get the desired results from model input voting duration in integer and once refer dataset in the jupyter notebook.
### Features
User Input: Collects Machine ID, Vote Choice, Location, and Voting Duration from the user.
Fraud Detection: Checks the input against a predefined dataset to identify potential fraudulent votes.
Custom Styling: Includes custom CSS for a visually appealing user interface.
### Prerequisites
To run this application, you need:
Python 3.0
Streamlit library
Pandas library
### Dataset
The dataset used in this application is defined in the code and consists of the following columns:
Machine_ID: Identifier for the voting machine.
Vote_Choice: The choice made by the voter (A, B, C, D).
Location: The location where the vote was cast (Loc1, Loc2, Loc3).
Voting_Duration: Duration of the voting process in seconds.
Fraudulent: Binary indicator of fraud (0 for No, 1 for Yes).
### How to run this app?
* Set up the enviornment : $ pip install streamlit pandas
* Save the code (Copy the code in some python file : 'evm_fraud.py')
* Run Streamlit application : Navigate the directory where you have saved your python file(cd path/to/your/file) and then 
execute the command - 'streamlit run evm_fraud.py'
* Open the application : After running the command, Streamlit will start a local server and provide a URL, typically http://localhost:8501
### Algorithms used in the dataset
The algorithms I have used are categorised as:
* RandomForestClassifier : Ideal for handling large datasets with a mix of numerical and categorical features. It is robust to
overfitting and manages the missing data and accuracy .
* Logistic Regresssion : It’s a good starting point for binary classification problems. It is said to be easily interpretable
and provides probabilities which can be usel for determining confidence of prediction.
* AdaBoostClassifier : Works well when you have a dataset with noisy data and outliers. It also improves the performance iteratively
and combines multiple weak learners to give strong classifiers.
* XGBoostClassifier : It is  for its performance and speed, especially on structured/tabular data. It handles missing values 
internally , prevents overfitting and improves generalization and it is comparatively efficient over other boosting
algorithms.
### Accuracy of different alogrithms applied
* RandomForestClassifier : 100%
* Logistic Regression Score : 60%
* AdaBoostClassifier : 100%
* XGBoost Classifier : 100%
