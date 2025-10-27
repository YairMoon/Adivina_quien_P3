# Adivina_quien_P3
![Portada del juego](https://github.com/YairMoon/Adivina_quien_P3/blob/main/images/portada.png?raw=true)


Adivina quien (personajes de marvel)
Adivina Quién – MARVEL (SHIELD Scanner) es un sistema experto interactivo inspirado en el clásico juego de “Adivina Quién”, pero llevado al universo de superhéroes y villanos de Marvel.

Tú piensas en un personaje del mundo Marvel (Vengadores, mutantes, villanos, Guardianes de la Galaxia, etc.) y el sistema trata de descubrir quién está haciendo preguntas de Sí / No. ¿Tu personaje usa armadura? ¿Es un vengador? ¿Es mutante? ¿Es un dios asgardiano? ¿Puedes trepar paredes? Cada respuesta filtra sospechosos hasta que la IA intenta identificar exactamente quién eres.

Este proyecto no es solo un juego de adivinanza rápida: es una demostración de un sistema experto de Inteligencia Artificial con encadenamiento hacia adelante. Eso significa que el “escáner” va razonando lógicamente a partir de tus respuestas y va descartando personajes que ya no cumplen con las pistas. Básicamente se comporta como si fuera una unidad de reconocimiento de SHIELD haciendo un análisis de identidad de un objetivo.

Características principales: • Interfaz estilo panel táctico de SHIELD, con escáner lateral de sospechosos activos.
• Motor de inferencia: el sistema elige preguntas inteligentes para reducir la lista de candidatos lo más rápido posible.
• Identificación final: cuando queda un solo personaje, el sistema lo presenta como “ALIADO” o “AMENAZA”.
• Manejo de ambigüedad: si todavía hay varios posibles (“puede ser Spider-Man o Venom…”), el sistema te muestra la lista de sospechosos y te pide confirmación.
• Aprendizaje incremental: si tu personaje no está en la base, el juego NO se rinde. Te deja entrenarlo.

Le dices quién era tu personaje.

El juego te hace una serie de preguntas de Sí / No (“¿es mutante?”, “¿usa armadura?”, “¿es alien?”, etc.).

Guarda ese personaje con todos sus atributos.

A partir de ahí, el sistema recordará ese personaje en futuras partidas.
• Memoria persistente en el navegador: los personajes nuevos se guardan localmente. Cuando vuelves a abrir el juego en este mismo dispositivo/navegador, el sistema ya conoce a los que le enseñaste antes.
• Sin descargas, sin instalación: corre directamente en el navegador.

¿Tecnología? Este proyecto nace como práctica de IA usando sistemas expertos clásicos (reglas lógicas, atributos booleanos, filtrado por descarte) y luego fue llevado a una versión web para que cualquiera pueda jugar sin instalar nada. El comportamiento imita una IA tipo agente de interrogatorio: va haciendo preguntas que dividen el espacio de posibilidades y se acerca cada vez más a la identidad real.

El flujo completo es:

Piensa en un personaje de Marvel (por ejemplo, Thor, Black Widow, Venom, Loki, Wolverine…).

Haga clic en “Iniciar Escaneo”.

Responde Sí / No a las preguntas del sistema.

Mira cómo se va reduciendo la lista de candidatos en tiempo real, como si fueras un objetivo bajo observación táctica.

El sistema intenta adivinar.

Si aciertas: misión completada.

Si falla: lo entrenas para que la próxima vez no falle.

 ¿Por qué esto es interesante? – Demuestra un sistema experto con encadenamiento hacia adelante (forward chaining): cada respuesta genera nuevas conclusiones y descarta hipótesis.
– Tiene una base de conocimiento inicial con héroes, villanos, mutantes, robots, dioses, alienígenas, etc., usando atributos tipo:

vengador

villano

mutante

extranjero

robot

dios

magia/hechicería

tecnología avanzada

garras

trepa_paredes

cambio de tamaño

Guardianes de la galaxia

x-men…y más.
Esto permite diferenciar personajes parecidos. Por ejemplo: Ant-Man y Spider-Man son héroes, humanos y con poderes, pero uno cambia de tamaño y el otro trepa paredes. Wolverine y Deadpool son mutantes violentos con curación… pero Wolverine tiene garras y es X-Men. El sistema usa justo esas diferencias para adivinar.

– Integra aprendizaje incremental: no es un juego estático. Evoluciona según lo que la gente le enseña.

⚠ Nota importante: Este es un proyecto fan-made con fines educativos / de demostración técnica. Los personajes mencionados pertenecen a Marvel / Disney. No es un producto oficial ni está afiliado, ni tiene multas comerciales.

En resumen: Es como jugar “¿Quién soy?” con la base de datos de SHIELD, pero el sistema aprende nuevos sospechosos cada vez que lo derrota.

¿Puedes engañar al escáner?
Intenta pensar en alguien que todavía no conoce… y enséñale. 
