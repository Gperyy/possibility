import random

import numpy as np
import plotly.express as px
from collections import Counter
import streamlit as st


def roll_die():
    return random.randint(1, 6)


class DiceRollerSimulation:
    def __init__(self, num_rolls):
        self.num_rolls = num_rolls
        self.results = {}

    def simulate_rolls(self):
        self.results = []
        for i in range(self.num_rolls):
            result = roll_die()
            self.results.append(result)
        return self.results

    def plot_results(self):
        counts = dict(Counter(self.results))
        fig = px.bar(x=list(counts.keys()), y=list(counts.values()), title="Zar Atma Sonuçları")
        fig.update_layout(xaxis_title="Zar Üzerindeki Sayılar", yaxis_title="Gözlemlenen Sonuçlar")
        fig.update_traces(marker=dict(color='rgb(255, 106, 106)'))
        return fig
