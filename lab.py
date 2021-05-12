import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
from numpy import pi
from scipy.fftpack import fft, fftfreq


#archivo = input('Ingrese archivo de sonido:' )
frecuenciaM, datos = waves.read('G13.wav') # frecuencia del muestreo y los datos.




# canales: monofónico o estéreo
cantidad = np.shape(datos) # cantidad de datos en datos.
muestras = cantidad[0]  # cantidad de datos del primer canal.
m = len(cantidad) # si el largo es 2 entonces existen 2 canales
#asumimos que es monofónico 
if m==2:
	print("El audio debe ser monofónico, un solo canal.")
	exit()


# rango de observación en segundos
inicia = 0.000 # inicio en 0
termina = muestras/frecuenciaM # final en segundos del audio.



# tiempos en eje x
p = 1/frecuenciaM # periodo
timeA = np.arange(inicia,termina,p) # arreglo para representar el tiempo.
plt.plot(timeA,datos)
plt.title('Audio sobre el tiempo')    
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (db)')
plt.savefig('fig1_audio_tiempo.png')
plt.show()





# frecuencia en eje x
n=muestras
FFT = fft(datos) / muestras # Normalizada  TRans de f
FFTfrq = fftfreq(muestras, p) # Recuperamos las frecuencias
plt.vlines(FFTfrq, 0, abs(FFT)) # Espectro de amplitud
plt.title('FFT, audio sobre la frecuencia') 
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud FFT (db)')
plt.savefig('fig2_audio_f.png')
plt.show()


# Espectograma.
plt.title('Espectograma')    
Pxx, freqs, bins, im = plt.specgram(datos,Fs=frecuenciaM,NFFT=152)
plt.xlabel('Tiempo (s)')
plt.ylabel('Frecuencia (Hz)')
plt.xlim(left=0,right=5)
plt.savefig('fig3_espectograma.png')
plt.show()