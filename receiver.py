from queue_rabbitMQ import Receiver
import sys, os

def main():
    host = 'localhost'
    cola = 'queue1'

    # PRIMER SUSCRIPTOR
    receiver_0 = Receiver(host)
    receiver_0.suscribir_cola(cola) 
    receiver_0.listen()

    # SEGUNDO SUSCRIPTOR
    receiver_1 = Receiver(host)
    receiver_1.suscribir_cola(cola) 
    receiver_1.listen()

    # TERCER SUSCRIPTOR
    receiver_2 = Receiver(host)
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


