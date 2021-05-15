from scipy import signal
import scipy.io.wavfile as waves
import matplotlib.pyplot as plt
import numpy as np

archivo = input('Ingrese archivo de sonido:' )
frecuenciaM, datos = waves.read(archivo) # frecuencia del muestreo y los datos.


cantidad = np.shape(datos) # cantidad de datos en datos.
muestras = cantidad[0]  # cantidad de datos del primer canal.

# rango de observación en segundos
inicia = 0.000 # inicio en 0
termina = muestras/frecuenciaM # final en segundos del audio.



corte = 400

wn = (2*corte)/frecuenciaM
 
b, a = signal.butter(8, wn, 'lowpass')   #Configuration filter 8 representa el orden del filtro
filtedData = signal.filtfilt(b, a, datos)  #data es la señal a filtrar

# tiempos en eje x
dt = 1/frecuenciaM # periodo
tab = np.arange(inicia,termina,dt)


plt.plot(tab,filtedData)
plt.show()
