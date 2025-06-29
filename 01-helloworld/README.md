La primera parte del tutorial comprende el ejemplo más sencillo.

Se asume que un servidor RabbitMQ está desplegado en localhost en el puerto por defecto.

Se crea un consumer en send.py y un producer en receive.py. Se ejecuta receive.py y se ejecuta varias veces send.py para observar como los mensajes son enviados a la cola y el consumer los recoge y los procesa con su callback.