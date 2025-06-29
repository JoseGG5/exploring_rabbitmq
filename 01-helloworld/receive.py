# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 12:38:20 2025

@author: Jose Antonio
"""

import os
import sys

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
    channel.queue_declare(queue='hello')  # Creamos una cola en el canal
    
    
    """ El receptor (consumer), debe registrar siempre una callback que es la función
        a la que se llamará una vez reciba algo a través de una cola dada."""
    
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
        
    channel.basic_consume(  # Describimos como debe consumir el consumer
        queue='hello',  # Cola en la que consume
        auto_ack=True,  # Auto confirma que lo ha recibido
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