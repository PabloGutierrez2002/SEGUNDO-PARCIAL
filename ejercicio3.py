import pyfirmata
import time
board = pyfirmata.Arduino('COM3')

it = pyfirmata.util.Iterator(board)
it.start()
poten = board.get_pin('a:0:i')

def  ascend():
    #Se encedera de manera acendente
    #se incrementa velocidad con potenciometro
    analog_value = poten.read()
    if analog_value is not None:
        delay = analog_value + 0.1
        board.digital[13].write(1)
        time.sleep(delay)
        board.digital[12].write(1)
        time.sleep(delay)
        board.digital[9].write(1)
        time.sleep(delay)
        board.digital[8].write(1)
        time.sleep(delay)
        board.digital[7].write(1)
        time.sleep(delay)
        board.digital[4].write(1)
        time.sleep(delay)
        board.digital[13].write(0)
        board.digital[12].write(0)
        board.digital[9].write(0)
        board.digital[8].write(0)
        board.digital[7].write(0)
        board.digital[4].write(0)
    else:
         time.sleep(0.1)

def descent():
    #Se prendera de manera decendente
    #se incrementa velocidad con potenciometro
    analog_value = poten.read()
    if analog_value is not None:
        delay = analog_value + 0.1
        board.digital[4].write(1)
        time.sleep(delay)
        board.digital[7].write(1)
        time.sleep(delay)
        board.digital[8].write(1)
        time.sleep(delay)
        board.digital[9].write(1)
        time.sleep(delay)
        board.digital[12].write(1)
        time.sleep(delay)
        board.digital[13].write(1)
        time.sleep(delay)
        board.digital[4].write(0)
        board.digital[7].write(0)
        board.digital[8].write(0)
        board.digital[9].write(0)
        board.digital[12].write(0)
        board.digital[13].write(0)
    else:
        time.sleep(0.1)

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

