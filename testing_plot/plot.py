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

uart_mcu = serial.Serial('/dev/cu.usbserial-A900D9PH', 115200, parity=serial.PARITY_NONE, \
   stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

'''#test read of package
a = uart_mcu.read(272)
print(f'{a}') 
'''

N = 272

fig = plt.figure(figsize=(12,6))
ax1 = plt.subplot(111)
theta = np.linspace(0, 2*np.pi, N)
fft_values = np.zeros(N)
fmt = "%df"% (N) #format for unpack function (64f)


'''def read_uart():
    global fft_values
    print("running thread")
    # reference string (">>>>") to indicate the end of the data packet
    while True:
        data_uart = uart_mcu.read(N)
        # convert the data to float
        if data_uart.__len__() == N * 4 + 4:
            fft_values = struct.unpack(fmt, np.flip(data_uart[0:(N * 4)])) '''

#plt.show()


'''Fs = 2000  # sampling freq
tstep = 1/Fs
f0 = 100
N = int(10 * Fs / f0)

t = np.linspace(0, (N -1)*tstep, N)
fstep = Fs/N
f = np.linspace(0, (N - 1)*fstep, N)

y = 1 * np.sin(2 * np.pi * f0 * t)

X = np.fft.fft(y)
X_mag = np.abs(X) / N

f_plot = f[0:int(N/2+1)]
x_mag_plot = 2 * X_mag[0:int(N/2+1)]
x_mag_plot[0] = x_mag_plot[0] / 2


fig, ax2 = plt.subplots(nrows=1, ncols=1)
#ax1.plot(t, y, '.-')
ax2.plot(f_plot, x_mag_plot, '.-')
plt.show()
t = np.linspace(0, (N -1)*tstep, N)
fstep = Fs/N
f = np.linspace(0, (N - 1)*fstep, N)

y = 1 * np.sin(2 * np.pi * f0 * t)

X = np.fft.fft(y)
X_mag = np.abs(X) / N

f_plot = f[0:int(N/2+1)]
x_mag_plot = 2 * X_mag[0:int(N/2+1)]
x_mag_plot[0] = x_mag_plot[0] / 2


#fig, [ax1, ax2] = plt.subplots(nrows=2, ncols=1)
#ax1.plot(t, y, '.-')
ax2.plot(f_plot, x_mag_plot, '.-')
plt.show()'''

