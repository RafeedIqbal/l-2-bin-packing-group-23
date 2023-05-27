import pyperf
from os import listdir
from os.path import isfile, join, basename
from macpacking.algorithms.online import *
from macpacking.reader import BinppReader


# We consider:
#   - 500 objects (N4)
#   - bin capacity of 120 (C2)
#   - and weight in the [20,100] interval (W2)
CASES = './_datasets/binpp/N4C2W2'
BINPACKERS = [WorstPossible(), FirstFit(), BestFit(), WorstFit()]


def main():
    '''Example of benchmark code'''
    cases = list_case_files(CASES)
    binpackers = BINPACKERS
    run_bench(cases, binpackers)


def list_case_files(dir: str) -> list[str]:
    return sorted([f'{dir}/{f}' for f in listdir(dir) if isfile(join(dir, f))])


def run_bench(cases: list[str], binpackers):
    runner = pyperf.Runner()
    for binpacker in binpackers:
        for case in cases:
            name = basename(case) + " " + binpacker.__class__.__name__
            data = BinppReader(case).online()
            runner.bench_func(name, binpacker, data)


if __name__ == "__main__":
    main()