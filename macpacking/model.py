from abc import ABC, abstractmethod
from typing import Iterator
from macpacking import WeightStream, WeightSet, Solution


class BinPacker(ABC):
    pass


class Online(BinPacker):
    def __call__(self, ws: WeightStream):
        capacity, stream = ws
        return self._process(capacity, stream)

    @abstractmethod
    def _process(self, c: int, stream: Iterator[int]) -> Solution:
        pass


class Offline(BinPacker):
    def __call__(self, ws: WeightSet):
        capacity, weights = ws
        return self._process(capacity, weights)

    @abstractmethod
    def _process(self, c: int, weights: list[int]) -> Solution:
        pass


# essentially offline but with a reduction in the capacity input so that it is a difficult problem
class ConstantBin(BinPacker):
    def __call__(self, ws: WeightSet):
        bins, weights = ws
        # divided by 10 so same datasets can be used to demonstrate capabilities
        # ideally new datasets need to be made
        return self._process(bins // 10, weights)

    @abstractmethod
    def _process(self, bins: int, weights: list[int]) -> Solution:
        pass
