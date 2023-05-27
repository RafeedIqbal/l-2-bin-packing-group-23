from os import listdir
from os.path import isfile, join, basename
from macpacking.algorithms.online import *
from macpacking.algorithms.offline import *
from macpacking.algorithms.baseline import ConstantBaseline
from macpacking.reader import BinppReader
from benchmarking.kpi import kpi_measurer


# We consider:
#   - 500 objects (N4)
#   - bin capacity of 120 (C2)
#   - and weight in the [20,100] interval (W2)
CASES = './_datasets/binpp/N4C2W2'
BINPACKERS = [WorstPossible(), FirstFit(), BestFit(), WorstFit()]
CONSTBINS = [MinBin(), ConstantBaseline()]

def main():
    '''Example of benchmark code'''
    cases = list_case_files(CASES)
    # for binpacker in BINPACKERS:
    #     run_bench(cases, binpacker)
    # run_bench2(cases)
    for binpacker in CONSTBINS:
        run_bench(cases, binpacker)


def list_case_files(dir: str) -> list[str]:
    return sorted([f'{dir}/{f}' for f in listdir(dir) if isfile(join(dir, f))])


def run_bench(cases: list[str], binpacker):
    print(binpacker)
    for case in cases:
        data = BinppReader(case).online()
        l = kpi_measurer(binpacker(data))
        print(l[0], l[1])

def run_bench2(cases: list[str]):
    print("FirstFitRefined")
    binpacker = FirstFitRefined()
    for case in cases:
        data = BinppReader(case).offline()
        l = kpi_measurer(binpacker(data))
        print(l[0], l[1])

def run_bench(cases: list[str], binpacker):
    print(binpacker)
    for case in cases:
        data = BinppReader(case).offline()
        l = kpi_measurer(binpacker(data))
        print(l[0], l[1])

if __name__ == "__main__":
    main()