# -*- coding: utf-8 -*-
"""
Genera datos-ideas-ia.js — banco de 365 días para el nicho
"IA y Automatización" (consultora de IA aplicada a autónomos y pymes).
Mismo esquema y mecánica que generar_banco_fiscalidad.py /
generar_banco_productividad.py.

Voz del nicho: clara, práctica y sin humo. Traduce lo técnico (prompt, agente,
flujo) a lenguaje llano. Habla de horas ahorradas y tareas concretas, nunca de
futurismo abstracto.
"""
import json

MESES = [("Julio",31), ("Agosto",31), ("Septiembre",30), ("Octubre",31),
         ("Noviembre",30), ("Diciembre",31), ("Enero",31), ("Febrero",28),
         ("Marzo",31), ("Abril",30), ("Mayo",31), ("Junio",30)]

CICLO_FORMATO = ["Reel","Carrusel","Reel","Post","Reel","Carrusel","Post"]
HASHTAGS_BASE = "#ia #automatizacion #pymes"

PILARES = {
 "Claude y ChatGPT": {
  "afecta": "lo que le sacas (o no) a la IA que ya tienes abierta",
  "cierre": "{subtema} marca la diferencia entre tener la IA de adorno y tener una ayudante que trabaja contigo cada día.",
  "subtemas": {
   "Usarla como buscador": {
    "pares": [
     ("Usar la IA como un Google caro es perderse el 90% de lo que sabe hacer.", "Escríbeme IA"),
     ("La IA no es para preguntarle cosas: es para encargarle trabajo.", "Guárdalo"),
     ("El cambio de mentalidad: de 'a ver qué sabe' a 'hazme esto'.", "¿La usas así?"),
    ],
    "hooks": [
     "Tienes Claude o ChatGPT abiertos en una pestaña. Y los usas para lo mismo que un buscador.",
     "Le preguntas a la IA lo que le preguntarías a Google. Ahí se queda el 90% de su potencial.",
     "La IA no es una enciclopedia: es una empleada. Deja de preguntarle y empieza a encargarle.",
     "'¿Qué es el marketing digital?' — pregunta de buscador. 'Escríbeme el plan de marketing de MI negocio' — encargo de verdad.",
     "Si tu historial con la IA parece un examen de cultura general, la estás desaprovechando.",
     "Google te da enlaces. La IA te da el trabajo hecho. Y tú la usas como Google.",
     "La diferencia entre curiosear con la IA y trabajar con ella: el verbo. Pregunta vs encarga.",
     "Un año con ChatGPT abierto y ni un solo proceso de tu negocio ha cambiado. Algo falla, y no es la IA.",
     "La IA que tienes gratis hoy hace cosas que hace 3 años costaban un sueldo. Úsala en serio.",
     "'Ya probé ChatGPT y no me convenció' — probaste el 5%. El otro 95% no se ve en la primera pregunta.",
     "Pídele a la IA algo que te dé pereza hacer HOY. Ahí empieza la relación de verdad.",
    ],
   },
   "Darle contexto": {
    "pares": [
     ("La IA no puede adivinar tu negocio: dale contexto real (quién eres, qué vendes, a quién) y todo cambia.", "Escríbeme IA"),
     ("Dos minutos de contexto ahorran veinte de correcciones.", "Guárdalo"),
     ("Un párrafo sobre tu negocio, guardado y listo para pegar: la mejor inversión de 5 minutos de este mes.", "¿Lo tienes?"),
    ],
    "hooks": [
     "La IA te responde genérico porque le hablas genérico. Contexto entra, calidad sale.",
     "Antes de pedirle nada, dile quién eres, qué vendes y a quién. Cambia TODO.",
     "El párrafo mágico: 4 líneas sobre tu negocio que convierten respuestas de manual en respuestas a medida.",
     "'Escríbeme un post' vs 'Escríbeme un post para dueñas de clínicas dentales que odian vender'. Compara resultados.",
     "La IA no sabe que tu cliente regatea, que tu sector es lento o que odias sonar comercial. Díselo.",
     "Ten guardado un texto con tu contexto de negocio y pégalo al empezar cada conversación. Rutina de 10 segundos.",
     "Cuanto más sabe de ti, menos corriges. La primera respuesta buena se fabrica antes de preguntar.",
     "Trata a la IA como a un empleado nuevo brillante: no sabe nada de tu empresa hasta que se lo cuentas.",
     "La respuesta 'de libro' que te dio la IA es un espejo: le diste una pregunta de libro.",
     "Proyecto/instrucciones personalizadas: la función de la IA que casi nadie usa y más tiempo ahorra.",
     "Deja de escribir prompts perfectos y empieza a dar contextos completos. El orden importa.",
    ],
   },
   "Iterar respuestas": {
    "pares": [
     ("La primera respuesta de la IA es un borrador: la buena sale en la segunda o tercera vuelta.", "Escríbeme IA"),
     ("Pedir cambios a la IA no es fracasar: es exactamente cómo se trabaja con ella.", "Guárdalo"),
     ("'Más corto', 'más directo', 'menos formal': tres órdenes que arreglan el 80% de las respuestas.", "¿Iteras o te conformas?"),
    ],
    "hooks": [
     "Le pides algo a la IA, no te gusta, cierras la pestaña. Error: ahí empezaba lo bueno.",
     "La primera respuesta de la IA casi nunca es la definitiva. Es el punto de partida.",
     "Con la IA no se pide y se acepta: se pide, se ajusta y se vuelve a ajustar. Como con un diseñador.",
     "'No me gusta' no es feedback ni para la IA ni para nadie. 'Hazlo más corto y sin tecnicismos' sí.",
     "Tres vueltas con la IA tardan 2 minutos. Rehacerlo tú desde cero, una hora.",
     "El botón de 'regenerar' es la herramienta menos usada y más útil de toda la IA.",
     "Guarda la conversación que funcionó: la próxima vez sigues desde ahí, no desde cero.",
     "Pídele a la IA 3 versiones del mismo texto y elige. Comparar es más fácil que imaginar.",
     "Cuando la IA se equivoca, díselo: 'esto está mal porque X'. Aprende dentro de la conversación.",
     "La conversación con la IA es eso: conversación. Los monólogos dan resultados de monólogo.",
     "Trabajar con IA es dirigir, no delegar a ciegas: tú tienes el criterio, ella la velocidad.",
    ],
   },
   "Contenido con IA": {
    "pares": [
     ("La IA redacta el borrador; tu criterio y tu historia lo hacen tuyo. Ese es el reparto.", "Escríbeme IA"),
     ("El contenido con IA no suena a robot si le das TU voz: ejemplos, expresiones y opiniones tuyas.", "Guárdalo"),
     ("Publicar más y mejor no va de escribir más rápido: va de no empezar nunca desde la página en blanco.", "¿Publicas más?"),
    ],
    "hooks": [
     "El contenido que 'suena a IA' es contenido al que no le diste tu voz. La culpa no es de la máquina.",
     "Un mes de posts en una tarde: el flujo IA + calendario que uso con mis clientas.",
     "La página en blanco murió: ahora todo empieza con un borrador de la IA y tu criterio encima.",
     "Dale a la IA tus 3 mejores posts y pídele más de eso. Aprende TU estilo, no uno genérico.",
     "La IA escribe rápido; tú sabes qué historia es verdad. Juntas, publicáis cada semana sin drama.",
     "'No tengo tiempo para redes' era verdad en 2022. Hoy es una decisión.",
     "El error del contenido con IA: publicar el borrador tal cual. Es masa, no pan.",
     "Pídele a la IA 20 ideas de post y quédate 5. Ideación en 3 minutos, criterio el de siempre: el tuyo.",
     "Tu experiencia + la velocidad de la IA = el contenido que tu competencia no puede copiar.",
     "Reciclar contenido con IA: un post bueno se convierte en reel, carrusel y newsletter en 10 minutos.",
     "La IA no te quita la voz: te quita la excusa.",
    ],
   },
   "Tu asistente diario": {
    "pares": [
     ("La IA rinde cuando se vuelve rutina: cada tarea pesada del día es una oportunidad de encargársela.", "Escríbeme IA"),
     ("No hace falta un gran proyecto de IA: hacen falta 5 usos pequeños cada día.", "Guárdalo"),
     ("El hábito es simple: antes de hacer algo aburrido, pregúntate '¿puede empezarlo la IA?'.", "¿Lo pruebas hoy?"),
    ],
    "hooks": [
     "Resumir la reunión, contestar ese email difícil, ordenar tus notas: tu asistente de IA ya hace todo eso.",
     "El email incómodo que llevas 2 días posponiendo: la IA te escribe el borrador en 20 segundos.",
     "Pega tus notas de la reunión y pide: resumen + tareas + email de seguimiento. Un minuto.",
     "La IA como asistente no es futuro: es dejar de redactar desde cero todo lo que ya redactas cada semana.",
     "Antes de cada tarea aburrida, una pregunta: ¿puede la IA hacer el primer 80%? Casi siempre: sí.",
     "Traducir, resumir, reescribir educadamente lo que querías decir de malas: el día a día real de la IA.",
     "Dale a la IA el PDF de 40 páginas y pide las 5 ideas clave. Leerlo entero era la vieja normalidad.",
     "Tu lista de tareas de hoy, pegada en la IA: 'ordénamela por impacto y dime por dónde empezar'.",
     "Prepara la reunión difícil ensayando con la IA: 'hazme las preguntas incómodas que me harán'.",
     "La IA de tu móvil también existe: dicta en el coche, ordena luego. Las ideas ya no se pierden.",
     "Un asistente que no se cansa, no juzga y no se pone malo. Y la mayoría lo usa una vez al mes.",
    ],
   },
  },
 },
 "Tareas repetitivas": {
  "afecta": "las horas que se te van cada semana en lo mismo",
  "cierre": "{subtema} es el mejor sitio para empezar con la automatización: poco riesgo, resultado visible desde la primera semana.",
  "subtemas": {
   "Mensajes repetidos": {
    "pares": [
     ("Si escribes el mismo mensaje más de 3 veces por semana, ya tienes tu primera automatización.", "Escríbeme AUTOMATIZA"),
     ("Responder siempre lo mismo a mano no es atención personalizada: es tiempo perdido con buena intención.", "Guárdalo"),
     ("Plantilla + toque personal de una línea = mismo cariño, 10% del tiempo.", "¿Cuál repites tú?"),
    ],
    "hooks": [
     "Copiar y pegar el mismo mensaje a cada cliente nuevo es trabajo que ya no deberías hacer tú.",
     "Cuenta cuántas veces escribiste 'nuestro horario es...' este mes. Esa cifra es tu primera automatización.",
     "El presupuesto tipo, la bienvenida, el 'cómo llegar': mensajes que se escriben UNA vez en la vida.",
     "Contestas las mismas 10 preguntas cada semana. Las mismas. Cada semana.",
     "Tu WhatsApp de empresa tiene respuestas rápidas integradas. Gratis. Sin usar.",
     "Personalizar no es escribir todo a mano: es cambiar una línea de una plantilla buena.",
     "Cada 'ahora te paso la info' que escribes a mano son 5 minutos que ya regalaste ayer. Y antes de ayer.",
     "El mensaje de seguimiento a presupuestos que no contestan: automatizable al 100% y nadie lo hace.",
     "Tus clientes preguntan siempre lo mismo porque nadie se lo cuenta antes. Eso también se automatiza.",
     "Una tarde montando plantillas te devuelve una hora cada semana. Para siempre.",
     "'Es que cada cliente es distinto' — el 80% de tus respuestas dice lo contrario.",
    ],
   },
   "Datos de un sitio a otro": {
    "pares": [
     ("Pasar datos a mano de una app a otra es el trabajo más automatizable que existe.", "Escríbeme AUTOMATIZA"),
     ("Cada copia-pega semanal es un puente sin construir entre dos herramientas que ya se conocen.", "Guárdalo"),
     ("El formulario que rellena tu hoja de cálculo solo: existe, es barato y se monta en una tarde.", "¿Lo montamos?"),
    ],
    "hooks": [
     "Copias datos del email a una hoja de cálculo, a mano, cada semana. En 2026.",
     "El pedido llega por WhatsApp, lo apuntas en un papel, lo pasas al Excel. Tres veces el mismo dato.",
     "Si tu lunes empieza pasando cosas de un sitio a otro, tu lunes es automatizable.",
     "Las apps que usas probablemente ya se conectan entre sí. Nadie se lo ha pedido.",
     "Cada dato que tecleas dos veces es un error esperando a pasar. Y tiempo pagado dos veces.",
     "El formulario de tu web puede escribir directamente en tu hoja de clientes. Sin ti en medio.",
     "'Luego lo paso al ordenador' — esa frase resume horas de tu mes que podrían no existir.",
     "Factura al Excel, Excel al gestor, gestor al email: una cadena humana para lo que hace un clic.",
     "Zapier, Make o la automatización de tu propia app: nombres raros, concepto simple: 'cuando pase X, haz Y'.",
     "La foto del ticket que se transcribe sola a tu contabilidad: eso ya existe y cuesta poco.",
     "Un cliente nuevo debería aparecer SOLO en tu lista, tu email y tu facturación. Una vez. En todas partes.",
    ],
   },
   "Documentos y plantillas": {
    "pares": [
     ("Los documentos que haces 'casi iguales' cada vez —presupuestos, contratos, informes— se generan solos.", "Escríbeme AUTOMATIZA"),
     ("Una buena plantilla no es pereza: es que el documento nº 50 salga tan bien como el nº 1.", "Guárdalo"),
     ("Rellenar huecos en vez de redactar desde cero: así se hacen los documentos en un negocio ordenado.", "¿Cuánto tardas tú?"),
    ],
    "hooks": [
     "Cada presupuesto que envías lo montas desde cero. El anterior era 90% igual.",
     "Presupuesto en 4 minutos: plantilla + datos del cliente + IA para el párrafo personalizado.",
     "Tu contrato tipo, tu propuesta tipo, tu informe tipo: si no existen, cada semana los reinventas.",
     "El documento que tardas una hora en hacer, con plantilla tarda diez minutos. Cada vez.",
     "Redactas 'a tu manera' cada propuesta y luego no recuerdas qué versión enviaste a quién.",
     "La IA rellena tu plantilla de propuesta con los datos de la reunión. Tú solo revisas y envías.",
     "Un buen sistema de plantillas responde más rápido que tu competencia. Y el rápido se lleva el sí.",
     "Informe mensual para clientes: mismo formato, datos nuevos. Receta perfecta para automatizar.",
     "Cada hora invertida en una buena plantilla se recupera la primera semana. Después, es regalo.",
     "Las plantillas no te quitan personalidad: te quitan lo mecánico para que pongas la personalidad donde importa.",
     "Tu carpeta de 'documentos enviados' guarda oro: los mejores son tus plantillas de mañana.",
    ],
   },
   "Clasificar información": {
    "pares": [
     ("Ordenar emails, notas y archivos a mano es trabajo de máquina que sigues haciendo tú.", "Escríbeme AUTOMATIZA"),
     ("La IA clasifica en segundos lo que a ti te roba la primera hora del día.", "Guárdalo"),
     ("Las reglas simples ('si viene de X, va a Y') llevan 20 años en tu email esperándote.", "¿Las usas?"),
    ],
    "hooks": [
     "La primera hora de tu día se va en ordenar el correo. La máquina lo hace en 4 segundos.",
     "Tu bandeja de entrada no necesita más disciplina: necesita 5 reglas automáticas.",
     "Pega 50 mensajes de clientes en la IA y pide: 'agrúpame las quejas por tema'. Minutos, no tardes.",
     "Los emails de facturas pueden archivarse solos en su carpeta. Desde siempre. Nadie activa la regla.",
     "Etiquetar, mover, archivar, marcar: verbos de robot que siguen en tu lista de tareas.",
     "La IA lee el email y te dice si es urgente, comercial o basura. Tú decides solo sobre los urgentes.",
     "Buscar 'aquel archivo que me pasaron por WhatsApp en marzo': el deporte nacional. Automatizable.",
     "Las reseñas de tus clientes, resumidas por la IA en 3 quejas y 3 elogios. De 200 opiniones a 1 página.",
     "Si clasificar te lleva más de 15 minutos al día, tienes un flujo esperando a nacer.",
     "El caos de información no se arregla ordenando más fuerte: se arregla con un embudo automático.",
     "Tu cerebro es para decidir, no para archivar. Delega el archivo en quien no se aburre: la máquina.",
    ],
   },
   "Detectar qué automatizar": {
    "pares": [
     ("La regla de las 3 veces: lo que repites igual más de 3 veces, apúntalo. Esa lista es tu plan.", "Escríbeme AUTOMATIZA"),
     ("No se empieza automatizando lo difícil: se empieza por lo aburrido y frecuente.", "Guárdalo"),
     ("Una semana apuntando tus tareas repetidas vale más que un mes leyendo sobre IA.", "¿Cuál es la tuya?"),
    ],
    "hooks": [
     "Si una tarea la repites más de 3 veces igual, no es trabajo. Es una automatización pendiente.",
     "El ejercicio de una semana: apunta cada tarea que hagas más de una vez. El viernes tendrás tu plan.",
     "No sabes qué automatizar porque nunca has mirado tu semana con esa pregunta.",
     "Lo primero que se automatiza no es lo más pesado: es lo más FRECUENTE. La frecuencia multiplica.",
     "Tu mejor candidata a automatización: aburrida, frecuente y con pasos siempre iguales. Todas la tenemos.",
     "¿Cuántas horas a la semana pasas haciendo algo que un flujo automatizado haría por ti?",
     "Pregunta a tu equipo qué tarea odian. Ahí suele estar la automatización más rentable.",
     "Automatiza primero lo que no da miedo: el recordatorio, la copia de seguridad, el archivo. Momentum.",
     "El mapa de tu semana tiene tesoros escondidos: tareas de 10 minutos que se repiten 20 veces.",
     "Si explicar la tarea cuesta una frase ('paso esto aquí cada viernes'), automatizarla cuesta poco.",
     "Empieza por UNA. La segunda automatización siempre es más fácil: ya sabes que funciona.",
    ],
   },
  },
 },
 "Miedo y excusas": {
  "afecta": "cuánto tardas en subirte (o en quedarte mirando)",
  "cierre": "{subtema} se supera igual que todo en tu negocio: empezando pequeño, con ayuda y sin humo.",
  "subtemas": {
   "No soy de tecnología": {
    "pares": [
     ("'No soy de tecnología' es la frase que más frena a los negocios que más lo necesitan.", "Escríbeme IA"),
     ("La IA de hoy se maneja hablando: si sabes explicar tu negocio, sabes usarla.", "Guárdalo"),
     ("No necesitas entender cómo funciona: necesitas saber qué pedirle. Como al coche.", "¿Te frena esto?"),
    ],
    "hooks": [
     "'Yo no soy de tecnología' — tampoco eres de mecánica y conduces un coche.",
     "La IA moderna se usa ESCRIBIENDO. Si sabes mandar un WhatsApp, sabes lo básico.",
     "No hace falta saber programar. Hace falta saber explicar qué quieres. Y eso ya lo haces con tu equipo.",
     "Mis clientas 'de letras' usan la IA mejor que muchos informáticos: saben pedir con claridad.",
     "La barrera no es técnica: es la primera media hora. Superada esa, todo rueda.",
     "Tu abuela usa videollamadas. Tú puedes usar IA. La curva es la misma: corta.",
     "Lo técnico ya lo resolvieron otros: tu trabajo es poner el criterio de negocio. Eso no lo tiene la máquina.",
     "Decir 'no soy de tecnología' en 2026 es como decir 'no soy de electricidad' en 1950.",
     "No te pido que entiendas la IA: te pido que le encargues UNA tarea esta semana.",
     "El manual de la IA cabe en una frase: escribe lo que necesitas como se lo dirías a una persona.",
     "La tecnología difícil es la que está mal hecha. La IA actual está hecha para hablarle.",
    ],
   },
   "Quedarse atrás": {
    "pares": [
     ("No te vas a quedar atrás por no saber de IA: te vas a quedar atrás por no empezar.", "Escríbeme IA"),
     ("Tu competencia no es más lista: solo empezó antes. Y eso tiene arreglo hoy mismo.", "Guárdalo"),
     ("La ventaja de la IA es acumulativa: cada mes que pasa, el que empezó suma y el que no, mira.", "¿Cuándo empiezas?"),
    ],
    "hooks": [
     "Mientras decides si la IA 'va contigo', tu competencia responde presupuestos en la mitad de tiempo.",
     "El 47% de los autónomos ya ve la IA como su mayor oportunidad este año. ¿Y tú?",
     "No hace falta ser el primero. Pero ser el último de tu sector tiene precio.",
     "Dentro de un año, usar IA será como tener web: nadie te aplaudirá por ello, pero se notará no tenerla.",
     "La brecha no es entre grandes y pequeños: es entre los que empezaron y los que 'lo están mirando'.",
     "Tu sector parece tranquilo hasta que un competidor contesta a las 23h con un asistente que no duerme.",
     "Quedarse atrás no duele de golpe: duele de a poco, cliente a cliente, hora a hora.",
     "'Esto de la IA es una moda' — se dijo de la web, del email y de las redes. ¿Cómo acabó?",
     "Los que esperaron 'a que madurara' internet compraron después los servicios de los que no esperaron.",
     "Empezar hoy con la IA es llegar pronto. El año que viene, es llegar a tiempo. Después, tarde.",
     "No compites contra la IA: compites contra negocios como el tuyo que YA la usan.",
    ],
   },
   "Empezar pequeño": {
    "pares": [
     ("No empieces por rehacer tu negocio: empieza por UNA tarea que te ahorre tiempo esta semana.", "Escríbeme EMPEZAR"),
     ("El primer paso con la IA debe ser tan pequeño que dé pereza NO darlo.", "Guárdalo"),
     ("Una tarea, una semana, un resultado visible: así se empieza sin agobios.", "¿Cuál eliges?"),
    ],
    "hooks": [
     "No necesitas una 'estrategia de IA'. Necesitas automatizar UNA tarea esta semana.",
     "El error de los principiantes: querer automatizarlo todo. El acierto: empezar por lo más tonto.",
     "Tu primer proyecto de IA debería caber en una tarde. Si no cabe, es demasiado grande para empezar.",
     "Empieza por la tarea que más pereza te da. La motivación de quitártela de encima es gasolina.",
     "Primera semana: la IA te escribe los emails difíciles. Solo eso. Ya notarás el enganche.",
     "Nadie aprendió a nadar estudiando el mar. Una tarea pequeña es tu piscina.",
     "El plan anti-agobio: 30 minutos, una tarea, esta semana. Sin cursos, sin gurús, sin humo.",
     "La confianza con la IA se construye con victorias pequeñas, no con proyectos épicos.",
     "De 'no sé por dónde empezar' a 'ya automaticé una cosa' hay una tarde. Literalmente.",
     "Si tu primer intento con la IA fracasa, elegiste una tarea demasiado grande. Reduce y repite.",
     "Lo pequeño compuesto gana: una tarea al mes son 12 procesos automáticos en un año.",
    ],
   },
   "Mitos de la IA": {
    "pares": [
     ("La mitad de lo que te frena de la IA son mitos: ni te sustituye, ni es carísima, ni es solo para técnicos.", "Escríbeme IA"),
     ("Desmontar un mito cuesta un minuto; vivir con él cuesta oportunidades cada semana.", "Guárdalo"),
     ("La IA real es más aburrida y más útil que la de las películas.", "¿Cuál te creías tú?"),
    ],
    "hooks": [
     "Mito: la IA te va a sustituir. Realidad: te va a sustituir un competidor que la use mejor que tú.",
     "Mito: la IA es cara. Realidad: la versión gratis ya hace el 80% de lo que tu negocio necesita.",
     "Mito: hay que saber programar. Realidad: hay que saber escribir un mensaje claro.",
     "Mito: la IA se equivoca mucho. Realidad: se equivoca como un becario brillante. Se revisa y punto.",
     "Mito: 'mi negocio es demasiado especial para la IA'. Todos los negocios responden emails.",
     "Mito: la IA es para empresas grandes. Realidad: al pequeño le cambia más la vida, porque no tiene equipo.",
     "Mito: usar IA es hacer trampa. ¿También lo era la calculadora?",
     "Mito: la IA es fría con los clientes. Realidad: más frío es tardar 3 días en contestar.",
     "Mito: 'cuando madure, me subo'. Ya maduró. Lo que crece ahora es la distancia con los que la usan.",
     "Mito: necesitas 'transformación digital'. Necesitas quitarle 5 horas de tareas tontas a tu semana.",
     "Mito: la IA inventa cosas y no es fiable. Verdad a medias: por eso el criterio sigue siendo tuyo. Como con todo.",
    ],
   },
   "El coste de esperar": {
    "pares": [
     ("Esperar también cuesta: cada mes sin automatizar son horas que pagas con tu tiempo libre.", "Escríbeme AHORRA"),
     ("El 'ya lo haré' con la IA se mide en horas perdidas: unas 20 al mes según la tarea.", "Guárdalo"),
     ("Empezar no cuesta casi nada; no empezar cuesta un poco cada día, y no se nota hasta que se suma.", "¿Echamos la cuenta?"),
    ],
    "hooks": [
     "Cada mes que esperas, alguien de tu sector ya está automatizando. El coste de esperar existe.",
     "'No tengo tiempo para mirar la IA' — precisamente por eso la necesitas.",
     "Haz la cuenta: 5 horas semanales en tareas repetitivas × tu tarifa/hora × 52 semanas. Eso cuesta esperar.",
     "La procrastinación tecnológica tiene factura: se paga en tardes de domingo poniéndote al día.",
     "Esperar 'al momento perfecto' para la IA es como esperar al momento perfecto para hacer deporte.",
     "El año pasado dijiste 'este año miro lo de la IA'. Van dos.",
     "Cada tarea que sigues haciendo a mano ya tiene solución inventada, probada y barata. Solo falta que la uses.",
     "No decidir también es decidir: estás eligiendo la versión lenta de tu negocio.",
     "El coste de la IA se ve en la factura. El coste de NO usarla se esconde en tu agenda.",
     "Un negocio que espera a 'verlo claro' compra caro lo que pudo aprender barato.",
     "La mejor fecha para empezar con la IA fue hace un año. La segunda mejor es este jueves.",
    ],
   },
  },
 },
 "Agentes": {
  "afecta": "el salto de usar la IA a que trabaje sola",
  "cierre": "{subtema} deja de ser ciencia ficción cuando lo ves aplicado a UNA tarea concreta de tu negocio.",
  "subtemas": {
   "Qué es un agente": {
    "pares": [
     ("Un agente de IA no responde preguntas: hace el trabajo completo, paso a paso, solo.", "Escríbeme AGENTE"),
     ("Agente en una frase: una IA a la que le das un objetivo, no una orden.", "Guárdalo"),
     ("La diferencia práctica: el chatbot te ayuda a trabajar; el agente trabaja.", "¿Lo conocías?"),
    ],
    "hooks": [
     "Un agente de IA no es un chatbot que responde. Es un sistema que hace el trabajo completo, solo.",
     "'Agente de IA' explicado sin humo: le das un objetivo y él decide los pasos. Como un empleado.",
     "Chatbot: '¿en qué te ayudo?'. Agente: 'ya está hecho, te dejo el resumen'.",
     "El agente lee el email, decide qué responder, lo agenda y te avisa solo si duda. Sin ti en medio.",
     "La palabra 'agente' suena a espía. Piensa mejor en 'becario incansable con instrucciones claras'.",
     "Un agente puede mirar tu agenda, tus emails y tu lista de tareas, y prepararte el día. Cada mañana.",
     "No es magia: es una IA con permisos para usar tus herramientas y un objetivo bien escrito.",
     "2026 no va de tener más IA: va de pasar de herramientas sueltas a agentes que trabajan solos.",
     "El salto mental: dejar de preguntarle cosas a la IA y empezar a asignarle responsabilidades.",
     "Tu primer agente no será Terminator: será algo tan tonto como 'revisa esto cada mañana y avísame si...'.",
     "Agente de IA en tu negocio = la parte de tu trabajo que tiene reglas claras, hecha sin ti.",
    ],
   },
   "Agente vs chatbot": {
    "pares": [
     ("Automatizar es que la máquina ejecute UNA orden; un agente decide los siguientes pasos solo.", "Escríbeme AGENTE"),
     ("La escalera: primero plantillas, luego automatizaciones, luego agentes. Cada peldaño ahorra más.", "Guárdalo"),
     ("No todo necesita un agente: a veces basta una regla tonta. Saber cuál toca es el oficio.", "¿En qué peldaño estás?"),
    ],
    "hooks": [
     "Automatización: 'cuando llegue un email, guárdalo'. Agente: 'gestiona mi bandeja y molesta solo si hace falta'.",
     "El chatbot contesta lo que sabe. El agente investiga lo que no sabe antes de contestar.",
     "Regla simple → automatización → agente: la escalera de la IA, explicada con ejemplos de negocio.",
     "No pagues un agente para lo que resuelve una regla de tu email. Ni uses reglas para lo que pide criterio.",
     "La automatización clásica se rompe si algo cambia. El agente se adapta: esa es la diferencia cara.",
     "Tu respuesta automática de WhatsApp es un loro. Un agente sería un recepcionista.",
     "¿Necesitas agente o plantilla? Test rápido: ¿la tarea requiere DECIDIR algo? Si no, plantilla.",
     "El chatbot de tu web frustra porque es un menú disfrazado. Los agentes de verdad conversan y resuelven.",
     "Un agente combina varias herramientas: lee aquí, calcula allá, escribe al final. El chatbot vive en su caja.",
     "Empieza con automatizaciones tontas; gana confianza; sube a agentes. El orden importa.",
     "La pregunta no es '¿chatbot o agente?': es '¿cuánto criterio necesita esta tarea?'.",
    ],
   },
   "Casos en negocio pequeño": {
    "pares": [
     ("Los agentes no son de multinacional: el negocio pequeño es donde más se nota una ayudante incansable.", "Escríbeme AGENTE"),
     ("Un caso real vale más que diez definiciones: mira lo que ya hacen negocios como el tuyo.", "Guárdalo"),
     ("Presupuestos, citas, seguimiento, reseñas: los 4 agentes estrella del negocio pequeño.", "¿Cuál te haría falta?"),
    ],
    "hooks": [
     "Una clínica pequeña: el agente confirma citas, gestiona cambios y rellena huecos libres. Solo.",
     "El agente que persigue presupuestos sin contestar: educado, constante y sin vergüenza. Recupera ventas dormidas.",
     "Caso real: tienda online de 1 persona con un agente que responde el 70% de las consultas. Bien.",
     "Tu agente de reseñas: detecta la opinión nueva, agradece, y si es mala te avisa ANTES de responder.",
     "El agente comercial silencioso: visita webs de potenciales clientes y te prepara la ficha antes de llamar.",
     "Una gestoría con un agente que clasifica los papeles que mandan los clientes. Se acabó el 'falta la factura de...'.",
     "El agente de contenido: te propone posts según lo que preguntan tus clientes esa semana. Material infinito.",
     "Peluquería, taller, despacho: distinto sector, mismo agente de citas. Las agendas son agendas.",
     "El autónomo con un agente que le resume cada mañana: emails importantes, citas del día y UNA prioridad.",
     "No tienes departamento de atención al cliente. Un agente bien montado es el 60% de uno.",
     "El caso más rentable suele ser el más aburrido: el agente que reclama facturas impagadas con dulzura.",
    ],
   },
   "Supervisión y confianza": {
    "pares": [
     ("A un agente se le dan responsabilidades poco a poco, como a un empleado nuevo: primero con supervisión.", "Escríbeme AGENTE"),
     ("El agente hace; tú apruebas lo delicado. Ese reparto se configura, no se sufre.", "Guárdalo"),
     ("La confianza en un agente se gana con dos semanas de revisar lo que hace. Después, vuela.", "¿Le darías las llaves?"),
    ],
    "hooks": [
     "¿Dejarías a un agente enviar emails por ti? Aún no. Por eso empiezan proponiendo y tú apruebas.",
     "Regla de oro con agentes: que pida permiso para lo importante y haga solo lo rutinario.",
     "Las dos semanas de rodaje: el agente propone, tú corriges. Después ya escribe como tú.",
     "El miedo a que 'la IA diga algo raro a un cliente' se resuelve con un botón: aprobar antes de enviar.",
     "A tu primer empleado no le diste las llaves el primer día. Con el agente, igual: acceso gradual.",
     "Un agente bien montado sabe cuándo NO sabe: y entonces te pregunta, no inventa.",
     "Los errores del agente en rodaje son datos gratis: cada corrección lo entrena para tu negocio.",
     "Supervisar un agente 10 minutos al día < hacer tú el trabajo 2 horas al día. La cuenta sale.",
     "'¿Y si se equivoca?' — ¿y cuando te equivocas tú con prisa un viernes? El agente al menos no tiene prisa.",
     "Límites claros: qué puede hacer solo, qué consulta, qué jamás toca. Se escribe UNA vez.",
     "La confianza no se declara: se construye tarea a tarea. Con personas y con agentes.",
    ],
   },
   "El salto de 2026": {
    "pares": [
     ("Lo nuevo no es la IA: es que ahora puede usar tus herramientas y completar trabajos enteros.", "Escríbeme AGENTE"),
     ("El salto de este año: de 'me ayuda a redactar' a 'me lleva este proceso'.", "Guárdalo"),
     ("No hace falta subirse a todo: hace falta entender qué cambió para decidir con criterio.", "¿Lo hablamos?"),
    ],
    "hooks": [
     "Hace dos años la IA escribía textos. Hoy gestiona procesos. El cambio de verbo lo cambia todo.",
     "El salto de 2026 no es tener más IA: es pasar de herramientas sueltas a agentes que trabajan solos.",
     "Tu software de siempre está metiendo agentes dentro sin que lo sepas. Mira las novedades de tus apps.",
     "La IA dejó de vivir en una pestaña: ahora se conecta a tu email, tu agenda y tu facturación.",
     "Antes: 'IA, escríbeme un email'. Ahora: 'IA, gestiona esta conversación hasta cerrar la cita'.",
     "Los agentes son la razón por la que 2026 no se parece a 2024. Y 2027 no se parecerá a esto.",
     "Cada mes salen agentes nuevos ya montados para sectores concretos. Quizá el tuyo ya existe.",
     "No es ciencia ficción cara: muchos agentes se montan con las suscripciones que YA pagas.",
     "La ventana está abierta: los primeros de cada sector en usar agentes van a fijar el nuevo ritmo.",
     "Del 'copiar y pegar de ChatGPT' al agente conectado hay un paso. Y es más corto de lo que parece.",
     "En 2027, 'contesta él solo' sonará tan normal como hoy suena 'tengo página web'.",
    ],
   },
  },
 },
 "Prompts": {
  "afecta": "la calidad de todo lo que la IA te devuelve",
  "cierre": "{subtema} es el 80% del resultado: la misma IA, con mejor pedido, trabaja el doble de fino.",
  "subtemas": {
   "La pregunta correcta": {
    "pares": [
     ("La mayoría no tiene un problema de herramientas: tiene un problema de cómo pedir las cosas.", "Escríbeme PROMPT"),
     ("Un prompt mal escrito da una respuesta de manual; uno bueno, un resultado que usas tal cual.", "Guárdalo"),
     ("Cambia cómo le pides las cosas a la IA y cambia el tiempo que te ahorra.", "¿Cómo pides tú?"),
    ],
    "hooks": [
     "Le pides algo a la IA y el resultado es genérico. El problema no es la IA: es la pregunta.",
     "La misma IA, dos prompts distintos, resultados de otra galaxia. El poder está en el pedido.",
     "'Hazme un post' es como decirle a un cocinero 'hazme comida'. Comerás algo, pero no lo que querías.",
     "La habilidad mejor pagada de esta década cabe en una frase: saber pedir con precisión.",
     "Si la respuesta de la IA no te sirve, léete tu pregunta: casi siempre el fallo está arriba.",
     "Preguntas vagas, respuestas vagas. La IA es un espejo con vocabulario.",
     "Tu resultado con la IA mejora un 80% con esta costumbre: decirle PARA QUÉ lo quieres.",
     "Antes de culpar a la IA de 'no entenderte', pregúntate si tu equipo te habría entendido con ese mensaje.",
     "El prompt es una orden de trabajo. ¿Le darías esa orden así de vaga a un empleado?",
     "No busques el 'prompt mágico' de un gurú: aprende las 4 piezas de un buen pedido y móntalos tú.",
     "Saber pedir a la IA es la nueva ofimática: básico, aprendible y sorprendentemente escaso.",
    ],
   },
   "Contexto y formato": {
    "pares": [
     ("Los dos aceleradores de cualquier prompt: contexto (quién eres, para qué) y formato (cómo lo quieres).", "Escríbeme PROMPT"),
     ("Pide el formato exacto: lista, tabla, 100 palabras, tono cercano. La IA obedece formatos de maravilla.", "Guárdalo"),
     ("El molde importa: la misma idea en tabla, lista o párrafo sirve para cosas distintas.", "¿Pides formato?"),
    ],
    "hooks": [
     "El truco más rentable del prompt: dile CÓMO quieres la respuesta. Tabla, lista, 3 frases, tono de amiga.",
     "'Respóndeme en máximo 100 palabras' — siete palabras que arreglan las respuestas-testamento.",
     "Contexto + formato: las dos piezas que separan un prompt de aficionado de uno profesional.",
     "Pídele la respuesta 'como si se lo explicaras a un cliente sin conocimientos'. El tono cambia entero.",
     "¿La IA te da respuestas kilométricas? Nunca le has dicho cuánto quieres que escriba.",
     "'Dámelo en tabla con columnas X, Y, Z' — y de repente la IA te hace el trabajo ordenado, no solo escrito.",
     "El formato es gratis: pedir la respuesta lista-para-pegar te ahorra el retoque de después.",
     "Dile a quién va dirigido el texto y la IA ajusta sola el nivel. Es su superpoder menos usado.",
     "Un buen prompt tiene menos de poesía y más de encargo de obra: medidas, materiales, plazo.",
     "'En el tono de mis posts anteriores' + pegar dos ejemplos: la IA clava tu voz en un intento.",
     "Respuesta demasiado formal, demasiado larga y demasiado plana: tres defectos, una causa: no pediste formato.",
    ],
   },
   "Ejemplos y límites": {
    "pares": [
     ("Enséñale un ejemplo de lo que quieres y la IA multiplica su puntería: se llama aprender de muestra.", "Escríbeme PROMPT"),
     ("Los límites también se piden: 'sin tecnicismos, sin emojis, sin exagerar'. Y obedece.", "Guárdalo"),
     ("Decir qué NO quieres ahorra tantas vueltas como decir qué sí.", "¿Le pones límites?"),
    ],
    "hooks": [
     "El prompt más eficaz del mundo incluye dos palabras: 'por ejemplo'.",
     "Pega un ejemplo de texto tuyo que te guste y di 'como este'. La mejora es inmediata.",
     "'Sin palabras grandilocuentes, sin emojis, sin prometer imposibles' — los límites que hacen tu texto creíble.",
     "La IA exagera por defecto ('¡revolucionario!', '¡increíble!'). Se le quita con una línea de límites.",
     "Muéstrale un ejemplo BUENO y uno MALO y explica por qué. Acabas de entrenar a tu asistente.",
     "Prohibirle palabras funciona: 'no uses disruptivo, ni sinergia, ni viaje'. Pruébalo hoy.",
     "El texto de la IA suena a todos porque nadie le enseña el ejemplo de UNO. Enséñale el tuyo.",
     "Los límites no encorsetan: liberan. Con las reglas claras, la IA acierta a la primera.",
     "'Máximo 2 frases por párrafo. Nada de listas. Trato de tú.' — tres límites, otro nivel de resultado.",
     "Cuando la IA hace algo que odias, conviértelo en regla para la próxima: así se construye tu prompt maestro.",
     "Ejemplo + límites + formato: el trío que convierte 'está bien' en 'lo publico tal cual'.",
    ],
   },
   "Prompts reutilizables": {
    "pares": [
     ("Un buen prompt reutilizable ahorra más que uno perfecto usado una vez: guárdalos como plantillas.", "Escríbeme PROMPT"),
     ("Tu biblioteca de prompts es un activo del negocio: cada uno es un proceso ya resuelto.", "Guárdalo"),
     ("El prompt que funcionó no se pierde: se guarda, se pule y se convierte en rutina.", "¿Los guardas?"),
    ],
    "hooks": [
     "Escribes desde cero cada vez el mismo tipo de pedido a la IA. Los prompts también se guardan.",
     "Tu carpeta de 'prompts que funcionan' vale más que cualquier curso de IA.",
     "El prompt del presupuesto, el del post, el del email difícil: escríbelos UNA vez, úsalos siempre.",
     "Un prompt reutilizable con huecos ([cliente], [servicio], [tono]) es una máquina de trabajo lista.",
     "Cada vez que la IA te dé un resultado excelente, para y guarda el prompt. Oro reutilizable.",
     "Mis clientas tienen 10-15 prompts guardados que usan a diario. Ese es todo su 'stack de IA'.",
     "El prompt maestro de tu negocio: contexto fijo + tarea variable. Se escribe una tarde, sirve un año.",
     "Compartir prompts con tu equipo = todos escriben con la calidad del que mejor pide.",
     "Deja de perseguir prompts de gurús de internet: el mejor prompt es el tuyo, versión 3.",
     "Los prompts se heredan: el de hoy es el borrador del de mañana. Verión a versión, mejora sola.",
     "Prompt sin guardar, aprendizaje perdido. La memoria del proceso es parte del proceso.",
    ],
   },
   "Resultados genéricos": {
    "pares": [
     ("El texto 'que suena a IA' es un síntoma: faltó tu contexto, tu ejemplo o tus límites.", "Escríbeme PROMPT"),
     ("Lo genérico no se arregla regenerando 10 veces: se arregla mejorando el pedido una vez.", "Guárdalo"),
     ("La IA da medianía por defecto y excelencia bajo dirección. La dirección eres tú.", "¿Te suena?"),
    ],
    "hooks": [
     "Si el texto de la IA lo podría firmar cualquiera, el prompt lo podría haber escrito cualquiera.",
     "El 'olor a ChatGPT' de un texto no viene de la IA: viene de un pedido sin alma.",
     "Regeneraste 8 veces y sigue sonando plano. El botón que necesitas no es ese: es editar tu prompt.",
     "'En un mundo cada vez más digital...' — si tu texto empieza así, la IA te está dando su relleno estándar.",
     "Las respuestas genéricas son el precio de las preguntas cómodas.",
     "La IA no conoce tus anécdotas, tus clientes ni tus manías. Sin eso, escribe para nadie.",
     "Texto correcto pero olvidable: el modo por defecto de la IA. Salir de ahí cuesta 3 líneas de prompt.",
     "Tu competencia también usa IA. La diferencia estará en quién le da mejor materia prima.",
     "Un texto genérico publicado es peor que no publicar: dice 'aquí no hay nadie'.",
     "Lo genérico se cura con detalles: un dato tuyo, un caso real, una opinión con firma.",
     "La IA es tu altavoz, no tu autor: si no le das nada tuyo, amplifica el vacío.",
    ],
   },
  },
 },
 "Horas ahorradas": {
  "afecta": "el tiempo que recuperas cada semana",
  "cierre": "{subtema} es la métrica que importa: la IA no va de tecnología, va de a qué dedicas tus horas.",
  "subtemas": {
   "Cuánto vale tu hora": {
    "pares": [
     ("Ponle precio a tu hora y cada tarea repetitiva se convierte en una factura que te haces a ti misma.", "Escríbeme AHORRA"),
     ("Tu hora tiene precio aunque nadie te la pague: es lo que dejas de generar mientras haces tareas tontas.", "Guárdalo"),
     ("La cuenta que lo cambia todo: tarifa/hora × horas en tareas automatizables × 52 semanas.", "¿Sale mucho?"),
    ],
    "hooks": [
     "¿Cuánto vale tu hora? Multiplícalo por las que pierdes en tareas que ya podrían hacerse solas.",
     "Facturas 50€/hora y pasas 6 horas semanales copiando datos. Son 15.600€ al año en trabajo de robot.",
     "Tu hora tiene precio incluso cuando nadie te la paga. Sobre todo cuando nadie te la paga.",
     "El dueño de negocio que hace tareas de 10€/hora está pagando muy caro ese 'yo me lo hago todo'.",
     "Antes de decir 'la IA es cara', calcula lo que cuesta el trabajo manual que evitas. Da risa la comparación.",
     "No es 'ahorrar tiempo': es liberar horas caras para trabajo caro. Contabilidad pura.",
     "La tarea de cada semana que odias tiene un precio anual. Ponle número y decidirás rápido.",
     "Tu tarifa por hora la conoces. ¿Y tu 'tarifa' haciendo papeleo? La misma. Ese es el problema.",
     "El presupuesto para automatizar sale solo: es una fracción de lo que cuesta NO hacerlo.",
     "Cobras por tu criterio y gastas el día en tareas sin criterio. La IA existe justo para ese desajuste.",
     "Cada hora recuperada vale su precio en dinero... o en llegar a recoger a los niños sin correr.",
    ],
   },
   "5 horas a la semana": {
    "pares": [
     ("5 horas semanales: el ahorro medio de un negocio que automatiza bien sus 3 tareas más repetidas.", "Escríbeme AHORRA"),
     ("No se trata de usar IA por moda: se trata de las horas que dejas de perder.", "Guárdalo"),
     ("5 horas a la semana son 26 días laborables al año. Un mes extra. De regalo.", "¿Qué harías con ellas?"),
    ],
    "hooks": [
     "5 horas a la semana. Eso recupera de media un negocio que automatiza bien solo 3 tareas.",
     "5 horas semanales recuperadas = un mes de trabajo al año. Un MES. Por automatizar 3 cosas.",
     "¿Qué harías con una tarde libre extra cada semana? La respuesta está en tus tareas repetidas.",
     "La primera semana ahorras 30 minutos. Al mes, 5 horas. La automatización es interés compuesto.",
     "No prometo duplicar tu facturación: prometo devolverte las tardes de domingo sin ponerte al día.",
     "Media jornada semanal se esconde en tus tareas repetitivas. Ve a buscarla.",
     "Las 5 horas no aparecen de golpe: aparecen 15 minutos aquí, 20 allá. Por eso nadie las ve hasta que las suma.",
     "Un cliente recuperó 6 horas semanales automatizando respuestas. Las invirtió en vender. Facturó más. Fin.",
     "El tiempo que recuperas la primera semana ya paga el esfuerzo de montarlo. Lo demás es beneficio.",
     "5 horas para vender, para pensar, para tu familia o para NADA. Tuyas. Ese es el producto.",
     "Suma tus microtareas de la semana: el total te va a enfadar. Bien: el enfado es el primer paso.",
    ],
   },
   "Antes y después": {
    "pares": [
     ("El antes/después de automatizar no es sutil: se nota en la agenda del primer mes.", "Escríbeme AHORRA"),
     ("Los casos reales convencen más que la teoría: mira cómo cambia una semana tipo.", "Guárdalo"),
     ("El 'después' no es trabajar menos horas necesariamente: es que tus horas valgan más.", "¿Quieres tu antes/después?"),
    ],
    "hooks": [
     "Antes: 2 horas al día contestando lo mismo. Después: 20 minutos revisando lo que contestó la IA.",
     "Antes: presupuestos el fin de semana. Después: presupuestos en 10 minutos entre visitas.",
     "El lunes de María antes de automatizar y el de ahora: misma dueña, otra vida.",
     "Antes: 'no me da la vida'. Después: 'me sobra un hueco y no sé qué hacer con él'. Casos reales.",
     "Antes: cerraba el mes en 2 días. Después: el informe se hace solo y ella lo lee con un café.",
     "El cambio no fue contratar: fue automatizar lo tonto. Mismo equipo, doble capacidad.",
     "Antes: contestaba a las 23h con culpa. Después: el agente responde al momento y ella cena tranquila.",
     "6 meses de diferencia entre las dos fotos. La inversión: dos tardes y una suscripción.",
     "Su semana tenía 15 horas de tareas mecánicas. Hoy tiene 3. Las otras 12 son de crecer.",
     "Antes archivaba facturas los domingos. Ahora las archiva nadie: se archivan.",
     "El 'después' más repetido entre mis clientas no es 'gano más': es 'se me quitó un peso'.",
    ],
   },
   "Medir el ahorro": {
    "pares": [
     ("Lo que no se mide no se valora: apunta cuánto tardabas antes y cuánto tardas ahora. Sorpresa garantizada.", "Escríbeme AHORRA"),
     ("Medir el ahorro convierte 'la IA está bien' en 'la IA me devuelve 14 horas al mes'. Otra conversación.", "Guárdalo"),
     ("La métrica simple: horas/semana en la tarea, antes y después. Nada más hace falta.", "¿Lo has medido?"),
    ],
    "hooks": [
     "'La IA me ayuda bastante' — ¿cuánto es bastante? Medirlo cambia lo que decides después.",
     "Un truco: cronometra HOY tus 3 tareas más pesadas. Es la foto del 'antes' que agradecerás tener.",
     "Sin medir, la automatización parece un gasto. Midiendo, es la mejor inversión del año. Es la misma.",
     "Horas ahorradas × tu tarifa = el ROI de la IA en tu negocio. Una multiplicación, no un master.",
     "Mide una sola cosa: minutos por presupuesto (o por pedido, o por respuesta). Antes y después.",
     "El Excel más rentable de tu negocio tiene 3 columnas: tarea, tiempo antes, tiempo ahora.",
     "Medir también te dice qué NO automatizar: si no ahorra o empeora, fuera. Sin romanticismo.",
     "Las horas ahorradas invisibles se las come la nada. Las medidas se convierten en decisiones.",
     "Cada mes, un número: horas recuperadas. Ese número justifica (o no) cada herramienta que pagas.",
     "Tu intuición dice 'esto va mejor'. Tu medición dice '11 horas al mes'. La segunda convence al socio.",
     "No midas 20 cosas: mide el tiempo de las 3 tareas gordas. El resto es ruido.",
    ],
   },
   "En qué inviertes lo recuperado": {
    "pares": [
     ("Las horas recuperadas hay que asignarlas a algo, o la rutina se las vuelve a comer.", "Escríbeme TIEMPO"),
     ("El destino de tus horas libres es una decisión de negocio: venta, estrategia o vida. Elige a propósito.", "Guárdalo"),
     ("Automatizar sin decidir qué harás con el tiempo es vaciar un cajón para volver a llenarlo de trastos.", "¿A qué las dedicarás?"),
    ],
    "hooks": [
     "Recuperaste 5 horas ¿y las rellenaste de más tareas tontas? El problema no era el tiempo.",
     "Las horas que te devuelve la IA necesitan destino: ventas, estrategia o vida. Si no, se evaporan.",
     "La pregunta incómoda tras automatizar: ¿qué vas a hacer TÚ que la máquina no pueda?",
     "Hora recuperada e invertida en vender vale x10. Invertida en scroll, x0. Misma hora.",
     "El verdadero proyecto no es automatizar: es decidir en qué eres insustituible y darle esas horas.",
     "Clientas que usaron sus horas nuevas: una lanzó un servicio, otra subió precios, otra sale a las 17h. Todas bien.",
     "Bloquea en la agenda las horas recuperadas ANTES de que la rutina las reclame. Son tuyas, defiéndelas.",
     "Automatizar para trabajar lo mismo y facturar igual es hacer trampa al solitario.",
     "Tu negocio no necesita que hagas más cosas: necesita que hagas MEJOR 3 cosas. Ahora tienes tiempo.",
     "Las primeras horas libres dan hasta ansiedad. Tranquila: es el síntoma de que llevabas años sin margen.",
     "Tiempo libre no es el premio: es la materia prima de tu siguiente etapa. Úsala con intención.",
    ],
   },
  },
 },
 "Herramientas y flujos": {
  "afecta": "que la IA trabaje conectada a tu negocio real",
  "cierre": "{subtema} bien elegido no complica tu negocio: lo simplifica desde la primera semana, o sobra.",
  "subtemas": {
   "Automatizar sin programar": {
    "pares": [
     ("Hoy se automatiza con herramientas visuales: arrastrar, conectar, listo. Programar ya no es requisito.", "Escríbeme AUTOMATIZA"),
     ("El 'no sé programar' dejó de ser excusa: las automatizaciones se montan como un esquema, con cajitas.", "Guárdalo"),
     ("Si sabes describir la tarea paso a paso, esa descripción ES casi la automatización.", "¿Lo intentamos?"),
    ],
    "hooks": [
     "No hace falta saber programar para automatizar tu negocio. Hace falta empezar por una sola tarea.",
     "Las automatizaciones de hoy se montan con cajitas y flechas. Si haces esquemas, sabes hacer esto.",
     "'Cuando llegue un email con factura, guárdala en la carpeta y apúntala en la hoja' — eso ya es código. Visual.",
     "El no-code no es una moda: es que las herramientas por fin hablan idioma humano.",
     "Montar tu primera automatización visual: 40 minutos, la mitad viendo que era más fácil de lo que creías.",
     "Sabes usar canva sin ser diseñadora. Puedes automatizar sin ser programadora. Misma revolución.",
     "La IA además te guía: descríbele el flujo que quieres y te dice qué conectar con qué.",
     "Los flujos visuales se copian: hay miles hechos para negocios como el tuyo. Copiar y adaptar, permitido.",
     "Tu primera automatización debería avergonzarte de simple. Las catedrales vienen después.",
     "Programar era la barrera. Ahora la barrera es solo sentarse una tarde. Más barata, igual de efectiva.",
     "Si montaste un mueble de Ikea, puedes montar un flujo de trabajo. Con menos tornillos sobrantes.",
    ],
   },
   "Conectar tus apps": {
    "pares": [
     ("Tus herramientas ya se conocen entre sí: el email, el calendario, la facturación. Solo falta presentarlas.", "Escríbeme FLUJO"),
     ("Cada conexión entre dos apps elimina un copia-pega semanal para siempre.", "Guárdalo"),
     ("Antes de contratar otra herramienta, conecta bien las que ya pagas.", "¿Están conectadas?"),
    ],
    "hooks": [
     "Pagas 5 herramientas que no se hablan entre sí. Tú eres el mensajero entre ellas.",
     "El formulario, el calendario, el email y la factura pueden ser UNA cadena automática. Hoy son 4 islas.",
     "Tu CRM y tu email llevan años queriendo conectarse. Nadie les ha dado permiso.",
     "Cita agendada → confirmación enviada → recordatorio programado → factura preparada. Cero clics tuyos.",
     "Revisa los ajustes de tus apps: la palabra 'integraciones' esconde horas de tu vida.",
     "La mitad de tus copia-pega existen porque nadie dedicó UNA tarde a conectar dos herramientas.",
     "Conectar apps no es de técnicos: es marcar casillas en un menú que nunca abres.",
     "Cada app nueva que contratas pregunta primero: ¿se conecta con lo que ya tengo? Si no, cuesta el doble.",
     "El dato debería viajar solo: del formulario a la lista, de la lista al email, del email a la venta.",
     "Antes de cambiar de herramienta 'porque esta no hace X', mira si conectándola con otra, X aparece.",
     "Tus apps conectadas son un empleado silencioso. Desconectadas, son 5 recibos mensuales.",
    ],
   },
   "IA en atención al cliente": {
    "pares": [
     ("La IA en atención no sustituye tu cercanía: cubre las horas y preguntas donde tu cercanía no llegaba.", "Escríbeme IA"),
     ("Responder al momento, aunque sea para decir 'mañana te confirmo', ya te pone por delante de la mayoría.", "Guárdalo"),
     ("El cliente no quiere hablar con un robot... ni esperar 2 días a un humano. Hay un punto medio bien hecho.", "¿Cómo atiendes tú?"),
    ],
    "hooks": [
     "Tu cliente escribe a las 22h. La IA le responde bien al momento. Tú te enteras a las 9, con todo resuelto.",
     "El 70% de las preguntas de tus clientes son las mismas 12. Eso, atendido al instante, es una IA bien montada.",
     "Perder un cliente por contestar tarde duele más que cualquier debate sobre robots.",
     "La IA de atención bien hecha dice 'esto mejor te lo confirma María mañana'. Saber derivar es parte del oficio.",
     "Respuesta inmediata + tono tuyo + derivación inteligente: la atención híbrida que se puede montar YA.",
     "Tus horas de atención no escalan. Las preguntas de tus clientes, sí. Esa tijera la cierra la IA.",
     "El miedo a 'perder el trato humano' es sano: por eso la IA atiende lo mecánico y tú lo importante.",
     "Un asistente que conoce tus servicios, precios y horarios responde mejor que tu yo cansado de las 20h.",
     "La primera respuesta ya no compite en calidad: compite en velocidad. La calidad va en la segunda.",
     "Pon a la IA a atender UNA semana y mira el registro: aprenderás qué preguntan de verdad tus clientes.",
     "'Es que mis clientes son mayores y quieren llamar' — perfecto: la IA te libera tiempo para atender llamadas.",
    ],
   },
   "IA para organizarte": {
    "pares": [
     ("La IA también ordena por dentro: tu semana, tus notas, tus prioridades. No solo produce, organiza.", "Escríbeme IA"),
     ("Pedirle a la IA que te ordene el caos de tareas es de las formas más rápidas de recuperar foco.", "Guárdalo"),
     ("Tu asistente de organización cuesta 0€ extra: es la misma IA con otra pregunta.", "¿Se lo has pedido?"),
    ],
    "hooks": [
     "Pega tu lista de tareas en la IA y pide: 'ordénamela por impacto y ponme horario'. Pruébalo hoy.",
     "No le has pedido nunca a la IA que te ayude a priorizar el día. Es gratis y tarda 20 segundos.",
     "La IA como jefa de gabinete: le cuentas el caos y te devuelve un plan. Cada lunes.",
     "Tus notas de voz desordenadas, transcritas y convertidas en lista de acciones. Ese flujo existe.",
     "'¿Qué se me está olvidando?' — pregúntaselo a la IA con tu contexto delante. Da respuestas incómodas y útiles.",
     "El repaso semanal con IA: pegas lo que pasó, te devuelve lo que aprendiste y lo que toca. 10 minutos.",
     "Usas la IA para curiosear y nunca para organizar de verdad tu negocio. Justo al revés que sus mejores usos.",
     "Dictarle el plan del día mientras desayunas y recibirlo ordenado por prioridades: rutina real de 2 minutos.",
     "La IA no procrastina, no se agobia y no le tiene manía a ninguna tarea: por eso ordena mejor que tú hoy.",
     "Piensas que la IA es solo para escribir textos. Organizar tu caos se le da incluso mejor.",
     "Tu cabeza para decidir, la IA para recordar y ordenar. Ese reparto de papeles gana siempre.",
    ],
   },
   "Elegir herramienta": {
    "pares": [
     ("La mejor herramienta de IA es la que usarás de verdad: simple, conectada a lo tuyo y a tu medida.", "Escríbeme IA"),
     ("Elegir herramienta por hype es coleccionar suscripciones; elegir por tarea es resolver el negocio.", "Guárdalo"),
     ("Primero la tarea, luego la herramienta. Ese orden te ahorra dinero y frustración.", "¿Cuál necesitas tú?"),
    ],
    "hooks": [
     "No necesitas la IA más potente: necesitas la que resuelve TU tarea sin manual de instrucciones.",
     "Cada semana sale una IA 'revolucionaria'. Tu negocio necesita una que funcione, no la última.",
     "El orden correcto: primero define la tarea, luego busca herramienta. Todo el mundo lo hace al revés.",
     "Coleccionar suscripciones de IA no es transformación digital: es una fuga de 200€ al mes.",
     "Antes de pagar una IA nueva: ¿lo hace ya la que tienes? El 60% de las veces, sí.",
     "La demo enamora, el uso diario retrata: pide prueba gratis y hazle TU caso real, no el de la demo.",
     "Una herramienta que tu equipo no adopta es cara aunque sea gratis.",
     "Los agregadores de 'las 100 mejores IAs' abruman. Tu lista real necesita 3: texto, atención y flujos.",
     "Elige aburrido: la herramienta con años, soporte y clientes como tú gana a la novedad brillante.",
     "Si a la semana no la has vuelto a abrir, la respuesta es no. Cancela sin culpa y prueba otra.",
     "Herramienta buena = te la explican en 2 frases y en una tarde está funcionando con TUS datos.",
    ],
   },
  },
 },
}

def normaliza(s):
    return s[0].lower() + s[1:] if s else s

def guion_para(formato, hook, subtema, afecta):
    st = normaliza(subtema)
    if formato == "Reel":
        return (f'Gancho (0-2s): "{hook}". Desarrollo (3-15s): Explica cómo {st} afecta a {afecta}, '
                f'con un ejemplo concreto de negocio y sin jerga técnica. Cierre (16-20s): el primer paso práctico, en una frase, sin humo.')
    if formato == "Carrusel":
        return (f'Portada: "{hook}". Slides 2-6: desarrollar {st} en pasos, errores o claves concretas, '
                f'una idea por slide, siempre aterrizado a un negocio real. Slide de cierre: resumen + CTA.')
    return (f'Foto o imagen tuya trabajando/pantalla de la herramienta. Caption cercano sobre {st}, '
            f'con un caso real (sin datos de cliente) y el resultado en horas ahorradas.')

def hashtag_subtema(subtema):
    slug = (subtema.lower()
            .replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
            .replace("ñ","n"))
    slug = "".join(c for c in slug if c.isalnum())
    return "#" + slug

colas = {}
for pil, info in PILARES.items():
    cola = []
    for subtema, datos in info["subtemas"].items():
        hooks = datos["hooks"]
        pares = datos["pares"]
        for i, hook in enumerate(hooks):
            idea_c, cta = pares[i % len(pares)]
            cola.append((subtema, hook, idea_c, cta))
    colas[pil] = cola
    assert len(cola) >= 52, f"{pil} solo tiene {len(cola)} filas, hacen falta >=52"

pilares_orden = list(PILARES.keys())
punteros = {p: 0 for p in pilares_orden}

filas = []
mes_idx = 0
dia_mes = 1
total = 365
pil_i = 0
hooks_vistos = set()
for n in range(1, total + 1):
    pil = pilares_orden[pil_i % len(pilares_orden)]
    pil_i += 1
    cola = colas[pil]
    idx = punteros[pil] % len(cola)
    punteros[pil] += 1
    subtema, hook, idea_c, cta = cola[idx]
    info = PILARES[pil]
    formato = CICLO_FORMATO[(n - 1) % len(CICLO_FORMATO)]
    guion = guion_para(formato, hook, subtema, info["afecta"])
    cierre = info["cierre"].format(subtema=subtema)
    caption = f"{hook} {idea_c} {cierre}"
    hashtags = f"{HASHTAGS_BASE} {hashtag_subtema(subtema)}"
    mes_nombre, mes_dias = MESES[mes_idx]
    if dia_mes > mes_dias:
        mes_idx += 1
        dia_mes = 1
        mes_nombre, mes_dias = MESES[mes_idx]
    fila = {
        "dia": n, "formato": formato, "pilar": pil,
        "idea": f"{subtema} — {idea_c}",
        "hook": hook, "cta": cta, "guion": guion, "caption": caption,
        "hashtags": hashtags, "objetivo": pil, "mes": mes_nombre,
    }
    filas.append(fila)
    hooks_vistos.add(hook)
    dia_mes += 1

assert len(filas) == 365
print("hooks unicos:", len(hooks_vistos), "/", len(filas))

salida = "window.IDEAS_IA = " + json.dumps(filas, ensure_ascii=False) + ";\n"
cabecera = "// Banco de contenido — IA Y AUTOMATIZACIÓN (365 días).\n"
with open("datos-ideas-ia.js", "w", encoding="utf-8") as f:
    f.write(cabecera + salida)
print("OK ->", len(filas), "días")
