import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Illustrating the central limit theorem with streamlit")
st.header("An App by Geraltwolf!")
st.subheader("This app simulates a thousand coin flips.")
st.write("Plotting histogram of the means")

perc_head=st.number_input(label='Chance of Coins Landing on Heads', min_value = 0.0, max_value = 1.0, value = 0.5)
binom_dist = np.random.binomial(1, perc_head, 1000)