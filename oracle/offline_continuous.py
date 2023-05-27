from oracle.oracle import *

# concrete combinations of the different possibilities
# put into a seperate file so from import * only imports offline continous classes


class Binpp(BinppRead, Offline, Continuous):
    pass


class Hard(HardRead, Offline, Continuous):
    pass


class Jburkardt(JburkardtRead, Offline, Continuous):
    pass
