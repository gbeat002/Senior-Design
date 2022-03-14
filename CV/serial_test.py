import time
import serial
from six_chars import six_chars

serial_port = serial.Serial(
    port="/dev/ttyACM0",
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    )



def serial_test(centroid):

    centroid_word=six_chars(centroid)

    print("sending")

    
    serial_port.write(bytes(centroid_word[0],'utf-8'))
    serial_port.write(bytes(centroid_word[1],'utf-8'))
    serial_port.write(bytes(centroid_word[2],'utf-8'))
    serial_port.write(bytes(centroid_word[3],'utf-8'))
    serial_port.write(bytes(centroid_word[4],'utf-8'))
    serial_port.write(bytes(centroid_word[5],'utf-8'))
    serial_port.write(bytes(centroid_word[6],'utf-8'))
    serial_port.write(bytes(centroid_word[7],'utf-8'))

