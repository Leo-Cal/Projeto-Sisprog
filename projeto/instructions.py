from motor import *


def jp(motor,memoria):

    # get membank
    #membank = [int(x) for x in str(motor.pc)]
    #membank = membank[0]
    membank = motor.pc >> 4


    # get attributes

    digits = [membank, memoria.memory[motor.pc + 1], memoria.memory[motor.pc + 2], memoria.memory[motor.pc + 3]]
    attribute = 0
    for val in digits:
        attribute = (attribute << 4) + val

    print("Atrribute",hex(attribute))  # test attribute

    motor.pc = attribute

    if(motor.trace):
        print("JP successful")

def jz(motor,memoria):

    #get membank
    membank = motor.pc >> 4

    #get attributes
    digits = [membank,memoria.memory[motor.pc+1], memoria.memory[motor.pc+2],memoria.memory[motor.pc+3]]
    attribute = 0
    for val in digits :
        attribute = (attribute<<4) + val

    print("Attribute",hex(attribute)) #test attribute

    #test jump condition
    if motor.acc == 0 :
        motor.pc = attribute
        if (motor.trace):
            print("JZ successfull")
    else:
        motor.pc = motor.pc + 4
        if not(motor.trace):
            print("JZ not successfull")


def jn(motor,memoria):

    # get membank
    membank = motor.pc >> 4

    # get attributes
    digits = [membank, memoria.memory[motor.pc + 1], memoria.memory[motor.pc + 2], memoria.memory[motor.pc + 3]]
    attribute = 0
    for val in digits:
        attribute = (attribute << 4) + val

    print("Attribute",hex(attribute))  # test attribute

    #test jump condition
    if motor.acc < 0 :
        motor.pc = attribute
        if (motor.trace):
            print("JN successfull")
    else:
        motor.pc = motor.pc + 4
        if not(motor.trace):
            print("JN not successfull")

def cn(motor,memoria):

    attribute = motor.pc + 1
    #RODAR INSTRUÇOES DE CONTROLE
    motor.pc = motor.pc + 1

def sumi(motor,memoria):

    # get membank
    membank = motor.pc >> 4

    # get attributes
    digits = [membank, memoria.memory[motor.pc + 1], memoria.memory[motor.pc + 2], memoria.memory[motor.pc + 3]]
    attribute = 0
    for val in digits:
        attribute = (attribute << 4) + val

    print("Attribute Address: ", hex(attribute))  # test attribute
    #print("Attribute :",memoria.memory[hex(attribute)])

    motor.acc = motor.acc + memoria.memory[attribute]

    print(motor.acc)

    motor.pc = motor.pc + 4

    if(motor.trace):
        print("Sum Successfull")


def subi(motor,memoria):

    # get membank
    membank = motor.pc >> 4

    # get attributes
    digits = [membank, memoria.memory[motor.pc + 1], memoria.memory[motor.pc + 2], memoria.memory[motor.pc + 3]]
    attribute = 0
    for val in digits:
        attribute = (attribute << 4) + val

    print("Attribute Address: ", hex(attribute))  # test attribute
    #print("Attribute :",memoria.memory[hex(attribute)])

    motor.acc = motor.acc - memoria.memory[attribute]

    print(motor.acc)

    motor.pc = motor.pc + 4

    if(motor.trace):
        print("Subtraction Successfull")

def mul(motor,memoria):

    # get membank
    membank = motor.pc >> 4

    # get attributes
    digits = [membank, memoria.memory[motor.pc + 1], memoria.memory[motor.pc + 2], memoria.memory[motor.pc + 3]]
    attribute = 0
    for val in digits:
        attribute = (attribute << 4) + val

    print("Attribute Address: ", hex(attribute))  # test attribute
    #print("Attribute :",memoria.memory[hex(attribute)])

    motor.acc = motor.acc * memoria.memory[attribute]

    print(motor.acc)

    motor.pc = motor.pc + 4

    if(motor.trace):
        print("Multiplication Successfull")

def divi(motor,memoria):

    # get membank
    membank = motor.pc >> 4

    # get attributes
    digits = [membank, memoria.memory[motor.pc + 1], memoria.memory[motor.pc + 2], memoria.memory[motor.pc + 3]]
    attribute = 0
    for val in digits:
        attribute = (attribute << 4) + val

    print("Attribute Address: ", hex(attribute))  # test attribute
    #print("Attribute :",memoria.memory[hex(attribute)])

    motor.acc = motor.acc / memoria.memory[attribute]

    print(motor.acc)

    motor.pc = motor.pc + 4

    if(motor.trace):
        print("Division Successfull")


def ld(motor,memoria):

    # get membank
    membank = motor.pc >> 4

    # get attributes
    digits = [membank, memoria.memory[motor.pc + 1], memoria.memory[motor.pc + 2], memoria.memory[motor.pc + 3]]
    attribute = 0
    for val in digits:
        attribute = (attribute << 4) + val

    print("Attribute Address: ", hex(attribute))  # test attribute

    motor.acc = memoria.memory[attribute]

    print(motor.acc)

    motor.pc = motor.pc + 4

    if(motor.trace):
        print("Load Successfull")

def mm(motor,memoria):

    # get membank
    membank = motor.pc >> 4

    # get attributes
    digits = [membank, memoria.memory[motor.pc + 1], memoria.memory[motor.pc + 2], memoria.memory[motor.pc + 3]]
    attribute = 0
    for val in digits:
        attribute = (attribute << 4) + val

    print("Attribute Address: ", hex(attribute))  # test attribute

    memoria.memory[attribute] = motor.acc

    print(memoria.memory[attribute])

    motor.pc = motor.pc + 4

    if(motor.trace):
        print("Move Successfull")

def sc(motor,memoria):

    #IMPLEMENTAR SUBROUTINE CALL
    attribute = motor.pc

def os(motor,memoria):

    attribute = motor.pc + 1
    #RODAR SYSTEM CALLS
    motor.pc = motor.pc + 2


def io(motor,memoria):

    attribute = motor.pc + 1
    # RODAR IO
    motor.pc = motor.pc + 2