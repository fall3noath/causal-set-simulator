# Causal Set Simulator

A computational physics project exploring discrete spacetime geometry through causal set theory.

<p align="center">
  <img src="examples/demo_screenshot.png" width="1200">
</p>

---

## Overview

This project simulates spacetime as a discrete causal structure rather than a continuous geometric manifold.

Instead of treating spacetime as infinitely smooth, the simulator models spacetime as a finite set of events connected by causal relationships. These relationships form a directed acyclic graph that approximates Lorentzian geometry.

The project combines ideas from:

- causal set theory
- general relativity
- graph theory
- discrete geometry
- computational physics

The central idea behind causal set theory is:

> spacetime geometry may emerge purely from causal order and discreteness.

This repository attempts to explore that idea computationally.

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

These interval relations define the causal structure used to construct the graph.

---

## Causal Set Theory

In causal set theory:

- events become graph nodes
- causal relationships become directed edges
- geometry emerges from graph structure

The resulting graph approximates spacetime geometry at large scales.

---

## Computational Pipeline

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

Longest chains within the causal graph approximate timelike geodesics.

The simulator computes longest directed paths through the reduced graph to estimate discrete worldlines and proper-time maximizing trajectories.

---

## Dimension Estimation

Longest chains within the causal graph approximate timelike geodesics.

The simulator computes longest directed paths through the reduced graph to estimate discrete worldlines and proper-time maximizing trajectories.

---

## Curved Spacetime Support

The framework includes a modular spacetime abstraction system.

Current implementations include:

- Minkowski spacetime
- Schwarzschild spacetime

This allows the simulator to model both flat and curved causal structures.


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
