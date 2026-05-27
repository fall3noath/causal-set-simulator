import json
import tempfile
import webbrowser

import plotly.graph_objects as go


COSMIC_STOPS = [
    (0.00, (255, 77, 248)),    # pink
    (0.20, (139, 92, 246)),    # purple
    (0.40, (0, 153, 255)),     # blue
    (0.60, (0, 229, 255)),     # cyan
    (0.80, (102, 255, 178)),   # green
    (1.00, (255, 240, 90)),    # yellow
]


def _interp_color(stops, t):
    t = max(0.0, min(1.0, t))

    for i in range(len(stops) - 1):
        t0, c0 = stops[i]
        t1, c1 = stops[i + 1]

        if t0 <= t <= t1:
            f = 0 if t1 == t0 else (t - t0) / (t1 - t0)
            r = c0[0] + (c1[0] - c0[0]) * f
            g = c0[1] + (c1[1] - c0[1]) * f
            b = c0[2] + (c1[2] - c0[2]) * f

            return int(r), int(g), int(b)

    return stops[-1][1]


def _color_for(t_value, t_min, t_max):
    norm = (
        0.5
        if t_max == t_min
        else (t_value - t_min) / (t_max - t_min)
    )

    return _interp_color(COSMIC_STOPS, norm)


def _rgb(c):
    return f"rgb({c[0]},{c[1]},{c[2]})"


def _rgba(c, a):
    return f"rgba({c[0]},{c[1]},{c[2]},{a})"


def _build_figure(events, graph, highlighted_path):
    t_values = [e.t for e in events]
    t_min, t_max = min(t_values), max(t_values)

    node_colors = [
        _color_for(e.t, t_min, t_max) for e in events
    ]

    edge_groups = {}

    for source, target in graph.edges:
        a = events[source]
        b = events[target]
        color = node_colors[source]

        edge_groups.setdefault(color, ([], []))
        edge_groups[color][0].extend([a.x, b.x, None])
        edge_groups[color][1].extend([a.t, b.t, None])

    fig = go.Figure()

    for color, (xs, ys) in edge_groups.items():
        fig.add_trace(
            go.Scatter(
                x=xs,
                y=ys,
                mode="lines",
                line=dict(width=0.6, color=_rgba(color, 0.18)),
                hoverinfo="none",
                showlegend=False,
                meta="edges",
            )
        )

    fig.add_trace(
        go.Scatter(
            x=[-1.15, 1.15],
            y=[-1.15, 1.15],
            mode="lines",
            line=dict(dash="dash", width=1, color="rgba(255,255,255,0.28)"),
            hoverinfo="none",
            showlegend=False,
            meta="lightcone",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=[1.15, -1.15],
            y=[-1.15, 1.15],
            mode="lines",
            line=dict(dash="dash", width=1, color="rgba(255,255,255,0.28)"),
            hoverinfo="none",
            showlegend=False,
            meta="lightcone",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[e.x for e in events],
            y=[e.t for e in events],
            mode="markers",
            marker=dict(
                size=7,
                color=[_rgb(c) for c in node_colors],
                line=dict(width=0.4, color="rgba(255,255,255,0.35)"),
            ),
            text=[
                f"Event {e.id}<br>t={e.t:.3f}<br>x={e.x:.3f}"
                for e in events
            ],
            hoverinfo="text",
            showlegend=False,
            meta="nodes",
        )
    )

    if highlighted_path is not None and len(highlighted_path) > 1:
        for i in range(len(highlighted_path) - 1):
            a = events[highlighted_path[i]]
            b = events[highlighted_path[i + 1]]
            color = _color_for(a.t, t_min, t_max)

            fig.add_trace(
                go.Scatter(
                    x=[a.x, b.x],
                    y=[a.t, b.t],
                    mode="lines",
                    line=dict(width=4.5, color=_rgb(color)),
                    hoverinfo="none",
                    showlegend=False,
                    meta="chain",
                )
            )

        chain_colors = [
            _color_for(events[i].t, t_min, t_max)
            for i in highlighted_path
        ]

        fig.add_trace(
            go.Scatter(
                x=[events[i].x for i in highlighted_path],
                y=[events[i].t for i in highlighted_path],
                mode="markers",
                marker=dict(
                    size=11,
                    color=[_rgb(c) for c in chain_colors],
                    line=dict(width=1.2, color="white"),
                ),
                hoverinfo="none",
                showlegend=False,
                meta="chain",
            )
        )

    fig.update_layout(
        paper_bgcolor="#02040a",
        plot_bgcolor="#02040a",
        margin=dict(l=60, r=30, t=70, b=60),
        font=dict(family="Inter, Courier New, monospace", color="#d7e1e8"),
        showlegend=False,
        title=dict(
            text=(
                "<span style='font-size:26px;color:#66fcff;"
                "letter-spacing:4px;'>CAUSAL SET SIMULATOR</span><br>"
                "<span style='font-size:13px;color:#9aa7b2;"
                "letter-spacing:3px;'>DISCRETE SPACETIME GEOMETRY</span>"
            ),
            x=0.5,
            y=0.97,
        ),
        xaxis=dict(
            title="x",
            range=[-1.2, 1.2],
            showgrid=True,
            gridcolor="rgba(120,150,180,0.08)",
            zeroline=False,
            linecolor="rgba(255,255,255,0.15)",
            mirror=True,
            tickfont=dict(color="#9aa7b2"),
        ),
        yaxis=dict(
            title="t",
            range=[-1.2, 1.2],
            showgrid=True,
            gridcolor="rgba(120,150,180,0.08)",
            zeroline=False,
            linecolor="rgba(255,255,255,0.15)",
            mirror=True,
            tickfont=dict(color="#9aa7b2"),
            scaleanchor="x",
            scaleratio=1,
        ),
    )

    fig.add_annotation(
        x=0.5,
        y=-0.13,
        xref="paper",
        yref="paper",
        text=(
            "<span style='letter-spacing:3px;'>MINKOWSKI SPACETIME"
            "&nbsp;&nbsp;|&nbsp;&nbsp;POISSON SPRINKLING</span>"
        ),
        showarrow=False,
        bordercolor="rgba(0,229,255,0.35)",
        borderwidth=1,
        borderpad=10,
        bgcolor="rgba(0,0,0,0.35)",
        font=dict(size=12, color="#00e5ff"),
    )

    return fig


_PAGE_TEMPLATE = r"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Causal Set Simulator</title>
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
<style>
  :root {
    --bg: #02040a;
    --panel: #07101a;
    --panel-border: rgba(0,229,255,0.18);
    --text: #d7e1e8;
    --muted: #8593a0;
    --accent: #66fcff;
    --pink: #ff4df8;
  }
  * { box-sizing: border-box; }
  html, body {
    margin: 0; padding: 0;
    background: var(--bg);
    color: var(--text);
    font-family: Inter, -apple-system, "Segoe UI", Roboto, sans-serif;
    height: 100%;
  }
  .app {
    display: grid;
    grid-template-columns: 220px 1fr 220px;
    gap: 16px;
    padding: 16px;
    height: 100vh;
  }
  .col-left, .col-right {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }
  .panel {
    background: var(--panel);
    border: 1px solid var(--panel-border);
    border-radius: 4px;
    padding: 16px 18px;
  }
  .panel h2 {
    margin: 0 0 14px 0;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 3px;
    color: var(--pink);
  }
  .panel.legend h2,
  .panel.controls h2 {
    color: var(--accent);
  }
  .stat-label {
    font-size: 12px;
    color: var(--muted);
    margin-top: 10px;
  }
  .stat-value {
    font-size: 18px;
    color: var(--text);
    margin-top: 2px;
  }
  .stat-divider {
    height: 1px;
    background: rgba(255,255,255,0.08);
    margin: 14px 0 8px 0;
  }
  .dim-value {
    font-size: 56px;
    color: var(--pink);
    font-weight: 300;
    text-align: center;
    line-height: 1;
    margin-top: 8px;
  }
  .dim-sub {
    text-align: center;
    color: var(--muted);
    font-size: 12px;
    margin-top: 6px;
  }
  .control-row { margin-bottom: 14px; }
  .control-row label {
    display: block;
    font-size: 12px;
    color: var(--muted);
    margin-bottom: 6px;
  }
  input[type=range] {
    width: 100%;
    accent-color: var(--accent);
  }
  select {
    width: 100%;
    background: #0a1722;
    color: var(--text);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 3px;
    padding: 6px 8px;
    font-size: 13px;
  }
  .toggle-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 10px 0;
    font-size: 13px;
    color: var(--text);
  }
  .switch {
    position: relative;
    width: 36px; height: 20px;
    background: rgba(255,255,255,0.12);
    border-radius: 10px;
    cursor: pointer;
    transition: background 0.2s;
  }
  .switch.on { background: var(--accent); }
  .switch::after {
    content: "";
    position: absolute;
    top: 2px; left: 2px;
    width: 16px; height: 16px;
    background: white;
    border-radius: 50%;
    transition: left 0.2s;
  }
  .switch.on::after { left: 18px; }
  .legend-row {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 10px 0;
    font-size: 12px;
    color: var(--text);
  }
  .legend-row .swatch {
    width: 28px;
    display: flex;
    justify-content: center;
  }
  .legend-row .sub {
    font-size: 10px;
    color: var(--muted);
    display: block;
  }
  .dot {
    width: 10px; height: 10px;
    border-radius: 50%;
    background: var(--accent);
  }
  .line-thin {
    width: 24px; height: 1px;
    background: rgba(255,255,255,0.4);
  }
  .line-thick {
    width: 24px; height: 3px;
    background: var(--accent);
    border-radius: 2px;
  }
  .line-dash {
    width: 24px; height: 0;
    border-top: 1px dashed rgba(255,255,255,0.45);
  }
  .tip-text {
    font-size: 12px;
    color: var(--muted);
    line-height: 1.5;
  }
  #plot {
    background: var(--bg);
    border-radius: 4px;
    min-height: 0;
  }
</style>
</head>
<body>
<div class="app">
  <div class="col-left">

    <div class="panel">
      <h2>SYSTEM INFO</h2>
      <div class="stat-label">Events</div>
      <div class="stat-value">__EVENTS__</div>
      <div class="stat-label">Causal Relations</div>
      <div class="stat-value">__RELATIONS__</div>
      <div class="stat-label">Longest Chain Length</div>
      <div class="stat-value">__CHAIN__</div>
      <div class="stat-divider"></div>
      <div class="stat-label" style="text-align:center;">Estimated Dimension</div>
      <div class="dim-value">__DIM__</div>
      <div class="dim-sub">(&approx; 1+1D)</div>
    </div>

    <div class="panel controls">
      <h2>CONTROLS</h2>
      <div class="control-row">
        <label>Point Size</label>
        <input id="pointSize" type="range" min="3" max="14" value="7">
      </div>
      <div class="control-row">
        <label>Edge Opacity</label>
        <input id="edgeOpacity" type="range" min="0" max="100" value="18">
      </div>
      <div class="control-row">
        <label>Color Gradient</label>
        <select><option>Cosmic</option></select>
      </div>
      <div class="toggle-row">
        <span>Show Light Cones</span>
        <div id="toggleCones" class="switch on"></div>
      </div>
      <div class="toggle-row">
        <span>Show Edges</span>
        <div id="toggleEdges" class="switch on"></div>
      </div>
      <div class="toggle-row">
        <span>Animate Path</span>
        <div id="toggleAnim" class="switch"></div>
      </div>
    </div>

    <div class="panel">
      <h2>TIP</h2>
      <div class="tip-text">
        Drag to pan, scroll to zoom,<br>
        hold shift and drag to box zoom.
      </div>
    </div>

  </div>

  <div id="plot"></div>

  <div class="col-right">
    <div class="panel legend">
      <h2>LEGEND</h2>
      <div class="legend-row">
        <div class="swatch"><div class="dot"></div></div>
        <span>Event</span>
      </div>
      <div class="legend-row">
        <div class="swatch"><div class="line-thin"></div></div>
        <span>Causal Edge</span>
      </div>
      <div class="legend-row">
        <div class="swatch"><div class="line-thick"></div></div>
        <span>Longest Chain
          <span class="sub">(Approx. Geodesic)</span>
        </span>
      </div>
      <div class="legend-row">
        <div class="swatch"><div class="line-dash"></div></div>
        <span>Light Cone</span>
      </div>
    </div>
  </div>
</div>

<script>
  const figure = __FIGURE_JSON__;
  const plotDiv = document.getElementById("plot");

  Plotly.newPlot(plotDiv, figure.data, figure.layout, {
    responsive: true,
    displaylogo: false,
    modeBarButtonsToRemove: ["lasso2d", "select2d"],
  });

  function tracesByMeta(meta) {
    const idx = [];
    figure.data.forEach((tr, i) => {
      if (tr.meta === meta) idx.push(i);
    });
    return idx;
  }

  document.getElementById("pointSize").addEventListener("input", e => {
    const v = parseFloat(e.target.value);
    Plotly.restyle(plotDiv, { "marker.size": v }, tracesByMeta("nodes"));
  });

  const baseEdgeColors = {};
  figure.data.forEach((tr, i) => {
    if (tr.meta === "edges") baseEdgeColors[i] = tr.line.color;
  });

  document.getElementById("edgeOpacity").addEventListener("input", e => {
    const a = parseFloat(e.target.value) / 100;
    Object.entries(baseEdgeColors).forEach(([i, col]) => {
      const m = col.match(/rgba?\((\d+),\s*(\d+),\s*(\d+)/);
      if (!m) return;
      const newCol = `rgba(${m[1]},${m[2]},${m[3]},${a})`;
      Plotly.restyle(plotDiv, { "line.color": newCol }, [parseInt(i)]);
    });
  });

  function toggleSwitch(el, meta) {
    const on = el.classList.toggle("on");
    Plotly.restyle(
      plotDiv,
      { visible: on ? true : "legendonly" },
      tracesByMeta(meta)
    );
  }

  document.getElementById("toggleCones").addEventListener("click", e => {
    toggleSwitch(e.currentTarget, "lightcone");
  });
  document.getElementById("toggleEdges").addEventListener("click", e => {
    toggleSwitch(e.currentTarget, "edges");
  });

  let animTimer = null;
  document.getElementById("toggleAnim").addEventListener("click", e => {
    const on = e.currentTarget.classList.toggle("on");
    const chainIdx = tracesByMeta("chain");
    if (on) {
      let phase = 0;
      animTimer = setInterval(() => {
        phase = (phase + 0.08) % (2 * Math.PI);
        const w = 4.5 + Math.sin(phase) * 1.8;
        Plotly.restyle(plotDiv, { "line.width": w }, chainIdx);
      }, 50);
    } else {
      clearInterval(animTimer);
      Plotly.restyle(plotDiv, { "line.width": 4.5 }, chainIdx);
    }
  });
</script>
</body>
</html>
"""


def interactive_causal_plot(
    events,
    graph,
    highlighted_path=None,
    estimated_dimension=None,
    causal_relations_count=None,
    open_browser=True,
):
    """
    Render the causal set as an interactive HTML dashboard.

    Parameters
    ----------
    events : list[Event]
    graph : networkx.DiGraph
        Graph to draw (typically the transitively reduced graph).
    highlighted_path : list[int] | None
        Node IDs along the longest chain.
    estimated_dimension : int | None
    causal_relations_count : int | None
        Optional override for the "Causal Relations" stat. Pass
        the full (un-reduced) edge count to reflect the underlying
        causal structure rather than the drawn reduced graph.
    open_browser : bool
        If True, automatically open the resulting HTML file.

    Returns
    -------
    str
        Path to the generated HTML file.
    """

    fig = _build_figure(events, graph, highlighted_path)

    relations = (
        graph.number_of_edges()
        if causal_relations_count is None
        else causal_relations_count
    )
    chain_len = (
        len(highlighted_path) if highlighted_path else 0
    )
    dim_text = (
        "—"
        if estimated_dimension is None
        else str(estimated_dimension)
    )

    fig_dict = fig.to_dict()

    def _to_native(obj):
        if hasattr(obj, "tolist"):
            return obj.tolist()
        return str(obj)

    figure_json = json.dumps(
        {"data": fig_dict["data"], "layout": fig_dict["layout"]},
        default=_to_native,
    )

    html = (
        _PAGE_TEMPLATE
        .replace("__EVENTS__", f"{len(events):,}")
        .replace("__RELATIONS__", f"{relations:,}")
        .replace("__CHAIN__", str(chain_len))
        .replace("__DIM__", dim_text)
        .replace("__FIGURE_JSON__", figure_json)
    )

    tmp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".html",
        mode="w",
        encoding="utf-8",
    )
    tmp.write(html)
    tmp.close()

    if open_browser:
        webbrowser.open("file://" + tmp.name)

    return tmp.name
