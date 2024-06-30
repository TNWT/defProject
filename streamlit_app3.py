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
###############################

class Dashboard:
    def __init__(self, counts):
        self.counts = counts
    def insert(self):
        data = pd.DataFrame([[self.counts[0], 'A'],
                            [self.counts[1], 'B'],
                            [self.counts[2], 'C'],
                            [self.counts[3], 'D']],
                            columns=["Count", "Category"])

        chart1 = (
            alt.Chart(data)
            .mark_bar()
            .encode(
                x=alt.X("Count"),
                y=alt.Y("Category",),
                color=alt.Color("Category"),
                text=alt.Text('Count:Q', format='.0f')
                ))

        chart2 = (
            alt.Chart(data)
            .mark_bar()
            .encode(
                x=alt.X("Count"),
                y=alt.Y("Category",),
                color=alt.Color("Category")
            )
        )
        return [chart1, chart2]
###############################

if button1:
    st.title("MEL count by Category")
    
    st.altair_chart(Dashboard(nm.counts_37).insert()[0], use_container_width=True)
elif button2:
    st.title("MEL count by Part and Time")
    st.altair_chart(Dashboard(nm.counts_77).insert()[1], use_container_width=True)
else:
    # Optionally, display some default text or instructions here
    st.title("Ethiopian")