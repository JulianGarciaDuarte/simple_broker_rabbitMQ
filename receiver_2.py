from queue_rabbitMQ import Receiver
import sys, os

def main():
    host = 'localhost'
    cola = 'queue1'

    # PRIMER SUSCRIPTOR
    def callback_0(ch, method, properties, body):
         print('El receiver_2 recibió esto:{}'.format(body))
    receiver_2 = Receiver(host)
    receiver_2.set_callback(callback_0)
    receiver_2.suscribir_cola(cola) 
    receiver_2.listen()

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Ejecucion interrumpida por el usuario.')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)