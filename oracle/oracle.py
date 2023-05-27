from abc import ABC, abstractmethod
import macpacking.reader as r
import csv


class Oracle(ABC):
    def __init__(self, algorithms):
        self.algorithms = algorithms
        self.load_dataset()

    def load_dataset(self):
        self.dataset = {}
        with open(self.source + ".csv") as d:
            file = csv.reader(d)
            next(file)
            for row in file:
                self.dataset[row[0]] = row[1]

    def add_algo(self, algorithm):
        self.algorithms.append(algorithm)

    def remove_algo(self, algorithm):
        self.algorithms.remove(algorithm)

    def experiment(self):
        results = self.calculate()
        return self.format(results)

    # runs all of the stored problems for each algorithm and returns them
    # stores the result for each group of algorithm and problem
    def calculate(self):
        results = {}
        for algorithm in self.algorithms:
            results[algorithm.__name__] = {}
            for problem, optimal in self.dataset.items():
                path = self.get_path(problem)
                reader = self.reader(path)
                algo = algorithm()
                result = self.compare(len(algo(self.read(reader))), int(optimal))
                results[algorithm.__name__][problem] = result

        return results

    # formats the results down to one number per algorithm
    # does this by updating a counter for each result
    # and then formats that value for all the results
    def format(self, results):
        averages = {}
        for algorithm, algo_res in results.items():
            count = 0
            for result in algo_res.values():
                count = self.update_count(count, result)
            averages[algorithm] = self.format_count(count, algo_res)

        return averages

    @abstractmethod
    def read(self, reader):
        pass

    @abstractmethod
    def compare(self, computed, optimal):
        pass

    @abstractmethod
    def get_path(self, problem):
        pass

    @abstractmethod
    def update_count(self, count, result):
        pass

    @abstractmethod
    def format_count(self, count, algo_res):
        pass


# abstract classes for continuous or discrete


class Discrete(Oracle):
    def compare(self, computed, optimal):
        return computed == optimal

    def update_count(self, count, result):
        if result:
            return count + 1
        else:
            return count

    def format_count(self, count, algo_res):
        return float(100 * count) / float(len(algo_res))


class Continuous(Oracle):
    def compare(self, computed, optimal):
        return computed - optimal

    def update_count(self, count, result):
        return count + result

    def format_count(self, count, algo_res):
        return float(count) / float(len(algo_res))


# abstract classes for reading online or offline


class Online(Oracle):
    def read(self, reader):
        return reader.online()


class Offline(Oracle):
    def read(self, reader):
        return reader.offline()


# different abstract classes for the different datasets


class BinppRead(Oracle):

    reader = r.BinppReader
    source = "_datasets/binpp"

    def get_path(self, problem):
        return self.source + "/" + problem.split("_")[0] + "/" + problem + ".BPP.txt"


class HardRead(Oracle):

    reader = r.BinppReader
    source = "_datasets/binpp-hard"

    def get_path(self, problem):
        return self.source + "/" + problem + ".BPP.txt"


class JburkardtRead(Oracle):

    reader = r.JburkardtReader
    source = "_datasets/jburkardt"

    def get_path(self, problem):
        start = self.source + "/" + problem.replace("_", "")
        return [start + "_c.txt", start + "_s.txt", start + "_w.txt"]
