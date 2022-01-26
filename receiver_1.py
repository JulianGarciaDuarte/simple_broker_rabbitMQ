from queue_rabbitMQ import Receiver
import sys, os

def main():
    host = 'localhost'
    cola = 'queue1'

    # PRIMER SUSCRIPTOR
    def callback_0(ch, method, properties, body):
         print('El receiver_1 recibió esto:{}'.format(body))
    receiver_1 = Receiver(host)
    receiver_1.set_callback(callback_0)
    receiver_1.suscribir_cola(cola) 
    receiver_1.listen()

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Ejecucion interrumpida por el usuario.')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)