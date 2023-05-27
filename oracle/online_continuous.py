from oracle.oracle import *

# concrete combinations of the different possibilities
# put into a seperate file so from import * only imports online continous classes


class Binpp(BinppRead, Online, Continuous):
    pass


class Hard(HardRead, Online, Continuous):
    pass


class Jburkardt(JburkardtRead, Online, Continuous):
    pass
