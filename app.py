import streamlit as st
import pandas as pd 


# sidebar elements
st.sidebar.write("Settings")
p_threshold = st.sidebar.slider("Select a p-value threshold", min_value=0.0,
                                max_value=1.0, step=0.05, value=0.05)
cat_algorithm = st.sidebar.selectbox(label="Select detection algorithm for categorical columns",
                                     options=['chi-square test'])
num_algorithm = st.sidebar.selectbox(label="Select detection algorithm for numerical columns",
                                     options=['kolmogorov-smirnov test'])

# main page
st.title("Data Drift Detection")
st.markdown(
    """
The following app can be used to detect simple data drift.
Two dataframes must be uploaded in order for the app to function:

* reference dataframe: this is the source of truth
* target dataframe: this is the dataframe to be investigated

""")


tab0, tab1, tab2 = st.tabs(["Guidelines", "Data", "Analysis"])

# Tab 0 - Guidelines

tab0.subheader("Algorithm setting")
tab0.markdown(
    """
* **P-value threshold**: This threshold is used to decide the drift threshold - any p-value below the threshold will result in the features being flagged
* **Categorical column algorithm**: This will choose the algorithm used to detect drift in categorical columns- it can only use chi-square test for now.
* **Numerical column algorithm**: This will choose the algorithm used to detect drift in numerical columns- it can only use kolmogorov-smirnov test for now.
"""
)

tab0.subheader("Workflow")
tab0.markdown(
    """
1. Toggle to the **Data** tab and upload two dataframes to be investigated
2. Toggle to the **Analysis** tab to see the result of the detection
"""
)

tab0.subheader("Notes")
tab0.markdown(
    """
* Ensure each column in a dataframe has the right data format before being uploaded - the data type detection in the app is not perfect
* DO NOT upload datetime columns - this will cause error 
* Ensure dataframe does **NOT** contain **ANY** missing values
* The algorithm will ignore any column that **IS NOT** present in the reference dataframe
"""
)



# Tab 1 - Data 

tab1.markdown("###### Upload dataframes")


# Tab 2 - Analysis

tab2.markdown("###### Analysis result")
