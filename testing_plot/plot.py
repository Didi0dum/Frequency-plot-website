from matplotlib import *
import matplotlib.pyplot as plt
import numpy as np

# Test time signal

Fs = 2000  # sampling freq
tstep = 1/Fs
f0 = 100
N = int(10 * Fs / f0)
from matplotlib import *
import matplotlib.pyplot as plt
import numpy as np

# Test time signal

Fs = 2000  # sampling freq
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


fig, [ax1, ax2] = plt.subplots(nrows=2, ncols=1)
ax1.plot(t, y, '.-')
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


fig, [ax1, ax2] = plt.subplots(nrows=2, ncols=1)
ax1.plot(t, y, '.-')
ax2.plot(f_plot, x_mag_plot, '.-')
plt.show()