from matplotlib import *
import matplotlib.pyplot as plt
import numpy as np
from gettext import npgettext
import struct
import serial
from serial.tools import list_ports
from matplotlib.animation import FuncAnimation 
from threading import Thread

'''port = list(list_ports.comports())
for p in port:
    print(f'device: {p.device}')
    print(f'description: {p.description}')
    print(f'Serial: {p.serial_number}')
    print(f'Pid: {p.pid}') '''

#init of uart
uart_mcu = serial.Serial('/dev/cu.usbserial-A900D9PH', 115200, parity=serial.PARITY_NONE, \
   stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

'''#test read of package
a = uart_mcu.read(280)
print(f'{a}')'''


header_size = 16
tail_size = 8
N = 256
whole_packet = 280

fig = plt.figure(figsize=(12,6))
ax1 = plt.subplot(111)

#init ot x_axis 
x_axis_samples = []
for i in range(128):
    x_axis_samples.append(i)

fft_values = np.zeros(128)
fmt = "%dH" % (N/2) #format for unpack function (64b of uart fft info in this case)


def read_uart():
    global fft_values
    global header
    global tail
    print("running thread")
    while True:
        '''data_uart = uart_mcu.read(whole_packet)
        print(f'{data_uart}')
        split = [data_uart[i] for i in range (0, len(data_uart))]
        header = [split[i] for i in range (0, header_size)]
        fft_values = [split[i] for i in range (16, N)]
        tail = [split[i] for i in range (272, tail_size)]
        header = bytes(header)
        fft_values = bytes(fft_values)
        tail = bytes(tail)
        print(f'header: {header}')
        print(f'values: {fft_values}')
        print(f'tail: {tail}')'''
        header = uart_mcu.read(header_size)
        #print(f'header: {header}')
        data_uart = uart_mcu.read(N)
        #print(f'data: {data_uart}')
        tail = uart_mcu.read(tail_size)
        #print(f'tail: {tail}')
        # convert the data to float
        print(data_uart.__len__())
        if data_uart.__len__() == N:
            fft_values = struct.unpack(fmt, data_uart)
            print(f'values: {fft_values}')

# animation function to update the plot
def plot_animation(i):
    global fft_values
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