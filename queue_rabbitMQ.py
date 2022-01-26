import pika

class Actor:
    def __init__(self, host:str):
        # Se inicia la conexion
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=host)
        )
        # Se crea el canal
        self.channel=self.connection.channel()
    
    def check_queue(self, name):
        # Verifica si la cola existe, de no hacerlo crea una nueva
        self.channel.queue_declare(queue=name)

    def end_connection(self):
        self.connection.close()
    
class Sender (Actor):
    def __init__(self, host):
        super().__init__(host)
    
    def send_message(self, exchange, queue_name, body):
        # Verifica que la cola existe, si no existe crea una
        self.check_queue(queue_name)
        # Envia el mensaje a la cola
        self.channel.basic_publish(
            exchange=exchange,
            routing_key=queue_name,
            body=body
        )
        print('Mensaje enviado! {}'.format(body))

    def callback(self, ch, method, properties, body):
        print(" [x] Received {}".format(body))

class Receiver(Actor):
    def __init__(self, host):
        super().__init__(host)

    def callback(self, ch, method, properties, body):
        print("Mensaje recibido: {}".format(body))

    def suscribir_cola(self, queue_name):
        # Se asegura que la cola exista
        self.check_queue(queue_name)
        # Suscribe el receptor a la cola especificada
        self.channel.basic_consume(
            queue=queue_name,
            auto_ack=True,
            on_message_callback=self.callback
        )
        print("Suscrito a {}!".format(queue_name))
    
    def listen(self):
        # Ciclo infinito, deja el Receiver esperando por mensajes
        self.channel.start_consuming()
