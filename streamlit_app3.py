import pandas as pd
import streamlit as st
import altair as alt
import New_mel as nm
from insert import Dashboard as ds

st.sidebar.title("Fleets")
button1 = st.sidebar.button("Q400", use_container_width=True)
button2 = st.sidebar.button("B737", use_container_width=True)


if button1:
    st.title("MEL count by Category")
    st.altair_chart(ds(nm.counts_37).insert(), use_container_width=True)
elif button2:
    st.title("MEL count by Part and Time")
    st.altair_chart(ds(nm.counts_77).insert(), use_container_width=True)
else:
    # Optionally, display some default text or instructions here
    st.title("Ethiopian")
