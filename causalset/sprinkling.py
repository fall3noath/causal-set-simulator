import numpy as np

from causalset.events import Event


def poisson_sprinkle(
    n,
    t_range=(-1, 1),
    x_range=(-1, 1),
    seed=None,
):
    rng = np.random.default_rng(seed)

    events = []

    for i in range(n):
        t = rng.uniform(*t_range)
        x = rng.uniform(*x_range)

        events.append(Event(i, t, x))

    return events
