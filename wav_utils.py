import struct
import wave
import numpy as np

def load_wave(file_path='test.wav', num_frames=None, sampling_rate=48000, time=None):
  with wave.open(file_path) as wave_file:
    if time is not None:
      num_frames = sampling_rate * time
    elif num_frames is None:
      num_frames = wave_file.getnframes()

    data = wave_file.readframes(num_frames)
    data = struct.unpack(f'{num_frames}h', data)
    return np.array(data)
