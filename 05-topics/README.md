
### Topics

En este capítulo se habla acerca de los topics y como hacer enrutamientos de una manera que nos da una mayor flexibilidad. El exchange direct 
mejora nuestro log pero tiene todavía deficiencias, como por ejemplo, no poder hacer enrutamientos en base a varios criterios (varias claves).

Para mejorar esto podemos definir un exchange de tipo `topic`. La routing key de los mensajes que lleguen al exchange será
una lista de palabras delimitadas por puntos. Estas palabras generalmente describen features conectadas al mensaje.

La binding key de las colas debe tener la misma forma, solo que en esta podemos usar los términos `*` y `#` para dar flexibilidad
a la hora de hacer matches. `*` puede ser sustituido por exactamente una palabra y `#` por cero o más.

Si por ejemplo enviamos a un exchange un mensaje con una routing key `brown.fox` y tenemos una cola con un binding key `*.fox` el mensaje será
enviado a esta. Si otro mensaje es `lazy.#` y enviamos el mensaje `lazy.girl.blonde` llegará a esa cola (igual que si enviasemos `lazy`).
