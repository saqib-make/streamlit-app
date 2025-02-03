import pandas as pd
import ydata_profiling as pandas_profiling  # Use pandas_profiling if you're on an older version
import streamlit as st
import seaborn as sns
from streamlit_pandas_profiling import st_profile_report

# Load the Titanic dataset
df = sns.load_dataset('titanic')

# Create the profile report
# pr = pandas_profiling.ProfileReport(df, config_file=None)
pr = df.profile_report()

# Display the profile report in Streamlit
st_profile_report(pr) 


 