from causalset.spacetime import Spacetime


class SchwarzschildSpacetime(Spacetime):
    def __init__(self, mass=1.0):
        self.mass = mass

    def schwarzschild_factor(self, r):
        return 1 - (2 * self.mass / r)

    def interval(self, a, b):
        dt = b.t - a.t
        dr = b.x - a.x

        r = (a.x + b.x) / 2

        if r <= 2 * self.mass:
            return float("-inf")

        factor = self.schwarzschild_factor(r)

        return factor * dt**2 - (dr**2 / factor)

    def causally_related(self, a, b):
        dt = b.t - a.t

        if dt <= 0:
            return False

        return self.interval(a, b) >= 0
