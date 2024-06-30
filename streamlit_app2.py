import pandas as pd
import streamlit as st
import altair as alt
import New_mel as nm


st.sidebar.title("Fleets")
button1 = st.sidebar.button("Q400", use_container_width=True)
button2 = st.sidebar.button("B737", use_container_width=True)


b737_ = nm.Mel_counter(nm.record_B737, nm.B737_inop_ac, nm.B737_cargo, nm.B737_passenger)
b777_ = nm.Mel_counter(nm.record_B777, nm.B777_inop_ac, nm.B777_cargo, nm.B777_passenger)

counts_77 = b777_.count()
counts_37 = b737_.count()


data = pd.DataFrame([[nm.counts_37[0], 'A'],
                     [nm.counts_37[1], 'B'],
                     [nm.counts_37[2], 'C'],
                     [nm.counts_37[3], 'D']],
                     columns=["Count", "Category"])

data2 = pd.DataFrame([[nm.counts_77[0], 'A'],
                     [nm.counts_77[1], 'B'],
                     [nm.counts_77[2], 'C'],
                     [nm.counts_77[3], 'D']],
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


data = {'item': ['apple', 'banana', 'orange', 'apple', 'pear', 'apple', "pear", 'orange']}
df = pd.DataFrame(data)

# Get value counts
repetitions = df['item'].value_counts()

# Filter values based on threshold
filtered_repetitions = repetitions[repetitions >= 2]

# Create DataFrame with repeated items and counts
repeated_df = pd.DataFrame({'item': filtered_repetitions.index, 'count': filtered_repetitions.values})


chart3 = (
    alt.Chart(repeated_df)
    .mark_bar()
    .encode(
        x=alt.X("count"),
        y=alt.Y("item",),
        color=alt.Color("count")
    )
)


if button1:
    st.title("MEL count by Category")
    
    st.altair_chart(chart2, use_container_width=True)

    st.table(repeated_df)
elif button2:
    st.title("MEL count by Part and Time")
    st.altair_chart(chart1, use_container_width=True)

    st.table(repeated_df)
else:
    # Optionally, display some default text or instructions here
    st.altair_chart(chart3, use_container_width=True)