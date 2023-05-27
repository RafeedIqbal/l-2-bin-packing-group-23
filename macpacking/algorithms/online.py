import math
from typing import List

from macpacking import Solution, WeightStream
from macpacking.model import Online


class NextFit(Online):
    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        bin_index = 0
        solution = [[]]
        remaining = capacity
        for w in stream:
            if remaining >= w:
                solution[bin_index].append(w)
                remaining = remaining - w
            else:
                bin_index += 1
                solution.append([w])
                remaining = capacity - w
        return solution


class WorstPossible(Online):
    # creates new bin for every new element
    def _process(self, c: int, stream: WeightStream) -> Solution:
        solution = []
        for w in stream:
            solution.append([w])
        return solution


class FirstFit(Online):
    # adds weight to first bin in which it can fit
    # adds a new bin if none exist
    def _process(self, c: int, stream: WeightStream) -> Solution:
        solution = []
        for w in stream:
            added = False
            for bin in solution:
                if (c - sum(bin)) >= w:
                    bin.append(w)
                    added = True
                    break
            if not added:
                solution.append([w])
        return solution


class BestFit(Online):

    # finds and stores the bin with the least remaining amount of space which can fit w
    # then adds the weight to the respective bin or adds a new one if none exist
    def _process(self, c: int, stream: WeightStream) -> Solution:
        solution = []

        for w in stream:
            min_bin = None
            min_space = math.inf

            for bin in solution:

                space = sum(bin)
                if space + w <= c and space < min_space:
                    min_space = space
                    min_bin = bin

            # if min_bin is none then that means that there were no valid bins
            # so if it has a value add w to that respective bin
            # if not then make a new bin
            if min_bin:
                solution[solution.index(min_bin)].append(w)
            else:
                solution.append([w])

        return solution


class WorstFit(Online):

    # finds and stores the bin with the most remaining amount of space which can fit w
    # then adds the weight to the respective bin or adds a new one if none exist
    def _process(self, c: int, stream: WeightStream) -> Solution:
        solution = []

        for w in stream:
            max_bin = None
            max_space = -math.inf

            for bin in solution:

                space = sum(bin)
                if space + w <= c and space > max_space:
                    max_space = space
                    max_bin = bin

            # if max_bin is none then that means that there were no valid bins
            # so if it has a value add w to that respective bin
            # if not then make a new bin
            if max_bin:
                solution[solution.index(max_bin)].append(w)
            else:
                solution.append([w])

        return solution
