from memoria import *
from loader import *
from dumper import *
from motor import *

def simulador():

    np.set_printoptions(formatter={'int': lambda x: hex(int(x))})

    memoria = Memoria(10)
    dumper = Dumper()
    loader = Loader()
    motor = Motor()

    dumper.dumpscreen(memoria)
    memoria.memory[0] = 0x9
    memoria.memory[1] = 0
    memoria.memory[2] = 0
    memoria.memory[3] = 0x4
    memoria.memory[4] = 5

    dumper.dumpscreen(memoria)

    dumper.dumpfile("test",memoria)
    loader.load("test.npy",memoria)
    dumper.dumpscreen(memoria)

    motor.fetch(memoria,0,0xf)

    dumper.dumpscreen(memoria)
    print(hex(motor.pc))





simulador()