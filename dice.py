import plotly.express as px
from collections import Counter


def roll_die():
    return random.randint(1, 6)


def simulate_rolls(num_rolls):
    results = []
    for i in range(num_rolls):
        result = roll_die()
        results.append(result)
    return results


num_rolls = int(input("Kaç kez zar atmak istiyorsunuz?: "))
results = simulate_rolls(num_rolls)

counts = dict(Counter(results))
fig = px.bar(x=list(counts.keys()), y=list(counts.values()), title="Zar Atma Sonuçları")
fig.show()
