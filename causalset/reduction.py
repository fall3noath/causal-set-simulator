import networkx as nx


def transitive_reduce(graph):
    if not nx.is_directed_acyclic_graph(graph):
        raise ValueError("Graph must be acyclic")

    return nx.transitive_reduction(graph)
