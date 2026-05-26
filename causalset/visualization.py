import matplotlib.pyplot as plt


def plot_causal_set(
    events,
    graph,
    highlighted_path=None,
    show_lightcone=True,
):
    fig, ax = plt.subplots(figsize=(8, 8))

    for source, target in graph.edges:
        a = events[source]
        b = events[target]

        ax.plot(
            [a.x, b.x],
            [a.t, b.t],
            linewidth=0.4,
            alpha=0.25,
        )

    for event in events:
        ax.scatter(event.x, event.t, s=20)

    if highlighted_path is not None:
        for i in range(len(highlighted_path) - 1):
            a = events[highlighted_path[i]]
            b = events[highlighted_path[i + 1]]

            ax.plot(
                [a.x, b.x],
                [a.t, b.t],
                linewidth=2.5,
                alpha=0.9,
            )

    if show_lightcone:
        t_vals = [-1, 1]

        ax.plot(t_vals, t_vals, linestyle="--")
        ax.plot([-t for t in t_vals], t_vals, linestyle="--")

    ax.set_xlabel("x")
    ax.set_ylabel("t")

    ax.set_title("Causal Set Geometry")

    plt.show()
