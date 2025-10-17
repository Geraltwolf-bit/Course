import streamlit as st
import numpy as np
import pandas as pd

st.title("Palmer's Penguins")
path = '/workspaces/Course/streamlit/penguins.csv'
penguins_df = pd.read_csv(path)
st.write(penguins_df.head())