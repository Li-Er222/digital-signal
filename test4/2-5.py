from thinkdsp import decorate
from thinkdsp import TriangleSignal
import matplotlib.pyplot as plt

def filter_spectrum(spectrum):
    spectrum.hs[1:] /= spectrum.fs[1:]
    spectrum.hs[0] = 0

wave = TriangleSignal(freq=440).make_wave(duration=0.5)

spectrum = wave.make_spectrum()
spectrum.plot(high=10000, color='r')
filter_spectrum(spectrum)
spectrum.scale(440)
spectrum.plot(high=10000)
decorate(xlabel='Frequency (Hz)')

filtered = spectrum.make_wave()
filtered.play("2-5.wav")
plt.show()