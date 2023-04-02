import streamlit as st
import numpy as np
from matplotlib import pyplot as plt

st.sidebar.write("Hi! I am in the sidebar")
x = np.linspace(0, 10, 100)
fig = plt.figure()
plt.plot(x, np.sin(x))
st.write(fig)