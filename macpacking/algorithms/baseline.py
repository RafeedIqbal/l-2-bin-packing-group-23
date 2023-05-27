from macpacking import Solution
from macpacking.model import Offline, ConstantBin
import binpacking as bp


class BenMaier(Offline):
    def _process(self, capacity: int, weights: list[int]) -> Solution:
        return bp.to_constant_volume(weights, capacity)


class ConstantBaseline(ConstantBin):
    def _process(self, bins: int, weights: list[int]) -> Solution:
        return bp.to_constant_bin_number(weights, bins)
