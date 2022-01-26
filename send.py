import pika
from queue_rabbitMQ import Sender

host = 'localhost'
queue = 'queue1'

# PRIMER PUBLICADOR
sender_0 = Sender(host) # Se inicia la conexion
sender_0.send_message('', queue, 'Enhorabuena un mensaje!') # Se envia el mensaje
sender_0.end_connection() # Se cierra la conexion (necesario por algo de buffers de red y no se que)

# SEGUNDO PUBLICADOR
sender_1 = Sender(host) # Se inicia la conexion
sender_1.send_message('', queue, 'Aca el segundo publicador!') # Se envia el mensaje
sender_1.end_connection() 

# TERCER PUBLICADOR
sender_2 = Sender(host) # Se inicia la conexion
sender_2.send_message('', queue, 'Este mensaje es el tercero, del tercer publicador') # Se envia el mensaje
sender_2.end_connection() 