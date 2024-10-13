import networkx as nx
import pandas as pd

G = nx.Graph()

file_path = 'ChinaRailway.xlsx'
df = pd.read_excel(file_path, sheet_name =0, engine='openpyxl')
df2 = pd.read_excel(file_path, sheet_name =1, engine='openpyxl')
df3 = pd.read_excel(file_path, sheet_name =2, engine='openpyxl')

destinations = df.iloc[2:43, 1]

for ports in destinations:
    G.add_node(ports.upper())


for i, row in df2.iterrows():
    station_a = row['STATION 1']  # Column B in Excel
    station_b = row['STATION 2']  # Column C in Excel
    distance = row['EST FREIGHT DISTANCE']    # Column E in Excel

    #Add an edge between station_a and station_b with the duration as the weight
    G.add_edge(station_a, station_b, weight=distance)

top_china_ports = df3['LOCATION OF PORT'].tolist()


shortest_paths = {}

for port1 in top_china_ports:
    shortest_paths[port1] = {}
    for port2 in top_china_ports:
        if port1 != port2:  # Avoid self-loops
            if nx.has_path(G, port1, port2):
                path = nx.shortest_path(G, source=port1, target=port2, weight='weight')
                total_distance = nx.path_weight(G, path, weight='weight')
                shortest_paths[port1][port2] = {
                    'path': path,
                    'total_distance': total_distance
            }
        else:
            shortest_paths[port1][port2] = None

for source, targets in shortest_paths.items():
    for target, info in targets.items():
        if info is not None:
            print(f"Shortest path from {source} to {target}: {info['path']} with total weight {info['total_distance']}")
        else:
            print(f"No path exists from {source} to {target}.")


