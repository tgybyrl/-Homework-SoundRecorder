import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100
recording_seconds = 6

myRecording = sd.rec(int(recording_seconds * fs),samplerate=fs,channels=2)
sd.wait()
write("SoundRecordEx.wav",fs, myRecording)