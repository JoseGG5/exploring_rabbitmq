# -*- coding: utf-8 -*-
"""
Created on Sun Jun 29 19:01:51 2025

@author: Jose Antonio
"""

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
        exchange='direct_logs',
        exchange_type='direct'  # Manda todos los mensajes que recibe a todas las colas que conoce
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
    
    """ Este script se ejecuta enviando varias severities por linea de comandos, cada vez que
    lo ejecutamos creamos una cola que tiene n binding keys siendo n el número de severidades
    que pasamos por línea de comandos. Si ejecutamos el script dos veces, una con parámetros info y warning
    y otra con error, tendremos dos colas, una enlazada con las claves info y warning y otra a la que llegaran
    los mensajes de error"""    
    
    severities = sys.argv[1:]
    if not severities:
        sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
        sys.exit(1)
    
    for severity in severities:
        print(f"Binding {queue_name} to exchange with key {severity}")
        channel.queue_bind(
            exchange='direct_logs',
            queue=queue_name,
            routing_key=severity  # La binding key
            )

    print(' [*] Waiting for logs. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(f" [x] {method.routing_key}:{body}")
        
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