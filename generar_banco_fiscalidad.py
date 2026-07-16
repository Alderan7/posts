# -*- coding: utf-8 -*-
"""
Genera datos-ideas-fiscalidad.js — banco de 365 días para el nicho
"Fiscalidad" (asesora fiscal para autónomos y pymes). Mismo esquema que
datos-ideas-personal.js / datos-ideas-productividad.js
(dia/formato/pilar/idea/hook/cta/guion/caption/hashtags/objetivo/mes) para que
funcione con el motor ya existente (bancoIdeas/renderBanco/usarIdeaBanco).

Misma mecánica que generar_banco_productividad.py: cada subtema tiene un POOL
de hooks (cada uno una idea distinta) y un pool pequeño de pares (idea_central,
cta) en rotación. El assert avisa si algún pilar baja de 52 filas.

Voz del nicho: clara, cercana, SIN alarmismo barato pero con urgencia real
cuando hay plazo. Traduce la jerga (RETA, IRPF, Verifactu...) a lenguaje llano.
Habla de pagar lo justo, plazos controlados y tranquilidad.
"""
import json

MESES = [("Julio",31), ("Agosto",31), ("Septiembre",30), ("Octubre",31),
         ("Noviembre",30), ("Diciembre",31), ("Enero",31), ("Febrero",28),
         ("Marzo",31), ("Abril",30), ("Mayo",31), ("Junio",30)]

CICLO_FORMATO = ["Reel","Carrusel","Reel","Post","Reel","Carrusel","Post"]
HASHTAGS_BASE = "#fiscalidad #autonomos #asesoriafiscal"

PILARES = {
 "Verifactu": {
  "afecta": "cómo vas a facturar a partir de ahora",
  "cierre": "{subtema} no es papeleo extra: es la nueva forma de facturar, y llegar tarde siempre sale más caro que prepararse.",
  "subtemas": {
   "Qué es Verifactu": {
    "pares": [
     ("Verifactu es que tu programa de facturación cumpla un formato validado por Hacienda. Ni más, ni menos.", "Escríbeme VERIFACTU"),
     ("No es una app nueva que comprar: es un requisito que tu facturación ya debería estar preparando.", "Guárdalo"),
     ("Entenderlo hoy con calma evita decidir con prisas cuando ya sea obligatorio.", "¿Lo tenías claro?"),
    ],
    "hooks": [
     "Verifactu explicado en una frase: tu programa de facturas tendrá que hablar el idioma de Hacienda.",
     "Has oído 'Verifactu' veinte veces y todavía nadie te lo ha explicado en cristiano.",
     "No, Verifactu no es un impuesto nuevo. Pero te afecta igual.",
     "Verifactu no va de pagar más: va de CÓMO emites cada factura.",
     "Si facturas con Word o Excel, Verifactu va especialmente contigo.",
     "Tu gestoría aún no te ha hablado de Verifactu. Eso ya es una señal.",
     "Verifactu convierte cada factura en un registro que no se puede borrar ni retocar.",
     "La palabra 'Verifactu' suena a robot. Lo que hay detrás es muy simple.",
     "Verifactu es a las facturas lo que el taquígrafo al camión: todo queda registrado.",
     "¿Facturas con un programa 'de toda la vida'? Verifactu va a jubilarlo.",
     "Verifactu en 15 segundos: qué es, a quién afecta y cuándo.",
    ],
   },
   "Plazos que se mueven": {
    "pares": [
     ("El plazo se ha movido más de una vez, pero la obligación no ha desaparecido: solo se aplaza.", "Escríbeme PLAZOS"),
     ("Que Hacienda mueva la fecha no significa que tú puedas dormirte: significa más margen para hacerlo bien.", "Guárdalo"),
     ("Prepararse con el plazo lejos es elegir; hacerlo el último mes es aceptar lo que haya.", "¿Te pilla bien?"),
    ],
    "hooks": [
     "Hacienda vuelve a mover la fecha de Verifactu. Lo peor que puedes hacer es relajarte.",
     "El plazo de Verifactu se aplaza… y la mitad de los autónomos lo celebra en vez de aprovecharlo.",
     "Cada vez que se retrasa Verifactu, alguien deja de prepararse. Y luego llegan las prisas.",
     "'Ya lo miraré cuando sea obligatorio' es el plan de la mayoría. Y el más caro.",
     "El día que Verifactu sea obligatorio ya será tarde para comparar opciones con calma.",
     "Las fechas de Verifactu cambian; tu necesidad de facturar bien, no.",
     "Un plazo aplazado es tiempo regalado. Casi nadie lo usa.",
     "¿Sabes la fecha real que te afecta a TI según seas sociedad o autónomo?",
     "El calendario de Verifactu tiene dos fechas distintas y mucha gente mira la que no es.",
     "Si esperas al último trimestre, elegirás tu programa de facturación con el agua al cuello.",
     "Aplazan Verifactu y piensas 'uf, me libré'. No te libraste: te dieron margen.",
    ],
   },
   "Tu programa de facturación": {
    "pares": [
     ("La pregunta no es si tu programa te gusta: es si va a cumplir con el formato de Hacienda.", "Escríbeme VERIFACTU"),
     ("Cambiar de programa con tiempo te deja elegir el que encaja contigo, no el primero que aparezca.", "Guárdalo"),
     ("Tu software de facturas es una decisión fiscal, no solo informática.", "¿Cuál usas tú?"),
    ],
    "hooks": [
     "Tu programa de facturación actual, ¿cumple ya con Verifactu? Si no lo sabes, esto es para ti.",
     "Facturar en Excel se acaba. Y no lo digo yo, lo dice la normativa.",
     "Hay programas que ya están adaptados a Verifactu y programas que nunca lo estarán.",
     "La factura en Word que llevas años usando tiene fecha de caducidad.",
     "No todos los programas 'bonitos' de facturas cumplen lo que viene. Pregunta antes de pagar.",
     "Tu programa de facturas debería estar avisándote de Verifactu. ¿Lo ha hecho?",
     "Elegir software de facturación hoy sin mirar Verifactu es comprar a ciegas.",
     "¿Facturas gratis con una plantilla descargada de internet? Hablemos de lo que viene.",
     "El 'a mí me funciona así desde hace 10 años' se va a encontrar con la normativa de frente.",
     "Cambiar de programa de facturación asusta menos que un requerimiento por facturar mal.",
     "Antes de renovar la suscripción de tu software, haz UNA pregunta: ¿cumple Verifactu?",
    ],
   },
   "Cómo prepararse": {
    "pares": [
     ("Prepararse para Verifactu son tres pasos: saber si te afecta, revisar tu programa y decidir con tiempo.", "Escríbeme VERIFACTU"),
     ("No necesitas entender la ley entera: necesitas saber qué cambia en TU caso concreto.", "Guárdalo"),
     ("Empezar antes te da margen para elegir el sistema, no para sufrirlo.", "¿Empezamos?"),
    ],
    "hooks": [
     "Prepararte para Verifactu te lleva una tarde. Improvisarlo, un trimestre.",
     "3 preguntas para saber si estás lista para Verifactu (la mayoría falla la segunda).",
     "Adaptarse a Verifactu no es difícil. Difícil es hacerlo con todo el mundo a la vez.",
     "Lo primero que reviso con cada cliente ante Verifactu no es el software: es cómo factura hoy.",
     "Si emites 10 facturas al mes, tu adaptación a Verifactu es más simple de lo que crees.",
     "El plan anti-agobio con Verifactu: un paso este mes, no diez en diciembre.",
     "Verifactu se prepara en horas cuando alguien te dice exactamente qué mirar.",
     "Tu checklist de Verifactu cabe en un post-it. Te lo enseño.",
     "La diferencia entre los que llegan bien a Verifactu y los que no: empezaron un trimestre antes.",
     "¿Facturas poco? Aun así te toca. Pero tu adaptación es la versión fácil.",
     "Prepararse para Verifactu con tiempo también es negociar mejor el precio de tu software.",
    ],
   },
   "Errores al adaptarse": {
    "pares": [
     ("El error más caro con Verifactu no es técnico: es pensar que tu caso 'seguro que no cuenta'.", "Escríbeme VERIFACTU"),
     ("Copiar lo que hizo otro autónomo puede no valer: tu obligación depende de tu situación.", "Guárdalo"),
     ("Adaptarse mal es peor que adaptarse tarde: revisa antes de dar nada por hecho.", "¿Te suena?"),
    ],
    "hooks": [
     "El error nº1 con Verifactu: pensar que va solo de empresas grandes.",
     "'Mi gestoría ya lo hará' es el plan de muchos. Pregúntale HOY si es verdad.",
     "Comprar el primer software que dice 'Verifactu ready' sin comparar: error clásico que viene.",
     "Hay quien está borrando y rehaciendo facturas 'para ordenar'. Con lo que viene, mal plan.",
     "Adaptarte a Verifactu no es instalar un programa y ya: es cambiar cómo corriges errores.",
     "Con Verifactu, una factura mal hecha no se borra: se rectifica. Son cosas distintas.",
     "El autónomo que factura 'cuando puede' con fechas bailadas tiene un problema con lo que viene.",
     "Creer que Verifactu es solo para quien factura mucho: primer mito a derribar.",
     "Esperar a que tu programa 'se actualice solo' sin confirmarlo: así se llega tarde.",
     "Con Verifactu, el truco de 'esta factura la hago con fecha de la semana pasada' se acabó.",
     "No preguntar a tiempo es el único error de Verifactu que no tiene arreglo barato.",
    ],
   },
  },
 },
 "Cuota autónomos": {
  "afecta": "lo que pagas cada mes sin mirarlo",
  "cierre": "{subtema} va de una sola cosa: cotizar por lo que de verdad ganas, ni un euro de más ni uno de menos.",
  "subtemas": {
   "Tramos por ingresos reales": {
    "pares": [
     ("La cuota ya no es fija: son 15 tramos según tus rendimientos netos reales.", "Escríbeme CUOTA"),
     ("Tu tramo se calcula con lo que ganas de verdad, no con lo que facturas.", "Guárdalo"),
     ("Rendimiento neto = ingresos menos gastos. Ese número decide tu cuota, y casi nadie lo mira.", "¿Sabes el tuyo?"),
    ],
    "hooks": [
     "15 tramos. Ingresos reales. Y la mayoría sigue cotizando a ojo.",
     "Tu cuota de autónomos ya no la eliges tú: la deciden tus números. ¿Los conoces?",
     "Facturar 3.000€ no es ganar 3.000€. Y tu cuota se calcula con el segundo número.",
     "¿Sabes en qué tramo de cuota estás AHORA MISMO? La mayoría no.",
     "La reforma de la cuota lleva años en marcha y muchos siguen pagando como en 2022.",
     "Tu cuota depende de tu rendimiento neto. Te explico ese palabro en 10 segundos.",
     "Dos autónomos que facturan lo mismo pueden pagar cuotas muy distintas. Y está bien que así sea.",
     "El tramo de cuota no es una multa ni un premio: es un espejo de tus números.",
     "Si no sabes tu rendimiento neto mensual, no sabes si tu cuota es la correcta.",
     "La pregunta que casi nadie se hace: ¿mi cuota de este mes corresponde a lo que gano este año?",
     "Cotizar por ingresos reales suena a lío. Es más justo que lo de antes, si lo revisas.",
    ],
   },
   "Pagar de más": {
    "pares": [
     ("Muchos autónomos pagan cuota de más por no revisar el tramo. Eso también es dinero perdido.", "Escríbeme CUOTA"),
     ("Pagar de más no te protege de nada: solo te descapitaliza mes a mes.", "Guárdalo"),
     ("Una revisión de 20 minutos puede ahorrarte cientos de euros al año en cuota.", "¿Cuándo la revisaste?"),
    ],
    "hooks": [
     "Pagas tu cuota cada mes. ¿Sabes si es la que te corresponde de verdad?",
     "Hay autónomos pagando 80€ de más AL MES por no revisar su tramo.",
     "Descubrí que una clienta llevaba dos años pagando cuota de más. Nadie se lo había mirado.",
     "Pagar cuota de más no da derecho a nada extra. Solo es dinero que se va.",
     "Si tus ingresos bajaron y tu cuota no, estás regalando dinero cada mes.",
     "El banco te cobra la cuota puntual cada mes. Puntualidad no es lo mismo que exactitud.",
     "¿Empezaste fuerte, bajaste ingresos y sigues en el tramo alto? Eso se corrige.",
     "La cuota que pagas hoy la elegiste (o te la eligieron) hace tiempo. ¿Sigue teniendo sentido?",
     "Nadie de la Seguridad Social te va a llamar para decirte 'oye, que estás pagando de más'.",
     "Cada mes que pasa sin revisar tu tramo es un mes más pagando a ciegas.",
     "Pagar de más en la cuota es el 'impuesto silencioso' del autónomo despistado.",
    ],
   },
   "Cambiar de tramo": {
    "pares": [
     ("Puedes cambiar de tramo hasta 6 veces al año. Es un derecho, no un trámite raro.", "Escríbeme CUOTA"),
     ("Si tus ingresos varían, tu cuota puede (y debe) variar con ellos.", "Guárdalo"),
     ("Cambiar de tramo se hace online en minutos. Lo difícil es acordarse de mirarlo.", "¿Lo has usado?"),
    ],
    "hooks": [
     "Tienes derecho a cambiar tu cuota 6 veces al año. ¿Cuántas has usado? Exacto: cero.",
     "Cambiaste de tramo hace un año… y nunca has vuelto a mirarlo.",
     "Tu negocio tiene meses altos y bajos. Tu cuota puede acompañarlos.",
     "Bajó la facturación este trimestre: puedes bajar la cuota. Legal, online y en minutos.",
     "El cambio de tramo no es 'buscarle las cosquillas' a nadie: está pensado para esto.",
     "Si el verano es tu temporada floja, tu cuota de verano puede reflejarlo.",
     "Subir de tramo cuando ganas más también te protege: cotizas por lo real.",
     "Las 6 ventanas de cambio de tramo tienen fechas concretas. Te las apunto.",
     "Cambiar de tramo a tiempo evita el susto de la regularización después.",
     "No cambiar nunca de tramo también es una decisión. Normalmente, la peor.",
     "¿Tu asesor te ha propuesto alguna vez revisar el tramo? Si no, pregúntate por qué.",
    ],
   },
   "Regularización anual": {
    "pares": [
     ("Al final del año, la Seguridad Social compara lo cotizado con lo ganado: eso es la regularización.", "Escríbeme CUOTA"),
     ("La regularización no es un castigo: es el ajuste entre lo que pagaste y lo que te tocaba.", "Guárdalo"),
     ("Quien revisa su tramo durante el año, llega a la regularización sin sorpresas.", "¿Preparada?"),
    ],
    "hooks": [
     "La palabra 'regularización' asusta. Te la traduzco: ajuste de cuentas anual, a favor o en contra.",
     "Un día te llega un cargo (o un ingreso) de la Seguridad Social. Es la regularización, y tiene lógica.",
     "Si cotizaste de menos, te reclaman la diferencia. Si cotizaste de más… te la devuelven.",
     "La regularización premia a quien llevó sus tramos al día y sorprende al que no miró nada.",
     "¿Te devolvieron dinero de la cuota? No es un regalo: es que pagaste de más todo el año.",
     "El susto de la regularización se fabrica 12 meses antes, mes a mes.",
     "Regularización en una frase: la Seguridad Social hace la cuenta que tú no hiciste.",
     "Hay quien descubre en la regularización lo que ganó de verdad el año pasado. Tarde.",
     "La regularización no se puede evitar. La sorpresa, sí.",
     "Si este año facturaste bastante más, ve apartando para la regularización. Te lo agradecerás.",
     "Mi trabajo es que la carta de la regularización te dé exactamente igual.",
    ],
   },
   "Alta y primeros años": {
    "pares": [
     ("La tarifa plana ayuda al empezar, pero tiene condiciones y fecha de fin: apúntalas.", "Escríbeme AUTONOMOS"),
     ("Darse de alta bien desde el día uno evita arrastrar errores años enteros.", "Guárdalo"),
     ("El salto de la tarifa plana a la cuota real hay que planificarlo, no descubrirlo en el banco.", "¿Te pasó?"),
    ],
    "hooks": [
     "La tarifa plana se acaba y tu cuota se multiplica. ¿Tienes fecha apuntada?",
     "Darse de alta de autónomo lleva 20 minutos. Darse de alta BIEN, algo más de cabeza.",
     "El primer año de autónomo se sobrevive mejor sabiendo 3 fechas y 2 modelos. Solo eso.",
     "Nadie te avisa del mes exacto en que tu tarifa plana termina. Nadie salvo tu asesora.",
     "Alta de autónomo: el epígrafe que eliges hoy condiciona lo que puedes deducir mañana.",
     "¿Alta a mitad de mes o el día 1? Ese detalle tiene consecuencias en tu cuota.",
     "Puedes tener derecho a ampliar la tarifa plana y no estar pidiéndolo.",
     "El error del primer año: gastar como si la cuota fuera a ser siempre la bonificada.",
     "Antes de darte de alta, decide una cosa: quién te va a llevar los papeles desde el día uno.",
     "Empezar de autónoma con miedo es normal. Empezar sin saber qué pagarás en 18 meses, evitable.",
     "El paso de 80€ a cuota completa duele menos si lo ves venir con un año de margen.",
    ],
   },
  },
 },
 "Renta e IRPF": {
  "afecta": "lo que declaras (y lo que te devuelven) cada año",
  "cierre": "{subtema} deja de dar miedo cuando se prepara con meses, no con días.",
  "subtemas": {
   "Obligación de declarar": {
    "pares": [
     ("Si estuviste de alta como autónomo aunque fuera UN día, te toca declarar. Sin mínimos.", "Escríbeme RENTA"),
     ("Las reglas de 'no llego al mínimo' de los asalariados no te valen siendo autónomo.", "Guárdalo"),
     ("Saber si estás obligada a declarar te lleva un minuto. Suponerlo, una sanción.", "¿Lo sabías?"),
    ],
    "hooks": [
     "Si fuiste autónomo un solo día del año, tienes que presentar la Renta. Aunque ganaras 200€.",
     "'Gané poco, no declaro'. Siendo autónoma, esa frase es una trampa.",
     "El mínimo de 22.000€ que conoce todo el mundo NO aplica a los autónomos.",
     "Te diste de alta en noviembre 'para probar'. Enhorabuena: ya tienes cita con la Renta.",
     "Muchas sanciones de Renta a autónomos son por NO presentar, no por presentar mal.",
     "¿Autónomo a ratos, con alta y baja el mismo año? Declaras igual.",
     "La Renta del autónomo no pregunta cuánto ganaste: pregunta si estuviste de alta.",
     "Presentar la Renta ganando poco suele salir a devolver. No presentarla, a sancionar.",
     "El año que 'no llegué a nada' también se declara. Y suele ser el más fácil.",
     "Declarar sin estar obligado a veces conviene: hay devoluciones que se pierden por no presentar.",
     "Tu primera Renta como autónoma: más fácil de lo que temes, más obligatoria de lo que crees.",
    ],
   },
   "Casillas y novedades": {
    "pares": [
     ("Cada campaña de Renta trae casillas nuevas. Las que te afectan a ti son dos o tres: localízalas.", "Escríbeme RENTA"),
     ("No hace falta saberse la Renta entera: hace falta saber qué cambió para tu caso.", "Guárdalo"),
     ("Las novedades fiscales se publican meses antes. Enterarse en abril es elegir el estrés.", "¿Al día?"),
    ],
    "hooks": [
     "Cada año cambian casillas de la Renta y te enteras cuando ya estás dentro del borrador.",
     "¿Sabes ya qué casillas nuevas te afectan este año? Te las resumo.",
     "La Renta no perdona la letra pequeña. Y cada año la letra pequeña cambia.",
     "Las 3 novedades de esta campaña que SÍ tocan a los autónomos.",
     "El borrador no incluye tu actividad de autónomo bien puesta. Esa parte es cosa tuya.",
     "Confirmar el borrador sin revisarlo: el clic más caro del año para un autónomo.",
     "Hay deducciones autonómicas nuevas cada año que casi nadie marca. Dinero que se queda ahí.",
     "Tu comunidad autónoma tiene deducciones propias. ¿Las has mirado alguna vez?",
     "Las novedades de la Renta no son para asustarte: algunas son a tu favor.",
     "Renta de este año: qué cambia, qué sigue igual y qué te conviene revisar dos veces.",
     "Si tu Renta de este año es 'copiar la del año pasado', algo se te está escapando.",
    ],
   },
   "Errores típicos": {
    "pares": [
     ("Los errores de Renta más comunes de los autónomos se repiten cada año. Y se evitan igual de fácil.", "Escríbeme RENTA"),
     ("Un error en la Renta no siempre sanciona, pero casi siempre cuesta: tiempo, recargo o devolución perdida.", "Guárdalo"),
     ("Revisar antes de presentar cuesta 15 minutos. Rectificar después, semanas.", "¿Revisas o confirmas?"),
    ],
    "hooks": [
     "El error de Renta más repetido entre autónomos: olvidar ingresos de una plataforma o cliente suelto.",
     "Metiste un gasto personal como gasto del negocio 'porque coló'. Hasta que no cuele.",
     "Presentar la Renta el último día: ahí nacen la mitad de los errores.",
     "Olvidaste los pagos del modelo 130 al hacer la Renta y pagaste dos veces. Se recupera, pero vaya susto.",
     "Ese ingreso pequeño 'que no dejará rastro' aparece cruzado en tu borrador. Siempre aparece.",
     "Cambiar de gestoría a mitad de año y que cada una declare 'su parte': receta para el lío.",
     "La factura de diciembre cobrada en enero: el clásico que descuadra Rentas.",
     "Deducir el 100% del móvil siendo tu único teléfono: revisable. Y revisado, últimamente.",
     "Errores de Renta que Hacienda perdona y errores que no: aprende a distinguirlos.",
     "Rectificar una Renta ya presentada es posible. Mejor aún es no tener que hacerlo.",
     "Tu Renta y tus 130 del año tienen que contar la misma película. Si no cuadran, pregunta llegará.",
    ],
   },
   "Retenciones y modelo 130": {
    "pares": [
     ("El modelo 130 es un adelanto trimestral de tu IRPF. No es un impuesto extra: es el mismo, a plazos.", "Escríbeme FISCAL"),
     ("Si facturas con retención a empresas, puede que ni te toque presentar el 130. Depende de un porcentaje.", "Guárdalo"),
     ("Entender la relación 130-Renta te quita el susto de 'pagar dos veces'.", "¿Lo tenías claro?"),
    ],
    "hooks": [
     "El modelo 130 explicado sin jerga: adelantas IRPF cada trimestre para no llorar en junio.",
     "¿Facturas a empresas con retención? Quizá el 130 ni te toca. Hay una regla del 70%.",
     "'Pagué el 130 todo el año y ahora la Renta me sale a pagar otra vez'. No: te descuentas lo adelantado.",
     "Retención del 7% o del 15%: elegir mal ese número te descuadra todo el año.",
     "Nuevo autónomo: puedes aplicar el 7% de retención tus primeros años. Casi nadie lo dice.",
     "El 130 sale de tus ingresos MENOS tus gastos. Si no registras gastos, adelantas de más.",
     "Trimestre flojo y aun así el 130 te sale alto: revisa qué gastos no estás contando.",
     "La retención que te quitan en cada factura es dinero tuyo a cuenta. En la Renta, vuelve.",
     "El baile 130-retenciones-Renta, explicado con una cuenta de servilleta.",
     "Si tu 130 sale a cero, también se presenta. A cero, pero se presenta.",
     "Pagar el 130 duele menos cuando entiendes que es tu Renta en cómodos plazos.",
    ],
   },
   "Preparar la Renta con tiempo": {
    "pares": [
     ("La Renta se gana en enero, no en junio: lo que ordenas ahora es estrés que te ahorras después.", "Escríbeme RENTA"),
     ("Declarar bien empieza meses antes de la campaña: con las facturas y gastos al día.", "Guárdalo"),
     ("Quien llega a abril con todo ordenado, elige cuándo presentar. Quien no, obedece al calendario.", "¿Cómo llegas tú?"),
    ],
    "hooks": [
     "Cada campaña de Renta trae una sorpresa nueva. Este año no tiene por qué ser la tuya.",
     "La Renta sin sustos se prepara en 3 ratos: uno en enero, uno en marzo y uno en abril.",
     "Presentar pronto tiene premio: si sale a devolver, cobras antes.",
     "El drama de la Renta suele ser un drama de carpetas: facturas sueltas, gastos sin apuntar.",
     "Junio es mal mes para descubrir cuánto ganaste el año pasado.",
     "Un truco simple: una carpeta al mes con facturas y gastos. La Renta se hace sola.",
     "¿Sabes ya, más o menos, si tu Renta saldrá a pagar o a devolver? Se puede estimar hoy.",
     "Si te sale a pagar, puedes fraccionar en dos plazos sin intereses. Con condiciones, pero se puede.",
     "La cita con la Renta no debería ser una caja sorpresa: los números ya existen desde enero.",
     "Renta a pagar no significa Renta mal hecha. A veces significa que ganaste más. Enhorabuena.",
     "Preparar la Renta con tiempo también es detectar deducciones ANTES de que caduque el plazo.",
    ],
   },
  },
 },
 "Deducciones": {
  "afecta": "cuánto pagas de más sin darte cuenta",
  "cierre": "{subtema} no es un truco: es conocer la norma y aplicarla con justificantes. Eso es pagar lo justo.",
  "subtemas": {
   "Gastos de casa": {
    "pares": [
     ("Si trabajas desde casa, parte de tus suministros es deducible. Con porcentaje y con reglas.", "Escríbeme DEDUCCIONES"),
     ("La clave del gasto de casa no es deducir mucho: es deducir el porcentaje correcto.", "Guárdalo"),
     ("Declarar los metros de tu despacho en el alta es lo que abre la puerta a estas deducciones.", "¿Lo hiciste?"),
    ],
    "hooks": [
     "Trabajas desde casa y no te deduces ni un euro de luz. Eso es pagar de más.",
     "La fórmula del 30% de los suministros de casa, explicada de una vez.",
     "Tu wifi, tu luz y tu agua tienen una parte deducible si trabajas en casa. Con condiciones.",
     "Deducir gastos de casa sin haber declarado el espacio de trabajo: el error de base.",
     "¿Cuántos metros de tu casa son 'oficina'? Ese dato vale dinero cada trimestre.",
     "El alquiler de casa es deducible solo en casos concretos. Te cuento cuáles antes de que la líes.",
     "Hipoteca, comunidad, IBI: qué parte toca deducir si tu despacho está en casa.",
     "Teletrabajas desde 2020 y nunca actualizaste tu situación fiscal. Dinero en la mesa cada año.",
     "El gasto de casa se deduce con una regla clara. Lo que no tiene regla clara, mejor pregúntalo.",
     "Deducirte 'toda la luz' de casa es tan mala idea como no deducirte nada.",
     "Casa y negocio comparten techo: los números también deben repartirse bien.",
    ],
   },
   "Vehículo y dietas": {
    "pares": [
     ("El coche y las dietas son las deducciones más deseadas y las más vigiladas: se hacen bien o no se hacen.", "Escríbeme DEDUCCIONES"),
     ("En vehículo, la regla cambia según tu actividad: lo que a un transportista le vale, a ti quizá no.", "Guárdalo"),
     ("Una dieta deducible tiene requisitos concretos: día laborable, desplazamiento, pago con tarjeta.", "¿Las cumples?"),
    ],
    "hooks": [
     "El coche del autónomo: la deducción más famosa y la peor entendida.",
     "¿Puedes deducirte la gasolina? Depende de una pregunta que casi nadie se hace primero.",
     "Comer fuera no siempre es 'dieta deducible'. Los requisitos son 4 y muy concretos.",
     "La dieta deducible: hasta 26,67€ al día, pagada con tarjeta, en día de trabajo. Sin eso, no hay dieta.",
     "El IVA del coche tiene su propia regla (50%) distinta de la del gasto. Sí, es lioso. Te lo aclaro.",
     "Furgoneta rotulada vs coche particular: dos mundos fiscales distintos.",
     "Pagaste la comida con clientes en efectivo: acabas de perder la deducción.",
     "Kilometraje, parking, peajes: qué se deduce, cuándo y con qué papel.",
     "Deducir el coche 'porque lo uso para trabajar' no basta: hay que poder demostrarlo.",
     "Las comidas de trabajo de agosto llaman la atención. Las de tu feria del sector, no. Contexto importa.",
     "Tu coche puede ser deducible al 100%, al 50% o nada. Tres letras deciden: uso.",
    ],
   },
   "Formación y herramientas": {
    "pares": [
     ("Todo lo que usas para tu actividad —cursos, software, equipo— es candidato a deducción.", "Escríbeme DEDUCCIONES"),
     ("La formación deducible es la relacionada con tu actividad: el matiz está en poder explicarlo.", "Guárdalo"),
     ("Si dudas de si un gasto 'entra', apúntalo y pregunta: peor es perderlo por defecto.", "¿Apuntas todo?"),
    ],
    "hooks": [
     "Ese curso que hiciste para mejorar en tu negocio: deducible. ¿Lo apuntaste?",
     "Pagas software cada mes (diseño, gestión, IA...) y no todo está en tus gastos. Revísalo.",
     "El ordenador nuevo, ¿gasto del año o amortización en varios? Depende del importe.",
     "Libros técnicos, suscripciones del sector, herramientas online: pequeñas cuotas que suman deducción.",
     "La cuota de autónomos es gasto deducible. Sí, la propia cuota. Hay quien no la incluye.",
     "El móvil, el hosting de tu web, tu email de empresa: gastos reales que a veces se quedan fuera.",
     "Formarte en IA para tu negocio es deducible. Formarte en repostería siendo asesora... difícil de defender.",
     "Cada suscripción que pagas con la tarjeta personal es una deducción que probablemente pierdes.",
     "Tu seguro de responsabilidad civil profesional: deducible y, a veces, olvidado.",
     "Autónomos que compran herramientas caras en diciembre: bien pensado, si es real y hace falta.",
     "La regla de oro de estos gastos: relación con la actividad + factura a tu nombre. Sin más magia.",
    ],
   },
   "Justificantes y facturas": {
    "pares": [
     ("Sin factura no hay deducción: el ticket casi nunca basta. Pide factura, siempre.", "Escríbeme DEDUCCIONES"),
     ("Un gasto sin justificante es un gasto que no existe para Hacienda, por real que sea.", "Guárdalo"),
     ("Guardar facturas 4 años no es manía: es el plazo en el que te las pueden pedir.", "¿Las guardas?"),
    ],
    "hooks": [
     "Compraste material, tiraste el ticket, perdiste la deducción. Historia real de cada semana.",
     "Ticket no es factura. Esa diferencia de una palabra vale dinero.",
     "'Con el ticket vale, ¿no?' — Para pagar sí. Para deducir, casi nunca.",
     "La factura simplificada con tu NIF: pídela siempre; te la tienen que dar.",
     "Las facturas se guardan 4 años como mínimo. ¿Dónde están las tuyas de hace 3?",
     "Amazon, gasolineras, supermercados: todos te dan factura si la pides. Nadie la pide.",
     "Un cajón de tickets borrosos no es contabilidad: en un año no se leerá ninguno.",
     "Foto de la factura + carpeta del mes: el sistema anti-pérdidas más simple que existe.",
     "El gasto era deducible, el justificante no aparece: resultado, pagas de más. Evitable al 100%.",
     "Facturas a tu nombre personal en vez del de tu actividad: pequeño detalle, gran problema.",
     "Cada factura que pides en el momento es una discusión que no tendrás dentro de 3 años.",
    ],
   },
   "Miedo a deducir": {
    "pares": [
     ("Deducir lo que te corresponde no 'llama la atención': lo que llama la atención es lo incoherente.", "Escríbeme AHORRO"),
     ("El miedo a Hacienda hace pagar de más a miles de autónomos cada año. La norma es tu aliada si la conoces.", "Guárdalo"),
     ("Entre deducirlo todo sin criterio y no deducir nada por miedo, existe un punto: el correcto.", "¿Dónde estás tú?"),
    ],
    "hooks": [
     "La mayoría de autónomos deja dinero en la mesa por miedo a 'llamar la atención' de Hacienda.",
     "Deducir bien no es un truco: es conocer la norma mejor que quien te cobra por no explicártela.",
     "Hay dos formas de perder dinero con Hacienda: deducir de más… y deducir de menos.",
     "'Por si acaso no lo meto' — esa frase, repetida 40 veces al año, es un sueldo perdido.",
     "No deducir nada 'para ir tranquila' es pagar un seguro carísimo contra un riesgo que no entiendes.",
     "Lo que Hacienda mira no es cuánto deduces: es si tu conjunto tiene sentido.",
     "¿Cuánto llevas sin revisar qué te puedes deducir de verdad? Años, ¿a que sí?",
     "El autónomo miedoso paga de más; el temerario paga sanciones. La informada paga lo justo.",
     "Una deducción con factura, criterio y relación con tu actividad no es valentía: es lo normal.",
     "Tu vecino se deduce hasta el gimnasio y tú ni la luz del despacho. Los dos lo hacen mal.",
     "El miedo fiscal se cura con información, no con resignación.",
    ],
   },
  },
 },
 "Control Hacienda": {
  "afecta": "lo que Hacienda ya sabe de tu negocio",
  "cierre": "{subtema} no va de esconderse mejor: va de declarar bien desde el principio, que es más barato y se duerme mejor.",
  "subtemas": {
   "Bizum y pagos electrónicos": {
    "pares": [
     ("Tu banco ya informa de los cobros por Bizum. La pregunta no es si se ve: es si lo declaras.", "Escríbeme HACIENDA"),
     ("Bizum no es el problema: el problema es cobrar por Bizum y no registrarlo como ingreso.", "Guárdalo"),
     ("Cobrar digital deja rastro. Úsalo a tu favor: es tu propia contabilidad automática.", "¿Lo declaras todo?"),
    ],
    "hooks": [
     "Tu banco ya informa a Hacienda de lo que cobras por Bizum. ¿Lo sabías?",
     "Si cobras por Bizum sin declararlo, el problema ya no es 'si te pillan'. Es 'cuándo'.",
     "El Bizum de 'entre amigos' y el Bizum de tu negocio no se parecen en nada a ojos de Hacienda.",
     "Los umbrales de información bancaria han bajado. Lo que antes 'no se veía', ahora se cruza.",
     "Cobrar 30€ por Bizum y no declararlo parece poca cosa. Multiplicado por un año, es un patrón.",
     "Las plataformas de pago también informan. Stripe, PayPal y compañía no son territorio invisible.",
     "'Me pagas por Bizum y ahorramos el IVA' — esa frase sale carísima por las dos partes.",
     "El rastro digital de tus cobros puede ser tu enemigo o tu mejor contabilidad. Tú eliges el bando.",
     "Vender por Wallapop o Vinted de forma habitual también tiene su casilla. Habitual es la palabra clave.",
     "Hacienda no persigue el Bizum: persigue el ingreso sin declarar. El canal da igual.",
     "Si tu cuenta recibe 40 bizums al mes 'de nada en concreto', tu banco ya lo está contando.",
    ],
   },
   "Cruce de datos": {
    "pares": [
     ("Hacienda cruza lo que declaras tú con lo que declaran tus clientes, tu banco y tus plataformas.", "Escríbeme HACIENDA"),
     ("No es que te vigilen más: es que tienen más datos que nunca para comparar.", "Guárdalo"),
     ("La coherencia es tu mejor defensa: que tu declaración cuente lo mismo que tus movimientos.", "¿Cuadra lo tuyo?"),
    ],
    "hooks": [
     "No es que Hacienda te vigile más. Es que tiene más datos que nunca para cruzar.",
     "Tu cliente declara la factura que te pagó. Si tú no la declaras, el cruce canta solo.",
     "El modelo 347 (operaciones de más de 3.005€) es el chivato silencioso: tu cliente te declara a ti.",
     "Hacienda sabe tu facturación aproximada antes de que presentes nada. La pregunta es si coincidirá.",
     "Los datos fiscales que te muestra Hacienda en tu Renta son lo que YA saben. Léelos con esa mentalidad.",
     "Ingresos declarados: 12.000€. Movimientos en cuenta: 35.000€. Esa diferencia es una pregunta andando.",
     "La IA también trabaja para Hacienda: los patrones raros se detectan solos.",
     "Un descuadre puntual se explica. Un descuadre cada trimestre, se investiga.",
     "Tus proveedores, tu banco, tus plataformas de venta: todos entregan su parte del puzle. Tú eres la otra.",
     "Declarar bien no es para 'que no te pillen': es para que cuando crucen datos, todo cuadre a la primera.",
     "El cruce de datos no tiene horario ni avisa: trabaja con lo que ya entregaste todo el año.",
    ],
   },
   "Requerimientos": {
    "pares": [
     ("Un requerimiento no es una acusación: es una pregunta con plazo. Se responde bien y a tiempo, y ya.", "Escríbeme HACIENDA"),
     ("Lo peor que puedes hacer con una carta de Hacienda es dejarla cerrada en un cajón.", "Guárdalo"),
     ("Responder un requerimiento con la documentación ordenada convierte un susto en un trámite.", "¿Te llegó una?"),
    ],
    "hooks": [
     "Te llega una carta de Hacienda y se te para el corazón. Respira: la mayoría son solo preguntas.",
     "Un requerimiento tiene plazo de respuesta. Ignorarlo es la única respuesta incorrecta.",
     "La notificación de Hacienda que no abres también cuenta: a los 10 días se da por notificada.",
     "Requerimiento no es sanción. Cómo lo respondas decide si acaba siéndolo.",
     "Hacienda te pide 'justificar un gasto'. Si guardaste la factura, esto dura 5 minutos.",
     "El buzón electrónico obligatorio: el sitio donde llegan cartas que nadie mira. Míralo.",
     "Recibir un requerimiento con los papeles en orden es casi un trámite. Sin ellos, una semana de agobio.",
     "'Comprobación limitada': suena fatal, suele ser rutina. Te explico qué miran.",
     "Responder tarde a Hacienda convierte preguntas baratas en problemas caros.",
     "Las cartas de Hacienda también se pueden recurrir. Y se ganan más de lo que crees, con papeles.",
     "Un requerimiento bien respondido a la primera cierra el tema. A la tercera ronda, ya es otra cosa.",
    ],
   },
   "Efectivo y límites": {
    "pares": [
     ("El límite de pago en efectivo entre empresas y autónomos es 1.000€. Superarlo sanciona a ambas partes.", "Escríbeme HACIENDA"),
     ("El efectivo no es ilegal: lo ilegal es usarlo para que un ingreso no exista.", "Guárdalo"),
     ("Cobra como quieras, pero regístralo todo: el problema nunca es el método, es el silencio.", "¿Lo sabías?"),
    ],
    "hooks": [
     "El límite de 1.000€ en efectivo con otros negocios: superarlo multa al que paga Y al que cobra.",
     "'Sin factura te lo dejo más barato' — esa rebaja la acabáis pagando los dos.",
     "Cobrar en efectivo es legal. Cobrar en efectivo y que no exista, no.",
     "El mito de 'el efectivo no deja rastro': tu margen, tu caja y tu estilo de vida sí lo dejan.",
     "Ingresos en efectivo sin registrar + gastos altos visibles = la cuenta que Hacienda hace sola.",
     "La denuncia del cliente descontento existe. Y el 'me lo cobró sin factura' es munición gratis.",
     "Meter en el banco 'de golpe' el efectivo de meses llama más la atención que declararlo cada mes.",
     "Si tu negocio es de mucho efectivo (peluquería, hostelería...), tu sector ya tiene módulos y ratios: te comparan.",
     "El efectivo de la hucha no cotiza... hasta que quieres comprar algo grande y no puedes justificarlo.",
     "Pagarle en B a un proveedor te deja sin factura, sin deducción y sin garantía. Tres pérdidas en una.",
     "La pregunta no es '¿cuánto puedo cobrar en efectivo?': es '¿está todo apuntado?'.",
    ],
   },
   "Declarar bien desde el principio": {
    "pares": [
     ("Declarar bien desde el día uno es más barato que corregir años después: los recargos crecen con el tiempo.", "Escríbeme FISCAL"),
     ("La tranquilidad fiscal no es suerte: es un sistema simple aplicado desde el principio.", "Guárdalo"),
     ("Empezar bien cuesta lo mismo que empezar mal. Corregir, no.", "¿Empezamos bien?"),
    ],
    "hooks": [
     "Lo importante no es ocultar mejor: es declarar bien desde el principio. Es más barato, de verdad.",
     "Regularizar tu situación ANTES de que te reclamen tiene descuento. Después, recargo.",
     "El autónomo que empieza declarando todo duerme mejor que el que 'ya lo arreglará'.",
     "Ponerse al día voluntariamente cuesta un recargo pequeño. Esperar la carta, mucho más.",
     "Ese ingreso que llevas 2 años sin declarar: aún estás a tiempo de arreglarlo por las buenas.",
     "La honestidad fiscal no es ingenuidad: es la estrategia más rentable a 5 años vista.",
     "Declararlo todo también te sirve A TI: para pedir hipoteca, ayudas o vender tu negocio algún día.",
     "Un negocio 'en B' no puede crecer: no puede contratar, ni financiarse, ni venderse. Se queda enano.",
     "Cada euro declarado hoy es un problema que no tendrás en 4 años.",
     "'Todo el mundo lo hace' es la frase que más sanciones ha pagado en este país.",
     "Tu yo del futuro —el que pide la jubilación, la baja o la hipoteca— te agradece cada euro declarado hoy.",
    ],
   },
  },
 },
 "Sanciones y plazos": {
  "afecta": "los sustos (evitables) con Hacienda",
  "cierre": "{subtema} casi nunca va de fraude: va de despistes con fecha. Y los despistes con fecha se curan con calendario.",
  "subtemas": {
   "Plazos trimestrales": {
    "pares": [
     ("Los trimestres fiscales tienen fecha fija: 20 de abril, julio, octubre y 30 de enero. Tatúatelas.", "Escríbeme PLAZOS"),
     ("El trimestre no avisa: llega. La diferencia está en si te pilla con los deberes hechos.", "Guárdalo"),
     ("Presentar el día 19 en vez del 21 es la diferencia entre trámite y recargo.", "¿Las tienes apuntadas?"),
    ],
    "hooks": [
     "20 de abril, 20 de julio, 20 de octubre, 30 de enero. Esas 4 fechas mandan en tu año.",
     "El trimestre fiscal siempre llega 'de repente'... cada tres meses, puntual como un reloj.",
     "¿Domiciliar los impuestos del trimestre? Entonces el plazo real acaba el día 15, no el 20.",
     "La semana del 20 tu gestoría está desbordada. Enviarle todo el 18 te convierte en su cliente favorito.",
     "Cada trimestre igual: facturas el día 19 a medianoche buscando papeles. Hay otra manera de vivir.",
     "El IVA que cobras no es tuyo: es un depósito que devuelves el día 20. Trátalo como tal.",
     "Un trimestre se prepara en 30 minutos al mes o en un fin de semana de pánico. Mismos números.",
     "Verano y trimestre de julio: la combinación que más recargos genera del año.",
     "Tu calendario fiscal personal depende de tus modelos: 303, 130, 111... Te hago la lista corta.",
     "Primer trimestre como autónoma: qué presentar, cuándo y qué pasa si no.",
     "El día 20 no se negocia. Tu nivel de estrés ese día, sí.",
    ],
   },
   "Recargos por presentar tarde": {
    "pares": [
     ("Presentar tarde SIN que te lo pidan tiene recargo suave y creciente: 1% + 1% por mes. Tarde pero voluntario.", "Escríbeme PLAZOS"),
     ("El recargo por llegar tarde es la sanción más evitable del sistema: solo pide puntualidad.", "Guárdalo"),
     ("Si se te pasó un plazo, presenta YA: cada mes que esperas, el recargo sube un escalón.", "¿Se te pasó?"),
    ],
    "hooks": [
     "Se te pasó el trimestre. Tranquila: si presentas tú antes de que te avisen, el recargo es pequeño.",
     "Presentar un día tarde: 1% de recargo. Esperar a que te lo pidan: mínimo 50% de sanción. Elige.",
     "El recargo por retraso crece cada mes: presentar 'ya que llego tarde, más adelante' es la peor lógica.",
     "Un año tarde por tu cuenta = 15% + intereses. La carta de Hacienda primero = otra liga muy superior.",
     "Llegar tarde a Hacienda tiene tarifa oficial. Y es sorprendentemente razonable si el paso lo das tú.",
     "'Como ya se me pasó, espero a ver si no se dan cuenta' — se dan cuenta. El cruce es automático.",
     "El recargo no es una multa moral: es un interés por demora. Sin vergüenza: se paga y se aprende.",
     "Presentaste tarde pero pagaste todo: el recargo se reduce un 25% si pagas en plazo el propio recargo.",
     "La declaración extemporánea (palabro) = presentar tarde voluntariamente = el mal menor con diferencia.",
     "Cada modelo olvidado prescribe a los 4 años. Vivir 4 años pendiente de eso sale más caro que el recargo.",
     "Recargo del 1% vs sanción del 50%: la diferencia entre corregir tú y que te corrijan.",
    ],
   },
   "Sanciones evitables": {
    "pares": [
     ("La mayoría de sanciones a autónomos no vienen de fraude: vienen de un plazo o un formulario olvidado.", "Escríbeme PLAZOS"),
     ("Una sanción evitable es doblemente dolorosa: cuesta dinero y no compró nada.", "Guárdalo"),
     ("Las sanciones tienen reducción por conformidad y pronto pago: hasta un 40% menos. Que no te lo cuenten tarde.", "¿Lo sabías?"),
    ],
    "hooks": [
     "Una sanción de Hacienda casi nunca viene de un fraude. Viene de un plazo que se pasó.",
     "El error no fue no pagar. Fue no saber que tenías que presentar algo ese mes.",
     "Sanción típica de autónomo: 200€ por un modelo informativo A CERO que no presentó. A cero. Duele doble.",
     "El modelo 347, el 390, el censo... los 'informativos' no pagan nada y sancionan igual si faltan.",
     "Cambiar de actividad o dirección sin comunicarlo (modelo 036/037): la sanción silenciosa.",
     "Las sanciones tienen descuento: conformidad + pronto pago = hasta 40% menos. Casi nadie lo usa bien.",
     "¿Cuánto te ha costado ya algún despiste con Hacienda? Ese dinero era evitable al 100%.",
     "La sanción más tonta del catálogo: no atender el buzón electrónico. Literalmente por no mirar el correo.",
     "Baja de autónomos mal hecha = seguir generando obligaciones de un negocio que ya no existe.",
     "Autónomo sin actividad no significa autónomo sin modelos. Ese matiz genera sanciones a diario.",
     "Cada sanción evitable que pagas es el sueldo de un buen calendario fiscal. Para varios años.",
    ],
   },
   "Calendario fiscal": {
    "pares": [
     ("Un calendario fiscal simple —tus 4-6 fechas del año— evita la mayoría de sanciones. Así de tonto.", "Escríbeme PLAZOS"),
     ("No necesitas saber fiscalidad: necesitas saber TUS fechas y quién te las prepara.", "Guárdalo"),
     ("El calendario fiscal claro es la diferencia entre estrés trimestral y rutina de 30 minutos.", "¿Tienes el tuyo?"),
    ],
    "hooks": [
     "Tu año fiscal cabe en 6 fechas. Te las apunto y no vuelves a llevarte sustos.",
     "Un calendario fiscal en la nevera evita más sanciones que cualquier asesor caro.",
     "Enero es el mes trampa: trimestre + resumen anual + 347 + Renta acechando. Se sobrevive con lista.",
     "Cada autónomo tiene SU calendario según sus modelos. El genérico de internet no es el tuyo.",
     "Mi trabajo, resumido: que ninguna fecha fiscal te pille de sorpresa nunca más.",
     "Las alarmas del móvil también valen para Hacienda: 4 avisos al año y a dormir tranquila.",
     "El calendario fiscal no es para ti: es para tu cabeza, que deja de vigilar fechas en segundo plano.",
     "Fechas fiscales + 10 días de margen para preparar = la fórmula anti-recargo definitiva.",
     "¿Sabes qué modelos TE tocan a ti? Esa lista corta es el 80% de tu tranquilidad fiscal.",
     "Un negocio con calendario fiscal presenta en plazo aunque el dueño esté de vacaciones.",
     "Deja de memorizar fechas: sistematízalas una vez y olvídate para siempre.",
    ],
   },
   "Regularizar antes": {
    "pares": [
     ("Regularizar antes de que te reclamen siempre sale más barato: es la regla de oro del sistema.", "Escríbeme FISCAL"),
     ("Un error fiscal descubierto por ti es un recargo; descubierto por ellos, una sanción.", "Guárdalo"),
     ("Nunca es tarde para ponerse al día, pero cada mes que pasa es un poco más caro.", "¿Hablamos de tu caso?"),
    ],
    "hooks": [
     "Regularizar antes de que te reclamen sale más barato. Siempre. Sin excepciones.",
     "Encontré un error en mi declaración de hace 2 años: ¿lo toco o lo dejo? Se toca. Te explico por qué.",
     "La complementaria: el botón de 'arreglarlo por las buenas' que casi nadie sabe que existe.",
     "Si el error fue a tu favor, rectificar también funciona al revés: puedes recuperar dinero de hasta 4 años.",
     "Dormir con un error fiscal conocido es pagarlo dos veces: en dinero futuro y en cabeza presente.",
     "Hacienda distingue entre error y ocultación. Corregir voluntariamente te coloca en el lado bueno.",
     "El plazo de prescripción son 4 años. Pero esperar la prescripción es un plan, no una estrategia.",
     "Cada trimestre que se presenta corrigiendo el anterior demuestra algo bueno: que alguien está mirando.",
     "'Mejor no remover' es el consejo de bar más caro de la fiscalidad española.",
     "Arreglar un descuido de 500€ hoy cuesta 505€. En una inspección, puede costar 750€ o más.",
     "La tranquilidad de tener TODO al día no cotiza en bolsa, pero se nota cada noche.",
    ],
   },
  },
 },
 "Gestión fiscal": {
  "afecta": "cómo llevas los papeles de tu negocio",
  "cierre": "{subtema} bien resuelto te devuelve horas y sustos: la fiscalidad ordenada es tiempo y margen, no burocracia.",
  "subtemas": {
   "Gestoría vs asesoría": {
    "pares": [
     ("Una gestoría presenta modelos; una asesoría te avisa ANTES de que las cosas pasen. Son servicios distintos.", "Escríbeme ASESORIA"),
     ("Lo barato de una gestoría que solo presenta sale caro en deducciones perdidas y avisos que no llegan.", "Guárdalo"),
     ("La pregunta clave a tu gestoría: '¿me avisarás de lo que me conviene, o solo de lo que me toca?'.", "¿Qué tienes tú?"),
    ],
    "hooks": [
     "Tu gestoría presenta tus modelos. ¿Pero alguien MIRA tus números? No es lo mismo.",
     "Diferencia entre gestoría y asesoría en una frase: una rellena, la otra piensa contigo.",
     "'Mi gestor no me avisó' — la frase más repetida en las primeras reuniones conmigo.",
     "Pagas 50€/mes de gestoría y pierdes 200€/mes en deducciones no aplicadas. La cuenta sale mal.",
     "Si solo hablas con tu gestoría 4 veces al año (los días 18), tienes un presentador, no un asesor.",
     "Tu gestoría debería hacerte preguntas. Si solo te pide papeles, algo falta.",
     "El asesor bueno no es el que te ahorra más: es el que te explica por qué y te avisa a tiempo.",
     "Enterarte de Verifactu por Instagram y no por tu gestoría: señal para reflexionar.",
     "Cambiar de asesoría da pereza. Quedarse en una que no te mira los números da pérdidas.",
     "Una asesoría que te conoce detecta en 10 minutos lo que un formulario nunca detectará.",
     "No necesitas la asesoría más grande: necesitas una que sepa tu nombre y tu sector.",
    ],
   },
   "Facturas bien hechas": {
    "pares": [
     ("Una factura completa lleva: número correlativo, fecha, NIF de ambos, concepto claro, base, IVA y total.", "Escríbeme FISCAL"),
     ("Facturar bien es gratis; las facturas mal numeradas o incompletas acaban costando en cualquier revisión.", "Guárdalo"),
     ("El concepto de la factura importa: 'servicios varios' es una invitación a preguntas.", "¿Las tuyas cumplen?"),
    ],
    "hooks": [
     "Tu factura tiene 7 datos obligatorios. La mayoría de facturas 'caseras' incumple 2.",
     "Facturas numeradas 1, 2, 5, 8... esos saltos cuentan una historia que no quieres contar.",
     "'Servicios varios — 500€' como concepto: la frase favorita de cualquier inspector.",
     "¿Factura sin IVA? Solo en casos concretos y citando la exención. 'Es que soy pequeño' no es uno.",
     "La numeración de facturas reinicia cada año o sigue: elige UNA regla y no la cambies jamás.",
     "Factura emitida y nunca cobrada: sigue contando para el IVA salvo que hagas el proceso de rectificar.",
     "El descuento que aplicas debe verse EN la factura, no en un acuerdo verbal aparte.",
     "Facturar a un particular y a una empresa no es igual: retenciones y datos cambian.",
     "Tu factura es tu imagen: una factura profesional cobra antes que un Word torcido.",
     "Rectificar una factura tiene su método (factura rectificativa). Borrarla y hacer otra, no es el método.",
     "La fecha de la factura marca su trimestre. 'La hago con fecha de la semana pasada' tiene consecuencias.",
    ],
   },
   "Separar dinero de impuestos": {
    "pares": [
     ("El IVA que cobras y el IRPF que adelantarás no son tuyos: sepáralos al cobrar y los trimestres dejan de doler.", "Escríbeme AHORRO"),
     ("La regla simple: de cada cobro, aparta un porcentaje fijo a otra cuenta. Sin excepciones.", "Guárdalo"),
     ("Los impuestos no son un imprevisto: son el gasto más previsible de tu año.", "¿Los apartas?"),
    ],
    "hooks": [
     "El truco financiero más simple del autónomo: el IVA no es tuyo. Apártalo el día que cobras.",
     "Cada trimestre el mismo drama: 'no tengo para el IVA'. Sí tenías: el día que cobraste cada factura.",
     "Una segunda cuenta solo para impuestos cambia tu vida fiscal más que cualquier app.",
     "¿Qué porcentaje apartar de cada cobro? Te doy la fórmula según tu actividad.",
     "Gastarse el IVA es pedirle un préstamo a Hacienda sin querer. Y Hacienda cobra puntual.",
     "El autónomo que aparta un 25% de cada cobro no conoce el estrés del día 20.",
     "Tus impuestos anuales son casi los mismos cada año. Que te sorprendan 4 veces al año es opcional.",
     "Cobras 1.000€ + IVA y piensas 'tengo 1.210€'. Tienes 1.000€. Y quizá menos. Esa mentalidad lo cambia todo.",
     "Aparta impuestos como pagas el alquiler: primero, fijo y sin negociar contigo misma.",
     "El colchón fiscal no es avaricia bancaria: es dormir bien 365 noches al año.",
     "Si necesitas financiar el pago del trimestre, el aviso llegó hace meses: revisemos el sistema.",
    ],
   },
   "Autónomo o SL": {
    "pares": [
     ("El salto a SL no va solo de facturación: va de responsabilidad, imagen y números concretos. Se calcula, no se intuye.", "Escríbeme FISCAL"),
     ("Constituir una SL 'porque queda mejor' sin echar números es pagar más por parecer más.", "Guárdalo"),
     ("Hay un punto donde la SL compensa de verdad. Está en TUS números, no en los del vecino.", "¿Echamos la cuenta?"),
    ],
    "hooks": [
     "'¿Me hago SL?' — la pregunta que todo autónomo se hace en el año bueno. La respuesta está en 3 números.",
     "El mito de los 40.000€: no hay cifra mágica para pasarse a SL. Hay una cuenta personalizada.",
     "Ser SL no te ahorra impuestos automáticamente: mueve las piezas de sitio. A veces a peor.",
     "La SL protege tu patrimonio personal... si haces las cosas bien. Si no, el juez levanta el velo.",
     "Autónomo societario: el híbrido que muchos descubren tarde, con su cuota y sus reglas propias.",
     "Una SL cuesta dinero cada año aunque no factures: contabilidad, registro, impuesto de sociedades.",
     "Pagarte sueldo o dividendos desde tu SL: dos caminos con impuestos distintos. Se elige con calculadora.",
     "El cliente grande que 'solo trabaja con SL' existe: a veces la sociedad se justifica por mercado, no por impuestos.",
     "Facturar 100.000€ como autónomo puede salir mejor que 60.000€ mal montados en SL.",
     "Montar la SL es fácil; lo caro es mantenerla sin necesitarla.",
     "De autónomo a SL hay un buen momento del año para saltar. Y no es diciembre a lo loco.",
    ],
   },
   "Cierre de año": {
    "pares": [
     ("Diciembre es el último mes para mover fichas fiscales: en enero, la foto del año ya está hecha.", "Escríbeme FISCAL"),
     ("El cierre de año fiscal se juega en noviembre-diciembre: aportaciones, gastos, inversiones y calendario.", "Guárdalo"),
     ("Una hora de revisión en noviembre vale más que tres gestiones en abril.", "¿Cerramos bien el año?"),
    ],
    "hooks": [
     "Lo que hagas antes del 31 de diciembre cuenta en ESTA Renta. Lo del 1 de enero, en la siguiente.",
     "El plan de pensiones aportado en diciembre desgrava este año. En enero, ya no. Detalles que valen dinero.",
     "Noviembre es el mes de mirar la foto: ¿cómo va tu año fiscal? Aún puedes retocarla.",
     "¿Comprar ese equipo ahora o en enero? La respuesta depende de cómo va tu año. Se calcula en 10 minutos.",
     "El cierre de año del autónomo en 5 preguntas: te las paso antes de que sea tarde.",
     "Facturar ese proyecto el 28 de diciembre o el 2 de enero cambia tu Renta. Elige con números.",
     "Diciembre: revisar gastos pendientes de facturar, deducciones sin usar y el tramo de cuota. Media mañana.",
     "Los seguros, cuotas y suscripciones anuales pagados en diciembre entran en este año. Adelántalos si conviene.",
     "El año fiscal no acaba en Nochevieja para ti: acaba cuando cuadras los números ANTES de Nochevieja.",
     "Enero siempre trae la frase 'ojalá lo hubiera mirado en diciembre'. Este año no.",
     "Un buen cierre de año no es maquillaje: es usar las reglas del juego a tu favor, en plazo.",
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
                f'traduciendo la jerga a lenguaje llano con un ejemplo concreto. Cierre (16-20s): qué hacer ahora, en una frase, sin alarmismo.')
    if formato == "Carrusel":
        return (f'Portada: "{hook}". Slides 2-6: desarrollar {st} en pasos, errores o claves concretas, '
                f'una idea por slide y siempre en lenguaje llano. Slide de cierre: resumen + CTA.')
    return (f'Foto o imagen tuya/del despacho. Caption cercano sobre {st}, '
            f'traduciendo la norma a lenguaje llano y conectándola con un caso real (sin datos personales).')

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

salida = "window.IDEAS_FISCALIDAD = " + json.dumps(filas, ensure_ascii=False) + ";\n"
cabecera = "// Banco de contenido — FISCALIDAD (365 días).\n"
with open("datos-ideas-fiscalidad.js", "w", encoding="utf-8") as f:
    f.write(cabecera + salida)
print("OK ->", len(filas), "días")
