import os
import sys
import time

import pika

""" El consumer debe conectarse al mismo server de RabbitMQ"""

def main():
    
    params_connection = pika.ConnectionParameters(
        host='localhost',
        port='5672'
        )
    connection = pika.BlockingConnection(params_connection)  # Creamos una conexión
    channel = connection.channel()  # Declaramos un canal
    
    channel.exchange_declare(
        exchange='logs',
        exchange_type='fanout'  # Manda todos los mensajes que recibe a todas las colas que conoce
    )

    """ Como cada vez que nos conectemos queremos ver los nuevos mensaje solo,
    hacemos que la cola no sea duradera y además le damos de nombre un empty string.
    Esto lo que hace es que cada vez que nos conectamos, el servidor RabbitMQ crea una cola
    con un nombre random.
    
    También queremos que cada vez que el consumer se desconecte la cola se borre. El flag
    exclusive = True hace esto.
    """
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue
    
    """ Ahora necesitamos hacer un binding entre las colas y el exchange, para que este
    sepa a que colas mandar los logs."""

    channel.queue_bind(exchange='logs',
                   queue=queue_name)

    """ El receptor (consumer), debe registrar siempre una callback que es la función
        a la que se llamará una vez reciba algo a través de una cola dada."""

    print(' [*] Waiting for logs. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(f" [x] {body}")
        
    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True
    )

    channel.start_consuming()  # Loop infinito que espera a recibir mensajes


if __name__ == "__main__":
    
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)