# Causal Set Simulator

A computational physics project exploring discrete spacetime geometry through causal set theory.

## Features

- Poisson spacetime sprinkling
- Relativistic causal relation detection
- Directed acyclic causal graph construction
- Transitive reduction
- Geodesic approximation through longest chains
- Dimension estimation
- Curved spacetime support
- Interactive visualization

## Physics Background

In 1+1 dimensional Minkowski spacetime:

ds² = -dt² + dx²

Two events are causally related if:

(t_B - t_A)^2 - (x_B - x_A)^2 >= 0

with:

t_B > t_A

The resulting directed graph approximates spacetime causal structure.

## Installation

pip install -r requirements.txt

## Run

python examples/minkowski_demo.py

## Future Goals

- Kruskal coordinates
- Penrose compactification
- GPU acceleration
- Higher-dimensional spacetimes
- Research-grade dimension estimators
