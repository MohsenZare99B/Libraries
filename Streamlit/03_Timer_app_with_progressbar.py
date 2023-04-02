import streamlit as st
import time as ts
from datetime import time

val = st.time_input("Set timer", value=time(0, 0, 0))
if str(val) == "00:00:00":
    st.write("Please set timer")
else:
    m, s, ms = map(int, str(val).split(':'))
    seconds = 60 * m + s + ms / 1000

    bar = st.progress(0)
    progress_status = st.empty()

    percentage = seconds / 100
    for i in range(100):
        bar.progress(i + 1)
        progress_status.write(str(i + 1) + '%')
        ts.sleep(percentage)