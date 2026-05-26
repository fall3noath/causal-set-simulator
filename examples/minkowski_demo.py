from causalset.sprinkling import poisson_sprinkle
from causalset.graph import build_causal_graph
from causalset.reduction import transitive_reduce
from causalset.geodesics import longest_chain
from causalset.dimension import estimate_dimension
from causalset.interactive import interactive_causal_plot
from causalset.minkowski import MinkowskiSpacetime


spacetime = MinkowskiSpacetime()

events = poisson_sprinkle(
    150,
    t_range=(-1, 1),
    x_range=(-1, 1),
    seed=42,
)

full_graph = build_causal_graph(events, spacetime)

reduced_graph = transitive_reduce(full_graph)

path = longest_chain(reduced_graph)

estimated_dimension = estimate_dimension(full_graph)

print(f"Estimated dimension: {estimated_dimension}")
print(f"Longest chain length: {len(path)}")

interactive_causal_plot(
    events,
    reduced_graph,
    highlighted_path=path,
)
