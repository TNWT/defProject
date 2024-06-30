import streamlit as st
import altair as alt
import pandas as pd


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
        return chart1
###############################

