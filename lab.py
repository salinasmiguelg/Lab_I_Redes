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


# rango de observación en segundos, se truncan los datos en un tiempo
inicia = 0.000
termina = 4.002
# observación en número de muestra
a = int(inicia*frecuenciaM)
b = int(termina*frecuenciaM)
parte = uncanal[a:b]



# Salida # Archivo de audio.wav
print('archivo de parte[] grabado...')
waves.write('parte01.wav', frecuenciaM, datos)




# Gráfica
plt.plot(parte)
plt.show()


# tiempos en eje x
dt = 1/frecuenciaM # periodo
ta = a*dt
tb = (b)*dt
tab = np.arange(ta,tb,dt)

plt.plot(tab,parte)
plt.xlabel('tiempo (s)')
plt.ylabel('Amplitud')
plt.show()




#n=2**15
# frecuencia en eje x
n=32016
y=parte
Y = fft(y) / n # Normalizada  TRans de f
frq = fftfreq(n, dt) # Recuperamos las frecuencias
plt.vlines(frq, 0, abs(Y)) # Espectro de amplitud
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Abs($Y$)')
plt.show()

