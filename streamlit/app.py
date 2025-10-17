import streamlit as st
import numpy as np
import pandas as pd

st.title("Palmer's Penguins")
penguins_df = pd.read_csv('penguins.csv')
st.write(penguins_df.head())