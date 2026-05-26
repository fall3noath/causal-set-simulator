# Causal Set Simulator

A computational physics project exploring discrete spacetime geometry through causal set theory.

<p align="center">
  <img src="examples/demo_screenshot.png" width="1200">
</p>

---

## Overview

This project simulates spacetime as a discrete causal structure rather than a continuous geometric manifold.

Instead of treating spacetime as infinitely smooth, the simulator models spacetime as a finite set of events connected by causal relationships. These relationships form a directed acyclic graph that approximates Lorentzian geometry.

The project explores ideas from:

- causal set theory
- general relativity
- discrete geometry
- graph theory
- computational spacetime physics

The core philosophical idea behind causal set theory is:

> spacetime geometry may emerge purely from causal order and discreteness.

This repository attempts to explore that idea computationally.

---

## Example Visualization

The simulator generates discrete spacetime events, computes relativistic causal structure, extracts geodesics, and visualizes the resulting causal network interactively.

Features of the visualization include:

- causal edges
- longest-chain geodesics
- light cone structure
- dimension estimation
- interactive spacetime exploration
- dark sci-fi dashboard interface

---

## Features

- Poisson spacetime sprinkling
- Relativistic causal relation detection
- Directed acyclic causal graph construction
- Transitive reduction
- Geodesic approximation through longest chains
- Dimension estimation
- Curved spacetime support
- Interactive visualization
- Modular spacetime abstraction system

---

## Physics Background

### Minkowski Spacetime

In special relativity, spacetime intervals are described by the Minkowski metric:

$$
ds^2 = -dt^2 + dx^2
$$

Two events are causally related if:

$$
(t_B - t_A)^2 - (x_B - x_A)^2 \geq 0
$$

with:

$$
t_B > t_A
$$

This determines whether information or influence can propagate between events without exceeding the speed of light.

The simulator uses these interval relations to construct a causal graph.

---

## Causal Set Theory

Causal set theory proposes that spacetime may fundamentally consist of:

- discrete events
- causal ordering relations

rather than continuous coordinates.

In this framework:

- events become graph nodes
- causal relationships become directed edges
- geometry emerges from graph structure

The resulting graph approximates spacetime geometry at large scales.

---

## Computational Pipeline

The simulator follows this pipeline:

```text
random spacetime events
        ↓
Lorentzian interval checks
        ↓
causal relation detection
        ↓
directed acyclic graph construction
        ↓
transitive reduction
        ↓
geodesic extraction
        ↓
dimension estimation
        ↓
interactive visualization
```

---

## Geodesic Approximation

In causal set theory, longest chains within the causal graph approximate timelike geodesics.

This project computes longest directed paths through the reduced causal graph to estimate discrete worldlines and proper-time maximizing trajectories.

---

## Dimension Estimation

The simulator includes a simplified dimension estimator based on causal relation density.

The goal is to estimate effective spacetime dimension using graph structure alone.

This explores one of the central questions of causal set theory:

> Can geometry emerge from causal order?

---

## Curved Spacetime Support

The framework includes a modular spacetime abstraction system.

Current implementations include:

- Minkowski spacetime
- Schwarzschild spacetime

This allows the simulator to model both flat and curved causal structures.

Future planned geometries include:

- Kruskal-Szekeres coordinates
- de Sitter spacetime
- Penrose compactifications

---

## Repository Structure

```text
causal-set-simulator/
│
├── causalset/
│   ├── events.py
│   ├── spacetime.py
│   ├── minkowski.py
│   ├── schwarzschild.py
│   ├── graph.py
│   ├── geodesics.py
│   ├── reduction.py
│   ├── dimension.py
│   ├── visualization.py
│   └── interactive.py
│
├── examples/
│   └── minkowski_demo.py
│
├── requirements.txt
└── README.md
```

---

## Installation

Install dependencies:

```bash
pip3 install -r requirements.txt
```

---

## Run

From the repository root:

```bash
PYTHONPATH=. python3 examples/minkowski_demo.py
```

---

## Technologies Used

- Python
- NumPy
- NetworkX
- Plotly
- Matplotlib

---

## Future Goals

- Penrose diagram visualization
- Kruskal coordinate support
- GPU acceleration
- Large-scale causal set generation
- WebGL visualization
- Research-grade dimension estimators
- Higher-dimensional spacetime simulation

---

## Why This Project Is Interesting

Most physics simulations numerically solve equations on continuous spacetime backgrounds.

This project instead attempts to reconstruct spacetime geometry itself from causal structure alone.

That makes it fundamentally a problem in:

- discrete geometry
- graph theory
- emergent structure
- computational relativity

rather than conventional numerical physics.
