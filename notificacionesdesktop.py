# Crearemos notificaciones de escritorio en nuestra laptop
# Importamos las librerías de plyer y time
from plyer import notification
import time

# Creamos un loop
while (True): 
    # dentro de la función notification.notify(title,message,timeout,etc.)
    notification.notify(
        title = "Recordatorio", # Escribimos el titulo de la notificación
        message = "Es momento de tomar un break, ¡bien hecho!", # escribimos el mensaje
        timeout = 10, # El tiempo que durará la notificación
    )
    # Cada 1 hora estará apareciendo la notificación, utilizamos el time sleep para lograr eso. 
    time.sleep(60*60) 










