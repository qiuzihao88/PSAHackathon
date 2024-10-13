import networkx as nx
import pandas as pd

G = nx.Graph()

file_path = 'ChinaRailway.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

destinations = df.iloc[2:38, 1]


for ports in destinations:
    G.add_node(ports)


