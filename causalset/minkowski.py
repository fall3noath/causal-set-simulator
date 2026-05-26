from causalset.spacetime import Spacetime


class MinkowskiSpacetime(Spacetime):
    def interval(self, a, b):
        dt = b.t - a.t
        dx = b.x - a.x

        return dt**2 - dx**2

    def causally_related(self, a, b):
        dt = b.t - a.t

        if dt <= 0:
            return False

        return self.interval(a, b) >= 0
