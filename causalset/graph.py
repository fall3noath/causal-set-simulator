import networkx as nx


def build_causal_graph(events, spacetime):
    graph = nx.DiGraph()

    for event in events:
        graph.add_node(
            event.id,
            t=event.t,
            x=event.x,
        )

    for a in events:
        for b in events:
            if a.id == b.id:
                continue

            if spacetime.causally_related(a, b):
                graph.add_edge(a.id, b.id)

    return graph
