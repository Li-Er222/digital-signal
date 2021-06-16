from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
from thinkdsp import decorate
import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import SquareSignal
from thinkdsp import TriangleSignal

class SawtoothSignal(Sinusoid):
    
    def evaluate(self, ts):
        cycles = self.freq * ts + self.offset / np.pi / 2
        frac, _ = np.modf(cycles)
        ys = normalize(unbias(frac), self.amp)
        return ys

sawtooth = SawtoothSignal().make_wave(duration=0.5, framerate=40000)
sawtooth.make_audio()
plt.subplot(321)
sawtooth.plot()
sawtooth.play("2-2.wav")
plt.subplot(322)
sawtooth.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')
plt.subplot(323)
sawtooth.make_spectrum().plot(color='gray')
square = SquareSignal(amp=0.5).make_wave(duration=0.5, framerate=40000)
plt.subplot(324)
square.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')
plt.subplot(325)
sawtooth.make_spectrum().plot(color='gray')
triangle = TriangleSignal(amp=0.79).make_wave(duration=0.5, framerate=40000)
plt.subplot(326)
triangle.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')

plt.show()

