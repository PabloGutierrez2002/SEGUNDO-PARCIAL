import pyfirmata
import time
board = pyfirmata.Arduino('COM3')

while True:
    #La primera mitad durante 1 segundo
    board.digital[13].write(1)
    board.digital[12].write(1)
    board.digital[9].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    board.digital[12].write(0)
    board.digital[9].write(0)

    board.digital[8].write(1)
    board.digital[7].write(1)
    board.digital[4].write(1)
    time.sleep(2)
    board.digital[8].write(0)
    board.digital[7].write(0)
    board.digital[4].write(0)