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

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
message = ' '.join(sys.argv[1:]) or "info: Hello World!"

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'

channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message)  # En este caso publicamos al exchange 
print(f" [x] Sent {severity}:{message}")
connection.close()