import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
from numpy import pi
from scipy.fftpack import fft, fftfreq, ifft 
# Documentacion:
# Transformada de fourier:
# https://docs.scipy.org/doc/scipy/reference/fftpack.html
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.read.html
# https://pybonacci.org/2012/09/29/transformada-de-fourier-discreta-en-python-con-scipy/
# Lectura, escritura y graficos:
# http://blog.espol.edu.ec/estg1003/audio-archivo-wav-en-python/
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.write.html
# http://blog.espol.edu.ec/estg1003/audio-archivo-wav-en-python/ 
# http://blog.espol.edu.ec/telg1001/audio-en-formato-wav/
# Espectograma:
# https://stackoverflow.com/questions/55312659/how-can-i-create-spectograms-from-wav-files-in-python-for-audio-classification

def lowpass(frecuenciaM, datos, corte):
	cantidad = np.shape(datos) # cantidad de datos en datos.
	muestras = cantidad[0]  # cantidad de datos del primer canal.

	# rango de observación en segundos
	inicia = 0.000 # inicio en 0
	termina = muestras/frecuenciaM # final en segundos del audio.

	wn = (2*corte)/frecuenciaM
	 
	b, a = signal.butter(8, wn, 'lowpass')   #Configuration filter 8 representa el orden del filtro
	filtedData = signal.filtfilt(b, a, datos)  #data es la señal a filtrar

	# tiempos en eje x
	dt = 1/frecuenciaM # periodo
	tab = np.arange(inicia,termina,dt)


	#plt.plot(tab,filtedData)
	#plt.show()

	return filtedData


def highpass(frecuenciaM, datos, corte):
	cantidad = np.shape(datos) # cantidad de datos en datos.
	muestras = cantidad[0]  # cantidad de datos del primer canal.

	# rango de observación en segundos
	inicia = 0.000 # inicio en 0
	termina = muestras/frecuenciaM # final en segundos del audio.

	wn = (2*corte)/frecuenciaM
	 
	b, a = signal.butter(8, wn, 'highpass')   #Configuration filter 8 representa el orden del filtro

	filtedData = signal.filtfilt(b, a, data)  #data es la señal a filtrar

	# tiempos en eje x
	dt = 1/frecuenciaM # periodo
	tab = np.arange(inicia,termina,dt)


	#plt.plot(tab,filtedData)
	#plt.show()

	return filtedData

def bandpass(frecuenciaM, datos, intervaloApertura, intervaloCorte):
	cantidad = np.shape(datos) # cantidad de datos en datos.
	muestras = cantidad[0]  # cantidad de datos del primer canal.

	# rango de observación en segundos
	inicia = 0.000 # inicio en 0
	termina = muestras/frecuenciaM # final en segundos del audio.

	wn1 = (2*intervaloApertura)/frecuenciaM
	wn2 = (2*intervaloCorte)/frecuenciaM
	 

	b, a = signal.butter(8, [wn1,wn2], 'bandpass')   #Configuration filter 8 representa el orden del filtro
	filtedData = signal.filtfilt(b, a, data)  #data es la señal a filtrar
	
	# tiempos en eje x
	dt = 1/frecuenciaM # periodo
	tab = np.arange(inicia,termina,dt)


	#plt.plot(tab,filtedData)
	#plt.show()

	return filtedData




archivo = input('Ingrese archivo de sonido:' )
frecuenciaM, datos = waves.read(archivo) # frecuencia del muestreo y los datos.


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
FFT = fft(datos) / muestras # transformada de fourier normalizada 
FFTfrq = fftfreq(muestras, p) # Recuperamos las frecuencias
plt.vlines(FFTfrq, 0, abs(FFT)) # Espectro de amplitud
plt.title('FFT, audio sobre la frecuencia') 
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud FFT (db)')
plt.savefig('fig2_audio_f.png')
plt.show()



antiFFT=ifft(FFT) # Se calcula la anti transformada de fourier
plt.plot(np.real(antiFFT))
plt.title('Antitransformada de fourier')    
plt.savefig('fig3_antitransformada.png')
plt.show()



# Espectograma.
plt.title('Espectograma')    
Pxx, freqs, bins, im = plt.specgram(datos,Fs=frecuenciaM,NFFT=256)
plt.xlabel('Tiempo (s)')
plt.ylabel('Frecuencia (Hz)')
plt.xlim(left=0,right=5)
plt.savefig('fig4_espectograma.png')
plt.show()