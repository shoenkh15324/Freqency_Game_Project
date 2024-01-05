# -*- coding: utf-8 -*-
import pyaudio

p = pyaudio.PyAudio()

# Print information about available audio devices
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(f"Index {i}: {info['name']}, {info['maxInputChannels']} input channels")

p.terminate()
