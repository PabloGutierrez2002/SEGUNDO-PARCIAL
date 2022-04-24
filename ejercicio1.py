import pyfirmata
import time
board = pyfirmata.Arduino('COM3')

def  ascend():
    #Se encedera de manera acendente
    board.digital[13].write(1)
    time.sleep(.5)
    board.digital[12].write(1)
    time.sleep(.5)
    board.digital[9].write(1)
    time.sleep(.5)
    board.digital[8].write(1)
    time.sleep(.5)
    board.digital[7].write(1)
    time.sleep(.5)
    board.digital[4].write(1)
    time.sleep(.5)
    board.digital[13].write(0)
    board.digital[12].write(0)
    board.digital[9].write(0)
    board.digital[8].write(0)
    board.digital[7].write(0)
    board.digital[4].write(0)

def descent():
    #Se prendera de manera decendente
    board.digital[4].write(1)
    time.sleep(.5)
    board.digital[7].write(1)
    time.sleep(.5)
    board.digital[8].write(1)
    time.sleep(.5)
    board.digital[9].write(1)
    time.sleep(.5)
    board.digital[12].write(1)
    time.sleep(.5)
    board.digital[13].write(1)
    time.sleep(.5)
    board.digital[4].write(0)
    board.digital[7].write(0)
    board.digital[8].write(0)
    board.digital[9].write(0)
    board.digital[12].write(0)
    board.digital[13].write(0)

def funcion():
    leds = input("Elija la una opción\n Ingrese + para acendente\n Ingrese - para decendente\n").upper()
    if leds == '+':
        while True:
            ascend()
            break
    elif leds == '-':
        while True:
            descent()
            break
while True:
    funcion()

