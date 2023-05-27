from macpacking import Solution, WeightSet
from macpacking.model import Offline, ConstantBin
from macpacking.algorithms.online import NextFit as Nf_online
from macpacking.algorithms.online import FirstFit as Ff_online
from macpacking.algorithms.online import BestFit as Bf_online
from macpacking.algorithms.online import WorstFit as Wf_online


class NextFit(Offline):
    def _process(self, capacity: int, weights: WeightSet) -> Solution:
        """An offline version of NextFit, ordering the weigh stream and
        delegating to the online version (avoiding code duplication)"""
        weights = sorted(weights, reverse=True)
        delegation = Nf_online()
        return delegation((capacity, weights))


class FirstFit(Offline):
    def _process(self, capacity: int, weights: WeightSet) -> Solution:
        """An offline version of FirstFit, ordering the weigh stream and
        delegating to the online version (avoiding code duplication)"""
        weights = sorted(weights, reverse=True)
        delegation = Ff_online()
        return delegation((capacity, weights))


class BestFit(Offline):
    def _process(self, capacity: int, weights: WeightSet) -> Solution:
        """An offline version of BestFit, ordering the weigh stream and
        delegating to the online version (avoiding code duplication)"""
        weights = sorted(weights, reverse=True)
        delegation = Bf_online()
        return delegation((capacity, weights))


class WorstFit(Offline):
    def _process(self, capacity: int, weights: WeightSet) -> Solution:
        """An offline version of WorstFit, ordering the weigh stream and
        delegating to the online version (avoiding code duplication)"""
        weights = sorted(weights, reverse=True)
        delegation = Wf_online()
        return delegation((capacity, weights))


class FirstFitRefined(Offline):
    def _process(self, capacity: int, weights: WeightSet) -> Solution:
        # Normalizing Factor
        factor = max(weights)
        c = capacity
        # Four Classes of Bins
        bins1 = [[]]
        bins2 = [[]]
        bins3 = [[]]
        bins4 = [[]]
        # Number of Occurrences of b2 elements
        m = 0
        for w in weights:
            n = w / factor
            added = False
            # A elements go in bins1
            if n > 1 / 2:
                for bin in bins1:
                    if (c - sum(bin)) >= w:
                        bin.append(w)
                        added = True
                        break
                if not added:
                    bins1.append([w])
            # B1 elements go in bins2
            elif 2 / 5 < n <= 1 / 2:
                for bin in bins2:
                    if (c - sum(bin)) >= w:
                        bin.append(w)
                        added = True
                        break
                if not added:
                    bins2.append([w])
            # B2 elements go in bins3
            # if it is the M*K th element (for m in (6,7,8,9) and any int k) it goes in bins 1
            elif 1 / 3 < n <= 2 / 5:
                m += 1
                if m % 6 == 0 or m % 7 == 0 or m % 8 == 0 or m % 9 == 0:
                    for bin in bins1:
                        if (c - sum(bin)) >= w:
                            bin.append(w)
                            added = True
                            break
                    if not added:
                        bins1.append([w])
                else:
                    for bin in bins3:
                        if (c - sum(bin)) >= w:
                            bin.append(w)
                            added = True
                            break
                    if not added:
                        bins3.append([w])
            # X elements go in bins4
            else:
                for bin in bins4:
                    if (c - sum(bin)) >= w:
                        bin.append(w)
                        added = True
                        break
                if not added:
                    bins4.append([w])
        solution = bins1 + bins2 + bins3 + bins4

        return solution


class MinBin(ConstantBin):

    # reads the capacity as the number of bins
    def _process(self, bins: int, weights: list[int]) -> Solution:
        # finds the bin with the smallest size and adds the element to that bin
        solution = []
        for _ in range(bins):
            solution.append([])
        sizes = [0] * bins

        for w in weights:
            index = sizes.index(min(sizes))
            solution[index].append(w)
            sizes[index] += w

        return solution
