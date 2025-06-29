# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 12:33:45 2025

@author: Jose Antonio
"""

import pika

params_connection = pika.ConnectionParameters(
    host='localhost',
    port='5672'
    )
connection = pika.BlockingConnection(params_connection)  # Creamos una conexión
channel = connection.channel()  # Declaramos un canal

""" La operación de crear una cola es idempotente, si ya existe no pasa nada, solo habrá una. """
channel.queue_declare(queue='hello')  # Creamos una cola en el canal

channel.basic_publish(exchange='',  # Los mensajes siempre pasan por un exchange antes, ver 03
                      routing_key='hello',  # Nombre de la cola
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()  # Importante asegurar que cerramos la cnx