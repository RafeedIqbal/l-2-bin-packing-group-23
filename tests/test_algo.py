from macpacking.algorithms.offline import *
from macpacking.reader import BinppReader


def occurrences(result, weight):
    count = 0
    for bin in result:
        count += bin.count(weight)
    return count


def all_occurences(result, oracle):
    valid = True
    weights = list(dict.fromkeys(oracle))
    for weight in weights:
        if occurrences(result, weight) != oracle.count(weight):
            valid = False
            break
    return valid


def max_bin_size(result, capacity):
    valid = True
    for bin in result:
        if sum(bin) > capacity:
            valid = False
            break
    return valid


def runner(algorithm, reader, dataset):
    reader = reader(dataset)
    data = reader.offline()
    result = algorithm()(data)
    assert max_bin_size(result, data[0])
    assert all_occurences(result, data[1])


# General Cases Test
def test_algorithms():
    algorithms = [NextFit, FirstFit, BestFit, WorstFit, FirstFitRefined]
    reader = BinppReader
    dataset = "../_datasets/binpp/N1C1W1/N1C1W1_B.BPP.txt"

    for algorithm in algorithms:
        runner(algorithm, reader, dataset)
