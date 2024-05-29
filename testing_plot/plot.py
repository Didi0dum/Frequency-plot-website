from matplotlib import *
import matplotlib.pyplot as plt
import numpy as np
from gettext import npgettext
import struct
import serial
from serial.tools import list_ports
from matplotlib.animation import FuncAnimation 
from threading import Thread
from packet import *

'''Com ports
port = list(list_ports.comports())
for p in port:
    print(f'device: {p.device}')
    print(f'description: {p.description}')
    print(f'Serial: {p.serial_number}')
    print(f'Pid: {p.pid}') '''

#init of uart
uart_mcu = serial.Serial('/dev/cu.usbserial-A900D9PH', 115200, parity=serial.PARITY_NONE, \
   stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

print("Enter device's number: ")
num = int(input())

'''#test read of package
a = uart_mcu.read(280)
print(f'{a}')'''

#sizes of components
header_size = 16
tail_size = 8
N = 256 #number of bytes in the fft data, so fft is N/2
whole_packet = 280

#instance for packet
tmp = Packet(0, 0, 0, num)

fig = plt.figure(figsize=(12,6))
ax1 = plt.subplot(111)

#init ot x_axis 
x_axis_samples = []
for i in range(int(N/2)):
    x_axis_samples.append(i)

fft_values = np.zeros(int(N/2))
fmt = "%dH" % (N/2) #format for unpack function ([H - unsigned short - 2 bytes] * N/2)

def read_uart():
    global fft_values
    print("running thread")
    while True:
        tmp.header = uart_mcu.read(header_size)
        print(f'header: {tmp.header}')
        tmp.data = uart_mcu.read(N)
        #print(f'data: {data_uart}')
        tmp.tail = uart_mcu.read(tail_size)
        #print(f'tail: {tail}')
        
        if tmp.validate_packet():
            # convert the data to float
            print(tmp.data.__len__())
            if tmp.data.__len__() == N:
                fft_values = struct.unpack(fmt, tmp.data)
                print(f'values: {fft_values}')

# animation function to update the plot
def plot_animation(i):
    
    # clearing the figure
    ax1.clear()
    #ax1.set_rscale('symlog')
    
    #updating the figure
    ax1.set_ylabel("kill me")
    ax1.set_ylim(0, 4000)
    ax1.plot(x_axis_samples, fft_values, '.-')

ani = FuncAnimation(fig, plot_animation, frames= 100, interval = 10, blit=False)

if __name__ == "__main__":
    t1 = Thread(target=read_uart, daemon=True)
    t1.start()
    plt.show()