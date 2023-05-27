from oracle.oracle import *

# concrete combinations of the different possibilities
# put into a seperate file so from import * only imports offline discrete classes


class Binpp(BinppRead, Offline, Discrete):
    pass


class Hard(HardRead, Offline, Discrete):
    pass


class Jburkardt(JburkardtRead, Offline, Discrete):
    pass
