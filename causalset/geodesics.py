import networkx as nx


def longest_chain(graph):
    if not nx.is_directed_acyclic_graph(graph):
        raise ValueError("Graph must be acyclic")

    return nx.dag_longest_path(graph)


def longest_chain_length(graph):
    if not nx.is_directed_acyclic_graph(graph):
        raise ValueError("Graph must be acyclic")

    return nx.dag_longest_path_length(graph)
