import pandas as pd
import streamlit as st
import altair as alt
import Deferral_report as dr


st.sidebar.title("Fleets")
button1 = st.sidebar.button("Q400", use_container_width=True)
button2 = st.sidebar.button("B737MAX", use_container_width=True)
button3 = st.sidebar.button("B737NG", use_container_width=True)
button4 = st.sidebar.button("B737-F", use_container_width=True)
button5 = st.sidebar.button("B767", use_container_width=True)
button6 = st.sidebar.button("B777", use_container_width=True)
button7 = st.sidebar.button("B777-F", use_container_width=True)
button8 = st.sidebar.button("B787", use_container_width=True)
button9 = st.sidebar.button("A350", use_container_width=True)

b737_ = dr.Mel_counter(dr.record_B737, dr.B737_inop_ac, dr.B737_cargo, dr.B737_passenger)
b777_ = dr.Mel_counter(dr.record_B777, dr.B777_inop_ac, dr.B777_cargo, dr.B777_passenger)

counts_77 = b777_.count()
counts_37 = b737_.count()


data = pd.DataFrame([[dr.counts_37[0][0], 'A'],
                     [dr.counts_37[0][1], 'B'],
                     [dr.counts_37[0][2], 'C'],
                     [dr.counts_37[0][3], 'D']],
                     columns=["Count", "Category"])

data2 = pd.DataFrame([[dr.counts_77[0][0], 'A'],
                     [dr.counts_77[0][1], 'B'],
                     [dr.counts_77[0][2], 'C'],
                     [dr.counts_77[0][3], 'D']],
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


data = {'item': ['apple', 'banana', 'orange', 'apple', 'pear', 'apple', "pear"]}
df = pd.DataFrame(data)

# Get value counts
repetitions = df['item'].value_counts()

# Filter values based on threshold
filtered_repetitions = repetitions[repetitions >= 2]

# Create DataFrame with repeated items and counts
repeated_df = pd.DataFrame({'item': filtered_repetitions.index, 'count': filtered_repetitions.values})




if button1:
    st.divider()
    st.header("MEL count by Category")
    st.altair_chart(chart2, use_container_width=True)
    st.divider()
    st.header("MEL count by Part and Time")
    st.altair_chart(chart1, use_container_width=True)
    st.divider()
    st.table(repeated_df)
elif button2:
    st.divider()
    st.header("MEL count by Part and Time")
    st.altair_chart(chart1, use_container_width=True)
    st.divider()
    st.header("MEL count by Category")
    st.altair_chart(chart2, use_container_width=True)
    st.divider()
    st.table(repeated_df)
    


