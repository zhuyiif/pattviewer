import numpy as np
import pylab as pl

channel1,channel2 = np.loadtxt('3mins-tonetest-april-26.txt', skiprows=0, unpack=True)


sampling_rate = 125
fft_size = 1250
t = np.arange(0, 100.0, 1.0/sampling_rate)
print(t.size)
x = channel1
xs = x[:fft_size]
xf = np.fft.rfft(xs)/fft_size
freqs = np.linspace(0, sampling_rate/2, fft_size/2+1)
xfp = 20*np.log10(np.clip(np.abs(xf), 1e-20, 1e100))
pl.figure(figsize=(8,4))
pl.subplot(211)
pl.plot(t[:fft_size], xs)
pl.xlabel(u"时间(秒)")
pl.title(u"波形和频谱")
pl.subplot(212)
pl.plot(freqs, xfp)
pl.xlabel(u"频率(Hz)")
pl.subplots_adjust(hspace=0.4)
pl.show()