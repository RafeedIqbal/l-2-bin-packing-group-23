from macpacking.reader import DatasetReader, BinppReader, JburkardtReader
from macpacking.algorithms.offline import *
from macpacking.algorithms.baseline import BenMaier

dataset = '_datasets/binpp/N1C1W1/N1C1W1_B.BPP.txt'
dataset = ['_datasets\jburkardt\p01_c.txt','_datasets\jburkardt\p01_s.txt','_datasets\jburkardt\p01_w.txt']

reader: DatasetReader = JburkardtReader(dataset)

binpacker = [NextFit, BestFit, FirstFit, WorstFit, BenMaier]

for bin in binpacker:
    a = bin()(reader.offline())
    print(bin.__name__ + ": " + str(a) + '\n')
