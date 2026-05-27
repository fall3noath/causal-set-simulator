from causalset.sprinkling import poisson_sprinkle
from causalset.graph import build_causal_graph
from causalset.reduction import transitive_reduce
from causalset.geodesics import (
    longest_chain,
    longest_chain_length,
)
from causalset.dimension import estimate_dimension
from causalset.interactive import interactive_causal_plot
from causalset.minkowski import MinkowskiSpacetime


print()
print("===================================")
print("CAUSAL SET SIMULATOR INITIALIZING")
print("===================================")
print()

spacetime = MinkowskiSpacetime()

events = poisson_sprinkle(
    150,
    t_range=(-1, 1),
    x_range=(-1, 1),
    seed=42,
)

print("[1] Spacetime events generated")

full_graph = build_causal_graph(events, spacetime)

print("[2] Causal graph constructed")

reduced_graph = transitive_reduce(full_graph)

print("[3] Transitive reduction complete")

path = longest_chain(reduced_graph)

print("[4] Longest geodesic chain computed")

estimated_dimension = estimate_dimension(full_graph)

print()
print("========== SYSTEM INFO ==========")
print(f"Events: {len(events)}")
print(f"Causal Relations: {full_graph.number_of_edges()}")
print(
    f"Longest Chain Length: "
    f"{longest_chain_length(reduced_graph)}"
)
print(f"Estimated Dimension: {estimated_dimension}")
print("=================================")
print()

interactive_causal_plot(
    events,
    reduced_graph,
    highlighted_path=path,
    estimated_dimension=estimated_dimension,
    causal_relations_count=full_graph.number_of_edges(),
)
