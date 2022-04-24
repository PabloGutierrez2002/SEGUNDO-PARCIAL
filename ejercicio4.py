import pyfirmata
import time

board = pyfirmata.Arduino('COM3')
it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin('a:0:i')

while True:
    analog_value = analog_input.read()

    if analog_value == 1:
            board.digital[4].write(1)
            board.digital[7].write(1)
            board.digital[8].write(1)
            board.digital[9].write(1)
            board.digital[12].write(1)
            board.digital[13].write(1)
            print("LEDS ENCENDIDOS")

    elif analog_value == 0.0049:
            board.digital[4].write(0)
            board.digital[7].write(0)
            board.digital[8].write(0)
            board.digital[9].write(0)
            board.digital[12].write(0)
            board.digital[13].write(0)
            print("lEDS APAGADOS")

