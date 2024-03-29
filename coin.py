from pygments.lexers import go
import numpy as np
import plotly.graph_objects as go


class CoinTossSimulation:
    def __init__(self, num_tosses):
        self.num_tosses = num_tosses
        self.p = 0.5
        self.results = np.random.binomial(1, self.p, self.num_tosses)
        self.proportion_heads = np.cumsum(self.results) / np.arange(1, self.num_tosses + 1)
        self.proportion_tails = 1 - self.proportion_heads
        self.probabilities = {}

    @property
    def run_simulation(self):
        results = np.random.binomial(1, self.p, self.num_tosses)
        proportion_heads = np.cumsum(results) / np.arange(1, self.num_tosses + 1)
        proportion_tails = 1 - proportion_heads
        result = [proportion_heads, proportion_tails]
        return result

    @property
    def plot_result(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=np.arange(1, self.num_tosses + 1), y=self.proportion_heads,
                                 mode='lines+markers',
                                 name='Tura Gelme Olasılığı'))

        fig.add_trace(go.Scatter(x=np.arange(1, self.num_tosses + 1), y=self.proportion_tails,
                                 mode='lines+markers',
                                 name='Yazı Gelme Olasılığı'))

        fig.update_layout(title='Yazı/Tura Gelme Olasılığının Karşılaştırılması',
                          xaxis_title='Atış Sayısı',
                          yaxis_title='Gözlemlenen Sonuçlar')

        return fig

