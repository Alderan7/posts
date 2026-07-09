# -*- coding: utf-8 -*-
"""
Genera datos-ideas-productividad.js — banco de 365 días para el nicho
"Productividad y Organización" (ayudar a dueños de negocio a llevar mejor
su agenda y estar más organizados). Mismo esquema que datos-ideas-personal.js
(dia/formato/pilar/idea/hook/cta/guion/caption/hashtags/objetivo/mes) para que
funcione con el motor ya existente (bancoIdeas/renderBanco/usarIdeaBanco).

Cada subtema tiene un POOL de "hooks" (muchos, cortos, cada uno una idea
distinta) y un pool pequeño de "pares" (idea_central, cta) que se reparten
en rotación. Así el HOOK —lo que de verdad se lee en pantalla— es único (o
casi) en los 365 días, igual que en datos-ideas-personal.js (365/365 hooks
únicos verificado), aunque el cta/caption sí se repita algo, como allí.
"""
import json

MESES = [("Julio",31), ("Agosto",31), ("Septiembre",30), ("Octubre",31),
         ("Noviembre",30), ("Diciembre",31), ("Enero",31), ("Febrero",28),
         ("Marzo",31), ("Abril",30), ("Mayo",31), ("Junio",30)]

CICLO_FORMATO = ["Reel","Carrusel","Reel","Post","Reel","Carrusel","Post"]
HASHTAGS_BASE = "#productividad #organizacion #dueñosdenegocio"

# ── Pilares: subtema -> {hooks:[...], pares:[(idea_central,cta), ...]} ────
PILARES = {
 "Agenda": {
  "afecta": "cómo se te va el día entero",
  "cierre": "{subtema} no se arregla con más horas: se arregla con una agenda que manda ella, no el WhatsApp.",
  "subtemas": {
   "Agenda desbordada": {
    "pares": [
     ("Sin una agenda que decides tú, decide el ruido de fuera.", "Escríbeme AGENDA"),
     ("Cuando no planificas, la semana pasa POR ti, no CONTIGO.", "Guárdalo"),
     ("Una agenda sana también tiene tiempo bloqueado para pensar, no solo para atender.", "¿Te pasa?"),
    ],
    "hooks": [
     "Tu agenda no la llevas tú. La lleva quien te escribe último.",
     "Miras el calendario del lunes y ya sientes cansancio.",
     "47 notificaciones antes de las 10 de la mañana.",
     "Tu agenda parece un Tetris que siempre pierdes.",
     "Llegas al viernes sin recordar en qué se te fue la semana.",
     "Tienes hueco para todo el mundo menos para ti.",
     "Aceptas reuniones porque decir que no incomoda.",
     "El primer imprevisto del día tira abajo todo lo planeado.",
     "Tienes la agenda llena y la sensación de no avanzar nada.",
     "Miras el móvil 80 veces al día sin darte cuenta.",
     "Vives apagando fuegos que otros encendieron por ti.",
     "Tu agenda de hoy la escribió el WhatsApp, no tú.",
     "Revisas la agenda de mañana y ya sabes que no vas a llegar a todo.",
    ],
   },
   "Reuniones": {
    "pares": [
     ("Una reunión sin próximos pasos claros es tiempo regalado, por útil que parezca.", "Guárdalo"),
     ("No todo necesita una reunión. Algunas cosas solo necesitan una pregunta clara.", "Cuéntame tu caso"),
     ("El tiempo de una reunión se expande hasta llenar el hueco que le dejas.", "¿De acuerdo?"),
    ],
    "hooks": [
     "Sales de la reunión sin saber quién hace qué ahora.",
     "3 reuniones seguidas y ni un minuto para respirar entre ellas.",
     "Convocas una reunión para lo que cabía en un mensaje.",
     "Nadie prepara la reunión, así que la reunión no prepara nada.",
     "Tu semana tiene más reuniones que horas para trabajar en lo que sale de ellas.",
     "La reunión duró una hora para decidir en cinco minutos.",
     "Sales agotada de reuniones que ni te tocaban a ti.",
     "Cada reunión sin acta se repite la semana que viene, casi igual.",
     "Programas reuniones antes de saber si de verdad hacen falta.",
     "Llevas tres reuniones esta semana que podían haber sido un audio de un minuto.",
     "Convocas a todo el equipo para algo que solo afecta a dos personas.",
     "Sales de la reunión con más dudas de las que tenías al entrar.",
    ],
   },
   "Interrupciones": {
    "pares": [
     ("Retomar el hilo después de una interrupción tarda más que la interrupción en sí.", "¿Te suena?"),
     ("Las interrupciones cortas suman jornadas enteras perdidas al mes.", "Escríbeme AGENDA"),
     ("El coste real de una interrupción no es su duración: es lo que tarda tu cabeza en volver.", "Cuéntamelo"),
    ],
    "hooks": [
     "Cada interrupción te cuesta más que el minuto que dura.",
     "Contestas el WhatsApp del negocio hasta en la cena.",
     "El 'tienes un minuto' de tu equipo nunca dura un minuto.",
     "Trabajas con el móvil boca arriba, vibrando cada dos minutos.",
     "Cada aviso de email te saca de lo que estabas haciendo.",
     "Dices 'ahora te atiendo' quince veces al día, a quince personas distintas.",
     "Una llamada de dos minutos te descoloca la tarde entera.",
     "Alguien te interrumpe 'un segundo' y se te va media hora de foco.",
     "Cada vez que te interrumpen, empiezas la tarea casi de cero otra vez.",
     "Tu jornada tiene más interrupciones que minutos de trabajo seguido.",
     "Alguien golpea la puerta 'solo una pregunta rápida' y se te va el hilo entero.",
    ],
   },
   "Bloques de tiempo": {
    "pares": [
     ("Lo que no se agenda, casi nunca se hace: se lo come lo que sí está agendado.", "Escríbeme AGENDA"),
     ("Bloquea primero lo que mueve el negocio. Lo demás encaja alrededor.", "Guárdalo"),
     ("Un bloque de tiempo realista empieza y termina; si no, no protege nada.", "Cuéntame tu caso"),
    ],
    "hooks": [
     "Sin bloques en el calendario, el día se llena solo de lo urgente.",
     "Reservas huecos para todo el mundo, menos para lo importante.",
     "Trabajas mejor por la mañana y aun así llenas la mañana de reuniones.",
     "Sin un bloque fijo, esa tarea importante lleva tres semanas 'para mañana'.",
     "Metes tareas de una hora en huecos de quince minutos.",
     "Tienes la mañana libre en el papel y llena en la práctica.",
     "Bloqueas dos horas para 'trabajo profundo' y las llenas de recados sueltos.",
     "Cada vez que planificas por bloques, algo 'urgente' te los rompe todos.",
     "Tienes tiempo bloqueado en el calendario que ni tú mismo respetas.",
    ],
   },
   "Fin de semana / desconexión": {
    "pares": [
     ("Desconectar el fin de semana no es pereza: es lo que te permite rendir el lunes.", "¿Te pasa?"),
     ("Un descanso a medias no recarga nada: solo aplaza el cansancio.", "Cuéntame tu caso"),
     ("Poner un límite de horario no te hace menos profesional: te hace más sostenible.", "¿De acuerdo?"),
    ],
    "hooks": [
     "Miras el correo del negocio en pijama, un domingo por la mañana.",
     "Tu cuerpo descansa el sábado. Tu cabeza, no.",
     "Vuelves de vacaciones más cansada que cuando te fuiste.",
     "El domingo por la tarde ya te pesa el lunes que viene.",
     "Contestas mensajes del negocio a las 23:00 de un sábado.",
     "Revisas el móvil del negocio nada más abrir los ojos, incluso en domingo.",
     "Te sientes culpable si un sábado no haces 'nada productivo'.",
     "Tu fin de semana empieza tarde porque el viernes acabas trabajando hasta las 20h.",
    ],
   },
  },
 },
 "Prioridades": {
  "afecta": "lo que de verdad avanza en tu negocio",
  "cierre": "{subtema} es la diferencia entre estar muy ocupada y estar avanzando de verdad.",
  "subtemas": {
   "Urgente vs importante": {
    "pares": [
     ("Lo urgente grita. Lo importante casi nunca lo hace, y por eso pierde.", "Escríbeme PRIORIDADES"),
     ("Estar ocupada todo el día no es lo mismo que haber avanzado en algo.", "Guárdalo"),
     ("Si vives resolviendo las urgencias ajenas, nunca llegas a las tuyas.", "¿Te pasa?"),
    ],
    "hooks": [
     "Llevas todo el día apagando fuegos y ni uno era tuyo.",
     "Acabas el día agotada y sin haber tocado lo que de verdad importa.",
     "Lo urgente de otros se convierte en tu urgencia, cada día.",
     "Pospones la tarea importante porque nunca parece urgente.",
     "Tu lista de tareas tiene 30 puntos y ninguno mueve la aguja.",
     "Confundes estar disponible con estar siendo productiva.",
     "Lo urgente de hoy te ha vuelto a robar el rato para lo importante.",
     "Terminas el día habiendo apagado fuegos ajenos y ninguno propio.",
     "Cada 'urgencia' de última hora te descuadra el plan de la semana entera.",
     "Le dedicas el doble de tiempo a lo que grita que a lo que de verdad importa.",
     "Si algo urge, se atiende. Si algo importa, casi nunca hay hueco.",
     "Contestas primero lo urgente y dejas lo importante para 'luego', otra vez.",
     "Un mensaje sin importancia te desvía más rápido que cualquier tarea clave.",
    ],
   },
   "Matriz de prioridades": {
    "pares": [
     ("Si no tienes clara la tarea número uno, cualquier cosa la sustituye.", "Escríbeme PRIORIDADES"),
     ("Cuando todo es prioridad, nada lo es. Elige una, máximo tres.", "Cuéntame tu caso"),
     ("No todas las tareas pesan lo mismo, aunque ocupen la misma línea en tu lista.", "Guárdalo"),
    ],
    "hooks": [
     "¿Sabrías decir, ahora mismo, cuál es TU tarea del día?",
     "Tienes 12 tareas 'importantes' hoy. Ninguna lo es de verdad.",
     "Tratas igual una llamada de cinco minutos que una decisión clave.",
     "Empiezas por lo fácil y dejas lo importante para 'cuando haya tiempo'.",
     "Tu día está lleno y aun así el negocio no avanza.",
     "Todo en tu lista lleva la etiqueta 'urgente', incluso lo que no lo es.",
     "Marcas 20 tareas como prioritarias y ninguna acaba haciéndose antes.",
     "Ordenas tu lista por lo primero que ves, no por lo que más importa.",
     "Le dedicas la misma energía a un email que a una decisión que cambia el mes.",
     "Tachas tareas fáciles todo el día y la difícil sigue igual que ayer.",
     "Terminas el día con la lista más corta pero con lo importante intacto.",
    ],
   },
   "Decir que no": {
    "pares": [
     ("Cada 'sí' que no quieres dar es un 'no' a tu propia agenda.", "Cuéntamelo"),
     ("Decir que no a tiempo es más barato que decir que sí y arrepentirte.", "Escríbeme PRIORIDADES"),
     ("Un 'no, ahora no puedo' bien dicho protege tu agenda y tu cabeza.", "Guárdalo"),
    ],
    "hooks": [
     "Dices que sí a todo por no quedar mal, y pagas tú.",
     "Aceptas ese cliente que sabes que no te conviene.",
     "Te cuesta más decir 'no puedo hoy' que quedarte hasta las 22h.",
     "Cada favor que aceptas sin pensarlo te quita hueco a ti.",
     "Sientes que decir que no te hace parecer menos disponible.",
     "Dijiste que sí sin mirar la agenda, y ahora no te cuadra nada.",
     "Aceptas un encargo más solo por no decepcionar a nadie.",
     "Te disculpas por decir que no, como si fuera un fallo tuyo.",
     "Cada vez que dices sí sin pensar, alguien más decide por ti.",
     "Te sientes aliviada las pocas veces que sí dices que no a tiempo.",
    ],
   },
   "Objetivos del mes": {
    "pares": [
     ("Sin un objetivo claro del mes, cualquier actividad parece progreso.", "Escríbeme PRIORIDADES"),
     ("Menos objetivos, bien elegidos, avanzan más que una lista imposible.", "Guárdalo"),
     ("Un objetivo sin revisión semanal es solo un buen propósito.", "¿Te pasa?"),
    ],
    "hooks": [
     "Llegas a fin de mes sin saber si avanzaste o solo estuviste ocupada.",
     "Te propones 15 metas el día 1 y no cierras ni tres.",
     "No revisas tus objetivos hasta que ya pasó el mes.",
     "Confundes estar ocupada con estar cerca de tu objetivo del mes.",
     "Empezaste el mes con una meta clara. Hoy ni te acuerdas cuál era.",
     "Tu objetivo del mes sigue en la nota donde lo escribiste el día 1, sin tocar.",
     "Mides el mes por lo cansada que acabas, no por lo que conseguiste.",
     "Cada mes te propones lo mismo y cada mes se queda a medias.",
     "Llegas al día 30 sin haber mirado ni una vez el objetivo que te pusiste.",
    ],
   },
   "La tarea que mueve el negocio": {
    "pares": [
     ("Casi siempre evitamos justo la tarea que más impacto tendría.", "Escríbeme PRIORIDADES"),
     ("Lo cómodo rara vez es lo que hace crecer un negocio.", "Guárdalo"),
     ("A veces avanzar no es hacer más, es decidir de una vez lo que llevas semanas rondando.", "Cuéntame tu caso"),
    ],
    "hooks": [
     "Hay UNA tarea que, si la hicieras hoy, cambiaría tu mes. Y la evitas.",
     "Pasas el día en tareas cómodas y evitas la incómoda que sí importa.",
     "Llevas semanas posponiendo esa llamada que abriría una puerta grande.",
     "Tu negocio necesita una decisión, no otra tarea más de la lista.",
     "Sabes exactamente qué tarea cambiaría el mes. Y hoy, otra vez, la esquivas.",
     "Esa tarea 'incómoda' de tu lista lleva ahí desde hace un mes entero.",
     "Prefieres ordenar la bandeja de entrada antes que tomar esa decisión pendiente.",
     "Haces diez tareas pequeñas para no enfrentarte a la única que de verdad importa.",
     "Sabes qué tarea da más miedo hacer. Justo esa es la que más falta hace.",
    ],
   },
  },
 },
 "Delegación": {
  "afecta": "cuánto puedes crecer sin quemarte",
  "cierre": "{subtema} no es soltar control: es dejar de ser el techo de tu propio negocio.",
  "subtemas": {
   "Hacerlo todo tú": {
    "pares": [
     ("Ese pensamiento es justo lo que te tiene atrapada en tareas de 5€ la hora.", "Escríbeme DELEGA"),
     ("Hacerlo todo tú no es compromiso: es un cuello de botella con tu nombre.", "Guárdalo"),
     ("Un negocio sano aguanta que su dueña se caiga un día sin caerse entero.", "Guárdalo"),
    ],
    "hooks": [
     "Si tú no lo haces, sientes que no se hace bien.",
     "Contestas tú cada mensaje, aunque tengas equipo para hacerlo.",
     "Te vas de vacaciones con el portátil 'por si acaso'.",
     "Sigues haciendo tareas que ya podrías haber soltado hace un año.",
     "Revisas cada detalle porque 'nadie lo hace como tú'.",
     "Tu negocio depende tanto de ti que ni puedes enfermar tranquila.",
     "Sigues facturando, limpiando y atendiendo tú misma, todo a la vez.",
     "Haces tareas de 5€ la hora mientras las de 500€ esperan en la lista.",
     "Si te pones mala un día, tu negocio entero se para contigo.",
     "Llevas años diciendo 'ya delegaré cuando tenga más tiempo'.",
     "Tu equipo te pregunta cosas que ya deberían saber resolver solos.",
     "Prefieres quedarte hasta tarde tú sola antes que explicarle la tarea a alguien.",
     "Te cuesta imaginar tu negocio funcionando un solo día sin ti detrás.",
     "Sigues abriendo tú la tienda cada mañana, aunque ya no deberías.",
    ],
   },
   "Confiar en el equipo": {
    "pares": [
     ("Si rehaces todo lo que delegas, en realidad nunca delegaste.", "Escríbeme DELEGA"),
     ("La confianza en el equipo empieza por instrucciones claras, no por fe ciega.", "Guárdalo"),
     ("Soltar lo importante, poco a poco, es cómo un equipo crece de verdad.", "Cuéntame tu caso"),
    ],
    "hooks": [
     "Delegas la tarea y luego la rehaces tú entera.",
     "No confías en tu equipo porque nunca les explicaste bien qué esperas.",
     "Corriges en público un error que podías haber hablado en privado.",
     "Te cuesta soltar tareas 'importantes' aunque tengas quien pueda con ellas.",
     "Le pides a tu equipo iniciativa y luego criticas cada decisión que toman.",
     "Delegaste la tarea, pero sigues mirando por encima del hombro cada hora.",
     "Tu equipo deja de proponer ideas porque ya sabe que las vas a cambiar todas.",
     "Le das una tarea a tu equipo y a los diez minutos ya estás preguntando cómo va.",
     "Confías en tu equipo para lo pequeño, pero nunca para lo que de verdad importa.",
     "Dices que confías en tu equipo, pero revisas cada cosa como si no lo hicieras.",
     "Contratas talento bueno y luego no le dejas decidir nada por sí mismo.",
    ],
   },
   "Documentar procesos": {
    "pares": [
     ("Lo que solo está en tu cabeza, se pierde contigo cada vez que faltas.", "Escríbeme DELEGA"),
     ("Un proceso escrito una vez se explica cero veces más.", "Guárdalo"),
     ("Documentar 20 minutos hoy ahorra horas de explicaciones el resto del año.", "¿Te pasa?"),
    ],
    "hooks": [
     "Si te fueras un mes, ¿alguien sabría cómo haces las cosas?",
     "Explicas la misma tarea por tercera vez este mes.",
     "No tienes ni un solo checklist para lo que repites cada semana.",
     "Cada nueva persona del equipo tarda semanas en 'coger el ritmo'.",
     "Todo tu proceso vive en tu cabeza, en ningún otro sitio.",
     "Explicaste ese proceso de palabra tres veces y aún se hace distinto cada vez.",
     "Si mañana faltas, nadie sabría por dónde seguir tu trabajo.",
     "Tienes procesos que funcionan de maravilla y que nunca pusiste por escrito.",
     "Cada persona nueva aprende las cosas de una forma distinta, a su manera.",
     "Un cliente pregunta algo que ya has respondido cien veces, de palabra.",
     "Tu 'manual de empresa' cabe entero en tu cabeza, y en ningún otro sitio.",
    ],
   },
   "Contratar ayuda": {
    "pares": [
     ("Una hora de tu tiempo bien pagada a otra persona te libera para lo que solo tú puedes hacer.", "Escríbeme DELEGA"),
     ("A veces contratar ayuda es justo lo que te falta para llegar a esos ingresos.", "Guárdalo"),
     ("Lo que a ti te cuesta horas, a otra persona especializada le cuesta minutos.", "¿De acuerdo?"),
    ],
    "hooks": [
     "Piensas que contratar ayuda es un gasto, no una inversión de tiempo.",
     "Llevas meses diciendo 'cuando tenga más ingresos contrato ayuda'.",
     "Sigues haciendo tú las tareas administrativas que odias.",
     "Calculas el coste de contratar y nunca el coste de no hacerlo.",
     "Sigues sin pedir ayuda porque 'total, ya casi lo tengo controlado'.",
     "Rechazas más trabajo del que puedes asumir tú sola, en vez de sumar manos.",
     "Te asusta más pagar una nómina que seguir perdiendo horas tú misma.",
    ],
   },
   "Soltar el control": {
    "pares": [
     ("Delegar de verdad implica soltar también el control minuto a minuto.", "Escríbeme DELEGA"),
     ("Si supervisar te cuesta más que ejecutar, no estás delegando: estás controlando.", "Guárdalo"),
     ("Soltar control no es soltar estándares: es soltar la necesidad de hacerlo tú todo.", "¿Te pasa?"),
    ],
    "hooks": [
     "Revisas cada tarea delegada como si aún fuera tuya.",
     "Te cuesta más vigilar la tarea que hacerla tú misma.",
     "Sientes que perder el control es perder calidad.",
     "Pides que te copien en cada email 'solo para estar al tanto'.",
     "Te cuesta irte a dormir sin haber revisado lo que hizo tu equipo hoy.",
     "Necesitas aprobar hasta la decisión más pequeña de tu equipo.",
     "Sueltas la tarea pero no sueltas la ansiedad de cómo va a salir.",
     "Prefieres hacerlo tú 'para asegurarte' antes que dejar que otro se equivoque y aprenda.",
     "Sigues llevando tú las llaves de todo, literal y figuradamente.",
    ],
   },
  },
 },
 "Foco": {
  "afecta": "lo que consigues acabar cada día",
  "cierre": "{subtema} no se soluciona con fuerza de voluntad: se soluciona quitando fricción antes de empezar.",
  "subtemas": {
   "Multitarea": {
    "pares": [
     ("Nadie hace tres cosas a la vez de verdad: solo las hace mal, tres veces.", "Escríbeme FOCO"),
     ("La multitarea no ahorra tiempo: lo reparte peor entre más cosas a medias.", "Guárdalo"),
     ("Empezar mucho y terminar poco cansa igual que trabajar de verdad, pero rinde menos.", "Cuéntame tu caso"),
    ],
    "hooks": [
     "Contestas el móvil, escribes un email y 'escuchas' una llamada. A la vez.",
     "Saltas de tarea en tarea y no terminas ninguna del todo.",
     "Tienes 12 pestañas abiertas y ninguna con tu atención completa.",
     "Empiezas cinco tareas antes de comer y acabas media.",
     "Contestas mensajes mientras 'trabajas' en otra cosa distinta.",
     "Tienes tres tareas abiertas a la vez y ninguna avanza de verdad.",
     "Crees que haces más cosas a la vez. En realidad, haces todas peor.",
     "Cambias de tarea cada dos minutos y te preguntas por qué cunde tan poco el día.",
     "Tienes el email abierto mientras atiendes una llamada y escribes un mensaje.",
     "Presumes de saber hacer diez cosas a la vez. Ninguna sale como debería.",
     "Vas de una tarea a otra sin darte cuenta, como si tuvieras diez pestañas mentales abiertas.",
     "Terminas el día con la sensación de haber hecho mucho y avanzado poco.",
    ],
   },
   "Distracciones (móvil/redes)": {
    "pares": [
     ("El móvil no roba veinte minutos: roba la concentración que tarda en volver.", "Escríbeme FOCO"),
     ("Ese gesto automático es la fuga de foco más silenciosa del día.", "Guárdalo"),
     ("Cada micro-distracción tiene un coste de reinicio que no ves, pero pagas.", "¿Te pasa?"),
    ],
    "hooks": [
     "Coges el móvil 'un momento' y se te van veinte minutos.",
     "Miras el móvil sin ni siquiera saber por qué lo cogiste.",
     "Abres Instagram '2 minutos' entre tarea y tarea. Nunca son 2.",
     "Trabajas con el teléfono a la vista, aunque no lo mires.",
     "Compruebas el móvil antes de terminar la frase que estabas escribiendo.",
     "Cada notificación te saca del hilo, aunque no la abras.",
     "Sientes la vibración del móvil y ya perdiste el foco, la mires o no.",
     "Desbloqueas el móvil 'para mirar la hora' y acabas en el buzón de mensajes.",
     "El scroll infinito te traga veinte minutos que juraste que serían dos.",
     "Silencias el móvil un rato y a los cinco minutos ya lo has vuelto a activar.",
     "Cada vez que te aburres un segundo, el móvil aparece solo en tu mano.",
    ],
   },
   "Trabajo profundo": {
    "pares": [
     ("El trabajo que de verdad mueve el negocio necesita tiempo sin cortes, no huecos sueltos.", "Escríbeme FOCO"),
     ("El trabajo profundo empieza por proteger el silencio, no solo el horario.", "Guárdalo"),
     ("Reserva tus horas de más energía para lo que de verdad requiere tu cabeza.", "¿De acuerdo?"),
    ],
    "hooks": [
     "No recuerdas la última vez que trabajaste 90 minutos sin interrupciones.",
     "Reservas 'tiempo para pensar' y lo primero que haces es mirar el móvil.",
     "Tu mejor hora del día se te va en tareas que podría hacer cualquiera.",
     "Necesitas silencio real para pensar, y llevas semanas sin encontrarlo.",
     "Tu trabajo más importante siempre queda para cuando ya no tienes energía.",
     "Cada vez que empiezas a concentrarte, algo o alguien te corta el hilo.",
     "Sabes qué tarea necesita tu mejor concentración y la dejas para el peor momento.",
     "Tardas más en 'entrar en calor' con una tarea que en hacerla de verdad.",
     "Confundes estar sentada trabajando con estar de verdad concentrada.",
     "Cada bloque de foco que te propones dura la mitad de lo planeado.",
    ],
   },
   "Empezar y no acabar": {
    "pares": [
     ("Cerrar una cosa da más impulso que empezar cinco a la vez.", "Escríbeme FOCO"),
     ("El último 20% de una tarea suele ser el que más se posterga, y el que más importa.", "Guárdalo"),
     ("El negocio no crece con ideas empezadas: crece con cosas terminadas.", "¿Te pasa?"),
    ],
    "hooks": [
     "Tienes cinco proyectos a medias y ninguno cerrado.",
     "Esa tarea lleva 'casi terminada' tres semanas.",
     "Te motiva empezar cosas nuevas más que terminar las viejas.",
     "Abres un proyecto nuevo antes de cerrar el que tenías a medias.",
     "Tu carpeta de 'proyectos en marcha' crece más rápido que la de 'terminados'.",
     "Te emociona el primer día de un proyecto y te aburre el último tramo.",
     "Tienes más ideas empezadas que horas del día para acabar ni una.",
     "Cambias de proyecto en cuanto el que tienes entre manos se pone cuesta arriba.",
     "Lo que más ilusión te hace es la idea nueva, no terminar la de siempre.",
     "Tu lista de 'pendientes de cerrar' no deja de crecer mes a mes.",
    ],
   },
   "Ambiente de trabajo": {
    "pares": [
     ("Un espacio desordenado le añade fricción mental a cada tarea, aunque no lo notes.", "Escríbeme FOCO"),
     ("El ambiente no solo distrae: agota, incluso cuando crees que te has acostumbrado.", "Guárdalo"),
     ("A veces el problema no es el sitio: es no haber decidido dónde SÍ te concentras.", "¿De acuerdo?"),
    ],
    "hooks": [
     "Tu mesa de trabajo tiene más caos que tu agenda.",
     "Trabajas rodeada de ruido y ya ni te das cuenta.",
     "Cambias de sitio diez veces buscando 'concentrarte mejor'.",
     "Tienes tantas cosas a la vista que tu cabeza nunca descansa del todo.",
     "Tu escritorio digital tiene tantos archivos sueltos como tu mesa real.",
     "Trabajas con la tele o la música de fondo 'para hacer algo de ruido'.",
     "Tienes tantas cosas apiladas en la mesa que ya no sabes qué hay debajo.",
     "Cambias de silla, de luz y de postura buscando algo que en realidad no está ahí.",
     "Tu espacio de trabajo cambia cada día porque nunca decidiste uno fijo.",
    ],
   },
  },
 },
 "Sistemas": {
  "afecta": "que tu negocio no dependa solo de ti",
  "cierre": "{subtema} es lo que separa un negocio que funciona de uno que sobrevive a base de memoria.",
  "subtemas": {
   "Checklists": {
    "pares": [
     ("La memoria falla incluso con lo que haces siempre. Un checklist no falla.", "Escríbeme SISTEMAS"),
     ("Lo que no está escrito compite por espacio con todo lo demás en tu cabeza.", "Guárdalo"),
     ("Un checklist simple convierte un error en algo que solo pasa una vez.", "¿Te pasa?"),
    ],
    "hooks": [
     "Se te olvidó un paso que llevas años haciendo. Otra vez.",
     "Cada vez confías más en 'ya me acordaré' y menos en apuntarlo.",
     "Repites un error que ya habías cometido el mes pasado.",
     "No tienes ni una lista para lo que repites cada semana en el negocio.",
     "Confías en tu memoria para tareas que haces solo una vez al mes.",
     "Cada vez que se te olvida un paso, prometes apuntarlo. Y no lo haces.",
     "Cada mes se te pasa el mismo pago porque nadie te lo recuerda a tiempo.",
     "Improvisas de memoria un proceso que ya deberías tener escrito hace tiempo.",
     "Descubres el fallo justo cuando ya es tarde para corregirlo sin coste.",
     "Cada nuevo empleado comete el mismo error que ya evitó el anterior, por no escribirlo.",
     "Tu cabeza hace de checklist para veinte procesos distintos, todos a la vez.",
    ],
   },
   "Rutinas": {
    "pares": [
     ("Decidir cada mañana desde cero gasta energía que podrías ahorrar con una rutina fija.", "Escríbeme SISTEMAS"),
     ("Una rutina simple, aunque imperfecta, gana siempre a un plan perfecto que no sigues.", "Guárdalo"),
     ("Un buen cierre de día decide con qué cabeza empiezas el siguiente.", "Cuéntame tu caso"),
    ],
    "hooks": [
     "Cada día decides desde cero cómo vas a organizarte.",
     "Tu día ideal existe solo en tu cabeza, nunca en la práctica.",
     "Empiezas el día mirando el móvil en la cama.",
     "No tienes un cierre de jornada: simplemente dejas de trabajar, agotada.",
     "Los primeros 10 minutos del día marcan el tono de las diez horas siguientes.",
     "Cada mañana improvisas un plan que no sobrevive a la primera hora.",
     "Tu rutina de la mañana depende de cómo te levantaste, no de un plan fijo.",
     "Cierras el ordenador sin saber muy bien con qué te vas a encontrar mañana.",
     "Cada semana empiezas de cero, sin un ritual que te ponga en marcha.",
     "Tu rutina 'ideal' solo dura hasta el primer imprevisto del lunes.",
     "No tienes ni un solo hábito fijo que se repita igual cada día laborable.",
    ],
   },
   "Herramientas digitales": {
    "pares": [
     ("Tres sistemas a medias pesan más que uno solo bien usado.", "Escríbeme SISTEMAS"),
     ("La mejor herramienta es la que de verdad usas, no la más completa.", "Guárdalo"),
     ("Cambiar de herramienta no arregla la falta de un sistema detrás.", "¿De acuerdo?"),
    ],
    "hooks": [
     "Apuntas tareas en tres sitios distintos y no confías en ninguno.",
     "Tienes la app de tareas perfecta. Y no la abres desde hace un mes.",
     "Buscas la app perfecta en vez de usar bien la que ya tienes.",
     "Cambias de app de organización cada dos meses, sin llegar a dominar ninguna.",
     "Pagas tres herramientas distintas y usas de verdad solo media de una.",
     "Configuraste esa app hace meses y nunca la volviste a tocar.",
     "Tienes suscripciones activas de herramientas que ni recuerdas para qué eran.",
     "Cada vez que algo falla, culpas a la herramienta y no a cómo la usas.",
     "Sigues anotando a mano lo que tu propia herramienta ya podría recordarte sola.",
     "Probaste tres apps de organización este año y ninguna llegó a la segunda semana.",
    ],
   },
   "Procesos repetibles": {
    "pares": [
     ("Sin un proceso repetible, cada caso te cuesta el doble de energía que debería.", "Escríbeme SISTEMAS"),
     ("Un proceso claro no te quita creatividad: te da un punto de partida fiable.", "Guárdalo"),
     ("Lo que funcionó una vez, conviértelo en plantilla para la próxima.", "Cuéntame tu caso"),
    ],
    "hooks": [
     "Cada nuevo cliente empieza un proceso distinto, inventado sobre la marcha.",
     "Tu forma de trabajar cambia según el día y el humor.",
     "Ya hiciste esto bien una vez, pero no lo convertiste en plantilla.",
     "Cada proyecto empieza de cero, como si el anterior no hubiera existido.",
     "Improvisas cada vez algo que ya resolviste bien hace meses.",
     "Cada presupuesto que envías tiene un formato distinto al anterior.",
     "Resuelves el mismo problema de cliente de una forma diferente cada vez.",
     "No tienes ni una plantilla para lo que haces una y otra vez, cliente tras cliente.",
     "Tu mejor proceso vive solo en tu cabeza, y cambia según el día que tengas.",
     "Cada miembro del equipo resuelve la misma tarea de una manera distinta.",
    ],
   },
   "Automatización simple": {
    "pares": [
     ("Si lo repites más de tres veces, probablemente se puede automatizar.", "Escríbeme SISTEMAS"),
     ("Automatizar lo repetitivo no es de empresa grande: es de cabeza que valora su tiempo.", "Guárdalo"),
     ("La automatización más simple es la que ya existe en las herramientas que ya usas.", "¿De acuerdo?"),
    ],
    "hooks": [
     "Escribes a mano la misma respuesta por décima vez esta semana.",
     "Copias y pegas datos de un sitio a otro, cada semana, a mano.",
     "Piensas que automatizar es complicado y ni lo has probado.",
     "Envías el mismo mensaje de seguimiento, letra por letra, cada vez.",
     "Haces a mano un cálculo que tu propia hoja de cálculo podría hacer sola.",
     "Rellenas el mismo formulario, campo a campo, para cada cliente nuevo.",
     "Actualizas a mano una hoja que podría llenarse sola con lo que ya tienes.",
     "Mandas recordatorios de pago uno a uno, escritos de cero cada vez.",
     "Programas manualmente publicaciones que podrían salir solas cada semana.",
     "Revisas a mano algo que un simple filtro automático haría en tu lugar.",
    ],
   },
  },
 },
 "Energía": {
  "afecta": "cuánto aguantas sin quemarte",
  "cierre": "{subtema} importa tanto como el tiempo: puedes tener horas libres y cero energía para usarlas.",
  "subtemas": {
   "Descanso": {
    "pares": [
     ("El descanso no es un premio por trabajar mucho: es lo que te permite trabajar bien.", "Escríbeme ENERGÍA"),
     ("Mirar el móvil no descansa la cabeza: solo la cambia de estímulo.", "Guárdalo"),
     ("Sin pausas, rindes menos las últimas horas de lo que crees.", "¿Te pasa?"),
    ],
    "hooks": [
     "Duermes seis horas y las llamas 'suficientes' porque no te queda otra.",
     "Tu único descanso es el scroll del móvil antes de dormir.",
     "No paras en todo el día 'porque hay mucho que hacer'.",
     "Comes delante del ordenador casi todos los días de la semana.",
     "Llamas 'descanso' a cambiar de pantalla, no a parar de verdad.",
     "Te sientes culpable si te sientas cinco minutos sin hacer nada.",
     "Confundes parar con perder el tiempo, aunque el cuerpo te pida frenar.",
     "Sales a 'desconectar' con el móvil del negocio en el bolsillo.",
     "Duermes mal porque tu cabeza sigue repasando la lista de mañana.",
     "Aplazas el descanso 'para cuando esté todo terminado'. Nunca lo está.",
    ],
   },
   "Burnout": {
    "pares": [
     ("Cuando hasta lo que te gustaba pesa, tu cuerpo te está avisando de algo.", "Escríbeme ENERGÍA"),
     ("La irritabilidad constante suele ser cansancio acumulado, no carácter.", "Guárdalo"),
     ("Esa temporada nunca termina sola. Hay que decidir parar, no esperar a poder.", "¿De acuerdo?"),
     ("Si tu negocio no aguanta que pares un día, el problema no es parar: es cómo está montado.", "Cuéntame tu caso"),
    ],
    "hooks": [
     "Ya no disfrutas lo que antes te encantaba de tu negocio.",
     "Te irritas por cosas pequeñas que antes ni notabas.",
     "Llevas meses diciendo 'en cuanto pase esta temporada, descanso'.",
     "Sientes que si paras un día, todo se derrumba.",
     "Te cuesta ilusionarte con algo que hace un año te motivaba muchísimo.",
     "Notas que te agotas por cosas que antes ni te movían la aguja.",
     "Te levantas ya cansada, antes incluso de empezar el día.",
     "Cada vez te cuesta más encontrar sentido a tareas que antes hacías con gusto.",
     "Sientes que das más de lo que te queda, cada semana un poco más.",
     "Notas un nudo en el estómago solo con pensar en abrir el ordenador.",
     "Te tomas un día libre y pasas la mitad pensando en el trabajo igualmente.",
    ],
   },
   "Horario y límites": {
    "pares": [
     ("Sin una hora de cierre, el trabajo se expande hasta ocupar todo el tiempo que le des.", "Escríbeme ENERGÍA"),
     ("Un horario con límites no te hace menos disponible: te hace más sostenible.", "Guárdalo"),
     ("Poner una hora de cierre, aunque la incumplas a veces, cambia cómo vives el resto del día.", "¿Te pasa?"),
    ],
    "hooks": [
     "Trabajas 'hasta que acabe', y nunca acaba.",
     "Contestas mensajes del negocio a cualquier hora, cualquier día.",
     "No tienes hora de cierre, así que el día 'de trabajo' dura 14 horas.",
     "Tu jornada empieza a las 8 y no tiene hora fija de terminar.",
     "Nunca has decidido a qué hora dejas de estar 'disponible' para el negocio.",
     "Cenas con el móvil al lado 'por si escribe alguien del trabajo'.",
     "Tu pareja o tu familia ya sabe que 'un momento' significa media hora.",
     "No tienes un límite claro entre tu vida y tu negocio, y ambos lo notan.",
     "Sigues trabajando aunque ya haya pasado tu hora de cierre, otra vez.",
     "Contestas un mensaje de trabajo en medio de una comida familiar.",
    ],
   },
   "Energía vs tiempo": {
    "pares": [
     ("El tiempo libre sin energía no sirve de mucho: gestiona las dos cosas, no solo el reloj.", "Escríbeme ENERGÍA"),
     ("Ordena tu día por energía, no solo por horario: rendirás el doble en menos tiempo.", "Guárdalo"),
     ("Cansancio no es sinónimo de esfuerzo bien invertido. A veces solo es desorden.", "¿De acuerdo?"),
    ],
    "hooks": [
     "Tienes la tarde libre y cero energía para aprovecharla.",
     "Haces las tareas que más energía piden justo cuando menos tienes.",
     "Confundes estar cansada con estar siendo productiva.",
     "Tienes tiempo de sobra algunos días y la cabeza demasiado agotada para usarlo.",
     "Guardas la tarea más difícil para la última hora, cuando ya no te queda energía.",
     "Tienes energía de sobra por la mañana y la gastas en tareas sin importancia.",
     "Planificas tu semana por horas disponibles, nunca por energía disponible.",
     "Te exiges el mismo rendimiento a las 9 de la mañana que a las 7 de la tarde.",
     "Sientes que 'no rindes' cuando en realidad solo te falta energía, no tiempo.",
     "Confundes tener la agenda vacía con tener la cabeza descansada.",
    ],
   },
   "Días buenos y malos": {
    "pares": [
     ("Un mal día no invalida el sistema. Solo es un mal día: mañana se retoma.", "Escríbeme ENERGÍA"),
     ("No todos los días dan lo mismo, y planificar como si fuera así te pasa factura.", "Guárdalo"),
     ("Un sistema bueno también sobrevive a los días malos, no solo a los buenos.", "¿Te pasa?"),
    ],
    "hooks": [
     "Un mal día te hace sentir que todo el sistema falla.",
     "Te exiges rendir igual todos los días del mes.",
     "Un día flojo te hace abandonar la rutina entera, otra vez.",
     "Planificas cada día como si fueras a tener la mejor energía del mundo.",
     "Un solo mal día te hace tirar la toalla con todo lo que llevabas construido.",
     "Te machacas por no rendir igual un lunes cualquiera que en tu mejor semana.",
     "Comparas tu peor día con el mejor día de otra persona en redes.",
     "Un mal día te hace posponer todo lo bueno que ya tenías planeado.",
     "Necesitas que todos los días salgan perfectos para sentir que 'vas bien'.",
     "Un imprevisto te descoloca el día entero, aunque el resto de la semana vaya bien.",
     "Te cuesta reconocer un buen día si no acabaste agotada.",
    ],
   },
  },
 },
 "Herramientas": {
  "afecta": "cuánto tiempo recuperas cada semana",
  "cierre": "{subtema} bien elegido no complica tu día: te lo simplifica desde la primera semana.",
  "subtemas": {
   "Apps de calendario": {
    "pares": [
     ("Un solo calendario, bien llevado, vale más que tres a medias.", "Escríbeme HERRAMIENTAS"),
     ("Cada paso extra entre agendar y recordar es una oportunidad de que se pierda.", "Guárdalo"),
     ("Los recordatorios no son para cuando fallas: son para no depender de acordarte siempre.", "¿Te pasa?"),
    ],
    "hooks": [
     "Tienes tres calendarios distintos y ninguno actualizado del todo.",
     "Agendas citas a mano y luego se te olvida pasarlas al móvil.",
     "No usas los recordatorios porque 'ya me acuerdo yo'.",
     "Tu calendario del móvil y el de la oficina nunca dicen lo mismo.",
     "Confirmas citas por tres canales distintos y aun así se te cruzan.",
     "Das dos citas a la misma hora porque miraste el calendario equivocado.",
     "Apuntas la cita en una libreta que luego se queda en casa.",
     "Tu calendario tiene huecos libres que en realidad ya están comprometidos.",
     "Programas una cita y se te olvida bloquear el tiempo de preparación antes.",
     "Confías en la memoria para citas que deberían estar en un calendario, no en tu cabeza.",
    ],
   },
   "Gestores de tareas": {
    "pares": [
     ("Lo que no sale de tu cabeza sigue ocupando espacio mental, aunque no lo hagas.", "Escríbeme HERRAMIENTAS"),
     ("Un gestor de tareas solo funciona si se convierte en costumbre, no en propósito de año nuevo.", "Guárdalo"),
     ("Un sistema de tareas centralizado evita que se te escape justo lo urgente.", "¿De acuerdo?"),
    ],
    "hooks": [
     "Tu lista de tareas vive en la cabeza, no en ningún sitio.",
     "Tienes una app de tareas y la usas solo la primera semana de cada mes.",
     "Anotas tareas en post-its que luego se pierden por la mesa.",
     "Tienes tareas apuntadas en cuatro sitios y ninguno es 'el bueno'.",
     "Empiezas el día sin saber cuál era la tarea que ayer marcaste como urgente.",
     "Tu lista de tareas mezcla lo del negocio con lo de casa, todo revuelto.",
     "Marcas una tarea como hecha y a la semana descubres que se te olvidó un paso.",
     "Tienes tareas de hace dos meses que siguen ahí, intactas, sin tocar.",
     "Cada vez que abres tu lista de tareas sientes más agobio que claridad.",
     "Escribes la tarea en un papel que después no vuelves a mirar.",
    ],
   },
   "Automatizaciones": {
    "pares": [
     ("Ese email que repites siempre igual es el primer candidato a automatizar.", "Escríbeme HERRAMIENTAS"),
     ("Muchas automatizaciones simples ya están a un clic, sin saberlo usas solo la mitad de tus apps.", "Guárdalo"),
     ("Antes de contratar más ayuda, revisa si tu herramienta actual ya lo resuelve.", "Cuéntame tu caso"),
    ],
    "hooks": [
     "Mandas el mismo email de bienvenida, a mano, cada vez.",
     "Nunca has probado a conectar tus propias herramientas entre sí.",
     "Haces a mano tareas que tu propio software ya podría hacer solo.",
     "Rellenas la misma plantilla a mano, cliente tras cliente.",
     "Tu web recoge datos que luego pasas a mano a otra hoja distinta.",
     "Contestas la misma pregunta frecuente, por privado, mensaje a mensaje.",
     "Subes cada foto y cada texto a mano en cada red social, una por una.",
     "Avisas manualmente a cada cliente del mismo cambio de horario.",
     "Pasas horas al mes haciendo tareas que ya existen como plantilla en tu propio software.",
     "Programas cada recordatorio de cobro a mano, cliente a cliente, mes a mes.",
    ],
   },
   "IA para organizarte": {
    "pares": [
     ("La IA no sustituye tu criterio: te libera del trabajo repetitivo alrededor de él.", "Escríbeme IA"),
     ("Pedirle a la IA que ordene tu caos de tareas es de las formas más rápidas de recuperar foco.", "Guárdalo"),
     ("No hace falta ser técnica: hace falta empezar por una tarea pequeña y repetitiva.", "¿De acuerdo?"),
    ],
    "hooks": [
     "Sigues escribiendo tú cada respuesta repetida, mensaje a mensaje.",
     "No le has pedido nunca a la IA que te ayude a priorizar el día.",
     "Te sigue dando respeto usar la IA para organizar tu negocio.",
     "Podrías pedirle a la IA que te ordene la semana, y sigues haciéndolo tú a mano.",
     "Usas la IA para curiosear y nunca para organizar de verdad tu negocio.",
     "Le preguntas a la IA curiosidades, pero nunca 'organízame la semana'.",
     "Piensas que la IA es solo para escribir textos, no para poner orden en tu caos.",
     "Sigues clasificando tú a mano cientos de mensajes que la IA podría ordenar.",
     "No le has dado ni una vez a la IA tu lista de tareas para que la priorice.",
     "Crees que pedirle ayuda a la IA es 'hacer trampa' en vez de trabajar mejor.",
    ],
   },
   "Notas y segundo cerebro": {
    "pares": [
     ("Una idea no anotada en el momento, casi siempre, se pierde para siempre.", "Escríbeme HERRAMIENTAS"),
     ("Un 'segundo cerebro' (notas organizadas) libera a tu cabeza de tener que recordarlo todo.", "Guárdalo"),
     ("De nada sirve anotar todo si luego no lo encuentras cuando lo necesitas.", "¿Te pasa?"),
    ],
    "hooks": [
     "Tienes ideas geniales que se te olvidan a los diez minutos.",
     "Tu cabeza intenta recordar cien cosas a la vez, todo el día.",
     "Buscas esa nota importante entre cien notas sueltas sin orden.",
     "Apuntas ideas en cinco apps distintas y no revisas ninguna después.",
     "Tuviste la idea perfecta en la ducha. Ya no la recuerdas.",
     "Escribes la idea en una servilleta que después acaba en la basura.",
     "Confías en 'ya me acordaré' para ideas que valen mucho más que tu memoria.",
     "Tienes cien notas sueltas y ni una carpeta que las ordene por tema.",
     "Vuelves a pensar una idea que ya habías tenido —y anotado en algún sitio— hace meses.",
     "Tu cabeza funciona de archivo, y cada día tiene menos hueco libre.",
     "Apuntas todo en el momento y luego nunca vuelves a revisarlo.",
     "Sabes que anotaste esa idea en algún sitio, pero no recuerdas cuál.",
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
        return (f'Gancho (0-2s): "{hook}". Desarrollo (3-15s): Explica cómo {st} {afecta}, '
                f'con un ejemplo breve y concreto. Cierre (16-20s): Frase de impacto que resuma la idea y conecte con tu posicionamiento.')
    if formato == "Carrusel":
        return (f'Portada: "{hook}". Slides 2-6: desarrollar {st} en pasos, errores o claves concretas, '
                f'una idea por slide. Slide de cierre: resumen + CTA.')
    return (f'Foto o imagen personal/de trabajo. Caption reflexivo sobre {st}, '
            f'conectando la idea con tu experiencia real y tu forma de organizarte.')

def hashtag_subtema(subtema):
    slug = (subtema.lower()
            .replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
            .replace("ñ","n"))
    slug = "".join(c for c in slug if c.isalnum())
    return "#" + slug

# ── Construir, por pilar, una cola de FILAS ya emparejadas hook<->par ──────
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

salida = "window.IDEAS_PRODUCTIVIDAD = " + json.dumps(filas, ensure_ascii=False) + ";\n"
cabecera = "// Banco de contenido — PRODUCTIVIDAD Y ORGANIZACIÓN (365 días).\n"
with open("datos-ideas-productividad.js", "w", encoding="utf-8") as f:
    f.write(cabecera + salida)
print("OK ->", len(filas), "días")
