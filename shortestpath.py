import networkx as nx
import pandas as pd

G = nx.Graph()

file_path = 'ChinaRailway.xlsx'
df = pd.read_excel(file_path, sheet_name =1, engine='openpyxl')
df2 = pd.read_excel(file_path, sheet_name =2, engine='openpyxl')

destinations = df.iloc[2:38, 1]


for ports in destinations:
    G.add_node(ports)


for i, row in df2.iterrows():
    station_a = row['STATION 1']  # Column B in Excel
    station_b = row['STATION 2']  # Column C in Excel
    duration = row['EST FREIGHT DURATION/MINS']    # Column E in Excel

    # Add an edge between station_a and station_b with the duration as the weight
    G.add_edge(station_a, station_b, weight=duration)

print("Edges in the graph:")
print(G.edges(data=True))
