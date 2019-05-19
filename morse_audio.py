import struct
import wave
import numpy as np
from wav_utils import load_wave

import matplotlib
import matplotlib.pyplot as plt

def morse2audio(morse, file_path, sampling_rate=48000, num_samples_percode=12000, frequency=440, amplitude=16000):
  num_samples = int(sampling_rate * len(morse) * 1/4)
  morse_array = np.array(list(morse)).astype(np.int)
  sine_mask = morse_array.repeat(num_samples_percode)
  sine_wave = [np.sin(2 * np.pi * frequency * t / sampling_rate) for t in range(num_samples)]
  morse_wave = [sine_wave[i] if sine_mask[i] == 1 else 0 for i in range(len(sine_wave))]
  
  nchannels = 1
  sampwidth = 2
  nframes = num_samples
  comptype = 'NONE'
  compname = 'not compressed'
  with wave.open(file_path, 'wb') as wave_file:
    wave_file.setparams(
      (nchannels, sampwidth, sampling_rate, nframes, comptype, compname)
    )
    for s in morse_wave:
      wave_file.writeframes(struct.pack('h', int(s * amplitude)))

def audio2morse(file_path, sampling_rate=48000, num_samples_percode=12000):
  wave = load_wave(file_path)
  middle_of_sample = int(num_samples_percode/2)
  morse = ''
  for i in range(middle_of_sample, len(wave), num_samples_percode):
    sample = max(wave[range(i-10,i+10)], key=abs)
    if sample == 0:
      morse += '0'
    else:
      morse += '1'
  return morse

