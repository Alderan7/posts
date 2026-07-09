/* ═══════════════════════════════════════════════════════════
   CALENDARIO VIRAL — 30 días de contenido YA REDACTADO
   ───────────────────────────────────────────────────────────
   Funciona SIN IA. Cada día trae:
   - slide : la PORTADA (gancho + formato viral). Es lo que se ve en la tarjeta.
   - desarrollo (solo Carrusel): slides intermedios YA escritos → el día genera
     un CARRUSEL COMPLETO (portada → desarrollo → cierre CTA) sin tocar la IA.
   Reel / Historia / Post = una sola pieza (su portada).

   slide.tipo: nota | chat | versus | frase | lista | claves | numero
   - "chat": items con prefijo "cliente:"/"yo:"/"IA:"
   - "versus": items = ["Etiqueta::texto", "Etiqueta::texto"]
   - *palabra* entre asteriscos = azul de marca
   ═══════════════════════════════════════════════════════════ */
window.RM_CALENDARIO = [
 {n:1, formato:"Reel", pilar:"Marketing", cta:"Guárdalo", slide:{
   tipo:"nota", fondo:"dark", eye:"MARKETING · VISIBILIDAD",
   head:"No necesitas más seguidores",
   body:"Necesitas que 100 personas correctas sepan que existes.\n\nLa visibilidad no es alcance: es precisión. Llegar a quien ya puede comprarte, no a todo el mundo.\n\nDeja de perseguir números y empieza a elegir a quién llegas.",
   cta:"Guárdalo"}},

 {n:2, formato:"Carrusel", pilar:"Fiscalidad", cta:"Compártelo con tu gestor", slide:{
   tipo:"versus", fondo:"dark", eye:"FISCALIDAD",
   head:"Lo que crees que te ahorra impuestos\ny lo que de verdad lo hace",
   items:["Lo que crees::Guardar todos los tickets y meter cuantos más gastos, mejor.","La realidad::Deducir bien los gastos que SÍ tocan: con factura y afectos a tu actividad. Calidad, no cantidad."],
   cta:"Compártelo con tu gestor"},
  desarrollo:[
   {tipo:"lista", fondo:"light", eye:"FISCALIDAD", head:"3 gastos que la gente olvida deducir",
    items:["*Formación* relacionada con tu sector.","*Software* y herramientas que usas para trabajar.","*Cuota* de autónomo y seguros ligados a tu actividad."], cta:""},
   {tipo:"frase", fondo:"dark", eye:"FISCALIDAD", head:"Deducir bien no es arriesgado.\nEs tu *derecho*, con factura y sentido común.", body:"", cta:""}]},

 {n:3, formato:"Post", pilar:"Mentalidad", cta:"Cuéntame tu caso", slide:{
   tipo:"frase", fondo:"light", eye:"MENTALIDAD",
   head:"Tu facturación es el espejo\nde tus hábitos, no de tu suerte.",
   body:"Los negocios estables se construyen. No se ganan en una rifa.",
   cta:"Cuéntame tu caso"}},

 {n:4, formato:"Reel", pilar:"IA", cta:"Escríbeme IA", slide:{
   tipo:"chat", fondo:"dark", eye:"INTELIGENCIA ARTIFICIAL",
   head:"Este mensaje resume por qué automatizar 👇",
   body:"Cliente",
   items:["cliente: Rosa, no tenía tiempo ni para responder mensajes","cliente: Ahora la IA me prepara respuestas y publicaciones","yo: ¿Cuántas horas dirías que recuperas a la semana?","cliente: Fácil 10. Y las uso en lo que de verdad da dinero"],
   cta:"Escríbeme IA"}},

 {n:5, formato:"Carrusel", pilar:"Autoridad", cta:"Guárdalo para revisarlo", slide:{
   tipo:"lista", fondo:"dark", eye:"AUTORIDAD",
   head:"5 señales de que tu empresa\nes mejor de lo que el mercado cree",
   items:["*Repites clientes* pero casi nadie nuevo te descubre.","Te *recomiendan*, pero no puedes provocar que pase.","Tu competencia *comunica mejor* y capta lo que tú harías mejor.","Sabes que tu trabajo *vale más* de lo que cobras.","Cada mes empiezas *de cero* a buscar clientes."],
   cta:"Guárdalo para revisarlo"},
  desarrollo:[
   {tipo:"frase", fondo:"blue", eye:"AUTORIDAD", head:"El problema no es tu *trabajo*.\nEs que el mercado no lo *ve*.", body:"", cta:""},
   {tipo:"lista", fondo:"light", eye:"AUTORIDAD", head:"Hazlo visible",
    items:["Muestra *casos reales*, no frases genéricas.","Habla de *resultados*, no de tareas.","Aparece *tú*: la gente confía en personas."], cta:""}]},

 {n:6, formato:"Historia", pilar:"Conversión", cta:"Escríbeme ESTRATEGIA", slide:{
   tipo:"chat", fondo:"dark", eye:"CONVERSIÓN",
   head:"Así empieza una conversación\nque acaba en cliente",
   body:"Nuevo contacto",
   items:["cliente: Hola, vi tu contenido y creo que necesito justo esto","cliente: ¿Cómo trabajas y por dónde empezaríamos?","yo: Primero miramos tus números y tu visibilidad","yo: Y de ahí sale el plan. Sin humo."],
   cta:"Escríbeme ESTRATEGIA"}},

 {n:7, formato:"Reel", pilar:"Storytelling", cta:"Cuéntame si te suena", slide:{
   tipo:"nota", fondo:"dark", eye:"HISTORIA REAL",
   head:"Vender más no siempre es crecer",
   body:"Conocí un negocio que facturaba muchísimo.\n\nY su dueño no dormía: márgenes mínimos, todo dependía de él, cero previsibilidad.\n\nEl problema no eran las ventas. Era la falta de sistema.\n\nCrecer es ganar tranquilidad, no solo facturar.",
   cta:"Cuéntame si te suena"}},

 {n:8, formato:"Carrusel", pilar:"Marketing", cta:"Guárdalo", slide:{
   tipo:"versus", fondo:"dark", eye:"MARKETING",
   head:"Marketing que gusta\ny marketing que vende",
   items:["Lo que gusta::Likes, alcance y comentarios bonitos. Sienta bien, pero no llena la agenda.","Lo que vende::Un mensaje claro a la persona correcta con una acción concreta. Menos aplausos, más clientes."],
   cta:"Guárdalo"},
  desarrollo:[
   {tipo:"lista", fondo:"light", eye:"MARKETING", head:"Qué hace que un contenido venda",
    items:["Un *hook* que frena el scroll en el primer segundo.","Una idea *clara*, no cinco a medias.","Una *llamada* concreta a actuar."], cta:""},
   {tipo:"frase", fondo:"blue", eye:"MARKETING", head:"Los likes no pagan facturas.\nLos *clientes*, sí.", body:"", cta:""}]},

 {n:9, formato:"Post", pilar:"Fiscalidad", cta:"Cuéntame cómo lo llevas", slide:{
   tipo:"frase", fondo:"blue", eye:"FISCALIDAD",
   head:"El dinero que no controlas hoy\nes el susto que te llevas en junio.",
   body:"Media hora al mes con tus números evita el agobio de la declaración.",
   cta:"Cuéntame cómo lo llevas"}},

 {n:10, formato:"Reel", pilar:"IA", cta:"Escríbeme IA", slide:{
   tipo:"versus", fondo:"dark", eye:"INTELIGENCIA ARTIFICIAL",
   head:"Lo que crees de la IA\ny lo que ya hace tu competencia",
   items:["Lo que crees::Es complicada, es para técnicos y no es para mi negocio.","La realidad::Tu competencia ya la usa para producir el doble en la mitad de tiempo. Y se nota."],
   cta:"Escríbeme IA"}},

 {n:11, formato:"Carrusel", pilar:"Crecimiento", cta:"Guárdalo", slide:{
   tipo:"lista", fondo:"dark", eye:"CRECIMIENTO",
   head:"Por qué unas empresas crecen\ny otras, haciendo lo mismo, se estancan",
   items:["*Visibilidad*: que el mercado sepa que existes, no solo tus clientes de siempre.","*Números claros*: decidir por datos, no por intuición.","*Sistema*: que el negocio no dependa solo de ti.","*Foco*: dejar de perseguir a todos para atraer a los correctos."],
   cta:"Guárdalo"},
  desarrollo:[
   {tipo:"frase", fondo:"blue", eye:"CRECIMIENTO", head:"Hacer bien tu trabajo es el *mínimo*.\nNo es lo que te hace *crecer*.", body:"", cta:""},
   {tipo:"lista", fondo:"light", eye:"CRECIMIENTO", head:"Lo que sí te hace crecer",
    items:["Que te *conozcan*: visibilidad constante.","Decidir por *datos*, no por intuición.","Un *sistema* que no dependa solo de ti."], cta:""}]},

 {n:12, formato:"Historia", pilar:"Autoridad", cta:"Cuéntame tu experiencia", slide:{
   tipo:"nota", fondo:"dark", eye:"AUTORIDAD",
   head:"Lo que nadie te dice\nde tener buena reputación",
   body:"Puedes ser el mejor de tu zona.\n\nPero si esa reputación no es visible, no capta clientes nuevos: se queda entre quienes ya te conocen.\n\nLa autoridad hay que hacerla pública. No esperar a que el boca a boca haga el trabajo.",
   cta:"Cuéntame tu experiencia"}},

 {n:13, formato:"Reel", pilar:"Conversión", cta:"Escríbeme SISTEMA", slide:{
   tipo:"chat", fondo:"dark", eye:"CONVERSIÓN",
   head:"El DM que llega cuando\nel contenido hace su trabajo",
   body:"Cliente potencial",
   items:["cliente: Llevo semanas leyéndote","cliente: No necesito que me convenzas, ya lo tengo claro","cliente: ¿Cómo empezamos?","yo: Así de fácil cuando el contenido explica bien lo que haces 💙"],
   cta:"Escríbeme SISTEMA"}},

 {n:14, formato:"Carrusel", pilar:"Storytelling", cta:"Guárdalo", slide:{
   tipo:"chat", fondo:"dark", eye:"HISTORIA REAL",
   head:"La conversación que le cambió\nel negocio a un cliente",
   body:"Cliente",
   items:["cliente: Trabajo muchísimo pero no despego","yo: ¿Cuánta gente nueva sabe cada mes que existes?","cliente: ...pocas, la verdad","yo: Ahí está el cuello de botella. No trabajas poco: no te ven."],
   cta:"Guárdalo"},
  desarrollo:[
   {tipo:"frase", fondo:"light", eye:"HISTORIA REAL", head:"No trabajaba poco.\nSimplemente, nadie nuevo sabía que *existía*.", body:"", cta:""},
   {tipo:"lista", fondo:"dark", eye:"HISTORIA REAL", head:"Lo que cambió en 30 días",
    items:["Empezó a *mostrarse* cada semana.","Un *mensaje claro* de a quién ayuda.","Dejó de *esperar* al boca a boca."], cta:""}]},

 {n:15, formato:"Post", pilar:"Mentalidad", cta:"¿Te pasa? Cuéntamelo", slide:{
   tipo:"frase", fondo:"light", eye:"MENTALIDAD",
   head:"No te falta tiempo.\nTe falta un sistema que no dependa de ti.",
   body:"Trabajar más horas no escala. Un sistema, sí.",
   cta:"¿Te pasa? Cuéntamelo"}},

 {n:16, formato:"Reel", pilar:"Marketing", cta:"Guárdalo", slide:{
   tipo:"nota", fondo:"dark", eye:"MARKETING · VISIBILIDAD",
   head:"Llevo años viendo negocios por dentro",
   body:"Y esto es lo que separa a los que crecen de los que se estancan:\n\nno es trabajar más, ni bajar precios, ni tener suerte.\n\nEs que el mercado correcto sepa que existen. La visibilidad estratégica gana a la suerte. Siempre.",
   cta:"Guárdalo"}},

 {n:17, formato:"Carrusel", pilar:"Fiscalidad", cta:"Compártelo con quien lo necesite", slide:{
   tipo:"lista", fondo:"dark", eye:"FISCALIDAD",
   head:"4 gastos que SÍ puedes deducir\ny puede que no estés deduciendo",
   items:["*Formación* relacionada con tu actividad.","*Software y herramientas* que usas para trabajar.","*Suministros* de tu espacio de trabajo (con sus reglas).","*Servicios profesionales*: gestoría, asesoría, marketing."],
   cta:"Compártelo con quien lo necesite"},
  desarrollo:[
   {tipo:"frase", fondo:"blue", eye:"FISCALIDAD", head:"Deducir de más asusta.\nDeducir de *menos* te cuesta dinero cada año.", body:"", cta:""},
   {tipo:"claves", fondo:"light", eye:"FISCALIDAD", head:"La regla de oro",
    items:["Que sea *de tu actividad*.","Que tengas *factura*.","Que puedas *justificarlo*."], cta:""}]},

 {n:18, formato:"Reel", pilar:"IA", cta:"Escríbeme IA", slide:{
   tipo:"chat", fondo:"dark", eye:"INTELIGENCIA ARTIFICIAL",
   head:"Le pedí esto a la IA\ny me ahorró una tarde",
   body:"Asistente",
   items:["yo: Resúmeme esta reunión de 40 min en 5 puntos claros","yo: Y escríbeme el email de seguimiento","IA: Hecho ✅ Te dejo ambos listos","yo: Lo que me llevaba una hora, en 20 segundos"],
   cta:"Escríbeme IA"}},

 {n:19, formato:"Carrusel", pilar:"Autoridad", cta:"Guárdalo", slide:{
   tipo:"versus", fondo:"dark", eye:"AUTORIDAD",
   head:"Autoridad real\ny postureo en redes",
   items:["Postureo::Frases motivadoras, foto perfecta y cero pruebas. Parece experto.","Autoridad real::Casos, datos y criterio que se demuestra. No lo dices tú: lo dicen tus resultados."],
   cta:"Guárdalo"},
  desarrollo:[
   {tipo:"lista", fondo:"light", eye:"AUTORIDAD", head:"Cómo se demuestra autoridad de verdad",
    items:["Con *casos* concretos, no promesas.","Con *datos* y números reales.","Con *criterio*: dices por qué, no solo qué."], cta:""},
   {tipo:"frase", fondo:"blue", eye:"AUTORIDAD", head:"La autoridad no se *proclama*.\nSe *demuestra*.", body:"", cta:""}]},

 {n:20, formato:"Historia", pilar:"Conversión", cta:"Escríbeme ESTRATEGIA", slide:{
   tipo:"nota", fondo:"dark", eye:"CONVERSIÓN",
   head:"El cliente perfecto\nno te encuentra por casualidad",
   body:"Llega porque dejaste un camino claro hasta ti:\n\nun mensaje que le habla a él, contenido que resuelve su duda y una acción sencilla para dar el paso.\n\nLa casualidad no es una estrategia. El camino, sí.",
   cta:"Escríbeme ESTRATEGIA"}},

 {n:21, formato:"Reel", pilar:"Crecimiento", cta:"Guárdalo", slide:{
   tipo:"versus", fondo:"dark", eye:"CRECIMIENTO",
   head:"Trabajar más\ny trabajar con criterio",
   items:["Trabajar más::Más horas, más cansancio, mismos resultados. El techo lo pones tú.","Trabajar con criterio::Mejores decisiones, más margen y menos desgaste. El negocio trabaja para ti."],
   cta:"Guárdalo"}},

 {n:22, formato:"Carrusel", pilar:"Marketing", cta:"Guárdalo para tu próximo post", slide:{
   tipo:"lista", fondo:"dark", eye:"MARKETING",
   head:"3 errores que hacen que tu contenido\nno venda (aunque tenga visitas)",
   items:["*Hook flojo*: si el primer segundo no engancha, no leen el resto.","*Sin llamada clara*: si no dices qué hacer, no hacen nada.","*Hablas a todos*: y quien habla a todos no le habla a nadie."],
   cta:"Guárdalo para tu próximo post"},
  desarrollo:[
   {tipo:"frase", fondo:"blue", eye:"MARKETING", head:"Muchas visitas y cero clientes\nno es problema de *alcance*.\nEs de *mensaje*.", body:"", cta:""},
   {tipo:"claves", fondo:"light", eye:"MARKETING", head:"Arréglalo así",
    items:["Primer segundo: un *hook* que pare el scroll.","Al final: una *acción* clara.","Siempre: háblale a *una* persona."], cta:""}]},

 {n:23, formato:"Post", pilar:"Fiscalidad", cta:"Cuéntame tu caso", slide:{
   tipo:"frase", fondo:"blue", eye:"FISCALIDAD",
   head:"Facturar mucho y ganar poco\ntambién es un problema fiscal.",
   body:"Mira el margen, no solo el ingreso. Ahí está tu rentabilidad real.",
   cta:"Cuéntame tu caso"}},

 {n:24, formato:"Reel", pilar:"Storytelling", cta:"Guárdalo", slide:{
   tipo:"chat", fondo:"dark", eye:"HISTORIA REAL",
   head:"El mensaje que resume\npor qué hago esto",
   body:"Cliente",
   items:["cliente: Rosa, este mes he dormido tranquilo por primera vez en años","cliente: Sé de dónde vienen mis clientes y cuánto voy a facturar","yo: Eso es lo que cambia tener un sistema","cliente: Gracias por no venderme humo 🙏"],
   cta:"Guárdalo"}},

 {n:25, formato:"Carrusel", pilar:"IA", cta:"Escríbeme IA", slide:{
   tipo:"lista", fondo:"dark", eye:"INTELIGENCIA ARTIFICIAL",
   head:"5 tareas que la IA puede hacer\npor tu negocio esta semana",
   items:["*Contenido*: ideas, guiones y publicaciones en minutos.","*Atención*: respuestas y seguimientos listos para enviar.","*Administración*: resúmenes, correos y textos repetitivos.","*Análisis*: entender tus números en lenguaje claro.","*Ideas*: desbloquear campañas cuando te quedas en blanco."],
   cta:"Escríbeme IA"},
  desarrollo:[
   {tipo:"numero", fondo:"blue", eye:"INTELIGENCIA ARTIFICIAL", head:"10h",
    body:"a la semana, recuperadas",
    items:["10h","Es el tiempo que la IA te quita en tareas repetitivas para que lo dediques a lo que da dinero."], cta:""},
   {tipo:"frase", fondo:"light", eye:"INTELIGENCIA ARTIFICIAL", head:"La IA no te *sustituye*.\nTe quita lo aburrido para que hagas lo que *importa*.", body:"", cta:""}]},

 {n:26, formato:"Historia", pilar:"Autoridad", cta:"Escríbeme AUTORIDAD", slide:{
   tipo:"chat", fondo:"dark", eye:"AUTORIDAD",
   head:"Así suena una recomendación\nque sí trae clientes",
   body:"Mensaje reenviado",
   items:["cliente: Un conocido me pasó tu cuenta","cliente: Me dijo 'esta sí sabe, y no vende humo'","yo: Esa es la mejor publicidad que existe","cliente: Por eso te escribo antes de mirar a nadie más"],
   cta:"Escríbeme AUTORIDAD"}},

 {n:27, formato:"Reel", pilar:"Conversión", cta:"Escríbeme SISTEMA", slide:{
   tipo:"nota", fondo:"dark", eye:"CONVERSIÓN",
   head:"Dejé de perseguir clientes\nel día que entendí esto",
   body:"Perseguir cansa y se nota: hueles a necesidad.\n\nAtraer es distinto: un mensaje claro, contenido que demuestra y una acción sencilla.\n\nDeja de correr detrás. Haz que vengan.",
   cta:"Escríbeme SISTEMA"}},

 {n:28, formato:"Carrusel", pilar:"Crecimiento", cta:"Guárdalo", slide:{
   tipo:"versus", fondo:"dark", eye:"CRECIMIENTO",
   head:"Empresa que depende de ti\ny empresa que funciona sin ti",
   items:["Depende de ti::Si paras, para todo. Vacaciones con el móvil. Techo de cristal.","Funciona sin ti::Sistemas, procesos y visibilidad. Creces aunque no estés delante."],
   cta:"Guárdalo"},
  desarrollo:[
   {tipo:"lista", fondo:"light", eye:"CRECIMIENTO", head:"Cómo se deja de depender de uno mismo",
    items:["*Procesos* escritos, no todo en tu cabeza.","*Sistemas* que captan aunque no estés.","*Visibilidad* que trabaja 24/7."], cta:""},
   {tipo:"frase", fondo:"blue", eye:"CRECIMIENTO", head:"Si tu negocio para cuando tú paras,\nno tienes una empresa: tienes un *empleo*.", body:"", cta:""}]},

 {n:29, formato:"Post", pilar:"Mentalidad", cta:"¿De acuerdo? Cuéntamelo", slide:{
   tipo:"frase", fondo:"light", eye:"MENTALIDAD",
   head:"Crecer con calma no es ir lento.\nEs no romper lo que ya funciona.",
   body:"El crecimiento sostenible aguanta. La prisa quema negocios.",
   cta:"¿De acuerdo? Cuéntamelo"}},

 {n:30, formato:"Reel", pilar:"Marketing", cta:"Escríbeme ESTRATEGIA", slide:{
   tipo:"chat", fondo:"dark", eye:"MARKETING",
   head:"El mensaje de cierre de mes\ncuando el contenido funciona",
   body:"Cliente",
   items:["cliente: Fin de mes y la agenda llena sin perseguir a nadie","yo: Eso es el contenido trabajando por ti","cliente: Ojalá haberlo hecho antes","yo: Nunca es tarde para dejar de depender de la suerte 💙"],
   cta:"Escríbeme ESTRATEGIA"}},
];
