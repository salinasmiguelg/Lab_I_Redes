import matplotlib.pyplot as plt
from scipy.io import wavfile

samplingFrequency, signalData = wavfile.read('G13.wav')


plt.title('Spectrogram')    
Pxx, freqs, bins, im = plt.specgram(signalData,Fs=samplingFrequency,NFFT=512)
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.xlim(left=0,right=5)

plt.savefig('fig11.png')