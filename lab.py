import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
from numpy import pi
from scipy.fftpack import fft, fftfreq


archivo = input('Ingrese archivo de sonido:' )
frecuenciaM, datos = waves.read(archivo) # frecuencia del muestreo y los datos.




# canales: monofónico o estéreo
cantidad = np.shape(datos) # cantidad de datos en datos.
muestras = cantidad[0]  # cantidad de datos del primer canal.
m = len(cantidad) # si el largo es 2 entonces existen 2 canales
canales = 1  #asumimos que es monofónico 
if (m>1):  # estéreo
	canales = cantidad[1]

# experimento con un canal
if (canales>1):
    canal = 0
    uncanal = datos[:,canal] 
else:
    uncanal = datos # se crea una copia de los datos


# rango de observación en segundos
inicia = 0.000 # inicio en 0
termina = muestras/frecuenciaM # final en segundos del audio.



# Salida # Archivo de audio.wav
print('archivo de parte[] grabado...')
waves.write('parte01.wav', frecuenciaM, datos)




# Gráfica
plt.plot(datos)
plt.show()


# tiempos en eje x
dt = 1/frecuenciaM # periodo
tab = np.arange(inicia,termina,dt)

plt.plot(tab,datos)
plt.xlabel('tiempo (s)')
plt.ylabel('Amplitud')
plt.show()




#n=2**15
# frecuencia en eje x
n=38912
y=datos
Y = fft(y) / n # Normalizada  TRans de f
frq = fftfreq(n, dt) # Recuperamos las frecuencias
plt.vlines(frq, 0, abs(Y)) # Espectro de amplitud
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Abs($Y$)')
plt.show()

