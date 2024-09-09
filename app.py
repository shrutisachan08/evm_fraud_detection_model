import pandas as pd
import streamlit as st

# Sample data
data = {
    'Machine_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 10,
    'Vote_Choice': ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D'] * 5,
    'Location': ['Loc1', 'Loc1', 'Loc1', 'Loc1', 'Loc2', 'Loc2', 'Loc2', 'Loc2', 'Loc3', 'Loc3', 'Loc3', 'Loc3', 'Loc1', 'Loc1', 'Loc1', 'Loc1', 'Loc2', 'Loc2', 'Loc2', 'Loc2'] * 5,
    'Voting_Duration': [10, 20, 30, 40, 15, 25, 35, 45, 50, 60, 12, 22, 32, 42, 18, 28, 38, 48, 55, 65] * 5,
    'Fraudulent': [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0] * 5
}

df2 = pd.DataFrame(data)

def get_fraudulent_value(machine_id, vote_choice, location, voting_duration):
    """
    Returns the fraudulent value for a given vote.

    Args:
      machine_id: The ID of the machine.
      vote_choice: The vote choice.
      location: The voting location.
      voting_duration: The voting duration.

    Returns:
      The fraudulent value (0 or 1).
    """
    # Find the index of the vote in the dataset
    for i, row in enumerate(zip(df2['Machine_ID'], df2['Vote_Choice'], df2['Location'], df2['Voting_Duration'])):
        if row == (machine_id, vote_choice, location, voting_duration):
            return df2['Fraudulent'][i]

    # If not found, return None or handle the case accordingly
    return None  # Or raise an exception, return a default value, etc.
# Custom CSS with visible colors and effects
custom_css = """
    <style>
    body {
        background-color: #f0f2f6;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background-color: #f0f2f6;
    }
    .css-18e3th9 {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        transition-duration: 0.4s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput input {
        background-color: #fff3e0;
        border: 2px solid #ff9800;
        border-radius: 5px;
        padding: 10px;
    }
    .stNumberInput input {
        background-color: #e3f2fd;
        border: 2px solid #2196f3;
        border-radius: 5px;
        padding: 10px;
    }
    .stSelectbox select {
        background-color: #e8f5e9;
        border: 2px solid #4caf50;
        border-radius: 5px;
        padding: 10px;
    }
    .result {
        font-size: 20px;
        font-weight: bold;
        color: #d32f2f;
        background-color: #ffebee;
        border: 2px solid #d32f2f;
        border-radius: 5px;
        padding: 10px;
        text-align: center;
    }
    </style>
    """

# Inject CSS into the Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)

# Streamlit application
st.title('EVM Fraud Detection')

machine_id = st.number_input("Enter Machine ID:", min_value=1, max_value=10)
vote_choice = st.selectbox("Select Vote Choice:", ['A', 'B', 'C', 'D'])
location = st.selectbox("Select Location:", ['Loc1', 'Loc2', 'Loc3'])
voting_duration = st.number_input("Enter Voting Duration(integer value):", min_value=0.0)

if st.button('Check Fraudulent'):
    result = get_fraudulent_value(machine_id, vote_choice, location, voting_duration)
    
    if result is not None:
        if result == 1:
            st.write("Fraud detected")
        else:
            st.write("No Fraud Detected")
    else:
        st.write("Record not found. Please check the input values.")
