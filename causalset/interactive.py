import plotly.graph_objects as go


def interactive_causal_plot(
    events,
    graph,
    highlighted_path=None,
):
    edge_x = []
    edge_y = []

    for source, target in graph.edges:
        a = events[source]
        b = events[target]

        edge_x.extend([a.x, b.x, None])
        edge_y.extend([a.t, b.t, None])

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        mode="lines",
        line=dict(width=1),
        opacity=0.3,
        hoverinfo="none",
    )

    node_trace = go.Scatter(
        x=[e.x for e in events],
        y=[e.t for e in events],
        mode="markers",
        marker=dict(size=6),
        text=[f"Event {e.id}" for e in events],
        hoverinfo="text",
    )

    traces = [edge_trace, node_trace]

    if highlighted_path is not None:
        path_x = []
        path_y = []

        for idx in highlighted_path:
            path_x.append(events[idx].x)
            path_y.append(events[idx].t)

        path_trace = go.Scatter(
            x=path_x,
            y=path_y,
            mode="lines+markers",
            line=dict(width=4),
            marker=dict(size=8),
            name="Geodesic",
        )

        traces.append(path_trace)

    fig = go.Figure(data=traces)

    fig.update_layout(
        title="Interactive Causal Set",
        xaxis_title="x",
        yaxis_title="t",
        showlegend=False,
    )

    fig.show()
