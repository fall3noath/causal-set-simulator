from abc import ABC, abstractmethod


class Spacetime(ABC):
    @abstractmethod
    def interval(self, a, b):
        pass

    @abstractmethod
    def causally_related(self, a, b):
        pass
