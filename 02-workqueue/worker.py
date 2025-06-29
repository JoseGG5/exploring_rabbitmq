# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 22:17:59 2025

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
    
    """ La operación de crear una cola es idempotente, si ya existe no pasa nada, solo habrá una. """
    channel.queue_declare(queue='task_queue2', durable=True)
    
    
    """ El receptor (consumer), debe registrar siempre una callback que es la función
        a la que se llamará una vez reciba algo a través de una cola dada."""
    
    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}")
        time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag = method.delivery_tag)
    
    
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(  # Describimos como debe consumir el consumer
        queue='task_queue2',  # Cola en la que consume
        auto_ack=False,
        on_message_callback=callback  # Por cada mensaje ejecuta la callback 
        )
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
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