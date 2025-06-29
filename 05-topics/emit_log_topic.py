# -*- coding: utf-8 -*-
"""
Created on Sun Jun 29 19:01:41 2025

@author: Jose Antonio
"""

import pika
import sys

params_connection = pika.ConnectionParameters(
    host='localhost',
    port='5672'
    )
connection = pika.BlockingConnection(params_connection)  # Creamos una conexión
channel = connection.channel()  # Declaramos un canal

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
message = ' '.join(sys.argv[2:]) or "Hello World!"

routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'

channel.basic_publish(exchange='topic_logs', routing_key=routing_key, body=message)  # En este caso publicamos al exchange 
print(f" [x] Sent {routing_key}:{message}")
connection.close()