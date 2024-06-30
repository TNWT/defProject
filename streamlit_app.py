import pandas as pd
import streamlit as st
import altair as alt



st.sidebar.title("Fleets")
button1 = st.sidebar.button("Q400", use_container_width=True)
button2 = st.sidebar.button("B737", use_container_width=True)


data = pd.DataFrame([[3, 'A'],
                     [5, 'B'],
                     [10, 'C'],
                     [34, 'D']],
                     columns=["Count", "Category"])

data2 = pd.DataFrame([[23, 'A'],
                     [34, 'B'],
                     [18, 'C'],
                     [64, 'D']],
                     columns=["Count", "Category"])

chart1 = (
    alt.Chart(data)
    .mark_bar()
    .encode(
        x=alt.X("Count"),
        y=alt.Y("Category",),
        color=alt.Color("Category")
    )
)

chart2 = (
    alt.Chart(data2)
    .mark_bar()
    .encode(
        x=alt.X("Count"),
        y=alt.Y("Category",),
        color=alt.Color("Category")
    )
)
if button1:
    st.title("MEL count by Category")
    st.altair_chart(chart2, use_container_width=True)
elif button2:
    st.title("MEL count by Part and Time")
    st.altair_chart(chart1, use_container_width=True)
else:
    # Optionally, display some default text or instructions here
    st.write("Click a button to display text.")

