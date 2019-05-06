from loader import  *
from memoria import  *
from dumper import *
import numpy as np
from instructions import *

class Motor():

    def __init__(self):

        self.trace = True
        self.pc = 0 #program counter
        self.buffer = np.array([])
        self.acc = 0 #Acumulador
        self.r0 = 0x0 #Registrador que guarda o endereço pra retorno de subrotina
        self.fetcher = {

            0x0 : "JP",
            0x1 : "JZ",
            0x2 : "JN",
            0x3 : "CN",
            0x4 : "+",
            0x5 : "-",
            0x6 : "*",
            0x7 : "/",
            0x8 : "LD",
            0x9 : "MM",
            0xA : "SC",
            0xB : "OS",
            0xC : "IO",

        }

        self.instruction = {

            "JP" : jp,
            "JZ" : jz,
            "JN" : jn,
            "CN" : cn,
            "+" : sumi,
            "-" : subi,
            "*" : mul,
            "/" : divi,
            "LD" : ld,
            "MM" : mm,
            "SC" : sc,
            "OS" : os,
            "IO" : io,
        }

    def fetch(self,memoria, init, end) :

        self.pc = init

        #while (self.pc < end) :

        mnemonic = self.fetcher.get(memoria.memory[self.pc])
        func = self.instruction.get(mnemonic)
        func(self,memoria)






