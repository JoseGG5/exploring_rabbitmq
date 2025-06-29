
### Pub/Sub

Hasta ahora, hemos hecho que cada mensaje se entregue únicamente a un worker, sin embargo, hay situaciones en las que nos interesaría entregar un mismo mensaje a varios workers. Este patrón es conocido como Pub(lish)/Sub(scribe).

### Exchanges

En el capítulo 01, cuando se definió la cola, se introdujo un exchange vacío. La idea central en un modelo de mensajería de RabbitMQ es que el producer nunca manda directamente mensajes a la cola, de hecho, la mayoría de veces ni siquiera sabe si un mensaje será mandado a alguna cola. El producer manda mensajes a un exchange.

Un exchange no es más que "algo" que se dedica a recibir mensajes de los producers y a enviarlos a colas basandose en las reglas definidas en el "exchange type". Estas reglas indican si por ejemplo el mensaje debe añadirse a una cola particular, o a muchas colas.

Hay 4 tipos de exchange type:

1. direct 
2. topic 
3. headers 
4. fanout

En este tutorial se usa el método `fanout`, el cual consiste en enviar todos los mensajes que se reciben a todas las colas que se conocen.

Notar que en el 01, el exchange vacío indicaba el exchange default, y esto significa que los mensajes so enrutan a la cola con el nombre especificado en `routing_key` directamente.

### Bindings

Una vez hemos creado un exchange, necesitamos asociarlo a una/varias colas para que sepa en que colas publicar. Esto se consigue con `channel.queue_bind`

