import memoria
import  numpy as np

class Dumper:

    def __init__(self):

        return


    def dumpfile(self,filename,memoria):

        np.save(filename,memoria.memory)

    def dumpscreen(self,memoria):

        print(memoria.memory)