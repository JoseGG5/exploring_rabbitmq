
### Routing

En este capítulo vamos a mejorar nuestro sistema de logs para hacer que solo los logs "críticos" lleguen a un worker que 
guardará el log en disco y los demás no. Esto se consigue ajustando el tipo de exchange y aplicando "routing keys" (claves de enrutamiento)
para que el exchange sepa a que cola mandar cada log.

Para esto usaremos un exchange `direct`. El algoritmo de enrutamiento de este exchange es sencillo, se mira el routing key del mensaje
y se manda a las colas cuyo binding key coincide con este.

Si por ejemplo tuviesemos múltiples colas todas con la misma binding key el comportamiento sería equivalente al del exchange `fanout`.