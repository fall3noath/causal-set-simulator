def ordering_fraction(graph):
    n = graph.number_of_nodes()

    if n <= 1:
        return 0

    relations = graph.number_of_edges()

    return relations / (n * (n - 1) / 2)


def estimate_dimension(graph):
    r = ordering_fraction(graph)

    if r <= 0:
        return 0

    estimates = {
        2: 0.5,
        3: 0.25,
        4: 0.125,
        5: 0.0625,
    }

    closest_dimension = min(
        estimates,
        key=lambda d: abs(estimates[d] - r),
    )

    return closest_dimension
