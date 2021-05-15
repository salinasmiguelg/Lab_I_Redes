import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
from numpy import pi
from scipy.fftpack import fft, fftfreq, ifft 
from scipy import signal

# Maximiliano Araya 20.467.583-K 
# Miguel Salinas 20.215.515-4
# Laboratorio I
# Redes de Computadores
# 14-05-2021


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
# Filtros:
# https://programmerclick.com/article/11751456084/

# DESCRIPCIÓN DEL PROGRAMA: El siguiente programa lee un archivo de extensión ".wav" para así obtener su frecuencia de muestreo junto con los datos
# para posteriormente procesar estos datos a través de la herramiente de "Transformada de Fourier" y a su vez aplicando dicha herramienta a filtro FIR diseñado.




# BLOQUE DE FUNCIONES:


# ENTRADA: frecuenciaM es un valor entero respectivo a la frencuencia de muestreo de los datos, datos una lista que contiene los datos 
# y corte un valor float correspondiente al corte para el filtro
# SALIDA: Una lista con los datos filtrados.
# OBJETIVO: Aplicar un filtro de pasa bajos a unos datos dados.
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
	return filtedData


# ENTRADA: frecuenciaM es un valor entero respectivo a la frencuencia de muestreo de los datos, datos una lista que contiene los datos 
# y corte un valor float correspondiente al corte para el filtro
# SALIDA: Una lista con los datos filtrados.
# OBJETIVO: Aplicar un filtro de pasa altos a unos datos dados.
def highpass(frecuenciaM, datos, corte):
	cantidad = np.shape(datos) # cantidad de datos en datos.
	muestras = cantidad[0]  # cantidad de datos del primer canal.

	# rango de observación en segundos
	inicia = 0.000 # inicio en 0
	termina = muestras/frecuenciaM # final en segundos del audio.

	wn = (2*corte)/frecuenciaM
	 
	b, a = signal.butter(8, wn, 'highpass')   #Configuration filter 8 representa el orden del filtro

	filtedData = signal.filtfilt(b, a, datos)  #data es la señal a filtrar

	# tiempos en eje x
	dt = 1/frecuenciaM # periodo
	tab = np.arange(inicia,termina,dt)
	return filtedData


# ENTRADA: frecuenciaM es un valor entero respectivo a la frencuencia de muestreo de los datos, datos una lista que contiene los datos,
# intervaloApertura un valor float correspondiente a la aporterura el intervalo de corte para el filtro 
# y intervaloCorte un valor float correspondiente a la cierre el intervalo de corte para el filtro
# SALIDA: Una lista con los datos filtrados.
# OBJETIVO: Aplicar un filtro de pasa banda a unos datos dados.
def bandpass(frecuenciaM, datos, intervaloApertura, intervaloCorte):
	cantidad = np.shape(datos) # cantidad de datos en datos.
	muestras = cantidad[0]  # cantidad de datos del primer canal.

	# rango de observación en segundos
	inicia = 0.000 # inicio en 0
	termina = muestras/frecuenciaM # final en segundos del audio.

	wn1 = (2*intervaloApertura)/frecuenciaM
	wn2 = (2*intervaloCorte)/frecuenciaM
	 

	b, a = signal.butter(8, [wn1,wn2], 'bandpass')   #Configuration filter 8 representa el orden del filtro
	filtedData = signal.filtfilt(b, a, datos)  #data es la señal a filtrar
	
	# tiempos en eje x
	dt = 1/frecuenciaM # periodo
	tab = np.arange(inicia,termina,dt)
	return filtedData





# BLOQUE PRINCIPAL:

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



# audio con tiempos en eje x
p = 1/frecuenciaM # periodo
timeA = np.arange(inicia,termina,p) # arreglo para representar el tiempo.
plt.plot(timeA,datos)
plt.title('Audio sobre el tiempo')    
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (db)')
plt.savefig('fig1_audio_tiempo.png')
plt.show()





# audio con frecuencia en eje x
FFT = fft(datos) / muestras # transformada de fourier normalizada 
FFTfrq = fftfreq(muestras, p) # Recuperamos las frecuencias
plt.vlines(FFTfrq, 0, abs(FFT)) # Espectro de amplitud
plt.title('FFT, audio sobre la frecuencia') 
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud FFT (db)')
plt.savefig('fig2_audio_frecuencia.png')
plt.show()



# antitransformada de la transformada del audio.
antiFFT=ifft(FFT) # Se calcula la anti transformada de fourier
plt.plot(np.real(antiFFT))
plt.title('Antitransformada de fourier')    
plt.savefig('fig3_antitransformada.png')
plt.show()



# Espectograma del audio.
plt.title('Espectograma')    
Pxx, freqs, bins, im = plt.specgram(datos,Fs=frecuenciaM,NFFT=256)
plt.xlabel('Tiempo (s)')
plt.ylabel('Frecuencia (Hz)')
plt.xlim(left=0,right=5)
plt.savefig('fig4_espectograma.png')
plt.show()





#
# Filtros
#

datosF=lowpass(frecuenciaM,datos, 2500)
muestras=np.shape(datosF)[0]
waves.write('Filtro lowpass.wav', frecuenciaM, datosF)

# audio filtrado con frecuencia en eje x.
FFT = fft(datosF) / muestras # transformada de fourier normalizada 
FFTfrq = fftfreq(muestras, p) # Recuperamos las frecuencias
plt.vlines(FFTfrq, 0, abs(FFT)) # Espectro de amplitud
plt.title('FFT, audio filtrado lowpass sobre la frecuencia') 
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud FFT (db)')
plt.savefig('fig5_audio_filtrado_lowpass_frecuencia.png')
plt.show()



# Espectograma del audio filtrado.
plt.title('Espectograma audio filtrado lowpass')    
Pxx, freqs, bins, im = plt.specgram(datosF,Fs=frecuenciaM,NFFT=256)
plt.xlabel('Tiempo (s)')
plt.ylabel('Frecuencia (Hz)')
plt.xlim(left=0,right=5)
plt.savefig('fig6_espectograma audio filtrado lowpass.png')
plt.show()






