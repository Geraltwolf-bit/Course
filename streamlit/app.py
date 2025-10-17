import streamlit as st
import numpy as np
import pandas as pd

st.title("Palmer's Penguins")
url = 'https://github.com/tylerjrichards/Streamlit-for-Data-Science/blob/main/penguin_app/penguins.csv'
penguins_df = pd.read_csv(url)
st.write(penguins_df.head())