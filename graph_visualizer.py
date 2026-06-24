import networkx as nx
import matplotlib.pyplot as plt
from graph_data import city_graph

def generate_graph_image(route=None):

    G = nx.DiGraph()

    for node in city_graph:
        for neighbor, weight in city_graph[node].items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(14, 10))

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color='skyblue',
        node_size=2500,
        font_size=10,
        font_weight='bold',
        arrows=True
    )

    labels = nx.get_edge_attributes(G, 'weight')

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=labels
    )

    if route and len(route) > 1:

        path_edges = list(zip(route, route[1:]))

        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=path_edges,
            edge_color='red',
            width=4
        )

    plt.title("Smart Delivery Route Optimization Graph")

    plt.savefig('static/graph.png')

    plt.close()