from oracle.oracle import *

# concrete combinations of the different possibilities
# put into a seperate file so from import * only imports online concrete classes


class Binpp(BinppRead, Online, Discrete):
    pass


class Hard(HardRead, Online, Discrete):
    pass


class Jburkardt(JburkardtRead, Online, Discrete):
    pass
