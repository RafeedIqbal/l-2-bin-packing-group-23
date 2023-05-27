from macpacking import Solution
from math import sqrt


def kpi_measurer(solution: Solution) -> (int, float):
    bins = 0
    total = 0
    variance = 0.0
    for b in solution:
        bins += 1
        total += sum(b)
    mean = total / bins
    for b in solution:
        variance += (mean - sum(b)) ** 2
    sd = sqrt(variance / bins)
    return bins, sd
