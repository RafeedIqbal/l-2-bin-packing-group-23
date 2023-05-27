from abc import ABC, abstractmethod
from os import path
from random import shuffle, seed
from macpacking import WeightSet, WeightStream


class DatasetReader(ABC):
    def offline(self) -> WeightSet:
        """Return a WeightSet to support an offline algorithm"""
        (capacity, weights) = self._load_data_from_disk()
        seed(42)  # always produce the same shuffled result
        shuffle(weights)  # side effect shuffling
        return (capacity, weights)

    def online(self) -> WeightStream:
        """Return a WeighStream, to support an online algorithm"""
        (capacity, weights) = self.offline()

        def iterator():  # Wrapping the contents into an iterator
            for w in weights:
                yield w  # yields the current value and moves to the next one

        return (capacity, iterator())

    @abstractmethod
    def _load_data_from_disk(self) -> WeightSet:
        """Method that read the data from disk, depending on the file format"""
        pass


class BinppReader(DatasetReader):
    """Read problem description according to the BinPP format"""

    def __init__(self, filename: str) -> None:
        if not path.exists(filename):
            raise ValueError(f"Unkown file [{filename}]")
        self.__filename = filename

    def _load_data_from_disk(self) -> WeightSet:
        with open(self.__filename, "r") as reader:
            nb_objects: int = int(reader.readline())
            capacity: int = int(reader.readline())
            weights = []
            for _ in range(nb_objects):
                weights.append(int(reader.readline()))
            return (capacity, weights)


class JburkardtReader(DatasetReader):
    """Read problem description according to the Jburkardts format"""

    def __init__(self, filenames: list[str]) -> None:
        if not path.exists(filenames[0]):
            raise ValueError(f"Unkown file [{filenames[0]}]")
        elif not path.exists(filenames[1]):
            raise ValueError(f"Unkown file [{filenames[1]}]")
        elif not path.exists(filenames[2]):
            raise ValueError(f"Unkown file [{filenames[2]}]")

        self.__cfile = filenames[0]
        self.__sfile = filenames[1]
        self.__wfile = filenames[2]

    # c file is capacity
    # s file is priority
    # w file is weight

    def _load_data_from_disk(self) -> WeightSet:
        with open(self.__cfile, "r") as c:
            capacity: int = int(c.readline())

        with open(self.__sfile, "r") as s_f:
            s = s_f.readlines()
            for i in range(len(s)):
                if s[i] != "":
                    s[i] = int(s[i])
                else:
                    s.remove(s[i])

        with open(self.__wfile, "r") as w_f:
            w = w_f.readlines()

        max_p = max(s)
        weights = []

        for p in range(1, max_p + 1):
            for i in range(len(s)):
                if s[i] == p:
                    weights.append(int(w[i]))

        return (capacity, weights)
