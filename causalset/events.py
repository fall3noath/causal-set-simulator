from dataclasses import dataclass


@dataclass(frozen=True)
class Event:
    id: int
    t: float
    x: float
