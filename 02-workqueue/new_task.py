# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 22:16:40 2025

@author: Jose Antonio
"""

import sys

import pika

params_connection = pika.ConnectionParameters(
    host='localhost',
    port='5672'
    )
connection = pika.BlockingConnection(params_connection)  # Creamos una conexión
channel = connection.channel()  # Declaramos un canal

""" La operación de crear una cola es idempotente, si ya existe no pasa nada, solo habrá una. """
channel.queue_declare(queue='task_queue2', durable=True)  # Creamos una cola duradera (en caso de que el server caiga) en el canal

message = ' '.join(sys.argv[1:]) or "Hello World!"  # Podemos coger args al ejecutar
channel.basic_publish(exchange='',
                      routing_key='task_queue2',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=pika.DeliveryMode.Persistent  # Para que los mensajes sean duraderos si se cae el server
                          )
                      )

print(f" [x] Sent {message}")

connection.close()
