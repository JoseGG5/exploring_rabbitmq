import pika
import sys

params_connection = pika.ConnectionParameters(
    host='localhost',
    port='5672'
    )
connection = pika.BlockingConnection(params_connection)  # Creamos una conexión
channel = connection.channel()  # Declaramos un canal

channel.exchange_declare(exchange='logs', exchange_type='fanout')
message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)  # En este caso publicamos al exchange 
print(f" [x] Sent {message}")
connection.close()