/* ════════════════════════════════════════════════════════
   BANCO DE COPY — organizado por PILAR + ÁNGULO
   ════════════════════════════════════════════════════════ */

const PILARES_MAP = {
  dolor:      ['bocaboca','regateo','saturacion','tiempo','familia'],
  educativo:  ['sistema','autoridad','resultados','estabilidad'],
  autoridad:  ['autoridad','sistema','resultados','premium'],
  conversion: ['bocaboca','sistema','estabilidad','regateo'],
  reframe:    ['objecion','precio','bocaboca','saturacion'],
  servicio:   ['sistema','premium','resultados','autoridad'],
  objecion:   ['objecion','precio','regateo','margen'],
};

const ANGULO_LABELS = {
  bocaboca:   'Dependencia del boca a boca',
  regateo:    'Clientes que regatean',
  saturacion: 'Saturación y tiempo perdido',
  autoridad:  'Autoridad digital y percepción',
  tiempo:     'Recuperar tiempo y familia',
  familia:    'Cenar con la familia tranquilo',
  estabilidad:'Estabilidad e ingresos predecibles',
  premium:    'Atraer clientes premium',
  margen:     'Dejar de competir por precio',
  objecion:   'Objeciones al marketing',
  precio:     'Precio vs. posicionamiento',
  sistema:    'Sistema de captación predecible',
  resultados: 'Resultados reales con datos',
};

/* ═══════════════════════════════════════════
   NICHOS DE MARCA — Reformas / Marca Personal
   La marca personal: estratega de crecimiento que combina
   fiscalidad + marketing + IA. Idea de fondo: por qué unas
   empresas crecen y otras no.
   ═══════════════════════════════════════════ */
const NICHO = {
  reformas: {
    nombre:'Reformas',
    eye:'Media Buyer · Empresas de Reformas',
    hashtags:'#reformas #empresadereformas #marketingparareformas #metaads #googleads #reformasintegrales',
    persona:'media buyer estratégica especializada en Meta Ads y Google Ads para empresas de reformas en España',
    lector:'un gerente o dueño de empresa de reformas (40-55 años), saturado, escéptico con el marketing, dependiente del boca a boca, con familia que le espera en casa',
    tono:'elegante, directo, lenguaje de negocio. NUNCA tecnicismos (CTR, CPL, funnel, pixel). Habla de tus obras rentables, tu agenda cubierta, tus clientes de calidad, tu estabilidad, tu tiempo, tu familia, tu autoridad',
    ctaEj:'SISTEMA, AGENDA, OBRAS',
    pills:['Meta Ads','Google Ads','Estrategia a medida','Resultados medibles'],
    p2head:'Tú te centras en las obras.\nYo me centro en llenar tu agenda.',
    p2sub:'Estrategia que convierte. Resultados que se notan.',
    usaBanco:true
  },
  personal: {
    nombre:'Marca Personal',
    eye:'Estrategia · Fiscalidad · Marketing · IA',
    hashtags:'#crecimientoempresarial #estrategiaempresarial #marketingdigital #inteligenciaartificial #pymes #autonomos #negocios',
    persona:'estratega de crecimiento empresarial: empezaste como asesora fiscal viendo negocios desde dentro (sus números y resultados) y descubriste que muchas empresas buenas no crecen simplemente porque el mercado no sabe que existen. Hoy combinas FISCALIDAD, MARKETING e INTELIGENCIA ARTIFICIAL para ayudar a las empresas a crecer de forma sostenible',
    lector:'un autónomo, profesional independiente o dueño de pyme (servicios, despachos, reformas y más) que hace bien su trabajo pero no consigue crecer, va saturado y sin tiempo, y está escéptico con el humo del marketing',
    tono:'estratégico, analítico, directo y elegante. Sin humo ni promesas vacías. Conectas los números con la visibilidad y la tecnología. Tu gran idea de fondo: por qué unas empresas crecen y otras se estancan',
    ctaEj:'CRECER, ESTRATEGIA, DATOS',
    pills:['Estrategia','Datos y fiscalidad','Marketing','Inteligencia Artificial'],
    p2head:'Tú te centras en tu trabajo.\nYo, en que tu empresa crezca.',
    p2sub:'Números, visibilidad y tecnología que hacen crecer tu negocio.',
    usaBanco:false,
    angulos:{
      crecimiento:'por qué unas empresas crecen y otras se estancan aunque hagan bien su trabajo',
      visibilidad:'una empresa excelente que el mercado no conoce no puede crecer',
      datos:'tomar decisiones por números reales y no por intuición',
      ia:'usar la inteligencia artificial para producir más en menos tiempo',
      estrategia:'combinar fiscalidad, marketing e IA para crecer de forma sostenible',
      autoridad:'posicionarte como referente para atraer mejores clientes',
    },
    labels:{
      crecimiento:'Por qué unas empresas crecen',
      visibilidad:'Ser visible para crecer',
      datos:'Decisiones basadas en datos',
      ia:'IA aplicada a tu negocio',
      estrategia:'Estrategia de crecimiento global',
      autoridad:'Autoridad y posicionamiento',
    },
    pilares:{
      dolor:['crecimiento','visibilidad','datos'],
      educativo:['datos','ia','estrategia'],
      autoridad:['autoridad','estrategia','crecimiento'],
      conversion:['estrategia','visibilidad','autoridad'],
      reframe:['crecimiento','datos','ia'],
      servicio:['estrategia','ia','autoridad'],
      objecion:['visibilidad','datos','crecimiento'],
    }
  }
};
let _nicho = (localStorage.getItem('rm_nicho')==='personal') ? 'personal' : 'reformas';
function getNicho(){ return _nicho; }
function N(){ return NICHO[_nicho] || NICHO.reformas; }
function marcaEye(){ return N().eye; }
function setNicho(v){
  _nicho = (v==='personal') ? 'personal' : 'reformas';
  localStorage.setItem('rm_nicho', _nicho);
  const lbl = document.getElementById('nichoLbl'); if(lbl) lbl.textContent = N().nombre;
  if(typeof actualizarAngulos==='function') actualizarAngulos();
}

const BANCO = {
  angulos: {
    bocaboca:   "dependencia del boca a boca y por qué destruye la estabilidad de una empresa de reformas",
    regateo:    "clientes que solo te piden precio, visitas perdidas y tiempo que te roban",
    saturacion: "tu saturación: vives atrapado entre obra, presupuestos y familia",
    autoridad:  "por qué una empresa peor puede captar más obras solo por comunicar mejor",
    sistema:    "cómo un sistema de captación predecible cambia la vida de una empresa de reformas",
    tiempo:     "recuperar tiempo, cenar con la familia y dejar de ser esclavo del propio negocio",
    familia:    "el coste real de un negocio sin sistema: tardes perdidas, cenas frías y fines de semana robados",
    premium:    "cómo atraer clientes de alto ticket que no regatean y respetan el presupuesto",
    objecion:   "objeciones al marketing digital en el sector reformas y cómo responderlas",
    precio:     "dejar de competir por precio y empezar a competir por autoridad y confianza",
    estabilidad:"estabilidad, previsibilidad y tranquilidad para empresas de reformas",
    margen:     "aumentar el ticket medio sin perder clientes dejando de ser el más barato",
    resultados: "resultados reales de campañas en el sector reformas con datos concretos",
  },

  hooks: {
    bocaboca:[
      "Llevas 15 años haciendo reformas perfectas.\n\nY el mes que viene no sabes si tendrás obras.",
      "El boca a boca no es una estrategia.\n\nEs rezar para que alguien te recomiende antes de que se acabe el mes.",
      "Tu empresa funciona por recomendación.\n\nEl problema es que no puedes encenderlo cuando lo necesitas.",
      "Llevas 20 años de experiencia.\n\nY este mes solo te han entrado 2 presupuestos.\n\nEsto es lo que puede cambiarlo.",
      "5 señales de que tu empresa de reformas depende demasiado del boca a boca.",
    ],
    regateo:[
      "3 visitas esta semana.\n\n3 presupuestos enviados.\n\n0 obras cerradas.\n\nEl problema no está en tu precio.",
      "Cada visita a alguien que solo busca el precio más bajo te roba algo que no vuelve: tu tarde.",
      "La mayoría no tiene problema de clientes.\n\nTiene problema de filtros.",
      "Si tu formulario de contacto tiene solo un campo, estás invitando a entrar a quien no puede pagarte.",
      "¿Cuántas horas al mes pierdes en presupuestos que nunca se cierran?",
    ],
    saturacion:[
      "Mañana: obra.\nMediodía: proveedor.\nTarde: visita comercial.\nNoche: presupuestos.\n\nAsí no se crece. Así se sobrevive.",
      "El mayor problema de tu empresa de reformas no es la competencia.\n\nEres tú, intentando hacerlo todo.",
      "Cuando todo depende de ti, tu negocio no es libre.\n\nTú tampoco.",
      "Tu negocio debería darte tranquilidad.\n\nNo ansiedad.",
      "Lo que más desgasta no es trabajar mucho.\n\nEs trabajar sin previsibilidad.",
    ],
    autoridad:[
      "Hay empresas de reformas peores que la tuya cerrando obras mejores.\n\nNo es casualidad. Es percepción.",
      "Tu calidad técnica es impecable.\n\nEl problema es que nadie lo sabe antes de verte.",
      "La imagen digital de tu empresa decide a qué tipo de cliente atraes antes de que digas una sola palabra.",
      "Si tus redes no transmiten autoridad, estás perdiendo obras sin darte cuenta.",
      "La diferencia entre una empresa que atrae clientes premium y una que pelea por precio\na menudo es solo una: la percepción.",
    ],
    sistema:[
      "12 leads cualificados en 7 días.\n\nNinguno preguntó por el precio antes de la visita.",
      "Hay una diferencia entre recibir contactos y tener un sistema que filtra, cualifica y llena agenda.\n\nSolo uno da estabilidad.",
      "Dejar de depender del boca a boca cambia más que tu facturación.\n\nCambia cómo duermes.",
      "De 2 presupuestos al mes a lista de espera de 6 semanas.\n\nSolo cambió el sistema de captación.",
      "La estabilidad no llega sola.\n\nSe construye.",
    ],
    tiempo:[
      "El verdadero lujo no es un coche mejor.\n\nEs poder apagar el móvil a las 19:00.",
      "Construiste una empresa para vivir mejor.\n\nNo para vivir estresado.",
      "¿Cuántas tardes más vas a cambiar por visitas que no valen la pena?",
      "Tu tiempo vale demasiado como para regalarlo en presupuestos que no se cierran.",
      "Cenar con tu familia con la mente despejada.\n\nEso también es un KPI.",
    ],
    familia:[
      "¿Cuándo fue la última vez que llegaste a casa antes de las 21:00 sin pendientes en la cabeza?",
      "Tu familia no necesita más dinero.\n\nNecesita más de ti presente.",
      "Construiste una empresa para darles una vida mejor.\n\nNo para perderte la suya.",
      "El verdadero coste de no tener sistema no aparece en la facturación.\n\nAparece en casa.",
      "Puedes trabajar 60 horas a la semana y ganar menos que quien trabaja 40 con un sistema que funciona.",
    ],
    premium:[
      "No necesitas más clientes.\n\nNecesitas mejores clientes.",
      "Hay un tipo de cliente que no regatrea, respeta los plazos y te recomienda después.\n\nCómo llegar a él.",
      "Cuando subes el precio y mejoras cómo te comunicas, el tipo de cliente cambia.\n\nSiempre.",
      "Una empresa premium no corre detrás de cualquier presupuesto.\n\nElige sus obras.",
      "Lo que mira un cliente de alto ticket antes de pedirte presupuesto.",
    ],
    objecion:[
      "«Ya probé publicidad y no funcionó.»\n\nQuizá tú también lo has pensado.\n\nY suele decirlo quien luego tiene los mejores resultados.",
      "No probaste publicidad.\n\nProbaste visibilidad sin estrategia de cualificación. Son cosas muy distintas.",
      "«Instagram no funciona para reformas.»\n\nNo. Instagram sin estrategia no funciona. Con estrategia, es otra historia.",
      "«No tengo tiempo para esto.»\n\nPrecisamente por eso necesitas que funcione sin depender de tu tiempo.",
      "Si el problema fuera la publicidad, empresas peores que la tuya no estarían llenando agenda.",
    ],
    precio:[
      "Competir por precio es lo que ocurre cuando tu empresa no transmite suficiente autoridad.",
      "La calidad técnica sin autoridad visual deja dinero encima de la mesa.",
      "Subir precios sin cambiar cómo comunicas tu empresa solo ahuyenta clientes.\n\nCambiar ambas cosas los atrae mejores.",
      "Si el cliente llega preguntando por precio antes de ver tu trabajo, el problema está antes de la visita.",
      "Menos curiosos. Más obras rentables.\n\nEso es lo que da un buen filtro de captación.",
    ],
    margen:[
      "No es subir precios.\n\nEs mejorar cómo percibes valor antes de que el cliente decida.",
      "El cliente que solo mira el precio es el cliente que nunca debiste atraer.",
      "Más obras a menor precio no es crecer.\n\nEs desgastarse más por menos.",
      "Cuando tu posicionamiento mejora, el ticket sube sin que tengas que justificarlo.",
      "¿Cuánto dejas encima de la mesa cada mes por no comunicar bien lo que vales?",
    ],
    estabilidad:[
      "Un trimestre cubierto.\n\nUna agenda planificada.\n\nUn negocio que no depende de la suerte.\n\nEso también se construye.",
      "La inestabilidad de clientes no es solo un problema financiero.\n\nEs ansiedad silenciosa todos los meses.",
      "Saber que seguirán entrando clientes cambia cómo diriges tu empresa.\n\nY cómo vives.",
      "Más control. Más margen. Más tranquilidad.\n\nAsí se ve un sistema de captación que funciona.",
      "Tu agenda debería estar cubierta antes de que acabe el mes.\n\nNo a ver qué pasa.",
    ],
    resultados:[
      "12 leads en la primera semana.\n3 semanas hasta lista de espera.\nEsto es lo que cambió.",
      "+127% de solicitudes. −32% de coste por conversión.\n\nNo es suerte. Es sistema.",
      "De ningún lead cualificado a 8 por semana en 30 días.\n\nEmpresa de reformas. Valencia.",
      "El ROI medio de las campañas que gestiono: 3.6×.\n\nDatos reales. Sin promesas vacías.",
      "¿Cuánto te cuesta cada presupuesto que no se cierra? Esto es lo que encontramos al medirlo.",
    ],
  },

  frases: [
    "El boca a boca no es una estrategia.\nEs una oración.",
    "La publicidad no se trata de impresionar.\nSe trata de conectar con quien importa.",
    "No necesitas más seguidores.\nNecesitas mejores clientes.",
    "Tu obra perfecta merece\nque el cliente perfecto la vea primero.",
    "El precio no es el problema.\nEl posicionamiento sí.",
    "Menos curiosos.\nMás obras rentables.",
    "Tu negocio debería darte estabilidad.\nNo ansiedad.",
    "Construiste una empresa para vivir mejor.\nNo para vivir estresado.",
    "La autoridad también se comunica.",
    "Más control. Más margen.\nMás tranquilidad.",
    "La estabilidad también se construye.",
    "Deja de perseguir presupuestos.\nEmpieza a filtrar mejor.",
    "La calidad técnica sin autoridad visual\ndeja dinero encima de la mesa.",
    "El objetivo no es facturar más a cualquier precio.\nEs crecer con calma y criterio.",
    "No vivas esperando a que te recomienden.",
  ],

  subtitulos: [
    "Esto cambió todo lo que hacía en Meta y Google.",
    "Lo que nadie del sector te dice en público.",
    "No es teoría. Es lo que aplico cada semana.",
    "Estrategia + datos + criterio = resultados.",
    "El sistema que uso con todas las empresas que trabajan conmigo.",
    "Más sencillo de lo que parece. Más poderoso de lo que imaginas.",
    "Cuatro años de campañas condensados en este carrusel.",
    "La explicación más directa que voy a darte.",
    "Desliza para ver el antes y el después real.",
    "Lo que separa una campaña rentable de una que sangra presupuesto.",
  ],

  ctas: [
    "Escríbeme CLIENTES","Escríbeme REFORMAS","Escríbeme SISTEMA",
    "Escríbeme ESTABILIDAD","Escríbeme AGENDA","Escríbeme RESULTADOS",
    "Escríbeme OBRAS","Escríbeme FILTRO","Escríbeme AUTORIDAD",
    "Escríbeme TIEMPO","Escríbeme MARGEN","Escríbeme PREMIUM",
  ],

  listas: {
    bocaboca:[
      ["*El boca a boca* no se controla: funciona cuando quiere, no cuando lo necesitas.","*No puedes planificar* ni ingresos ni agenda cuando dependes de que alguien te recuerde.","*Aceptas obras que no encajan* por miedo a quedarte sin trabajo ese mes.","*Tu crecimiento tiene techo* porque no puedes escalar una recomendación."],
    ],
    regateo:[
      ["*El primer filtro* está en el anuncio: el copy que descalifica al que no puede pagarte.","*El segundo filtro* está en el formulario: 3-4 preguntas antes de que lleguen al teléfono.","*El tercer filtro* está en el primer mensaje: velocidad y tono de respuesta determinan quién sigue.","*El cuarto filtro* está en la visita: solo para quien ya pasó los tres anteriores."],
    ],
    autoridad:[
      ["*Prueba social específica*: casos similares al del cliente, no fotos genéricas de obra.","*Claridad de proceso*: que sepa exactamente qué pasará desde el presupuesto.","*Imagen coherente*: que la percepción digital esté a la altura de la calidad real de la obra.","*Un solo punto de contacto*: que no tenga que perseguirte para saber cómo va su proyecto."],
    ],
    sistema:[
      ["*Google Ads* para quien ya sabe que quiere reformar. Intención declarada, conversión directa.","*Meta Ads* para quien todavía no sabe que tú existes. Demanda latente, coste menor.","*Formulario de cualificación* para filtrar antes de que lleguen al teléfono.","*Seguimiento en menos de 20 minutos*: el primero que responde bien suele cerrar la obra."],
    ],
    premium:[
      ["*Hablar del resultado*, no del proceso: el cliente no compra azulejos, compra tranquilidad.","*Usar el precio como filtro*, no como gancho: el cliente correcto no huye del precio justo.","*Mostrar casos con datos*: metros, días, presupuesto real. La especificidad genera confianza.","*Autoridad visual coherente*: que la imagen de tu empresa esté a la altura de tu trabajo real."],
    ],
    estabilidad:[
      ["*Previsibilidad*: saber que el mes siguiente está cubierto antes de que acabe este.","*Autoridad*: que el tipo de cliente que te contacta ya sepa que puedes cobrar lo que vales.","*Tiempo*: dejar de regalar tardes a presupuestos que nunca se cierran.","*Control*: tener un sistema que funciona sin que todo dependa de ti."],
    ],
    default:[
      ["*Estabilidad*: saber que el mes siguiente está cubierto antes de que acabe este.","*Autoridad*: que el tipo de cliente que te contacta ya sepa que puedes cobrar lo que vales.","*Tiempo*: dejar de regalar tardes a presupuestos que nunca se cierran.","*Control*: tener un sistema que funciona sin que todo dependa de ti."],
    ],
  },

  antes:[
    ["2 presupuestos al mes. Todo por recomendación. Sin control ni previsibilidad.","12 leads cualificados por semana. Sistema activo. Agenda cubierta 3 semanas por adelantado."],
    ["Anuncio publicado. Sin respuesta. Presupuesto gastado sin entender por qué.","Campaña ajustada. 8 leads en 5 días. Coste por lead: 14 €. CPL real medido."],
    ["Visitas a clientes que solo comparan precio. Tardes perdidas. Sin cierres.","Clientes que llegan informados, con presupuesto y sin preguntar por descuentos."],
    ["Meses buenos y meses flojos sin explicación. Nóminas con ansiedad cada trimestre.","Sistema predecible. Ingresos estables. Posibilidad de planificar a 3 meses vista."],
    ["Empresa buena, imagen genérica. Compitiendo contra empresas peores que comunican mejor.","Posicionamiento claro. Imagen que transmite el nivel real del trabajo. Clientes premium."],
  ],

  debates:[
    ["¿Las reformas se venden\npor *precio* o por *confianza*?","Por confianza. El precio es excusa cuando no ven el valor real.","Por precio. El mercado de reformas es muy competitivo."],
    ["¿*Instagram* o *Google*\npara captar reformas?","Google. La intención de búsqueda ya está declarada y la conversión es directa.","Meta. Llegas antes que la competencia a un coste menor."],
    ["¿Boca a boca o *sistema\nde captación digital*?","Sistema digital. El boca a boca es bueno pero no se controla ni se escala.","Boca a boca. Es la forma más auténtica de crecer en este sector."],
    ["¿*Especialista* en un tipo\nde reforma o generalista?","Especialista. Más autoridad, mejor cliente, menos competencia de precio.","Generalista. Más mercado, más obras, más crecimiento a corto plazo."],
    ["¿El dueño debe aparecer\nen cámara o puede ser *la empresa*?","El dueño. La gente compra a personas, la cara da confianza inmediata.","La empresa. Más profesional, más escalable cuando el negocio crezca."],
  ],

  stats:[
    ["+127%::Aumento de solicitudes","-32%::Coste por conversión","3.6x::ROI promedio de campañas","+89::Negocios escalados"],
    ["+340%::Leads cualificados","−28%::Coste por lead","5.2x::Retorno medio","60d::Agenda llena"],
    ["12::Leads en primera semana","3::Semanas hasta lista de espera","−40%::Coste por cierre","+20%::Ticket medio"],
    ["+200%::Solicitudes de presupuesto","48h::Primeros leads","4x::Ratio de cierre","+15%::Precio medio de obra"],
  ],

  procesos:[
    ["Análisis:Entiendo tu negocio y tu cliente ideal.","Estrategia:Diseño campañas con objetivo claro.","Ejecución:Creo, lanzo y optimizo cada detalle.","Escalado:Aumento los resultados de forma rentable."],
    ["Diagnóstico:Audito tu situación actual en 2 horas.","Configuración:Estructuro la campaña desde cero.","Lanzamiento:Campaña activa en menos de 48 h.","Optimización:Ajusto semanalmente para mejorar el CPL."],
    ["Define:Identificamos al cliente ideal con precisión.","Crea:Construimos el anuncio que le habla a él.","Lanza:Campaña activa con el presupuesto correcto.","Mejora:Datos → decisiones → mejores resultados."],
  ],

  servicios:[
    ["Estrategia de campañas Meta Ads","Segmentación avanzada por perfil de cliente","Creatividades que filtran antes de la visita","Optimización basada en datos reales","Escalado rentable mes a mes"],
    ["Definición de cliente ideal y ángulo de captación","Configuración técnica de campañas (Meta + Google)","Cualificación de leads antes de llegar al teléfono","Seguimiento y optimización semanal","Reportes claros en lenguaje de negocio"],
  ],

  eyebrows:[
    "Media Buyer · Empresas de Reformas",
    "Estrategia · Meta + Google · Reformas",
    "Captación de clientes · Sector Reformas",
    "Media Buyer Estratégica · Reformas",
    "Resultados reales · Empresas de Reformas",
  ],

  // Copy listo para Instagram por ángulo
  instagramCopy: {
    bocaboca:{
      caption:"¿Tu empresa depende de que alguien te recomiende en el momento justo?\n\nEso no es una estrategia. Es una oración.\n\nCuéntame: ¿cuántos presupuestos pediste este mes que vinieron del boca a boca? 👇",
      hashtags:"#reformas #empresadereformas #captacionclientes #marketingdigital #mediabuyerstrategy #bocaaboca #sistemadecaptacion #reformasintegrales",
    },
    regateo:{
      caption:"¿Cuántas horas pierdes al mes en presupuestos que nunca se cierran?\n\nEl problema no es tu precio. Es que estás atrayendo al cliente equivocado antes de la visita.\n\n¿Te ha pasado? 👇",
      hashtags:"#reformas #clientesfantasma #empresadereformas #sistemadecaptacion #mediabuyerstrategy #cualificacion #captaciondigital #reformasintegrales",
    },
    saturacion:{
      caption:"¿A qué hora del día terminas de verdad?\n\nEl mayor problema no es la competencia. Eres tú, intentando hacerlo todo.\n\nCuéntame en comentarios 👇",
      hashtags:"#conciliacion #empresadereformas #autonomosaturado #marketinglocal #reformasvalencia #burnout #mediabuyerstrategy #reformas",
    },
    autoridad:{
      caption:"¿Tu perfil de Instagram transmite la calidad real de tu trabajo?\n\nSi no, estás perdiendo obras antes de que el cliente te llame.\n\n¿Qué transmite la imagen de tu empresa? 👇",
      hashtags:"#autoridad #brandingdigital #reformasintegrales #imagenonline #mediabuyerstrategy #empresadereformas #marketingdigital #reformas",
    },
    tiempo:{
      caption:"¿Cuándo fue la última vez que desconectaste de verdad? 👨‍👩‍👧‍👦\n\nSi tu negocio no puede funcionar sin ti, no tienes una empresa. Tienes un trabajo mal pagado.\n\n¿Cómo lo ves tú?",
      hashtags:"#conciliacion #libertadfinanciera #reformasintegrales #empresariodereformas #burnout #mediabuyerstrategy #reformas #sistemadecaptacion",
    },
    familia:{
      caption:"¿Para qué montaste tu empresa? Cuéntame en comentarios 👇\n\nPorque si la respuesta tiene que ver con tu familia, quizás es hora de revisar cómo funciona el negocio.",
      hashtags:"#conciliacion #libertad #reformas #empresadereformas #mediabuyerstrategy #familia #emprendedor #reformasintegrales",
    },
    estabilidad:{
      caption:"¿Cómo cambiaría tu negocio si supieras que el mes que viene ya está cubierto? 💬\n\nEso también se construye. No es suerte.\n\nEscríbeme si quieres saber cómo.",
      hashtags:"#estabilidadfinanciera #reformas #sistemadecaptacion #mediabuyerstrategy #empresadereformas #captacionclientes #reformasintegrales #marketing",
    },
    premium:{
      caption:"¿Estás atrayendo al cliente que paga lo que merece tu trabajo?\n\nO estás perdiendo tardes con quien solo quiere el precio más bajo.\n\n¿Qué tipo de cliente quieres en los próximos 3 meses? 👇",
      hashtags:"#clientespremium #reformasluxury #posicionamiento #autoridad #empresadereformasintegrales #mediabuyerstrategy #captacion #reformas",
    },
    objecion:{
      caption:"«Ya probé publicidad y no funcionó.»\n\nEs la frase que más escucho de los que luego tienen los mejores resultados.\n\n¿Qué pasó cuando lo intentaste? 👇",
      hashtags:"#marketingdigital #reformasinstagram #estrategiacontenidos #mediabuyerstrategy #antesdespues #captacionreformas #reformas #empresadereformas",
    },
    precio:{
      caption:"¿Estás cobrando lo que realmente vale tu trabajo? 🔑\n\nSi el cliente llega preguntando por precio antes de ver lo que haces, el problema está antes de la visita.",
      hashtags:"#margen #reformasintegrales #altoticket #empresadereformas #estrategiacomercial #mediabuyerstrategy #captacion #posicionamiento",
    },
    margen:{
      caption:"¿Cuánto dejas encima de la mesa cada mes por no comunicar bien lo que vales?\n\nNo es subir precios. Es mejorar la percepción antes de que el cliente decida. 🎯",
      hashtags:"#margen #ticketmedio #reformasintegrales #altoticket #empresadereformas #mediabuyerstrategy #posicionamiento #captacion",
    },
    sistema:{
      caption:"¿Puedes encender tu captación cuando quieres o solo esperas?\n\nHay una diferencia entre recibir contactos y tener un sistema. Solo uno da estabilidad. 💡",
      hashtags:"#bocaaboca #sistemadecaptacion #reformas #marketingreformas #empresadereformas #mediabuyerstrategy #captacionclientes #reformasintegrales",
    },
    resultados:{
      caption:"Datos reales de campañas en el sector reformas. Sin promesas vacías.\n\nSi quieres saber cómo aplico esto a tu empresa, escríbeme por DM 💬",
      hashtags:"#captacionclientes #reformas #mediabuyerstrategy #sistemadecaptacion #reformasvalencia #resultados #metaads #googleads",
    },
    default:{
      caption:"¿Cómo está funcionando tu captación de clientes este mes?\n\nCuéntame en comentarios 👇",
      hashtags:"#reformas #empresadereformas #captacionclientes #marketingdigital #mediabuyerstrategy #sistemadecaptacion #reformasintegrales",
    },
  },
};

/* ═══════════════════════════════════════════
   ESTADO GLOBAL
   ═══════════════════════════════════════════ */
let SLIDES   = [];
let cur      = 0;
let modo     = 'carrusel'; // 'post' 1 slide 4:5 | 'carrusel' varios 4:5 | 'reel' 1 portada 9:16
// Altura del lienzo según modo: reel = 1920 (9:16), resto = 1350 (4:5)
function stageH(){ return modo==='reel' ? 1920 : 1350 }
let guias    = false;
const MARCA  = 'Rosa María';
const HANDLE = '@rosamariamedia';

// Biblioteca de imágenes: [{id, url, name}]
let MEDIA = [];
let mediaIdCounter = 0;
// Destino activo al asignar desde biblioteca
let asignandoTarget = null; // 'fondo' | 'antes' | 'despues'

// Tamaños de tipografía (px) — calibrados con el feed real de Rosa María
let T = { eye:16, head:104, body:30, items:26, stat:88, cta:16 };

/* ═══════════════════════════════════════════
   HELPERS
   ═══════════════════════════════════════════ */
function rnd(arr){ return arr[Math.floor(Math.random()*arr.length)] }
function p(s){
  if(!s) return '';
  return s.replace(/\*\*(.+?)\*\*/g,'<strong>$1</strong>')
          .replace(/\*(.+?)\*/g,'<em class="kw">$1</em>')   // palabra clave → azul
          .replace(/\n/g,'<br>');
}

// Auto-resaltado de palabras clave del negocio (azul de marca)
const KW_POTENTES = ['estabilidad','clientes','autoridad','sistema','tiempo','familia',
  'premium','agenda','obras','reformas','precio','margen','control','previsibilidad',
  'confianza','resultados','captación','captacion','percepción','percepcion','libertad',
  'tranquilidad','rentables','rentable','calidad'];

function pK(s){
  if(!s) return '';
  // Si ya tiene marcado manual (*...*), respetarlo y no auto-resaltar
  if(/\*/.test(s)) return p(s);
  let count = 0;
  const out = s.replace(/([A-Za-zÁÉÍÓÚáéíóúñÑ]+)/g, (m)=>{
    if(count >= 2) return m;                 // máximo 2 por titular
    const base = m.toLowerCase();
    if(KW_POTENTES.includes(base)){ count++; return '*'+m+'*'; }
    return m;
  });
  return p(out);
}
function fc(f){ return f==='light'?'SL':f==='blue'?'SB':'SD' }
function isSq(){ return false }       // nunca cuadrado
function slideH(){ return modo==='reel' ? 'h192' : 'h135' }   // 1920 en reel, 1350 resto
function spClass(){ return modo==='reel' ? 'SPreel' : 'SP' }  // padding con zonas seguras en reel
function delay(ms){return new Promise(r=>setTimeout(r,ms))}

// Tamaño del logo en slides (px de alto), persistente
function getLogoTam(){ return parseInt(localStorage.getItem('rm_logo_tam')||'46')||46; }
function setLogoTam(px){
  px=Math.max(30,Math.min(140,parseInt(px)||46));
  localStorage.setItem('rm_logo_tam', String(px));
  const sl=document.getElementById('logoTam'); if(sl) sl.value=px;
  const lbl=document.getElementById('logoTamLbl');
  if(lbl) lbl.textContent = px<=44?'S':px<=64?'M':px<=90?'L':'XL';
  if(typeof show==='function' && SLIDES.length) show(cur);   // re-render con el nuevo tamaño
  if(typeof buildThumbs==='function' && SLIDES.length) buildThumbs();
}

// Isotipo RM según fondo: BLANCO solo en negro/oscuro; NEGRO en azul y claro
function logoHTML(fondo){
  const src = (fondo==='light' || fondo==='blue') ? 'logo-rm-negro-iso.png' : 'logo-rm-blanco-iso.png';
  const h = getLogoTam();
  return `<div class="logo-wrap" style="--logo-h:${h}px"><img class="slide-logo-img" src="${src}" alt="RM" onerror="this.outerHTML='<span class=\\'rm\\'>RM</span>'"></div>`;
}

/* ═══════════════════════════════════════════
   BIBLIOTECA DE MEDIA
   ═══════════════════════════════════════════ */
function cargarImagenes(files){
  Array.from(files).forEach(file=>{
    const reader = new FileReader();
    reader.onload = e=>{
      const id = ++mediaIdCounter;
      MEDIA.push({id, url: e.target.result, name: file.name});
      renderMediaGrid();
    };
    reader.readAsDataURL(file);
  });
}

function renderMediaGrid(){
  const grid = document.getElementById('mlibGrid');
  if(!MEDIA.length){
    grid.innerHTML = '<div class="mlib-empty">Sin fotos aún.<br>Sube imágenes<br>para usarlas en slides.</div>';
    return;
  }
  grid.innerHTML = MEDIA.map(m=>`
    <div class="mlib-item" id="mitem-${m.id}" title="Clic para usar esta foto" onclick="usarMedia(${m.id})">
      <img src="${m.url}" alt="${m.name}">
      <button class="mlib-del" onclick="event.stopPropagation();borrarMedia(${m.id})">✕</button>
      <div class="mlib-use">✓ Usar</div>
    </div>`).join('');
}

function borrarMedia(id){
  MEDIA = MEDIA.filter(m=>m.id!==id);
  // limpiar referencias en slides
  SLIDES.forEach(s=>{
    if(s.imgFondo===id) s.imgFondo=null;
    if(s.imgFondo2===id) s.imgFondo2=null;
    if(s.imgAntes===id) s.imgAntes=null;
    if(s.imgDespues===id) s.imgDespues=null;
  });
  renderMediaGrid();
  show(cur);
}

function seleccionarMedia(id){
  document.querySelectorAll('.mlib-item').forEach(el=>el.classList.remove('selected'));
  const el = document.getElementById('mitem-'+id);
  if(el) el.classList.add('selected');
}

function usarMedia(id){
  // Si hay un target de asignación activo, asignar directamente
  if(asignandoTarget){
    asignarImagen(id, asignandoTarget);
    asignandoTarget = null;
    return;
  }

  const d = SLIDES[cur];
  if(!d) return;

  const tiposFoto = ['foto','fototxt','autoridad','bafoto'];

  if(tiposFoto.includes(d.tipo)){
    // Slide ya es de tipo foto — asignar al destino correcto
    if(d.tipo === 'bafoto'){
      if(!d.imgAntes) asignarImagen(id, 'antes');
      else asignarImagen(id, 'despues');
    } else {
      asignarImagen(id, 'fondo');
    }
  } else {
    // Slide es de tipo texto — convertirlo a "foto" automáticamente
    d.tipo = 'foto';
    d.overlay = 'dark';
    d.imgFondo = id;
    const sel = document.getElementById('cTipo');
    if(sel) sel.value = 'foto';
    show(cur);
    refreshThumb(cur);
    sincronizarPanelImg(d);
    toast2('✓ Foto asignada — ajusta posición en el panel →');
  }

  // Saltar al tab Editar y mostrar los controles de imagen
  abrirTabEditar();
  setTimeout(()=>{
    const row = document.getElementById('rowImgLayout');
    if(row && row.style.display!=='none') row.scrollIntoView({behavior:'smooth',block:'center'});
  }, 120);
}

function abrirAsignador(target){
  asignandoTarget = target;
  // Highlight visual en biblioteca
  document.querySelectorAll('.mlib-item').forEach(el=>el.classList.remove('selected'));
  toast2(`Selecciona una foto de la biblioteca → ${target}`);
}

function asignarImagen(id, target){
  const d = SLIDES[cur];
  if(!d) return;
  if(target==='fondo')   d.imgFondo   = id;
  if(target==='fondo2')  d.imgFondo2  = id;
  if(target==='antes')   d.imgAntes   = id;
  if(target==='despues') d.imgDespues = id;
  show(cur);
  refreshThumb(cur);
  sincronizarPanelImg(d);
}

function getImgUrl(id){
  if(!id) return null;
  const m = MEDIA.find(m=>m.id===id);
  return m ? m.url : null;
}

function setImgLayout(layout){
  if(!SLIDES.length) return;
  SLIDES[cur].imgLayout = layout;
  // Actualizar botones activos
  ['bg','inset','splitl','splitr','top','bottom','duo'].forEach(k=>{
    const btn = document.getElementById('l'+k);
    if(btn) btn.classList.remove('on');
  });
  const map = {'bg-full':'bg','inset':'inset','split-left':'splitl','split-right':'splitr','top-half':'top','bottom-half':'bottom','duo':'duo'};
  const btn = document.getElementById('l'+(map[layout]||'bg'));
  if(btn) btn.classList.add('on');
  // Mostrar/ocultar fila de segunda foto
  const r2=document.getElementById('rowImg2');
  if(r2) r2.style.display = layout==='duo' ? '' : 'none';
  show(cur); refreshThumb(cur);
}

/* ═══════════════════════════════════════════
   IA: SUGERIR UBICACIÓN IDEAL DE LA IMAGEN
   Heurística según contenido del slide
   ═══════════════════════════════════════════ */
function sugerirLayoutIA(){
  if(!SLIDES.length) return;
  const d = SLIDES[cur];
  if(!['foto','fototxt','autoridad'].includes(d.tipo)){
    toast2('Este slide no usa foto');
    return;
  }

  const headLen = (d.head||'').length;
  const bodyLen = (d.body||'').length;
  const totalTxt = headLen + bodyLen;
  const esRetrato = d.tipo === 'autoridad';
  const nombreFoto = (MEDIA.find(m=>m.id===d.imgFondo)?.name || '').toLowerCase();

  let layout, overlay, txtPos, imgX=50, imgY=50, zoom=110, razon;

  // ── Reglas de decisión ──
  if(esRetrato || /perfil|retrato|rosa|maria|portrait|persona|mujer|hombre|face/.test(nombreFoto)){
    // Foto de persona → split, cara a un lado, texto al otro
    layout = 'split-right';
    overlay = 'none';
    txtPos = 'center';
    imgX = 50; imgY = 30; // enfocar parte superior (cara)
    zoom = 115;
    razon = 'Retrato → foto a un lado, texto al otro. Enfoque en la cara.';
  }
  else if(/grafic|chart|dashboard|ads|analytic|datos|stats|result|pantalla|laptop|screen/.test(nombreFoto)){
    // Gráficas/datos → recuadro limpio para que se lean
    layout = 'inset';
    overlay = 'dark';
    txtPos = 'top';
    zoom = 100;
    razon = 'Gráfica/datos → recuadro limpio para que se lea bien.';
  }
  else if(totalTxt > 120){
    // Mucho texto → imagen a media altura, texto tiene espacio
    layout = 'top-half';
    overlay = 'dark';
    txtPos = 'center';
    zoom = 115;
    razon = 'Texto largo → imagen arriba, texto con espacio abajo.';
  }
  else if(totalTxt < 50){
    // Poco texto → foto a sangre completa, máximo impacto
    layout = 'bg-full';
    overlay = 'dark';
    txtPos = 'bottom';
    zoom = 115;
    razon = 'Texto corto → foto completa a sangre, máximo impacto.';
  }
  else{
    // Equilibrado → fondo completo con texto centrado
    layout = 'bg-full';
    overlay = 'dark';
    txtPos = 'center';
    zoom = 112;
    razon = 'Equilibrado → fondo completo con overlay y texto centrado.';
  }

  // Aplicar todo
  d.imgLayout = layout;
  d.overlay   = overlay;
  d.txtPos    = txtPos;
  d.imgX      = imgX;
  d.imgY      = imgY;
  d.imgZoom   = zoom;

  show(cur);
  refreshThumb(cur);
  sincronizarPanelImg(d);
  toast2('✨ ' + razon);
}

function sincronizarPanelImg(d){
  const tiposConFoto   = ['foto','fototxt','autoridad'];
  const tiposConFondo  = tiposConFoto;
  const tiposConBA     = ['bafoto'];
  const tiposConOverlay= tiposConFoto;
  const tiposConLayout = tiposConFoto;

  const hasFoto = tiposConFondo.includes(d.tipo);
  const hasBA   = tiposConBA.includes(d.tipo);
  document.getElementById('rowImgFondo').style.display   = hasFoto ? '' : 'none';
  document.getElementById('rowImgBef').style.display     = hasBA   ? '' : 'none';
  document.getElementById('rowImgAft').style.display     = hasBA   ? '' : 'none';
  document.getElementById('rowIAbtn').style.display      = hasFoto ? '' : 'none';
  document.getElementById('rowImgOverlay').style.display = hasFoto ? '' : 'none';
  document.getElementById('rowOvOpacity').style.display  = (hasFoto && (d.overlay||'dark')!=='none') ? '' : 'none';
  document.getElementById('rowImgLayout').style.display  = hasFoto ? '' : 'none';
  document.getElementById('rowImg2').style.display       = (hasFoto && d.imgLayout==='duo') ? '' : 'none';
  document.getElementById('rowImgPos').style.display     = hasFoto ? '' : 'none';
  document.getElementById('rowTxtPos').style.display     = hasFoto ? '' : 'none';

  // Sincronizar sliders
  if(hasFoto){
    const ix=document.getElementById('rImgX'),iy=document.getElementById('rImgY'),iz=document.getElementById('rImgZ');
    const vx=document.getElementById('vImgX'),vy=document.getElementById('vImgY'),vz=document.getElementById('vImgZ');
    if(ix){ix.value=d.imgX??50; vx.textContent=(d.imgX??50)+'%'}
    if(iy){iy.value=d.imgY??50; vy.textContent=(d.imgY??50)+'%'}
    if(iz){iz.value=d.imgZoom??110; vz.textContent=(d.imgZoom??110)+'%'}
    const oo=document.getElementById('rOvOp'); if(oo){oo.value=d.ovOpacity??65; document.getElementById('vOvOp').textContent=(d.ovOpacity??65)+'%'}
    const tp=document.getElementById('cTxtPos'); if(tp) tp.value=d.txtPos||'center';
    const ov=document.getElementById('cOverlay'); if(ov) ov.value=d.overlay||'dark';
    // Preview segunda foto
    const p2=document.getElementById('iaFondo2Prev'); const u2=getImgUrl(d.imgFondo2);
    if(p2){ if(u2){ p2.outerHTML=`<img class="ia-prev" id="iaFondo2Prev" src="${u2}">`; document.getElementById('iaFondo2Lbl').textContent='Foto asignada ✓'; }
            else if(p2.tagName==='IMG'){ p2.outerHTML='<div class="ia-none" id="iaFondo2Prev"></div>'; document.getElementById('iaFondo2Lbl').textContent='Sin imagen'; } }
    // Sliders y botones del modo dúo
    const x2=document.getElementById('rImgX2'); if(x2){x2.value=d.imgX2??50; document.getElementById('vImgX2').textContent=(d.imgX2??50)+'%'}
    const y2=document.getElementById('rImgY2'); if(y2){y2.value=d.imgY2??50; document.getElementById('vImgY2').textContent=(d.imgY2??50)+'%'}
    const z2=document.getElementById('rImgZ2'); if(z2){z2.value=d.imgZoom2??110; document.getElementById('vImgZ2').textContent=(d.imgZoom2??110)+'%'}
    const dd=d.duoDir||'h';
    document.getElementById('duoH')?.classList.toggle('on', dd==='h');
    document.getElementById('duoV')?.classList.toggle('on', dd==='v');
    const dt=d.duoTxt||'bottom';
    document.getElementById('duoTxtB')?.classList.toggle('on', dt==='bottom');
    document.getElementById('duoTxtT')?.classList.toggle('on', dt==='top');
    // Botones layout
    const layout=d.imgLayout||'bg-full';
    const map={'bg-full':'bg','inset':'inset','split-left':'splitl','split-right':'splitr','top-half':'top','bottom-half':'bottom'};
    ['bg','inset','splitl','splitr','top','bottom'].forEach(k=>{
      const b=document.getElementById('l'+k); if(b) b.classList.toggle('on',map[layout]===k||('bg'===k&&layout==='bg-full'));
    });
  }

  // preview miniatura fondo
  const prevFondo = document.getElementById('iaFondoPrev');
  const urlF = getImgUrl(d.imgFondo);
  if(urlF){
    prevFondo.outerHTML = `<img class="ia-prev" id="iaFondoPrev" src="${urlF}">`;
    document.getElementById('iaFondoLbl').textContent = 'Foto asignada ✓';
  } else {
    if(prevFondo.tagName==='IMG') prevFondo.outerHTML=`<div class="ia-none" id="iaFondoPrev"></div>`;
    document.getElementById('iaFondoLbl').textContent = 'Sin imagen';
  }
  // antes
  const prevA = document.getElementById('iaAntesPrev');
  const urlA = getImgUrl(d.imgAntes);
  if(urlA){
    prevA.outerHTML = `<img class="ia-prev" id="iaAntesPrev" src="${urlA}">`;
    document.getElementById('iaAntesLbl').textContent = 'Foto asignada ✓';
  } else {
    if(prevA && prevA.tagName==='IMG') prevA.outerHTML=`<div class="ia-none" id="iaAntesPrev"></div>`;
    document.getElementById('iaAntesLbl').textContent = 'Sin imagen';
  }
  // despues
  const prevD = document.getElementById('iaDesPrev');
  const urlD = getImgUrl(d.imgDespues);
  if(urlD){
    prevD.outerHTML = `<img class="ia-prev" id="iaDesPrev" src="${urlD}">`;
    document.getElementById('iaDesLbl').textContent = 'Foto asignada ✓';
  } else {
    if(prevD && prevD.tagName==='IMG') prevD.outerHTML=`<div class="ia-none" id="iaDesPrev"></div>`;
    document.getElementById('iaDesLbl').textContent = 'Sin imagen';
  }
  // overlay
  if(d.overlay) document.getElementById('cOverlay').value = d.overlay;
}


function toast2(msg){
  const t=document.getElementById('toast');
  t.textContent=msg; t.classList.add('on');
  setTimeout(()=>{ t.textContent='✓ Copiado'; t.classList.remove('on'); },2200);
}

/* ═══════════════════════════════════════════
   RENDERIZADORES — SLIDES CON FOTO
   ═══════════════════════════════════════════ */
function bgImgTag(imgId, extraStyle='', d={}){
  const url = getImgUrl(imgId);
  if(!url) return `<div style="position:absolute;inset:0;background:#111;z-index:0"></div>`;
  const x = d.imgX ?? 50;
  const y = d.imgY ?? 50;
  const z = (d.imgZoom ?? 110) / 100;
  return `<img src="${url}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:${x}% ${y}%;transform:scale(${z});transform-origin:${x}% ${y}%;z-index:0;display:block;${extraStyle}">`;
}

function rFoto(d,n){
  const ov      = d.overlay || 'dark';
  const layout  = d.imgLayout || 'bg-full';
  const txtPos  = d.txtPos || 'center';
  const sq      = isSq();
  const pad     = sq ? 'SP108' : 'SP';
  const isDark  = ov === 'dark' || ov === 'none';
  const txtColor= isDark ? '#F5F1EA' : '#1A1A1A';
  const subColor= isDark ? 'rgba(245,241,234,.75)' : 'rgba(26,26,26,.65)';
  const acColor = '#38B6FF';
  const justify = txtPos==='top' ? 'flex-start' : txtPos==='bottom' ? 'flex-end' : 'center';

  // Overlay con transparencia variable (ovOpacity 0-100, default 65)
  const opBase = (d.ovOpacity ?? 65) / 100;          // intensidad abajo
  const opMid  = Math.max(0, opBase - 0.30);         // intensidad media
  const opTop  = Math.max(0, opBase - 0.50);         // intensidad arriba
  const ovStyle = ov==='none' ? '' :
    ov==='dark'
      ? `position:absolute;inset:0;z-index:1;background:linear-gradient(to top,rgba(26,26,26,${opBase}) 0%,rgba(26,26,26,${opMid}) 45%,rgba(26,26,26,${opTop}) 100%)`
      : `position:absolute;inset:0;z-index:1;background:linear-gradient(to top,rgba(245,241,234,${Math.min(1,opBase+0.25)}) 0%,rgba(245,241,234,${opMid+0.1}) 45%,rgba(245,241,234,${opTop}) 100%)`;

  // Bloque de texto reutilizable
  const txtBlock = `
    <div style="flex:1;display:flex;flex-direction:column;justify-content:${justify};gap:24px;padding-top:${txtPos==='top'?'20px':'40px'}">
      <div style="height:1px;background:${isDark?'rgba(255,255,255,.18)':'rgba(26,26,26,.12)'}"></div>
      <h1 class="TDlg" style="font-size:${sq?Math.round(T.head*.88):T.head}px;color:${txtColor};text-shadow:0 2px 16px rgba(0,0,0,.4)">${pK(d.head)}</h1>
      <div style="height:1px;background:${isDark?'rgba(255,255,255,.18)':'rgba(26,26,26,.12)'}"></div>
      ${d.body?`<p class="TBdy" style="font-size:${T.body}px;color:${subColor}">${p(d.body)}</p>`:''}
    </div>
    <div class="SF">
      <span class="TCap" style="font-size:${T.cta}px;color:${subColor}">${HANDLE}</span>
      <span class="TCap" style="font-size:${T.cta}px;color:${acColor}">${p(d.cta)}</span>
    </div>`;

  const header = `
    <div class="SH">
      <div style="display:flex;align-items:center;gap:12px">
        <div class="abar" style="background:${acColor}"></div>
        <span class="TEye" style="font-size:${T.eye}px;color:${subColor}">${p(d.eye)}</span>
      </div>
      ${logoHTML(d.fondo)}
    </div>`;

  // ── LAYOUTS ──
  if(layout === 'bg-full'){
    return `<div class="slide ${slideH()}" style="position:relative;overflow:hidden;background:#111">
  ${bgImgTag(d.imgFondo,'',d)}
  ${ovStyle?`<div style="${ovStyle}"></div>`:''}
  <div class="${pad}" style="position:relative;z-index:2;display:flex;flex-direction:column;height:100%">
    ${header}${txtBlock}
  </div>
</div>`;
  }

  if(layout === 'inset'){
    const bgC = isDark ? '#1A1A1A' : '#F5F1EA';
    return `<div class="slide ${fc(d.fondo)} ${slideH()} ${spClass()} SP" style="position:relative">
  ${header}
  <div style="flex:1;display:flex;flex-direction:column;justify-content:${justify};gap:24px;padding-top:20px">
    <div style="position:relative;border-radius:10px;overflow:hidden;width:100%;aspect-ratio:16/9;flex-shrink:0">
      ${bgImgTag(d.imgFondo,'border-radius:0',d)}
    </div>
    <h1 class="TDlg Ct" style="font-size:${Math.round(T.head*.78)}px">${pK(d.head)}</h1>
    ${d.body?`<p class="TBdy Cb" style="font-size:${T.body}px">${p(d.body)}</p>`:''}
  </div>
  <div class="SF">
    <span class="TCap Cm" style="font-size:${T.cta}px">${HANDLE}</span>
    <span class="TCap Ca" style="font-size:${T.cta}px">${p(d.cta)}</span>
  </div>
</div>`;
  }

  if(layout === 'split-left' || layout === 'split-right'){
    const imgFirst = layout === 'split-left';
    const bgSlide  = isDark ? '#1A1A1A' : '#F5F1EA';
    const imgCol   = `<div style="position:relative;overflow:hidden">${bgImgTag(d.imgFondo,'',d)}</div>`;
    const txtCol   = `<div style="display:flex;flex-direction:column;justify-content:${justify};padding:80px 60px;gap:20px;background:${bgSlide}">
      <div style="display:flex;align-items:center;gap:10px"><div class="abar"></div><span class="TEye" style="font-size:${T.eye}px;color:${subColor}">${p(d.eye)}</span></div>
      <h1 class="TDlg" style="font-size:${Math.round(T.head*.75)}px;color:${txtColor}">${pK(d.head)}</h1>
      ${d.body?`<p class="TBdy" style="font-size:${Math.round(T.body*.9)}px;color:${subColor}">${p(d.body)}</p>`:''}
      <div style="margin-top:auto;display:flex;justify-content:space-between;align-items:center">
        <span class="TCap" style="font-size:${T.cta}px;color:${subColor}">${HANDLE}</span>
        ${logoHTML(d.fondo)}
      </div>
    </div>`;
    return `<div class="slide ${slideH()}" style="display:grid;grid-template-columns:1fr 1fr;overflow:hidden">
  ${imgFirst ? imgCol+txtCol : txtCol+imgCol}
</div>`;
  }

  if(layout === 'top-half' || layout === 'bottom-half'){
    const imgTop   = layout === 'top-half';
    const bgSlide  = isDark ? '#1A1A1A' : '#F5F1EA';
    const imgH     = sq ? '50%' : '55%';
    const imgBlock = `<div style="position:relative;overflow:hidden;height:${imgH};flex-shrink:0">${bgImgTag(d.imgFondo,'',d)}</div>`;
    const txtArea  = `<div style="flex:1;display:flex;flex-direction:column;justify-content:center;padding:60px 90px;gap:20px;background:${bgSlide}">
      <div style="display:flex;align-items:center;gap:10px"><div class="abar"></div><span class="TEye" style="font-size:${T.eye}px;color:${subColor}">${p(d.eye)}</span></div>
      <h1 class="TDlg" style="font-size:${Math.round(T.head*.8)}px;color:${txtColor}">${pK(d.head)}</h1>
      ${d.body?`<p class="TBdy" style="font-size:${T.body}px;color:${subColor}">${p(d.body)}</p>`:''}
      <div style="display:flex;justify-content:space-between;align-items:center;margin-top:auto">
        <span class="TCap" style="font-size:${T.cta}px;color:${subColor}">${HANDLE}</span>
        <span class="TCap" style="font-size:${T.cta}px;color:${acColor}">${p(d.cta)}</span>
      </div>
    </div>`;
    return `<div class="slide ${slideH()}" style="display:flex;flex-direction:column;overflow:hidden">
  ${imgTop ? imgBlock+txtArea : txtArea+imgBlock}
</div>`;
  }

  if(layout === 'duo'){
    // Dos fotos + texto. Cada foto con su propio enfoque/zoom.
    const bgSlide = isDark ? '#1A1A1A' : '#F5F1EA';
    const dir = d.duoDir || 'h';        // 'h' lado a lado | 'v' apiladas
    const zonaTxt = d.duoTxt || 'bottom'; // dónde va el texto: 'bottom' | 'top'
    // Foto 2 usa sus propios valores (con fallback a los de foto 1)
    const d2 = {imgX: d.imgX2 ?? 50, imgY: d.imgY2 ?? 50, imgZoom: d.imgZoom2 ?? 110};
    // Bloque de las dos fotos
    const dosFotos = dir==='v'
      ? `<div style="height:46%;display:flex;flex-direction:column;flex-shrink:0">
           <div style="flex:1;position:relative;overflow:hidden;border-bottom:3px solid ${bgSlide}">${bgImgTag(d.imgFondo,'',d)}</div>
           <div style="flex:1;position:relative;overflow:hidden">${bgImgTag(d.imgFondo2,'',d2)}</div>
         </div>`
      : `<div style="height:46%;display:flex;flex-shrink:0">
           <div style="flex:1;position:relative;overflow:hidden;border-right:3px solid ${bgSlide}">${bgImgTag(d.imgFondo,'',d)}</div>
           <div style="flex:1;position:relative;overflow:hidden">${bgImgTag(d.imgFondo2,'',d2)}</div>
         </div>`;
    const bloqueTxt = `<div class="SP" style="flex:1;display:flex;flex-direction:column;justify-content:center;padding:60px 90px">
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:18px"><div class="abar"></div><span class="TEye" style="font-size:${T.eye}px;color:${subColor}">${p(d.eye)}</span></div>
    <h1 class="TDlg" style="font-size:${Math.round(T.head*.82)}px;color:${txtColor}">${pK(d.head)}</h1>
    ${d.body?`<p class="TBdy" style="font-size:${T.body}px;color:${subColor};margin-top:18px">${p(d.body)}</p>`:''}
    <div style="display:flex;justify-content:space-between;align-items:center;margin-top:auto;padding-top:24px">
      <span class="TCap" style="font-size:${T.cta}px;color:${subColor}">${HANDLE}</span>
      <span class="TCap" style="font-size:${T.cta}px;color:${acColor}">${p(d.cta)}</span>
    </div>
  </div>`;
    return `<div class="slide ${slideH()}" style="display:flex;flex-direction:column;overflow:hidden;background:${bgSlide}">
  ${zonaTxt==='top' ? bloqueTxt+dosFotos : dosFotos+bloqueTxt}
</div>`;
  }

  // Fallback
  return rHead(d,n);
}

function rBAFoto(d,n){
  const its = d.items||[];
  const txtA = (its[0]||'').replace(/^Antes:\s*/i,'');
  const txtD = (its[1]||'').replace(/^Después:\s*/i,'');
  return `<div class="slide SD ${slideH()} sBAFoto" style="position:relative">
  <div class="baf-half bef" style="position:relative;overflow:hidden">
    ${bgImgTag(d.imgAntes)}
    <div class="baf-ov" style="position:absolute;inset:0;z-index:1;background:linear-gradient(0deg,rgba(10,10,10,.85) 0%,rgba(10,10,10,.2) 100%)"></div>
    <div class="baf-content" style="position:relative;z-index:2">
      <div class="baf-badge"><span class="baf-dot"></span>Antes</div>
      <p class="baf-txt">${p(txtA||'Situación anterior')}</p>
      <span style="font-size:${T.cta}px;color:rgba(255,255,255,.35);letter-spacing:.12em;text-transform:uppercase">${HANDLE}</span>
    </div>
  </div>
  <div class="baf-divider" style="position:absolute;top:50%;left:0;right:0;height:2px;background:#38B6FF;z-index:10;display:flex;align-items:center;justify-content:center">
    <span style="background:#38B6FF;color:#fff;font-size:12px;font-weight:700;letter-spacing:.12em;padding:4px 14px;border-radius:20px">VS</span>
  </div>
  <div class="baf-half aft" style="position:relative;overflow:hidden">
    ${bgImgTag(d.imgDespues)}
    <div class="baf-ov" style="position:absolute;inset:0;z-index:1;background:linear-gradient(0deg,rgba(10,10,10,.82) 0%,rgba(10,10,10,.15) 100%)"></div>
    <div class="baf-content" style="position:relative;z-index:2">
      <div class="baf-badge"><span class="baf-dot"></span>Después</div>
      <p class="baf-txt">${p(txtD||'Resultado conseguido')}</p>
      <span style="font-size:${T.cta}px;color:#38B6FF;letter-spacing:.1em;text-transform:uppercase">${p(d.cta)}</span>
    </div>
  </div>
</div>`;
}

function rFotoTxt(d,n){
  const sq = isSq();
  const fc2 = fc(d.fondo);
  return `<div class="slide ${fc2} ${slideH()} sFotoTxt">
  <div class="ft-img" style="position:relative;overflow:hidden">${bgImgTag(d.imgFondo)}</div>
  <div class="ft-txt">
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px">
      <div class="abar"></div>
      <span class="TEye Ca" style="font-size:${T.eye}px">${p(d.eye)}</span>
    </div>
    <h1 class="TDmd Ct" style="font-size:${Math.min(T.head,90)}px">${pK(d.head)}</h1>
    ${d.body?`<p class="TBdy Cb" style="font-size:${T.body}px;margin-top:20px">${p(d.body)}</p>`:''}
    <div style="margin-top:auto;padding-top:28px;display:flex;justify-content:space-between;align-items:center">
      <span class="TCap Cm" style="font-size:${T.cta}px">${HANDLE}</span>
      ${logoHTML(d.fondo)}
    </div>
  </div>
</div>`;
}

function rAutoridad(d,n){
  return `<div class="slide SD ${slideH()} sAutoridad">
  <div class="aut-foto" style="position:relative;overflow:hidden">
    ${bgImgTag(d.imgFondo)}
    <div class="aut-ov" style="position:absolute;inset:0;z-index:1;background:linear-gradient(90deg,transparent 55%,#1A1A1A 100%)"></div>
  </div>
  <div class="aut-txt">
    <div style="display:flex;align-items:center;gap:12px">
      <div class="abar"></div>
      <span class="TEye Ca" style="font-size:${T.eye}px">${p(d.eye||marcaEye())}</span>
    </div>
    <h1 class="TDsm Ct" style="font-size:${Math.min(T.head,78)}px;margin-top:16px">${pK(d.head)}</h1>
    ${d.body?`<p class="TBdy Cb" style="font-size:${T.body}px">${p(d.body)}</p>`:''}
    <div style="margin-top:auto;display:flex;flex-direction:column;gap:14px">
      <div style="height:1px;background:rgba(245,241,234,.1)"></div>
      <div style="display:flex;justify-content:space-between;align-items:center">
        <span class="TCap Cm" style="font-size:${T.cta}px">${HANDLE}</span>
        <span class="TCap Ca" style="font-size:${T.cta}px">${p(d.cta)}</span>
      </div>
    </div>
  </div>
</div>`;
}

/* ═══════════════════════════════════════════
   PANEL TABS
   ═══════════════════════════════════════════ */
function switchTab(id, btn){
  document.querySelectorAll('.rtab').forEach(t=>t.classList.remove('on'));
  document.querySelectorAll('.rpanel').forEach(p=>p.classList.remove('on'));
  btn.classList.add('on');
  document.getElementById('tab-'+id).classList.add('on');
  // El COPY se reconstruye con el contenido actual al abrir su pestaña
  if(id==='copy' && SLIDES.length) refrescarCopy();
}

function abrirTabEditar(){
  document.querySelectorAll('.rtab').forEach(t=>t.classList.remove('on'));
  document.querySelectorAll('.rpanel').forEach(p=>p.classList.remove('on'));
  const tab = document.querySelector('.rtab');
  if(tab) tab.classList.add('on');
  document.getElementById('tab-editar').classList.add('on');
}

/* ═══════════════════════════════════════════
   PILARES Y ÁNGULOS
   ═══════════════════════════════════════════ */
function actualizarAngulos(){
  const pilar = document.getElementById('cPilar').value;
  const cfg = N();
  const mapa = cfg.pilares || PILARES_MAP;
  const labels = cfg.labels || ANGULO_LABELS;
  const angulos = mapa[pilar] || [];
  const sel = document.getElementById('cAngulo');
  sel.innerHTML = '<option value="auto">⚡ Automático (aleatorio)</option>' +
    angulos.map(a=>`<option value="${a}">${labels[a]||a}</option>`).join('');
}

/* ═══════════════════════════════════════════
   TIPOGRAFÍA
   ═══════════════════════════════════════════ */
function applyType(){
  T.eye   = parseInt(document.getElementById('rEye').value);
  T.head  = parseInt(document.getElementById('rHead').value);
  T.body  = parseInt(document.getElementById('rBody').value);
  T.items = parseInt(document.getElementById('rItems').value);
  T.stat  = parseInt(document.getElementById('rStat').value);
  T.cta   = parseInt(document.getElementById('rCta').value);
  document.getElementById('vEye').textContent   = T.eye+'px';
  document.getElementById('vHead').textContent  = T.head+'px';
  document.getElementById('vBody').textContent  = T.body+'px';
  document.getElementById('vItems').textContent = T.items+'px';
  document.getElementById('vStat').textContent  = T.stat+'px';
  document.getElementById('vCta').textContent   = T.cta+'px';
  if(SLIDES.length){ buildThumbs(); show(cur); }
}

function resetType(){
  const defaults = {rEye:16,rHead:104,rBody:30,rItems:26,rStat:88,rCta:16};
  Object.entries(defaults).forEach(([id,v])=>{ document.getElementById(id).value=v; });
  applyType();
}

/* ═══════════════════════════════════════════
   RENDERIZADORES
   ═══════════════════════════════════════════ */
function rHead(d,n){
  const sq=isSq();
  return`<div class="slide ${fc(d.fondo)} ${slideH()} ${sq?'sPost':'sHook'} ${spClass()}">
  <div class="SH">
    <div style="display:flex;align-items:center;gap:12px">
      <div class="abar"></div>
      <span class="TEye Cm" style="font-size:${T.eye}px">${p(d.eye)}</span>
    </div>
    ${logoHTML(d.fondo)}
  </div>
  <div class="zone">
    <div class="HL Cl"></div>
    <h1 class="TDlg Ct" style="font-size:${sq?Math.round(T.head*.88):T.head}px">${pK(d.head)}</h1>
    <div class="HL Cl"></div>
    ${d.body?`<p class="TBdy Cb" style="font-size:${T.body}px">${p(d.body)}</p>`:''}
  </div>
  <div class="SF">
    <span class="TCap Cm" style="font-size:${T.cta}px">${HANDLE}</span>
    <span class="TCap Ca" style="font-size:${T.cta}px">${p(d.cta)}</span>
  </div>
  <div class="BGN Cn" style="font-size:${sq?400:500}px">${n}</div>
</div>`;}

function rFrase(d,n){
  const sq=isSq();
  return`<div class="slide ${fc(d.fondo)} ${slideH()} sFrase ${spClass()}">
  <div class="SH">
    <div style="display:flex;align-items:center;gap:12px">
      <div class="abar"></div>
      <span class="TEye Cm" style="font-size:${T.eye}px">${p(d.eye)}</span>
    </div>
    ${logoHTML(d.fondo)}
  </div>
  <div class="zone">
    <div class="qm Cm">"</div>
    <h1 class="TDlg Ct" style="font-size:${sq?Math.round(T.head*.88):T.head}px">${pK(d.head)}</h1>
    ${d.body?`<p class="TBdy Cb" style="font-size:${T.body}px">${p(d.body)}</p>`:''}
    <div style="display:flex;align-items:center;gap:12px">
      <div class="abar"></div>
      <span class="TCap Cm" style="font-size:14px">${MARCA} · ${HANDLE}</span>
    </div>
  </div>
  <div class="SF">
    <span class="TCap Cm" style="font-size:${T.cta}px">${HANDLE}</span>
    <span class="TCap Ct" style="font-size:${T.cta}px">${p(d.cta)}</span>
  </div>
</div>`;}

function rBA(d,n){
  const its=d.items||[];
  const bt=(its[0]||'').replace(/^Antes:\s*/i,'');
  const at=(its[1]||'').replace(/^Después:\s*/i,'');
  return`<div class="slide SD ${slideH()} sBA">
  <div class="bah bef">
    <div class="babadge"><span class="badot"></span>Antes</div>
    <p class="batext">${p(bt)}</p>
    <div class="bafoot">
      <span style="font-family:var(--F-SAN);font-size:${T.cta}px;color:rgba(245,241,234,.2);letter-spacing:.12em;text-transform:uppercase">${HANDLE}</span>
      <span style="font-family:var(--F-SAN);font-size:${T.cta}px;color:rgba(245,241,234,.2);letter-spacing:.12em;text-transform:uppercase">${n}</span>
    </div>
    <div class="badiv"></div>
  </div>
  <div class="bah aft">
    <div class="babadge"><span class="badot"></span>Después</div>
    <p class="batext">${p(at)}</p>
    <div class="bafoot">
      ${logoHTML(d.fondo)}
      <span style="font-family:var(--F-SAN);font-size:${T.cta}px;color:#38B6FF;letter-spacing:.1em;text-transform:uppercase">${p(d.cta)}</span>
    </div>
  </div>
</div>`;}

function rLista(d,n){
  const items = d.items||[];
  const count = items.length||4;
  // Tamaño de fuente adaptativo: más items → letra más pequeña
  const tamItems = count<=2 ? T.items+6
                 : count===3 ? T.items+3
                 : count===4 ? T.items
                 : count===5 ? T.items-3
                 : T.items-5;
  // Número acento: más pequeño con más items
  const tamNum  = count<=3 ? 36 : count<=4 ? 30 : 24;
  const rows = items.map((it,i)=>`
<div class="lrow">
  <span class="lnum" style="font-size:${tamNum}px;line-height:1;min-width:${tamNum+2}px">${String(i+1).padStart(2,'0')}</span>
  <span class="ltxt" style="font-size:${tamItems}px;line-height:${count>=5?1.3:1.45};font-weight:300">${p(it)}</span>
</div>`).join('');
  // Zona con clase para layout adaptativo
  const zoneClass = `lzone lzone-${count}`;
  return`<div class="slide ${fc(d.fondo)} ${slideH()} sLista ${spClass()}">
  <div class="SH">
    <div style="display:flex;align-items:center;gap:12px">
      <div class="abar"></div>
      <span class="TEye Ca" style="font-size:${T.eye}px">${p(d.eye)}</span>
    </div>
    ${logoHTML(d.fondo)}
  </div>
  <h1 class="TDsm Ct" style="margin-top:${count>=5?16:24}px;font-size:${Math.min(T.head,count>=5?72:84)}px">${pK(d.head)}</h1>
  <div class="${zoneClass}">${rows}</div>
  <div class="SF">
    <span class="TCap Cm" style="font-size:${T.cta}px">${HANDLE}</span>
    <span class="TCap Ca" style="font-size:${T.cta}px">${p(d.cta)}</span>
  </div>
</div>`;}

function rStats(d,n){
  const cells=(d.items||[]).map(it=>{
    const [num,lbl]=it.split('::');
    return`<div class="scell"><div class="snum" style="font-size:${T.stat}px">${p(num)}</div><div class="slbl" style="font-size:17px">${p(lbl)}</div></div>`;
  }).join('');
  return`<div class="slide ${fc(d.fondo)} ${slideH()} sStats ${spClass()}">
  <div class="SH">
    <div style="display:flex;align-items:center;gap:12px">
      <div class="abar"></div>
      <span class="TEye Ca" style="font-size:${T.eye}px">${p(d.eye)}</span>
    </div>
    ${logoHTML(d.fondo)}
  </div>
  <div class="sgrid">${cells}</div>
  <div class="SF">
    <span class="TCap Cm" style="font-size:${T.cta}px">${HANDLE}</span>
    <span class="TCap Cm" style="font-size:${T.cta}px">${n} · ${SLIDES.length}</span>
  </div>
</div>`;}

function rProceso(d,n){
  const steps=(d.items||[]).map((it,i)=>{
    const [title,...rest]=it.split(':');
    const desc=rest.join(':').trim();
    return`<div class="pstep">
      <div class="pnum">${i+1}</div>
      <div class="ptitle">${p(title)}</div>
      <div class="pdesc" style="font-size:${T.items}px">${p(desc)}</div>
    </div>`;
  }).join('');
  return`<div class="slide ${fc(d.fondo)} ${slideH()} sProceso ${spClass()}">
  <div class="SH">
    <div style="display:flex;align-items:center;gap:12px">
      <div class="abar"></div>
      <span class="TEye Ca" style="font-size:${T.eye}px">${p(d.eye)}</span>
    </div>
    ${logoHTML(d.fondo)}
  </div>
  <h1 class="TDsm Ct" style="margin-top:24px;font-size:${Math.min(T.head,84)}px">${pK(d.head)}</h1>
  <div class="stepsrow">${steps}</div>
  <div class="SF">
    <span class="TCap Cm" style="font-size:${T.cta}px">${HANDLE}</span>
    <span class="TCap Ca" style="font-size:${T.cta}px">${p(d.cta)}</span>
  </div>
</div>`;}

function rServ(d,n){
  const rows=(d.items||[]).map(it=>`
<div class="svrow">
  <div class="svcheck">✓</div>
  <span class="svtxt" style="font-size:${T.items}px;line-height:1.3;font-weight:300">${p(it)}</span>
</div>`).join('');
  return`<div class="slide ${fc(d.fondo)} ${slideH()} sServ ${spClass()}">
  <div class="SH">
    <div style="display:flex;align-items:center;gap:12px">
      <div class="abar"></div>
      <span class="TEye Ca" style="font-size:${T.eye}px">${p(d.eye)}</span>
    </div>
    ${logoHTML(d.fondo)}
  </div>
  ${d.head?`<h1 class="TDsm Ct" style="margin-top:24px;font-size:${Math.min(T.head,84)}px">${pK(d.head)}</h1>`:''}
  <div class="svzone">${rows}</div>
  <div class="SF">
    <span class="TCap Cm" style="font-size:${T.cta}px">${HANDLE}</span>
    <span class="TCap Ca" style="font-size:${T.cta}px">${p(d.cta)}</span>
  </div>
</div>`;}

function rDebate(d,n){
  const o=d.items||[];
  return`<div class="slide ${fc(d.fondo)} ${slideH()} sDebate ${spClass()}">
  <div class="SH">
    <div style="display:flex;align-items:center;gap:12px">
      <div class="abar"></div>
      <span class="TEye Cm" style="font-size:${T.eye}px">${p(d.eye)}</span>
    </div>
    ${logoHTML(d.fondo)}
  </div>
  <div class="dq"><h1 class="TDsm Ct" style="font-size:${Math.min(T.head,84)}px">${pK(d.head)}</h1></div>
  <div class="dopts">
    <div class="dopt dopt-a" style="font-size:${T.items}px">${p(o[0]||'Opción A')}</div>
    <div class="dopt dopt-b" style="font-size:${T.items}px">${p(o[1]||'Opción B')}</div>
  </div>
  <div class="SF">
    <span class="TCap Cm" style="font-size:${T.cta}px">${HANDLE}</span>
    <span class="TCap Cm" style="font-size:${T.cta}px">${p(d.cta)}</span>
  </div>
</div>`;}

function rCTA(d,n){
  return`<div class="slide ${fc(d.fondo)} ${slideH()} sCTA ${spClass()}">
  <div class="SH">
    <div style="display:flex;align-items:center;gap:12px">
      <div class="abar"></div>
      <span class="TEye Cm" style="font-size:${T.eye}px">${p(d.eye)}</span>
    </div>
    ${logoHTML(d.fondo)}
  </div>
  <div class="zone">
    <div class="HL Cl"></div>
    <h1 class="TDlg Ct" style="font-size:${T.head}px">${pK(d.head)}</h1>
    <div class="HL Cl"></div>
    ${d.body?`<p class="TBdy Cb" style="font-size:${T.body}px">${p(d.body)}</p>`:''}
    <div class="ctapill" style="font-size:${T.cta}px"><span>→</span><span>${p(d.cta)}</span></div>
  </div>
  <div class="SF">
    <span class="TCap Cm" style="font-size:${T.cta}px">${HANDLE}</span>
    ${logoHTML(d.fondo)}
  </div>
  <div class="BGN Cn" style="font-size:380px;opacity:.04">${n}</div>
</div>`;}

/* ── Layouts plantilla feed (v12) ── */

// Pills: headline + foto enmarcada opcional + badges (portadas P1 / P9)
function rPills(d,n){
  const pillFs=Math.round(T.items*.66);
  const pills=(d.items||[]).filter(Boolean).map(it=>`<span class="pill" style="font-size:${pillFs}px">${p(it)}</span>`).join('');
  const url=getImgUrl(d.imgFondo);
  const media=url?`<div class="marcofoto"><img src="${url}" alt=""></div>`:'';
  return`<div class="slide ${fc(d.fondo)} ${slideH()} ${spClass()}">
  <div class="SH">
    <div style="display:flex;align-items:center;gap:12px">
      <div class="abar"></div>
      <span class="TEye Ca" style="font-size:${T.eye}px">${p(d.eye)}</span>
    </div>
    ${logoHTML(d.fondo)}
  </div>
  <h1 class="TDmd Ct" style="margin-top:30px;font-size:${Math.min(T.head,86)}px">${pK(d.head)}</h1>
  ${d.body?`<p class="TBdy Cm" style="font-size:${T.body}px;margin-top:18px">${p(d.body)}</p>`:''}
  ${media}
  <div class="pillzone">${pills}</div>
  <div class="SF">
    <span class="TCap Cm" style="font-size:${T.cta}px">${HANDLE}</span>
    <span class="TCap Ca" style="font-size:${T.cta}px">${p(d.cta)}</span>
  </div>
</div>`;}

// Claves numeradas: head + filas con número serif (portada P6)
function rClaves(d,n){
  const rows=(d.items||[]).filter(Boolean).map((it,i)=>`
    <div class="clvrow"><div class="clvnum">${i+1}</div><div class="clvtxt" style="font-size:${T.items}px">${p(it)}</div></div>`).join('');
  return`<div class="slide ${fc(d.fondo)} ${slideH()} ${spClass()}">
  <div class="SH">
    <div style="display:flex;align-items:center;gap:12px">
      <div class="abar"></div>
      <span class="TEye Ca" style="font-size:${T.eye}px">${p(d.eye)}</span>
    </div>
    ${logoHTML(d.fondo)}
  </div>
  <h1 class="TDmd Ct" style="margin-top:28px;font-size:${Math.min(T.head,84)}px">${pK(d.head)}</h1>
  ${d.body?`<p class="TBdy Cm" style="font-size:${T.body}px;margin-top:16px">${p(d.body)}</p>`:''}
  <div class="clvzone">${rows}</div>
  <div class="SF">
    <span class="TCap Cm" style="font-size:${T.cta}px">${HANDLE}</span>
    <span class="TCap Ca" style="font-size:${T.cta}px">${p(d.cta)}</span>
  </div>
</div>`;}

// Testimonio: estrellas + cita + avatar (portada P7)
// d.body = "Nombre::Rol" — sustituir por citas REALES de clientes
function rTestimonio(d,n){
  const [nom,rol]=(d.body||'Cliente::Empresa de reformas · España').split('::');
  const url=getImgUrl(d.imgFondo);
  const avatar=url?`<img src="${url}" alt="">`
    :`<span style="font-family:var(--F-SER);font-style:italic;font-size:36px;color:#38B6FF">${p((nom||'C').trim()[0]||'C')}</span>`;
  return`<div class="slide ${fc(d.fondo)} ${slideH()} ${spClass()}">
  <div class="SH">
    <div style="display:flex;align-items:center;gap:12px">
      <div class="abar"></div>
      <span class="TEye Ca" style="font-size:${T.eye}px">${p(d.eye)}</span>
    </div>
    ${logoHTML(d.fondo)}
  </div>
  <div class="tstzone">
    <div class="tststars">★★★★★</div>
    <h1 class="tstq Ct" style="font-size:${Math.min(T.head,64)}px">«${pK(d.head)}»</h1>
    <div class="tstwho">
      <div class="tstavatar">${avatar}</div>
      <div>
        <div class="tstname Ct" style="font-size:${Math.round(T.body*1.05)}px">${p(nom)}</div>
        <div class="tstrole Ct" style="font-size:${Math.round(T.body*.85)}px">${p(rol||'')}</div>
      </div>
    </div>
  </div>
  <div class="SF">
    <span class="TCap Cm" style="font-size:${T.cta}px">${HANDLE}</span>
    <span class="TCap Ca" style="font-size:${T.cta}px">${p(d.cta)}</span>
  </div>
</div>`;}

// Móvil: mockup de teléfono mostrando TU anuncio (portada P5, centro del grid)
function rMovil(d,n){
  const url=getImgUrl(d.imgFondo);
  const shot=url?`<img src="${url}" style="width:100%;flex:1;object-fit:cover;min-height:0" alt="">`
    :`<div style="flex:1;min-height:0;background:linear-gradient(135deg,#38B6FF,#1A9AE8);display:flex;align-items:center;justify-content:center"><span style="font-family:var(--F-SER);font-style:italic;font-size:64px;color:#fff">RM</span></div>`;
  return`<div class="slide ${fc(d.fondo)} ${slideH()} ${spClass()}">
  <div class="SH">
    <div style="display:flex;align-items:center;gap:12px">
      <div class="abar"></div>
      <span class="TEye Ca" style="font-size:${T.eye}px">${p(d.eye)}</span>
    </div>
    ${logoHTML(d.fondo)}
  </div>
  <h1 class="TDmd Ct" style="margin-top:24px;font-size:${Math.min(T.head,70)}px;text-align:center">${pK(d.head)}</h1>
  <div class="phzone">
    <div class="phframe"><div class="phnotch"></div>
      <div class="phscreen">
        <div style="display:flex;align-items:center;gap:10px;padding:20px 18px 12px">
          <div style="width:34px;height:34px;border-radius:50%;background:#1A1A1A;color:#F5F1EA;display:flex;align-items:center;justify-content:center;font-family:var(--F-SER);font-style:italic;font-size:15px;flex-shrink:0">RM</div>
          <div>
            <div style="font-family:var(--F-SAN);font-weight:600;font-size:15px;color:#1A1A1A">${MARCA}</div>
            <div style="font-family:var(--F-SAN);font-size:11px;color:rgba(26,26,26,.5)">Publicidad</div>
          </div>
        </div>
        ${shot}
        <div style="padding:14px 18px 18px;display:flex;flex-direction:column;gap:11px">
          <div style="font-family:var(--F-SAN);font-size:14px;color:#1A1A1A;font-weight:500;line-height:1.35">${p(d.body||'Reformas de alto valor · Presupuesto en 24h')}</div>
          <div style="background:#38B6FF;color:#fff;text-align:center;border-radius:8px;padding:11px;font-family:var(--F-SAN);font-weight:600;font-size:14px">Más información</div>
        </div>
      </div>
    </div>
  </div>
  <div class="SF">
    <span class="TCap Cm" style="font-size:${T.cta}px">${HANDLE}</span>
    <span class="TCap Ca" style="font-size:${T.cta}px">${p(d.cta)}</span>
  </div>
</div>`;}

// Portada de REEL 9:16 — hook grande centrado, con zonas seguras IG/TikTok
function rReel(d,n){
  const url=getImgUrl(d.imgFondo);
  const isDark = d.fondo!=='light';
  const txt = isDark ? '#F5F1EA' : '#1A1A1A';
  const sub = isDark ? 'rgba(245,241,234,.8)' : 'rgba(26,26,26,.7)';
  const opBase=(d.ovOpacity ?? 55)/100;
  const bg = url
    ? `<img src="${url}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:0" alt="">
       <div style="position:absolute;inset:0;z-index:1;background:linear-gradient(to bottom,rgba(26,26,26,${Math.min(1,opBase+0.15)}) 0%,rgba(26,26,26,${opBase-0.15}) 40%,rgba(26,26,26,${Math.min(1,opBase+0.25)}) 100%)"></div>`
    : '';
  return`<div class="slide ${fc(d.fondo)} ${slideH()} ${spClass()}" style="position:relative;overflow:hidden">
  ${bg}
  <div class="reel-safe-top"></div><div class="reel-safe-bot"></div>
  <div style="position:relative;z-index:5;display:flex;flex-direction:column;height:100%">
    <div style="display:flex;justify-content:center">${logoHTML(d.fondo)}</div>
    <div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:34px;text-align:center;align-items:center">
      <span class="TEye" style="font-size:${T.eye+4}px;color:#38B6FF;letter-spacing:.22em">${p(d.eye||'REEL')}</span>
      <h1 class="TDlg" style="font-size:${Math.min(T.head+18,120)}px;color:${txt};line-height:1.05">${pK(d.head)}</h1>
      ${d.body?`<p class="TBdy" style="font-size:${T.body+6}px;color:${sub};max-width:820px">${p(d.body)}</p>`:''}
    </div>
    <div style="text-align:center;display:flex;flex-direction:column;gap:20px;align-items:center">
      <div style="display:inline-flex;align-items:center;gap:12px;background:#38B6FF;color:#fff;padding:20px 40px;border-radius:999px;font-family:var(--F-SAN);font-weight:600;font-size:${T.cta+8}px">▶ ${p(d.cta||'Dale al play')}</div>
      <span class="TCap" style="font-size:${T.cta}px;color:${sub}">${HANDLE}</span>
    </div>
  </div>
</div>`;}

function renderTipo(d,n){
  if(d.tipo==='reel') return rReel(d,n);
  switch(d.tipo){
    case'hook': case'post': return rHead(d,n);
    case'frase':            return rFrase(d,n);
    case'ba':               return rBA(d,n);
    case'lista':            return rLista(d,n);
    case'stats':            return rStats(d,n);
    case'proceso':          return rProceso(d,n);
    case'servicio':         return rServ(d,n);
    case'debate':           return rDebate(d,n);
    case'cta':              return rCTA(d,n);
    case'foto':             return rFoto(d,n);
    case'bafoto':           return rBAFoto(d,n);
    case'fototxt':          return rFotoTxt(d,n);
    case'autoridad':        return rAutoridad(d,n);
    case'pills':            return rPills(d,n);
    case'claves':           return rClaves(d,n);
    case'testimonio':       return rTestimonio(d,n);
    case'movil':            return rMovil(d,n);
    default:                return rHead(d,n);
  }
}

function render(d,i){
  const n=String(i+1).padStart(2,'0');

  // ── Escala de texto por slide (txtScale) ──
  // Truco: escalamos T temporalmente para que TODOS los renderers
  // respeten el tamaño de ESTE slide sin tocar cada función.
  const scale = (d.txtScale ?? 100) / 100;
  let html;
  if(scale !== 1){
    const bak = {...T};
    T.head=Math.round(bak.head*scale); T.body=Math.round(bak.body*scale);
    T.items=Math.round(bak.items*scale); T.eye=Math.round(bak.eye*scale);
    T.cta=Math.round(bak.cta*scale); T.stat=Math.round(bak.stat*scale);
    html = renderTipo(d,n);
    T.head=bak.head; T.body=bak.body; T.items=bak.items;
    T.eye=bak.eye; T.cta=bak.cta; T.stat=bak.stat;
  } else {
    html = renderTipo(d,n);
  }

  // ── Alineación + posición vertical + desplazamiento (no destructivo) ──
  const align = d.txtAlign || 'left';
  const vpos  = d.txtVPos || '';
  const dx    = d.txtDX || 0;
  const dy    = d.txtDY || 0;
  const needsWrap = align!=='left' || vpos || dx || dy;
  if(needsWrap){
    // Inyectamos estilo scoped: marcamos el slide con un id único
    const uid = 'sl'+i;
    let css = `#${uid} h1,#${uid} p{text-align:${align}!important}`;
    if(vpos==='top')    css += `#${uid} .zone,#${uid} .lzone,#${uid} [class*=zone]{justify-content:flex-start!important}`;
    if(vpos==='bottom') css += `#${uid} .zone,#${uid} .lzone,#${uid} [class*=zone]{justify-content:flex-end!important}`;
    if(vpos==='center') css += `#${uid} .zone,#${uid} .lzone,#${uid} [class*=zone]{justify-content:center!important}`;
    if(dx||dy)          css += `#${uid} .SP,#${uid} .SP108{transform:translate(${dx}px,${dy}px)}`;
    // Insertar id en el primer div .slide
    html = html.replace(/class="slide/, `id="${uid}" class="slide`);
    html = `<style>${css}</style>` + html;
  }
  return html;
}

/* ═══════════════════════════════════════════
   GENERADOR
   ═══════════════════════════════════════════ */
async function generar(){
  const btn=document.getElementById('btnGen');
  btn.classList.add('loading');
  document.getElementById('btnGenTxt').textContent='Generando...';

  const ov=document.getElementById('genOv');
  const txEl=document.getElementById('genTxt');
  const stEl=document.getElementById('genSteps');
  ov.classList.add('on');

  const pasos=['Analizando pilar y ángulo...','Generando copy con IA...','Construyendo estructura...','Aplicando diseño de marca...'];
  stEl.innerHTML=pasos.map(t=>`<div class="gen-step">${t}</div>`).join('');
  const sEls=stEl.querySelectorAll('.gen-step');

  sEls[0].classList.add('ok');
  await delay(350);

  const pilar = document.getElementById('cPilar').value;
  const selAngulo = document.getElementById('cAngulo').value;
  const mapaPilar = N().pilares || PILARES_MAP;
  const anguloBank = N().angulos || BANCO.angulos;
  const posibles = mapaPilar[pilar] || Object.keys(anguloBank);
  const angulo = (selAngulo === 'auto' || !selAngulo)
    ? rnd(posibles)
    : selAngulo;

  txEl.textContent=`${pilar.toUpperCase()} · ${angulo}`;

  sEls[1].classList.add('ok');
  txEl.textContent='Generando copy con IA...';

  let aiData=null;
  try{ aiData=await fetchAI(angulo); }
  catch(e){ console.warn('API no disponible, usando banco local',e.message); }

  sEls[2].classList.add('ok');
  await delay(250);

  const numSlides = parseInt(document.getElementById('cNumSlidesTop')?.value || document.getElementById('cNumSlides')?.value)||7;
  // Si el usuario forzó una posición de feed, fijarla antes de construir
  const forz = getFeedForzada();
  if(modo==='carrusel' && forz) setFeedPos(parseInt(forz));
  const nuevo = modo==='reel' ? buildReel(angulo,aiData)
              : modo==='post' ? buildPost(angulo,aiData)
              : buildCarrusel(angulo,aiData,numSlides);
  SLIDES.length=0;
  nuevo.forEach(s=>SLIDES.push(s));

  sEls[3].classList.add('ok');
  txEl.textContent='¡Listo!';
  await delay(500);

  cur=0;
  buildThumbs();
  show(0);
  scaleStage();
  document.getElementById('navCnt').textContent=
    modo==='post'?'1 / 1':`1 / ${SLIDES.length}`;

  // Avanzar contador de feed SOLO en modo Auto (si está forzado, se queda fijo)
  if(modo==='carrusel' && !getFeedForzada()) avanzarFeedPos();
  actualizarFeedLabel();

  // Actualizar panel Copy y tags Pexels
  actualizarCopy(angulo, aiData);
  actualizarTagsPexels(angulo);

  ov.classList.remove('on');
  btn.classList.remove('loading');
  document.getElementById('btnGenTxt').textContent='Generar';
}

async function fetchAI(angulo){
  const cfg=N();
  const angs=cfg.angulos||BANCO.angulos;
  const desc=angs[angulo]||Object.values(angs)[0];
  const prompt=`Eres Rosa María, ${cfg.persona}.

Escribes DIRIGIÉNDOTE EN SEGUNDA PERSONA (tú/tu) directamente al lector: ${cfg.lector}. Le hablas de TÚ, como si lo tuvieras delante.

REGLA CRÍTICA: NUNCA uses nombres propios. NUNCA hables del lector en tercera persona. SIEMPRE en segunda persona: "tú", "tu empresa", "tu negocio", "te pasa", "llevas años...".

Tu tono: ${cfg.tono}.

Genera copy para un carrusel de Instagram sobre: "${desc}".

Responde SOLO en JSON válido sin markdown:
{
  "hook": "headline impactante (puede tener \\n para saltos de línea)",
  "hook_sub": "subtítulo (1 frase corta, máx 12 palabras)",
  "frase": "frase polémica o de autoridad (puede tener \\n)",
  "frase_sub": "subtítulo de la frase (1-2 frases)",
  "lista_head": "titular del slide de lista",
  "lista": ["item 1 con *palabra clave* en cursiva", "item 2", "item 3", "item 4"],
  "debate_q": "pregunta del debate (puede tener \\n y *cursiva*)",
  "debate_a": "opción A (frase corta)",
  "debate_b": "opción B (frase corta)",
  "cta_head": "headline del CTA final (puede tener \\n)",
  "cta_body": "subtítulo CTA (1-2 frases)",
  "cta_word": "UNA PALABRA en mayúsculas para el CTA (ej: ${cfg.ctaEj})"
}`;

  const key = getGroqKey();
  if(!key) throw new Error('sin-key');   // sin key → generar() usa el banco local

  const res=await fetch('https://api.groq.com/openai/v1/chat/completions',{
    method:'POST',
    headers:{'Content-Type':'application/json','Authorization':'Bearer '+key},
    body:JSON.stringify({
      model:'llama-3.3-70b-versatile',
      temperature:0.9,
      max_tokens:1200,
      response_format:{type:'json_object'},
      messages:[{role:'user',content:prompt}]
    })
  });
  if(!res.ok) throw new Error(`HTTP ${res.status}`);
  const data=await res.json();
  const txt=data.choices?.[0]?.message?.content||'';
  return JSON.parse(txt.replace(/```json|```/g,'').trim());
}

/* ─── Clave Groq (IA de copy) — guardada solo en el navegador ─── */
function getGroqKey(){ return (localStorage.getItem('groq_key')||'').trim(); }
function getPixabayKey(){ return (localStorage.getItem('pixabay_key')|| (window.RM_CONFIG&&RM_CONFIG.pixabay_key) || '').trim(); }
function guardarKeyGroq(v){
  localStorage.setItem('groq_key', (v||'').trim());
  const st=document.getElementById('groqStatus');
  if(st){
    if(getGroqKey()){ st.style.color='#38B6FF'; st.textContent='✓ IA activada — cada generación usa copy nuevo'; }
    else { st.style.color='var(--UI-M)'; st.textContent='Sin key: se usa el banco de copys.'; }
  }
}

/* ══════════════════════════════════════════════════════
   SISTEMA DE FEED — contador persistente (posiciones 1-9)
   ══════════════════════════════════════════════════════ */
const FEED_KEY = 'rm_feed_pos';

function getFeedPos(){ return parseInt(localStorage.getItem(FEED_KEY)||'1')||1; }
function setFeedPos(p){ localStorage.setItem(FEED_KEY, String(((p-1)%9)+1)); }
function avanzarFeedPos(){ setFeedPos(getFeedPos()+1); }

// Posición FORZADA por el selector ('' = Auto, avanza por el feed)
let feedForzada = '';
function getFeedForzada(){ return feedForzada; }
function cambiarFeedSel(v){
  feedForzada = v;
  if(v){ setFeedPos(parseInt(v)); }   // fijar la posición elegida
  actualizarFeedLabel();
}

function actualizarFeedLabel(){
  const p = getFeedPos();
  const sel = document.getElementById('feedPosSel');
  if(sel){
    // Poblar opciones una sola vez
    if(sel.options.length <= 1){
      let html = `<option value="">Auto ▸ siguiente</option>`;
      for(let i=1;i<=9;i++) html += `<option value="${i}">P${i} · ${FEED_TIPOS[i]?.nombre||''}</option>`;
      sel.innerHTML = html;
    }
    sel.value = feedForzada;
    // Reflejar posición actual en la opción Auto
    if(sel.options[0]) sel.options[0].textContent = `Auto ▸ P${p}`;
  }
}

// Descripción de cada posición del feed — grid alterno #1A1A1A / #F5F1EA / foto
// (plantilla de referencia: 9 tiles, P5 = centro con el móvil)
const FEED_TIPOS = {
  1:{ nombre:'Portada + pills',        fondo_portada:'dark',  tema:'presentacion' },
  2:{ nombre:'Trabajar conmigo (foto)',fondo_portada:'light', tema:'metodo'       },
  3:{ nombre:'Foto ambiente + titular',fondo_portada:'foto',  tema:'contexto'     },
  4:{ nombre:'Beneficios / lista',     fondo_portada:'light', tema:'beneficios'   },
  5:{ nombre:'Móvil — tu anuncio',     fondo_portada:'dark',  tema:'demo'         },
  6:{ nombre:'3 claves numeradas',     fondo_portada:'light', tema:'educativo'    },
  7:{ nombre:'Testimonio / caso',      fondo_portada:'dark',  tema:'prueba'       },
  8:{ nombre:'Foto aspiracional',      fondo_portada:'foto',  tema:'deseo'        },
  9:{ nombre:'CTA + pills',            fondo_portada:'dark',  tema:'conversion'   },
};

// ⚠ PLANTILLAS de testimonio — SUSTITUYE por citas reales de tus clientes
const TESTIMONIOS_RM=[
  {q:'Pasamos de depender del boca a boca a tener obras planificadas con dos meses de antelación.', n:'Cliente', r:'Empresa de reformas · Madrid'},
  {q:'Por primera vez sé cuánto me cuesta conseguir una obra y cuánto me deja.', n:'Cliente', r:'Reformas integrales · Valencia'},
  {q:'Dejamos de pelear presupuestos a la baja. Ahora llegan clientes que valoran el trabajo.', n:'Cliente', r:'Empresa familiar · Sevilla'},
];

function mostrarFeedInfo(){
  const pos = getFeedPos();
  const tipos = Object.entries(FEED_TIPOS).map(([k,v])=>
    `${k==pos?'▶':'  '} P${k}: ${v.nombre}${k==pos?' ← SIGUIENTE':''}`
  ).join('\n');
  const msg = `POSICIÓN ACTUAL EN EL FEED: P${pos}\n\n${tipos}\n\n` +
    `Cada vez que generas un carrusel, la posición avanza automáticamente.\n` +
    `¿Resetear al inicio (P1)?`;
  if(confirm(msg)){ setFeedPos(1); actualizarFeedLabel(); }
}

/* ══════════════════════════════════════════════════════
   SECUENCIAS INTERNAS POR TIPO DE FEED
   Cada secuencia define los slides interiores según el
   número de slides seleccionado (3-10).
   Formato: { tipo, fondo, eye_key, rol }
   rol: qué contenido debe ir en ese slide
   ══════════════════════════════════════════════════════ */

// Bloques de construcción reutilizables
function bloqueHook(ai,angulo,eye,cta){
  const h=BANCO.hooks[angulo]||BANCO.hooks.sistema;
  return {tipo:'hook',fondo:'dark',eye,
    head:ai?ai.hook:rnd(h),
    body:ai?ai.hook_sub:rnd(BANCO.subtitulos),
    items:[],cta:'Desliza →'};
}
function bloqueFrase(ai,fondo,eye){
  return {tipo:'frase',fondo,eye:'Esto nadie lo dice',
    head:ai?ai.frase:rnd(BANCO.frases),
    body:ai?ai.frase_sub:rnd(BANCO.subtitulos),
    items:[],cta:'¿Incómodo? Bien. →'};
}
function bloqueLista(ai,angulo,fondo,eye,cta){
  const l=BANCO.listas[angulo]||BANCO.listas.default;
  return {tipo:'lista',fondo,eye,
    head:ai?ai.lista_head:'Lo que necesita tu cliente ideal para contratar sin pedir descuento.',
    body:'',items:ai&&ai.lista?ai.lista:rnd(l),cta:`${cta} →`};
}
function bloqueStats(eye){
  return {tipo:'stats',fondo:'light',eye:'Resultados que hablan',
    head:'',body:'',items:rnd(BANCO.stats),cta:''};
}
function bloqueStatsMetrica(){
  return {tipo:'lista',fondo:'light',eye:'Qué significa cada número',
    head:'Antes de ver las cifras, entiende qué miden.',
    body:'',
    items:['*CPL (Coste por lead)*: lo que pagas por cada contacto cualificado.',
           '*Tasa de cierre*: cuántos leads se convierten en obras reales.',
           '*ROI*: por cada euro invertido, cuánto recuperas.',
           '*Coste por obra*: el dato que de verdad importa a tu negocio.'],
    cta:'Ahora sí, los números →'};
}
function bloqueDebate(ai,deb,cta){
  return {tipo:'debate',fondo:'dark',eye:'Tú decides',
    head:ai?ai.debate_q:deb[0],body:'',
    items:[ai?ai.debate_a:deb[1],ai?ai.debate_b:deb[2]],
    cta:'Comenta tu respuesta ↓'};
}
function bloqueCTA(ai,cta){
  return {tipo:'cta',fondo:'dark',eye:'Siguiente paso',
    head:ai?ai.cta_head:`Si quieres clientes que pagan lo que vales,\nescríbeme una palabra.`,
    body:ai?ai.cta_body:`Sin rodeos. Te cuento cómo lo haría para tu empresa de reformas.`,
    items:[],cta:ai?`Escríbeme ${ai.cta_word} →`:`${cta} →`};
}
function bloqueCTAFoto(ai,cta){
  return {tipo:'autoridad',fondo:'dark',eye:'Siguiente paso',
    head:ai?ai.cta_head:`Hagamos que tu próximo cliente\nte encuentre.`,
    body:ai?ai.cta_body:`Estrategia. Enfoque. Resultados.`,
    items:[],cta:ai?`Escríbeme ${ai.cta_word} →`:`${cta} →`};
}
function bloqueProceso(cta){
  return {tipo:'proceso',fondo:'light',eye:'Paso a paso',
    head:'El proceso, sin humo',body:'',items:rnd(BANCO.procesos),cta:`${cta} →`};
}
function bloqueServicio(cta){
  return {tipo:'servicio',fondo:'light',eye:'Lo que incluye',
    head:'Cómo trabajo contigo',body:'',items:rnd(BANCO.servicios),cta:`${cta} →`};
}
function bloqueVsAgencia(cta){
  return {tipo:'lista',fondo:'dark',eye:'Tú decides bien',
    head:'¿Especialista o agencia?\nLo que nadie te explica antes de contratar.',
    body:'',
    items:['*Especialista*: enfoque total en tu sector, sin cuenta de 50 clientes encima.',
           '*Agencia*: más estructura, pero tu empresa es una más.',
           '*Especialista*: resultados medibles y conversación directa.',
           '*Agencia*: procesos más lentos, más intermediarios, más coste fijo.'],
    cta:`${cta} →`};
}
function bloquePruebaSocial(){
  return {tipo:'stats',fondo:'light',eye:'Números reales',
    head:'',body:'',items:rnd(BANCO.stats),cta:''};
}
function bloqueBA(){
  const ba=rnd(BANCO.antes);
  return {tipo:'ba',fondo:'light',eye:'',head:'',body:'',
    items:[`Antes: ${ba[0]}`,`Después: ${ba[1]}`],cta:'Sigue leyendo →'};
}
function bloqueFotoPortada(ai,angulo){
  const h=BANCO.hooks[angulo]||BANCO.hooks.sistema;
  return {tipo:'autoridad',fondo:'dark',eye:marcaEye(),
    head:ai?ai.hook:rnd(h),
    body:ai?ai.hook_sub:'',
    items:[],cta:'Desliza →'};
}
function bloqueFotoAmbiente(ai,angulo){
  const h=BANCO.hooks[angulo]||BANCO.hooks.sistema;
  return {tipo:'foto',fondo:'dark',eye:rnd(BANCO.eyebrows),
    head:ai?ai.hook:rnd(h),
    body:ai?ai.hook_sub:'',
    items:[],cta:'Desliza →'};
}

// Variantes tipo 7 (Revelación)
function buildRevelacion(ai,angulo,numSlides){
  const variante = rnd([7,7,7,7,7,7,7,7]); // índice 0-7 → variantes A-H
  const h=BANCO.hooks[angulo]||BANCO.hooks.sistema;
  const cta=rnd(BANCO.ctas);
  const eye=rnd(BANCO.eyebrows);

  // Todas las variantes: portada oscura, CTA al final, contenido en el medio
  const portada = {tipo:'hook',fondo:'dark',eye,
    head:ai?ai.hook:rnd(h),
    body:ai?ai.hook_sub:rnd(BANCO.subtitulos),
    items:[],cta:'Desliza →'};

  const VARIANTES = [
    // 7A — 1 error grande
    (n)=>{
      const mid=[
        {tipo:'frase',fondo:'dark',eye:'El error más caro',
          head:ai?ai.frase:rnd(BANCO.frases),body:'',items:[],cta:'Sigue →'},
        {tipo:'lista',fondo:'dark',eye:'Por qué en reformas es peor',
          head:'Este error cuesta más en el sector reformas que en cualquier otro.',
          body:'',items:['Sin filtro previo, cada visita es una tarde perdida.',
            'Sin cualificación, el precio siempre es el único argumento.',
            'Sin sistema, el siguiente mes empieza desde cero.',
            'Con la familia esperando en casa.'],cta:'Sigue →'},
        {tipo:'lista',fondo:'light',eye:'Las consecuencias reales',
          head:'Lo que pasa cuando no se corrige a tiempo.',body:'',
          items:rnd(BANCO.listas[angulo]||BANCO.listas.default),cta:'Sigue →'},
        {tipo:'lista',fondo:'light',eye:'La solución',
          head:'Cómo lo solucionamos desde el primer día.',body:'',
          items:rnd(BANCO.procesos),cta:`${cta} →`},
      ];
      return comprimirSlides(portada,mid,bloqueCTA(ai,cta),n);
    },
    // 7B — 3 errores
    (n)=>{
      const mid=[
        {tipo:'hook',fondo:'dark',eye:'Error 1 de 3',
          head:'Lanzar publicidad sin cualificar al lead.',
          body:'Generas visitas, no obras. El presupuesto se va, la agenda no se llena.',
          items:[],cta:'Siguiente error →'},
        {tipo:'hook',fondo:'dark',eye:'Error 2 de 3',
          head:'Usar las mismas creatividades semanas seguidas.',
          body:'La fatiga publicitaria es real. El coste sube, los resultados bajan.',
          items:[],cta:'Siguiente error →'},
        {tipo:'hook',fondo:'dark',eye:'Error 3 de 3',
          head:'No medir lo que importa de verdad.',
          body:'Las métricas de vanidad no pagan nóminas. El coste por obra sí importa.',
          items:[],cta:'Y la solución →'},
        {tipo:'lista',fondo:'light',eye:'Qué hacer en su lugar',
          head:'Los tres cambios que cambian el resultado.',body:'',
          items:rnd(BANCO.procesos),cta:`${cta} →`},
      ];
      return comprimirSlides(portada,mid,bloqueCTA(ai,cta),n);
    },
    // 7C — X cosas que no sabías
    (n)=>{
      const mid=[
        {tipo:'hook',fondo:'dark',eye:'Cosa 1',
          head:'Tu cliente ideal ya está en Meta buscando una empresa de reformas.',
          body:'Solo que no encuentra la tuya porque no la estás poniendo delante de él.',
          items:[],cta:'Sigue →'},
        {tipo:'hook',fondo:'dark',eye:'Cosa 2',
          head:'El boca a boca no se ha ido.\nSimplemente ya no es suficiente.',
          body:'Con un sistema digital, el boca a boca se convierte en multiplicador.',
          items:[],cta:'Sigue →'},
        {tipo:'hook',fondo:'dark',eye:'Cosa 3',
          head:'Bajar precios para competir es la señal de que falta posicionamiento.',
          body:'El cliente premium no busca el más barato. Busca al que más inspira confianza.',
          items:[],cta:'Sigue →'},
        {tipo:'hook',fondo:'light',eye:'Cosa 4',
          head:'Un lead cualificado vale diez veces más que uno sin filtrar.',
          body:'No es cuestión de volumen. Es cuestión de calidad antes de la visita.',
          items:[],cta:'Lo que esto cambia →'},
        {tipo:'lista',fondo:'light',eye:'Lo que cambia saberlo',
          head:'Aplicar esto transforma la forma en que captas obras.',body:'',
          items:rnd(BANCO.procesos),cta:`${cta} →`},
      ];
      return comprimirSlides(portada,mid,bloqueCTA(ai,cta),n);
    },
    // 7D — Mitos vs realidad
    (n)=>{
      const mid=[
        {tipo:'hook',fondo:'dark',eye:'Mito 1',
          head:'«La publicidad no funciona para reformas.»',
          body:'REALIDAD: No funciona sin estrategia de cualificación. Con ella, es el canal más predecible.',
          items:[],cta:'Siguiente mito →'},
        {tipo:'hook',fondo:'dark',eye:'Mito 2',
          head:'«Necesito muchos seguidores para vender.»',
          body:'REALIDAD: Con 500 seguidores y una campaña bien segmentada puedes llenar tu agenda.',
          items:[],cta:'Siguiente mito →'},
        {tipo:'hook',fondo:'dark',eye:'Mito 3',
          head:'«Ya lo intenté y no funcionó.»',
          body:'REALIDAD: Probaste visibilidad sin sistema de conversión. Son cosas distintas.',
          items:[],cta:'La realidad completa →'},
        {tipo:'lista',fondo:'light',eye:'La verdad sobre cada mito',
          head:'Lo que cambia cuando aplicas estrategia real.',body:'',
          items:rnd(BANCO.procesos),cta:`${cta} →`},
      ];
      return comprimirSlides(portada,mid,bloqueCTA(ai,cta),n);
    },
    // 7E — Lo que nadie te dice
    (n)=>{
      const mid=[
        {tipo:'hook',fondo:'dark',eye:'Lo que nadie te dice — 1',
          head:'La mayoría de leads que recibes ya han decidido\nantes de que contestes.',
          body:'Lo que comunicas antes de la llamada decide si viene con dinero o con excusas.',
          items:[],cta:'Sigue →'},
        {tipo:'hook',fondo:'dark',eye:'Lo que nadie te dice — 2',
          head:'El presupuesto de publicidad no es el problema.\nEs cómo se gestiona.',
          body:'Con 300€/mes bien invertidos superas a quien gasta 2.000€ sin estrategia.',
          items:[],cta:'Sigue →'},
        {tipo:'hook',fondo:'dark',eye:'Lo que nadie te dice — 3',
          head:'Tu mejor vendedor no eres tú.\nEs la percepción que tienes antes de hablar.',
          body:'La autoridad digital trabaja mientras tú estás en obra.',
          items:[],cta:'Por qué importa →'},
        {tipo:'lista',fondo:'light',eye:'Por qué importa todo esto',
          head:'Lo que cambia cuando lo aplicas.',body:'',
          items:rnd(BANCO.procesos),cta:`${cta} →`},
      ];
      return comprimirSlides(portada,mid,bloqueCTA(ai,cta),n);
    },
    // 7F — Antes/después mental
    (n)=>{
      const mid=[
        {tipo:'hook',fondo:'dark',eye:'Así piensa la mayoría',
          head:'«Necesito más visitas para cerrar más obras.»',
          body:'Más visitas sin filtro = más tardes perdidas, más presupuestos que no se cierran.',
          items:[],cta:'El problema de ese enfoque →'},
        {tipo:'hook',fondo:'dark',eye:'El problema de ese enfoque',
          head:'Cuando cualquier lead es bienvenido,\ntu tiempo no tiene valor.',
          body:'Y el cliente lo nota antes de la visita.',
          items:[],cta:'Así debería pensarse →'},
        {tipo:'hook',fondo:'light',eye:'Así debería pensarse',
          head:'«Necesito menos visitas, pero mejores.»',
          body:'Un lead cualificado cierra en la primera visita. Sin regateo. Sin dudas.',
          items:[],cta:'El resultado del cambio →'},
        {tipo:'lista',fondo:'light',eye:'El resultado del cambio',
          head:'Lo que ocurre cuando cambias el enfoque.',body:'',
          items:rnd(BANCO.procesos),cta:`${cta} →`},
      ];
      return comprimirSlides(portada,mid,bloqueCTA(ai,cta),n);
    },
    // 7G — La pregunta que nadie hace
    (n)=>{
      const mid=[
        {tipo:'frase',fondo:'dark',eye:'La pregunta que nadie hace',
          head:'¿Por qué una empresa de reformas peor que la tuya\ncierra más obras que tú?',
          body:'No es la calidad. Es lo que comunican antes de que el cliente llame.',
          items:[],cta:'La respuesta incómoda →'},
        {tipo:'hook',fondo:'dark',eye:'La respuesta incómoda',
          head:'Porque la percepción llega antes que la realidad.',
          body:'El cliente decide por lo que ve, no por lo que tú sabes que haces.',
          items:[],cta:'Qué hay detrás →'},
        {tipo:'lista',fondo:'light',eye:'Qué hay detrás',
          head:'Lo que construye esa percepción antes de la visita.',body:'',
          items:['*Imagen digital*: ¿transmite el nivel real de tu trabajo?',
            '*Comunicación*: ¿habla el idioma de tu cliente ideal?',
            '*Cualificación*: ¿filtra antes de que llegue a ti?',
            '*Consistencia*: ¿apareces cuando tu cliente te busca?'],cta:'Cómo cambia tu estrategia →'},
        {tipo:'lista',fondo:'light',eye:'Cómo cambia tu estrategia',
          head:'Cuando corriges la percepción, cambia el tipo de cliente que llega.',body:'',
          items:rnd(BANCO.procesos),cta:`${cta} →`},
      ];
      return comprimirSlides(portada,mid,bloqueCTA(ai,cta),n);
    },
    // 7H — Ranking de peor a mejor
    (n)=>{
      const mid=[
        {tipo:'hook',fondo:'dark',eye:'Nivel 1 — Mal',
          head:'Sin publicidad, sin sistema.\nSolo boca a boca.',
          body:'Ingresos impredecibles. El mes siguiente es siempre una incógnita.',
          items:[],cta:'Nivel 2 →'},
        {tipo:'hook',fondo:'dark',eye:'Nivel 2 — Regular',
          head:'Con publicidad, sin estrategia.\nDinero que se va sin resultados claros.',
          body:'Visibilidad sin cualificación. Leads que no cierran.',
          items:[],cta:'Nivel 3 →'},
        {tipo:'hook',fondo:'light',eye:'Nivel 3 — Bien',
          head:'Con publicidad y cualificación.\nLeads que llegan preparados.',
          body:'Mejor ratio de cierre. Menos visitas, más obras.',
          items:[],cta:'Nivel 4 →'},
        {tipo:'hook',fondo:'light',eye:'Nivel 4 — Óptimo',
          head:'Sistema completo: atracción, cualificación,\nseguimiento y escalado.',
          body:'Agenda predecible. Clientes premium. Tiempo recuperado.',
          items:[],cta:'¿En qué nivel estás? →'},
        {tipo:'lista',fondo:'light',eye:'¿En qué nivel estás tú?',
          head:'El nivel donde estás determina el techo de tu empresa.',body:'',
          items:rnd(BANCO.procesos),cta:`${cta} →`},
      ];
      return comprimirSlides(portada,mid,bloqueCTA(ai,cta),n);
    },
  ];

  const varIdx = Math.floor(Math.random()*8);
  return VARIANTES[varIdx](numSlides);
}

// Compresión inteligente: siempre portada + CTA, el medio se comprime/expande
function comprimirSlides(portada, medios, ctaSlide, n){
  if(n<=2) return [portada, ctaSlide];
  if(n===3) return [portada, medios[0]||ctaSlide, ctaSlide];

  const hueco = n - 2; // slots disponibles para el medio
  // Seleccionar los primeros `hueco` medios (ya ordenados por prioridad)
  const seleccionados = medios.slice(0, hueco);
  return [portada, ...seleccionados, ctaSlide].slice(0, n);
}

/* ─── Construir carrusel — NUEVO SISTEMA ─── */
function buildCarrusel(angulo,ai,numSlides=7){
  const pos = getFeedPos();
  const eye = rnd(BANCO.eyebrows);
  const cta = rnd(BANCO.ctas);
  const deb = rnd(BANCO.debates);
  const listaArr = BANCO.listas[angulo]||BANCO.listas.default;

  let slides = [];

  switch(pos){

    // P1 — Portada + pills (presentación/autoridad, estilo plantilla)
    case 1:{
      const portada = {tipo:'pills',fondo:'dark',eye:marcaEye(),
        head: ai?ai.hook:rnd(BANCO.hooks[angulo]||BANCO.hooks.sistema),
        body:'',
        items:N().pills,
        cta:'Desliza →'};
      const medios = [
        {tipo:'hook',fondo:'dark',eye:'El problema que resuelvo',
          head:ai?ai.frase:rnd(BANCO.frases),
          body:ai?ai.frase_sub:rnd(BANCO.subtitulos),items:[],cta:'Sigue →'},
        {tipo:'lista',fondo:'light',eye:'Por qué yo',
          head:'Lo que me diferencia de quien promete y no entrega.',body:'',
          items:['Especializada 100% en empresas de reformas en España.',
            'Solo acepto clientes con los que puedo generar resultados reales.',
            'Reportes en lenguaje de negocio, sin tecnicismos.',
            'Tú te centras en las obras. Yo me centro en llenar tu agenda.'],cta:'Cómo lo hago →'},
        {tipo:'proceso',fondo:'light',eye:'Cómo lo resuelvo',
          head:'El proceso, sin humo.',body:'',items:rnd(BANCO.procesos),cta:'Los resultados →'},
        bloqueStats(eye),
        bloqueCTAFoto(ai,cta),
      ];
      slides = comprimirSlides(portada, medios, bloqueCTAFoto(ai,cta), numSlides);
      break;
    }

    // P2 — Trabajar conmigo (light + tu foto, estilo plantilla)
    case 2:{
      const portada = {tipo:'fototxt',fondo:'light',eye:'Cómo es trabajar conmigo',
        head:N().p2head,
        body: ai?ai.hook_sub:N().p2sub,
        items:[],cta:'Desliza →'};
      const medios = [
        bloqueLista(ai,angulo,'dark',eye,cta),
        bloqueFrase(ai,'dark',eye),
        {tipo:'lista',fondo:'light',eye:'El resumen',
          head:'Lo que te llevas de este carrusel.',body:'',
          items:rnd(BANCO.procesos),cta:'Guarda esto →'},
        bloqueDebate(ai,deb,cta),
      ];
      slides = comprimirSlides(portada, medios, bloqueCTA(ai,cta), numSlides);
      break;
    }

    // P3 — Foto ambiente + texto (contexto/sector)
    case 3:{
      const portada = bloqueFotoAmbiente(ai,angulo);
      const medios = [
        {tipo:'hook',fondo:'dark',eye:'El problema del sector',
          head:ai?ai.hook:rnd(BANCO.hooks[angulo]||BANCO.hooks.sistema),
          body:'Este es el punto de partida de la mayoría de empresas de reformas en España.',
          items:[],cta:'Lo que marca la diferencia →'},
        bloqueLista(ai,angulo,'light',eye,cta),
        {tipo:'proceso',fondo:'light',eye:'Cómo aplicarlo',
          head:'Los pasos que cambian el resultado.',body:'',
          items:rnd(BANCO.procesos),cta:'El resultado →'},
        bloqueStats(eye),
      ];
      slides = comprimirSlides(portada, medios, bloqueCTA(ai,cta), numSlides);
      break;
    }

    // P4 — Beneficios / lista (light, estilo plantilla)
    case 4:{
      const portada = {tipo:'servicio',fondo:'light',eye:'Lo que consigues',
        head:'Un sistema de captación\npensado para reformas.',body:'',
        items:['Leads cualificados que sí pueden pagar tu trabajo.',
          'Agenda previsible: obras planificadas con semanas de antelación.',
          'Anuncios que hablan el idioma de tu cliente ideal.',
          'Datos claros: sabes qué entra y cuánto cuesta.'],cta:'Los números →'};
      const medios = [
        bloqueStatsMetrica(),
        {tipo:'hook',fondo:'dark',eye:'Contexto — antes',
          head:'Antes de empezar, esto es lo que solía pasar.',
          body:rnd(BANCO.hooks[angulo]||BANCO.hooks.sistema),
          items:[],cta:'Qué se hizo →'},
        {tipo:'proceso',fondo:'light',eye:'Qué se hizo',
          head:'La estrategia que cambió los números.',body:'',
          items:rnd(BANCO.procesos),cta:'El desglose →'},
        bloqueBA(),
        {tipo:'lista',fondo:'light',eye:'Qué significa para ti',
          head:'Estos resultados no son un caso aislado.\nSon un sistema replicable.',body:'',
          items:['Un sistema que cualifica antes de la visita.',
            'Creatividades que hablan el idioma de tu cliente ideal.',
            'Optimización semanal basada en datos reales.',
            'Escalado cuando los números lo piden.'],cta:`${cta} →`},
      ];
      slides = comprimirSlides(portada, medios, bloqueCTA(ai,cta), numSlides);
      break;
    }

    // P5 — Móvil con tu anuncio (centro del grid, estilo plantilla)
    case 5:{
      const portada = {tipo:'movil',fondo:'dark',eye:'Así te ve tu cliente ideal',
        head:'Tu empresa, en el móvil\nde quien busca reformar.',
        body:'Reformas de alto valor · Presupuesto en 24h',
        items:[],cta:'Desliza →'};
      const medios = [
        {tipo:'hook',fondo:'dark',eye:'Por qué esto importa',
          head:ai?ai.hook:rnd(BANCO.hooks[angulo]||BANCO.hooks.sistema),
          body:ai?ai.hook_sub:'',items:[],cta:'El error común →'},
        {tipo:'hook',fondo:'dark',eye:'El error común',
          head:'Invertir sin posicionamiento previo\nes gastar sin base sólida.',
          body:'El anuncio amplifica lo que ya existe. Si la base es débil, el resultado también.',
          items:[],cta:'La alternativa →'},
        bloqueLista(ai,angulo,'light',eye,cta),
      ];
      slides = comprimirSlides(portada, medios, bloqueCTA(ai,cta), numSlides);
      break;
    }

    // P6 — 3 claves numeradas (light, estilo plantilla)
    case 6:{
      const portada = {tipo:'claves',fondo:'light',eye:'Antes de invertir',
        head:'¿Invertir en publicidad?\n3 claves que debes saber.',body:'',
        items:(ai&&ai.lista)?ai.lista.slice(0,3):[
          'Define presupuesto: cuánto puedes invertir sin ahogar la caja.',
          'Piensa a medio plazo: los sistemas rentables se construyen, no se improvisan.',
          'Exige datos: si no puedes medirlo, no lo pagues.'],
        cta:'Desliza →'};
      const medios = [
        {tipo:'lista',fondo:'light',eye:'Para quién es',
          head:'Este servicio es para ti si...',body:'',
          items:['Tienes una empresa de reformas con equipo propio.',
            'Ya tienes obras pero quieres más estabilidad y previsibilidad.',
            'Estás harto de depender del boca a boca o de leads sin filtrar.',
            'Quieres escalar sin que todo dependa de ti.'],cta:'Cómo funciona →'},
        bloqueProceso(cta),
        bloqueVsAgencia(cta),
        bloqueStats(eye),
      ];
      slides = comprimirSlides(portada, medios, bloqueCTA(ai,cta), numSlides);
      break;
    }

    // P7 — Testimonio / caso de éxito (dark, estilo plantilla)
    // (la Revelación de 8 variantes sigue disponible en buildRevelacion)
    case 7:{
      const t = rnd(TESTIMONIOS_RM);
      const portada = {tipo:'testimonio',fondo:'dark',eye:'Lo que dicen mis clientes',
        head:t.q, body:`${t.n}::${t.r}`, items:[], cta:'El caso completo →'};
      const medios = [
        bloqueStatsMetrica(),
        bloqueStats(eye),
        bloqueBA(),
        bloqueProceso(cta),
      ];
      slides = comprimirSlides(portada, medios, bloqueCTA(ai,cta), numSlides);
      break;
    }

    // P8 — Foto aspiracional (full-bleed, estilo plantilla) + proceso interior
    case 8:{
      const proc = rnd(BANCO.procesos);
      const portada = {tipo:'foto',fondo:'dark',eye:rnd(BANCO.eyebrows),
        head:'El estándar que tu cliente\nespera ver antes de llamarte.',
        body:'Tu mejor obra es tu mejor anuncio. Úsala.',
        items:[],cta:'Desliza →',imgLayout:'bg-full',txtPos:'bottom'};
      const pasos = proc.map((p,i)=>{
        const [tit,desc]=p.split(':');
        return {tipo:'hook',fondo:i%2===0?'dark':'light',
          eye:`Paso ${i+1} de ${proc.length}`,
          head:tit,body:desc||'',items:[],cta:i<proc.length-1?'Siguiente →':'El resultado →'};
      });
      const resultado = {tipo:'stats',fondo:'light',eye:'El resultado final',
        head:'',body:'',items:rnd(BANCO.stats),cta:''};
      const medios = [...pasos, resultado];
      slides = comprimirSlides(portada, medios, bloqueCTA(ai,cta), numSlides);
      break;
    }

    // P9 — CTA + pills (dark, estilo plantilla)
    case 9:{
      const portada = {tipo:'pills',fondo:'dark',eye:'Trabaja conmigo',
        head: ai?ai.cta_head:'El crecimiento no es suerte.\nEs estrategia.',body:'',
        items:N().pills,
        cta:ai?`Escríbeme ${ai.cta_word} →`:`${cta} →`};
      const medios = [
        {tipo:'hook',fondo:'dark',eye:'Mi propuesta de valor',
          head:ai?ai.frase:rnd(BANCO.frases),
          body:ai?ai.frase_sub:'',items:[],cta:'La objeción más común →'},
        {tipo:'hook',fondo:'dark',eye:'La objeción que más escucho',
          head:'«Ya probé publicidad y no funcionó.»',
          body:'No probaste publicidad. Probaste visibilidad sin sistema de cualificación. Son cosas distintas.',
          items:[],cta:'Mi respuesta →'},
        {tipo:'lista',fondo:'light',eye:'Por qué ahora es diferente',
          head:'Lo que hace que este sistema funcione donde otros fallan.',body:'',
          items:rnd(BANCO.procesos),cta:'Los números →'},
        bloquePruebaSocial(),
      ];
      slides = comprimirSlides(portada, medios, {tipo:'cta',fondo:'dark',eye:'Escríbeme',
        head:'Una sola palabra.\nTe cuento cómo lo haría para tu empresa.',
        body:'Sin compromiso. Sin rodeos.',
        items:[],cta:ai?`Escríbeme ${ai.cta_word} →`:`${cta} →`}, numSlides);
      break;
    }

    default:{
      // Fallback genérico si algo falla
      slides = buildCarruselLegacy(angulo,ai,numSlides);
    }
  }

  return slides;
}

// Fallback legacy por si algo falla
function buildCarruselLegacy(angulo,ai,numSlides=7){
  const hooksArr=BANCO.hooks[angulo]||BANCO.hooks.sistema;
  const listaArr=BANCO.listas[angulo]||BANCO.listas.default;
  const ba=rnd(BANCO.antes);
  const deb=rnd(BANCO.debates);
  const eye=rnd(BANCO.eyebrows);
  const cta=rnd(BANCO.ctas);
  const seq=rnd([['dark','light','blue','dark','light','dark','dark'],['dark','light','dark','dark','light','dark','blue']]);
  const todos=[
    {tipo:'hook',fondo:seq[0],eye,head:ai?ai.hook:rnd(hooksArr),body:ai?ai.hook_sub:rnd(BANCO.subtitulos),items:[],cta:'Desliza →'},
    {tipo:'ba',fondo:seq[1],eye:'',head:'',body:'',items:[`Antes: ${ba[0]}`,`Después: ${ba[1]}`],cta:'Sigue →'},
    {tipo:'frase',fondo:seq[2],eye:'Esto nadie lo dice',head:ai?ai.frase:rnd(BANCO.frases),body:ai?ai.frase_sub:rnd(BANCO.subtitulos),items:[],cta:'¿Incómodo? Bien. →'},
    {tipo:'lista',fondo:seq[3],eye,head:ai?ai.lista_head:'Lo que necesita tu cliente ideal.',body:'',items:ai&&ai.lista?ai.lista:rnd(listaArr),cta:`${cta} →`},
    {tipo:'stats',fondo:'light',eye:'Resultados que hablan',head:'',body:'',items:rnd(BANCO.stats),cta:''},
    {tipo:'debate',fondo:seq[5],eye:'Tú decides',head:ai?ai.debate_q:deb[0],body:'',items:[ai?ai.debate_a:deb[1],ai?ai.debate_b:deb[2]],cta:'Comenta ↓'},
    {tipo:'cta',fondo:seq[6],eye:'Siguiente paso',head:ai?ai.cta_head:`Si quieres clientes que pagan lo que vales,\nescríbeme.`,body:ai?ai.cta_body:'',items:[],cta:ai?`Escríbeme ${ai.cta_word} →`:`${cta} →`},
  ];
  return todos.slice(0,numSlides);
}

/* ─── Construir post único ─── */
/* ─── Construir portada de REEL + guión ─── */
let ULTIMO_GUION = '';
function buildReel(angulo,ai){
  const hook = ai ? ai.hook : rnd(BANCO.hooks[angulo]||BANCO.hooks.sistema);
  const sub  = ai ? ai.hook_sub : rnd(BANCO.subtitulos);
  const cta  = ai ? `Escríbeme ${ai.cta_word}` : rnd(BANCO.ctas);
  // Guion de 20-30s: gancho + 3 puntos + cierre
  const puntos = (ai && ai.lista) ? ai.lista.slice(0,3) : (BANCO.listas[angulo]||BANCO.listas.default).slice(0,3);
  ULTIMO_GUION =
`🎬 GUION REEL — ${angulo}  ·  ${MARCA}

⏱ 0-3s · GANCHO (a cámara, directo):
"${hook}"

⏱ 3-6s · CONTEXTO:
${sub}

⏱ 6-20s · DESARROLLO (3 claves):
1. ${puntos[0]||''}
2. ${puntos[1]||''}
3. ${puntos[2]||''}

⏱ 20-27s · CIERRE + CTA:
"${cta}. Te leo en comentarios o por DM."

— NOTAS DE GRABACIÓN —
• Formato vertical 9:16, buena luz natural, plano medio.
• Sube subtítulos siempre (80% ve sin sonido).
• Texto en pantalla = el gancho los primeros 3s.
• Portada = esta imagen (súbela como "cover" del reel).

— CAPTION —
${hook}

${sub}

${cta} 👇
#reformas #empresadereformas #marketingdigital #metaads #reformasintegrales`;

  return [{tipo:'reel', fondo:'dark', eye:'Reel', head:hook, body:sub,
    items:[], cta:'Dale al play', ovOpacity:55}];
}

function buildPost(angulo,ai){
  const hooksArr=BANCO.hooks[angulo]||BANCO.hooks.sistema;
  const tipo=rnd(['hook','frase']);
  const fondo=rnd(['dark','light','blue']);
  const eye=rnd(BANCO.eyebrows);
  const cta=rnd(BANCO.ctas);
  if(tipo==='frase'){
    return[{tipo:'frase',fondo,eye,
      head:ai?ai.frase:rnd(BANCO.frases),
      body:ai?ai.frase_sub:rnd(BANCO.subtitulos),
      items:[],cta:`${cta} →`}];
  }
  return[{tipo:'post',fondo,eye,
    head:ai?ai.hook:rnd(hooksArr),
    body:ai?ai.hook_sub:rnd(BANCO.subtitulos),
    items:[],cta:`${cta} →`}];
}

/* ═══════════════════════════════════════════
   PANEL COPY
   ═══════════════════════════════════════════ */
// Contexto de la última generación, para poder refrescar el COPY al vuelo
let COPY_CTX = { angulo:'sistema', ai:null };

function actualizarCopy(angulo, ai){
  COPY_CTX = { angulo: angulo||COPY_CTX.angulo, ai: ai||null };
  refrescarCopy();
}

// Construye el COPY a partir del CONTENIDO REAL en pantalla (SLIDES + modo)
function refrescarCopy(){
  const container = document.getElementById('copyContent');
  if(!container) return;
  const angulo = COPY_CTX.angulo;
  const ai = COPY_CTX.ai;
  const copyData = BANCO.instagramCopy[angulo] || BANCO.instagramCopy.default;
  const esc = s => String(s==null?'':s).replace(/[<>]/g,'');

  // Hook REAL = titular del primer slide generado (lo que se ve en la imagen)
  const hookReal = (SLIDES[0]?.head) || (ai?ai.hook:'') || (BANCO.hooks[angulo]?.[0]) || '';
  const ctaReal  = (SLIDES[SLIDES.length-1]?.cta || '').replace(/\s*[→↓👇]+\s*$/,'').trim();

  // Etiqueta de formato coherente con lo generado
  const fmt = modo==='reel' ? '🎬 Reel'
            : modo==='post' ? '📄 Post'
            : `🗂 Carrusel · ${SLIDES.length} slides`;

  // ── Caption: arranca con el HOOK real + desarrollo del banco (sin su hook) ──
  const partes = (copyData.caption||'').split('\n\n');
  const cuerpo = partes.length>1 ? partes.slice(1).join('\n\n') : (copyData.caption||'');
  let caption = hookReal ? `${hookReal}\n\n${cuerpo}` : (copyData.caption||'');
  if(ctaReal && !caption.includes(ctaReal)) caption += `\n\n${ctaReal} 👇`;
  const hashtags = (getNicho()==='personal') ? N().hashtags : (copyData.hashtags||N().hashtags);

  // ── Reel: además mostrar el GUION generado ──
  const bloqueGuion = (modo==='reel' && typeof ULTIMO_GUION!=='undefined' && ULTIMO_GUION) ? `
    <div class="copy-label" style="margin-top:4px">Guión del reel</div>
    <div class="copy-text" style="white-space:pre-wrap;font-size:10px">${esc(ULTIMO_GUION)}</div>
    <button class="cbtn" onclick="copiar(this.previousElementSibling.textContent)">📋 Copiar guión</button>` : '';

  container.innerHTML = `
    <div style="display:inline-block;font-size:8px;font-weight:700;letter-spacing:.08em;color:var(--UI-A);background:rgba(56,182,255,.12);padding:3px 8px;border-radius:4px;margin-bottom:2px">${fmt}</div>
    <div style="font-size:8px;color:var(--UI-M);margin:2px 0 4px">Texto tomado de lo que ves en pantalla ahora</div>
    <div class="copy-label">Hook (headline del slide 1)</div>
    <div class="copy-text">${esc(hookReal)}</div>
    <button class="cbtn" onclick="copiar(this.previousElementSibling.textContent)">📋 Copiar hook</button>
    ${bloqueGuion}
    <div class="copy-label">Caption Instagram</div>
    <div class="copy-text" style="white-space:pre-wrap">${esc(caption)}</div>
    <button class="cbtn" onclick="copiar(this.previousElementSibling.textContent)">📋 Copiar caption</button>
    <div class="copy-label">Hashtags</div>
    <div class="copy-text hashtags">${hashtags}</div>
    <button class="cbtn" onclick="copiar(this.previousElementSibling.textContent)">📋 Copiar hashtags</button>
    <div class="copy-label" style="margin-top:4px">Todo junto</div>
    <button class="cbtn" onclick="copiar(\`${esc(caption).replace(/`/g,'')}\n\n${hashtags}\`)">📋 Copiar caption + hashtags</button>
  `;

  actualizarPromptsMJ(angulo);
}

/* ═══════════════════════════════════════════
   PROMPTS MIDJOURNEY / DALL·E
   ═══════════════════════════════════════════ */
const MJ_BASE = '--ar 4:5 --style raw --v 6.1 --q 2';
const MJ_BASE_SQ = '--ar 1:1 --style raw --v 6.1 --q 2';

const MJ_PROMPTS = {
  // Por tipo de slide
  foto_hook: [
    'modern spanish home renovation, open plan living room, white walls, warm lighting, minimal furniture, editorial photography, architectural digest style',
    'beautiful kitchen renovation spain, marble countertops, dark cabinetry, professional photo, interior design magazine',
    'luxury bathroom renovation, freestanding bathtub, natural stone, soft light, high-end real estate photo',
  ],
  foto_empresario: [
    'spanish male entrepreneur 40s, professional business photo, modern office, blue jacket, confident smile, editorial portrait',
    'construction company owner spain, professional headshot, neutral background, business attire, trust and authority',
    'renovation company director, professional portrait, modern workspace, natural light, high-end corporate photography',
  ],
  foto_media_buyer: [
    'marketing dashboard on laptop screen, meta ads manager, campaign results, dark office, blue light, professional workspace, top view flat lay',
    'digital marketing graphs charts growing, facebook ads performance, clean data visualization, dark background, blue accent colors',
    'media buyer workspace, dual monitors showing ad campaigns, analytics dashboard, modern dark office, professional atmosphere',
  ],
  foto_antes: [
    'old outdated kitchen before renovation, worn cabinets, dated style, realistic interior photo, natural light',
    'bathroom before renovation, old tiles, outdated fixtures, worn surfaces, realistic documentary photography',
    'living room before renovation, old furniture, worn walls, dated interior, realistic photo',
  ],
  foto_despues: [
    'stunning modern kitchen after renovation, new cabinets, stone countertops, professional interior photography, warm lighting',
    'luxury bathroom after renovation, new tiles, modern fixtures, spa atmosphere, architectural photography',
    'contemporary living room after renovation, clean design, neutral palette, designer furniture, natural light',
  ],
  foto_autoridad: [
    'professional woman media buyer 35 years old, blue blazer, laptop, modern office, confident posture, editorial portrait, natural light',
    'female marketing strategist, professional headshot, home office, warm neutral tones, approachable and expert look',
  ],
  foto_graficas: [
    'facebook meta ads dashboard showing positive ROI results, laptop screen, dark office, professional photo, blue screen glow',
    'google ads campaign analytics showing growth charts, marketing results dashboard, professional workspace photography',
    'social media marketing results presentation, graphs showing increase, business meeting, professional environment',
  ],
};

// Búsquedas Pexels sugeridas por ángulo
const PEXELS_SUGERIDAS = {
  bocaboca:   ['home renovation', 'construction worker', 'house remodel'],
  regateo:    ['business negotiation', 'renovation quote', 'construction budget'],
  saturacion: ['stressed businessman', 'overworked entrepreneur', 'construction stress'],
  autoridad:  ['professional woman laptop', 'marketing expert', 'business authority'],
  sistema:    ['business growth chart', 'marketing dashboard', 'sales funnel'],
  tiempo:     ['family home', 'work life balance', 'evening dinner family'],
  familia:    ['happy family home', 'renovation new home', 'family house'],
  premium:    ['luxury home renovation', 'high end interior', 'premium kitchen'],
  objecion:   ['business meeting', 'client presentation', 'marketing strategy'],
  precio:     ['renovation quote', 'construction budget', 'home improvement cost'],
  margen:     ['business profit', 'revenue growth', 'construction company success'],
  estabilidad:['modern renovated home', 'beautiful interior', 'home transformation'],
  resultados: ['marketing results', 'business analytics', 'campaign success'],
  default:    ['home renovation', 'interior design', 'modern house'],
};

function actualizarPromptsMJ(angulo){
  const tipo = SLIDES[cur]?.tipo || 'hook';
  const esSq = isSq();
  const params = esSq ? MJ_BASE_SQ : MJ_BASE;

  // Seleccionar prompts relevantes según slide activo y ángulo
  let prompts = [];

  if(['foto','fototxt'].includes(tipo)){
    prompts = MJ_PROMPTS.foto_hook;
  } else if(tipo==='bafoto'){
    prompts = [...MJ_PROMPTS.foto_antes.slice(0,1), ...MJ_PROMPTS.foto_despues.slice(0,1)];
  } else if(tipo==='autoridad'){
    prompts = MJ_PROMPTS.foto_autoridad;
  } else if(['autoridad','sistema','resultados'].includes(angulo)){
    prompts = [...MJ_PROMPTS.foto_media_buyer, ...MJ_PROMPTS.foto_graficas];
  } else if(['premium','estabilidad','margen'].includes(angulo)){
    prompts = MJ_PROMPTS.foto_hook;
  } else {
    prompts = [...MJ_PROMPTS.foto_hook.slice(0,1), ...MJ_PROMPTS.foto_empresario.slice(0,1), ...MJ_PROMPTS.foto_media_buyer.slice(0,1)];
  }

  // Búsquedas Pexels sugeridas
  const pexelsSug = PEXELS_SUGERIDAS[angulo] || PEXELS_SUGERIDAS.default;

  const mjEl = document.getElementById('mjContent');
  if(!mjEl) return;

  mjEl.innerHTML = `
    <div class="copy-label" style="margin-top:0">Buscar en Pexels</div>
    <div style="display:flex;flex-wrap:wrap;gap:4px;margin-top:4px">
      ${pexelsSug.map(q=>`<span class="mj-tag" style="cursor:pointer" onclick="buscarPexelsTermino('${q}')">${q}</span>`).join('')}
    </div>

    <div class="copy-label" style="margin-top:10px">Prompts Midjourney / DALL·E</div>
    <div style="font-size:8px;color:var(--UI-M);margin-bottom:6px">Copia, pega en Midjourney o ChatGPT Image. El estilo ya incluye los parámetros.</div>
    ${prompts.map((pr,i)=>`
      <div class="mj-block" id="mjp${i}">${pr}, ${params}</div>
      <button class="cbtn" onclick="copiar(document.getElementById('mjp${i}').textContent)">📋 Copiar prompt ${i+1}</button>
    `).join('')}

    <div class="copy-label" style="margin-top:8px">Prompt estilo marca RM</div>
    <div class="mj-block" id="mjpRM">dark minimal background #1A1A1A, white cream text overlay, blue accent #38B6FF, instagram post design for renovation company marketing, professional editorial style, montserrat font aesthetic ${params}</div>
    <button class="cbtn" onclick="copiar(document.getElementById('mjpRM').textContent)">📋 Copiar prompt marca</button>
  `;
}

/* ═══════════════════════════════════════════
   PEXELS API
   ═══════════════════════════════════════════ */
// API Key de Pexels por defecto (gratuita, sin coste — solo rate limit 200/h)
const PEXELS_KEY_DEFAULT = 'DQlg4GAqeCIIF3CkZpcFQBopg7PztGO8uKcVXHi8XnYCyWDSEo1QvyqC';

function guardarKeyPexels(val){
  localStorage.setItem('pexels_key', val);
}

function getPexelsKey(){
  const saved = localStorage.getItem('pexels_key');
  const input = document.getElementById('pexelsKey');
  const key = saved || PEXELS_KEY_DEFAULT;
  if(input) input.value = key;
  return key;
}

function esLocalhost(){
  return location.protocol === 'http:' || location.protocol === 'https:';
}

function actualizarTagsPexels(angulo){
  const tags = PEXELS_SUGERIDAS[angulo] || PEXELS_SUGERIDAS.default;
  const el = document.getElementById('pexelsTags');
  if(!el) return;
  el.innerHTML = tags.map(t=>
    `<span class="mj-tag" style="cursor:pointer" onclick="buscarPexelsTermino('${t}')">${t}</span>`
  ).join('');
  // Mostrar aviso si aún está en file://
  const st = document.getElementById('pexelsStatus');
  if(st){
    if(!esLocalhost()){
      st.style.color = '#ff9f43';
      st.textContent = '⚠ Doble clic en iniciar.py para activar búsqueda';
    } else {
      st.style.color = '#38B6FF';
      st.textContent = '✓ Conectado — busca cualquier foto';
    }
  }
}

async function buscarPexels(){
  const q = document.getElementById('pexelsQ')?.value?.trim();
  if(!q){ toast2('Escribe algo para buscar'); return; }
  const keyInput = document.getElementById('pexelsKey');
  if(keyInput?.value) guardarKeyPexels(keyInput.value);
  buscarPexelsTermino(q);
}

let _pexQ='', _pexPage=1;
function verMasFotos(){ buscarPexelsTermino(_pexQ, _pexPage+1); }

// Abrir el modal de resultados mostrando SOLO el panel indicado
function soloResultado(id, titulo){
  ['pexelsResults','vidResults','musResults'].forEach(x=>{
    const el=document.getElementById(x); if(el) el.style.display=(x===id)?'block':'none';
  });
  const modal=document.getElementById('resModal');
  if(modal){
    modal.classList.add('on');
    const t=document.getElementById('resModalTitle'); if(t&&titulo) t.textContent=titulo;
    const body=modal.querySelector('.resm-body');
    if(body && !body._scrollWired){
      body._scrollWired=true;
      body.addEventListener('scroll',()=>{
        if(body.scrollTop+body.clientHeight >= body.scrollHeight-120){
          // scroll infinito: cargar la siguiente página del panel activo
          const b=document.querySelector('#resModal button[id$="MasBtn"]');
          if(b && !b._cargando){ b._cargando=true; b.click(); }
        }
      });
    }
  }
}
function cerrarModalRes(){
  const m=document.getElementById('resModal'); if(m) m.classList.remove('on');
  if(_musAudio){ _musAudio.pause(); _musAudio=null; }
}
document.addEventListener('keydown',e=>{ if(e.key==='Escape') cerrarModalRes(); });

// Botón "Ver más" reutilizable (id único por grid)
function botonVerMas(fn, id){
  return `<button id="${id}" onclick="${fn}()" style="grid-column:1/-1;padding:7px;margin-top:4px;font-size:9px;font-weight:600;background:var(--UI-B);border:1px solid var(--UI-A);color:var(--UI-A);border-radius:4px;cursor:pointer">Ver más ↓</button>`;
}

async function buscarPexelsTermino(q, page){
  page = page || 1;
  _pexQ = q; _pexPage = page;
  const qInput = document.getElementById('pexelsQ');
  if(qInput) qInput.value = q;

  // Abrir biblioteca si está cerrada
  const lib = document.getElementById('mediaLib');
  if(lib.classList.contains('hidden')) toggleMedia();

  const keyInput = document.getElementById('pexelsKey');
  const key = (keyInput?.value?.trim()) || localStorage.getItem('pexels_key') || PEXELS_KEY_DEFAULT;

  const resultsBox = document.getElementById('pexelsResults');
  const grid = document.getElementById('pexelsGrid');
  soloResultado('pexelsResults', '📷 Fotos: '+q);
  if(page===1) grid.innerHTML = '<div class="mlib-empty">🔍 Buscando...</div>';

  try{
    const PER=24;
    const res = await fetch(
      `https://api.pexels.com/v1/search?query=${encodeURIComponent(q)}&per_page=${PER}&page=${page}&orientation=portrait`,
      { headers:{ 'Authorization': key } }
    );
    if(res.status === 401){
      grid.innerHTML = '<div class="mlib-empty" style="color:#ff6b6b">❌ API Key incorrecta</div>';
      return;
    }
    if(!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    if(!data.photos?.length){
      if(page===1) grid.innerHTML = '<div class="mlib-empty">Sin resultados.<br>Prueba otro término.</div>';
      const b=document.getElementById('pexMasBtn'); if(b) b.remove();
      return;
    }
    const itemsHTML = data.photos.map(ph=>`
      <div class="mlib-item pexels-item" title="Clic para usar · 📷 ${ph.photographer}"
        onclick="importarFotoPexels('${(ph.src.large2x||ph.src.large).replace(/'/g,'%27')}','${ph.photographer.replace(/['"]/g,'')}')">
        <img src="${ph.src.medium}" loading="lazy" alt="${ph.alt||''}">
        <div class="mlib-use">✓ Usar</div>
      </div>`).join('');
    const btnOld=document.getElementById('pexMasBtn'); if(btnOld) btnOld.remove();
    if(page===1) grid.innerHTML = itemsHTML; else grid.insertAdjacentHTML('beforeend', itemsHTML);
    if(data.photos.length >= PER) grid.insertAdjacentHTML('beforeend', botonVerMas('verMasFotos','pexMasBtn'));
  }catch(e){
    // Falló el fetch — casi seguro CORS desde file://
    if(!esLocalhost()){
      grid.innerHTML = `<div class="mlib-empty" style="color:#ff9f43;line-height:1.8">
        ⚠️ Tu navegador bloquea Pexels<br>al abrir el archivo directo.<br><br>
        <b style="color:var(--UI-T)">Solución:</b> doble clic en<br>
        <b style="color:#38B6FF">iniciar.py</b> (carpeta POSTS)<br><br>
        <span style="font-size:8px;color:var(--UI-M)">Abre el generador en localhost<br>y Pexels funciona al instante</span>
      </div>`;
    } else {
      grid.innerHTML = `<div class="mlib-empty" style="color:#ff6b6b">Error: ${e.message}</div>`;
    }
  }
}

/* ─── Buscar vídeos de fondo para reels (Pexels + Pixabay) ─── */
let _vidQ='', _vidPage=1;
function verMasVideos(){ buscarVideosPexels(_vidPage+1); }

async function buscarVideosPexels(page){
  const status = document.getElementById('vidStatus');
  page = page || 1;
  const q = (page>1) ? _vidQ : (document.getElementById('vidQ')?.value?.trim());
  if(!q){ if(status){status.style.color='#ff9f43';status.textContent='Escribe qué vídeo buscar.';} return; }
  _vidQ = q; _vidPage = page;
  const key = (document.getElementById('pexelsKey')?.value?.trim()) || localStorage.getItem('pexels_key') || PEXELS_KEY_DEFAULT;

  const box = document.getElementById('vidResults');
  const grid = document.getElementById('vidGrid');
  soloResultado('vidResults', '🎬 Vídeos: '+q);
  if(page===1) grid.innerHTML='<div class="mlib-empty">🔍 Buscando vídeos...</div>';
  if(status){ status.style.color='var(--UI-M)'; status.textContent='Clic en un vídeo para descargarlo.'; }

  const tarjeta = (poster, link, dur, fuente) =>
    `<div class="mlib-item pexels-item" title="📹 ${dur||''}s · ${fuente} — clic para descargar"
      onclick="descargarVideoPexels('${(link||'').replace(/'/g,'%27')}','${q.replace(/[^a-z0-9]/gi,'_')}',${dur||0})">
      <img src="${poster}" loading="lazy" alt="">
      <div class="mlib-use">⬇ ${fuente} ${dur||''}s</div>
    </div>`;

  try{
    const PER=16;
    const res = await fetch(`https://api.pexels.com/videos/search?query=${encodeURIComponent(q)}&per_page=${PER}&page=${page}&orientation=portrait`,
      { headers:{ Authorization:key } });
    if(res.status===401){ grid.innerHTML='<div class="mlib-empty" style="color:#ff6b6b">❌ API Key incorrecta</div>'; return; }
    if(!res.ok) throw new Error('HTTP '+res.status);
    const data = await res.json();
    let html = (data.videos||[]).map(v=>{
      const f = (v.video_files||[]).filter(x=>x.height>=x.width).sort((a,b)=>b.height-a.height)
                  .find(x=>x.height<=1920) || (v.video_files||[])[0] || {};
      return tarjeta(v.image, f.link, v.duration, 'Pexels');
    }).join('');

    // Segunda fuente: Pixabay (si hay key) — más variedad
    const pk = getPixabayKey();
    if(pk){
      try{
        const rp = await fetch(`https://pixabay.com/api/videos/?key=${pk}&q=${encodeURIComponent(q)}&per_page=${PER}&page=${page}`);
        if(rp.ok){
          const dp = await rp.json();
          html += (dp.hits||[]).map(h=>{
            const vs = h.videos||{};
            const cand = [vs.large,vs.medium,vs.small,vs.tiny].filter(Boolean);
            const vert = cand.find(x=>x.height>=x.width) || cand[0] || {};
            const poster = vert.thumbnail || (vs.tiny&&vs.tiny.thumbnail) || '';
            return tarjeta(poster, vert.url, h.duration, 'Pixabay');
          }).join('');
        }
      }catch(_){/* Pixabay opcional */}
    }

    const btnOld=document.getElementById('vidMasBtn'); if(btnOld) btnOld.remove();
    if(!html){ if(page===1) grid.innerHTML='<div class="mlib-empty">Sin vídeos.<br>Prueba otro término.</div>'; return; }
    if(page===1) grid.innerHTML = html; else grid.insertAdjacentHTML('beforeend', html);
    if((data.videos?.length||0) >= PER) grid.insertAdjacentHTML('beforeend', botonVerMas('verMasVideos','vidMasBtn'));
  }catch(e){
    if(!esLocalhost()){ grid.innerHTML=`<div class="mlib-empty" style="color:#ff9f43;line-height:1.8">⚠️ Abre con <b style="color:#38B6FF">iniciar.py</b><br>para buscar vídeos.</div>`; }
    else { grid.innerHTML=`<div class="mlib-empty" style="color:#ff6b6b">Error: ${e.message}</div>`; }
  }
}

/* ─── Música libre de derechos (Jamendo, Creative Commons) ─── */
function getJamendoKey(){ return (localStorage.getItem('jamendo_key')|| (window.RM_CONFIG&&RM_CONFIG.jamendo_key) || '').trim(); }
function guardarKeyJamendo(v){
  localStorage.setItem('jamendo_key',(v||'').trim());
  const st=document.getElementById('musStatus');
  if(st){ if(getJamendoKey()){ st.style.color='#38B6FF'; st.textContent='✓ Client ID guardado. Busca música arriba.'; }
    else { st.style.color='var(--UI-M)'; st.textContent='Gratis en developer.jamendo.com (crea una app → Client ID).'; } }
}

let _musQ='', _musPage=0, _musAudio=null;
function verMasMusica(){ buscarMusica(_musPage+1); }

async function buscarMusica(page){
  page = page || 0;
  const status=document.getElementById('musStatus');
  const q=(page>0)?_musQ:(document.getElementById('musQ')?.value?.trim());
  if(!q){ if(status){status.style.color='#ff9f43';status.textContent='Escribe qué música buscar.';} return; }
  const key=getJamendoKey();
  if(!key){ if(status){status.style.color='#ff9f43';status.textContent='Pega tu Client ID de Jamendo (gratis en developer.jamendo.com).';} return; }
  _musQ=q; _musPage=page;

  const box=document.getElementById('musResults'), grid=document.getElementById('musGrid');
  soloResultado('musResults', '🎵 Música: '+q);
  if(page===0) grid.innerHTML='<div class="mlib-empty">🔍 Buscando música...</div>';

  try{
    const PER=20, offset=page*PER;
    const url=`https://api.jamendo.com/v3.0/tracks/?client_id=${key}&format=json&limit=${PER}&offset=${offset}`
            + `&search=${encodeURIComponent(q)}&audioformat=mp32&order=popularity_total&include=musicinfo`;
    const r=await fetch(url);
    const d=await r.json();
    if(d.headers?.status!=='success'){ grid.innerHTML=`<div class="mlib-empty" style="color:#ff6b6b">❌ Client ID inválido o sin acceso.</div>`; return; }
    const tracks=d.results||[];
    if(!tracks.length){ if(page===0) grid.innerHTML='<div class="mlib-empty">Sin música.<br>Prueba otro término.</div>'; return; }
    const fmt=s=>{s=Math.round(s||0);return Math.floor(s/60)+':'+String(s%60).padStart(2,'0');};
    const filas=tracks.map(t=>{
      const dl=(t.audiodownload_allowed?t.audiodownload:t.audio)||t.audio;
      const nombre=(t.name||'').replace(/'/g,'’'), artista=(t.artist_name||'').replace(/'/g,'’');
      return `<div style="display:flex;align-items:center;gap:8px;background:#0A0A0A;border:1px solid var(--UI-B);border-radius:5px;padding:6px 8px">
        <button onclick="reproMusica('${(t.audio||'').replace(/'/g,'%27')}',this)" title="Escuchar" style="flex-shrink:0;width:26px;height:26px;border-radius:50%;border:none;background:var(--UI-A);color:#fff;cursor:pointer;font-size:11px">▶</button>
        <div style="flex:1;min-width:0">
          <div style="font-size:10px;color:var(--UI-T);font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">${nombre}</div>
          <div style="font-size:8px;color:var(--UI-M);white-space:nowrap;overflow:hidden;text-overflow:ellipsis">${artista} · ${fmt(t.duration)}</div>
        </div>
        <button onclick="descargarMusica('${(dl||'').replace(/'/g,'%27')}','${nombre.replace(/[^a-z0-9]/gi,'_').slice(0,30)}')" title="Descargar" style="flex-shrink:0;width:26px;height:26px;border-radius:5px;border:1px solid var(--UI-B2);background:var(--UI-B);color:var(--UI-A);cursor:pointer;font-size:12px">⬇</button>
      </div>`;
    }).join('');
    const btnOld=document.getElementById('musMasBtn'); if(btnOld) btnOld.remove();
    if(page===0) grid.innerHTML=filas; else grid.insertAdjacentHTML('beforeend',filas);
    if(tracks.length>=PER) grid.insertAdjacentHTML('beforeend',
      `<button id="musMasBtn" onclick="verMasMusica()" style="padding:7px;font-size:9px;font-weight:600;background:var(--UI-B);border:1px solid var(--UI-A);color:var(--UI-A);border-radius:4px;cursor:pointer">Ver más ↓</button>`);
    if(status){ status.style.color='#38B6FF'; status.textContent='▶ escucha · ⬇ descarga (a Descargas → reel-video/videos_entrada/).'; }
  }catch(e){
    grid.innerHTML=`<div class="mlib-empty" style="color:#ff6b6b">Error: ${e.message}</div>`;
  }
}

// Reproducir/parar preview
function reproMusica(url, btn){
  if(_musAudio){ _musAudio.pause(); document.querySelectorAll('#musGrid button').forEach(b=>{ if(b.textContent==='⏸') b.textContent='▶'; }); }
  if(btn && btn.textContent==='⏸'){ btn.textContent='▶'; _musAudio=null; return; }
  _musAudio=new Audio(url); _musAudio.play().catch(()=>{});
  if(btn){ btn.textContent='⏸'; _musAudio.onended=()=>{ btn.textContent='▶'; }; }
}

// Descargar mp3
async function descargarMusica(url, nombre){
  if(!url) return;
  const status=document.getElementById('musStatus');
  if(status){ status.style.color='#38B6FF'; status.textContent='Descargando música...'; }
  try{
    const res=await fetch(url); const blob=await res.blob();
    const a=document.createElement('a'); a.href=URL.createObjectURL(blob);
    a.download=`musica_${nombre||'jamendo'}.mp3`; a.click();
    setTimeout(()=>URL.revokeObjectURL(a.href),1500);
    if(status){ status.style.color='#38B6FF'; status.textContent='✓ Descargada. Muévela a reel-video/videos_entrada/ (o úsala en IG).'; }
  }catch(e){ window.open(url,'_blank'); if(status){ status.style.color='#ff9f43'; status.textContent='Se abrió en otra pestaña: guárdala con clic derecho.'; } }
}

// Descarga el mp4 al ordenador (va a Descargas; muévelo a reel-video/videos_entrada/)
async function descargarVideoPexels(url, slug, dur){
  if(!url) return;
  const status = document.getElementById('vidStatus');
  if(status){ status.style.color='#38B6FF'; status.textContent='Descargando vídeo...'; }
  try{
    const res = await fetch(url);
    const blob = await res.blob();
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = `pexels_${slug}_${dur}s.mp4`;
    a.click();
    setTimeout(()=>URL.revokeObjectURL(a.href),1500);
    if(status){ status.style.color='#38B6FF'; status.textContent='✓ Descargado. Muévelo a reel-video/videos_entrada/'; }
  }catch(e){
    // Fallback: abrir en pestaña para guardar manualmente
    window.open(url,'_blank');
    if(status){ status.style.color='#ff9f43'; status.textContent='Se abrió en otra pestaña: guárdalo con clic derecho.'; }
  }
}

/* ─── Generar imagen con IA (Pollinations.ai — gratis, sin API key) ─── */
async function generarImagenIA(){
  const prompt = document.getElementById('iaPrompt')?.value?.trim();
  const status = document.getElementById('iaStatus');
  const btn = document.getElementById('iaBtn');
  if(!prompt){ if(status){status.style.color='#ff9f43';status.textContent='Escribe qué imagen quieres.';} return; }

  const [w,h] = (document.getElementById('iaFormato')?.value || '1080x1350').split('x').map(Number);
  const conEstilo = document.getElementById('iaEstilo')?.checked;
  // Estilo fotográfico coherente con la marca (opcional)
  const estilo = conEstilo
    ? ', professional interior photography, modern home renovation, natural light, elegant, high quality, photorealistic, cinematic'
    : '';
  const full = prompt + estilo;
  const seed = Math.floor(Math.random()*1e6);   // semilla → cada generación distinta
  const url = `https://image.pollinations.ai/prompt/${encodeURIComponent(full)}`
            + `?width=${w}&height=${h}&seed=${seed}&nologo=true&model=flux`;

  if(btn){ btn.disabled=true; btn.textContent='⏳'; }
  if(status){ status.style.color='#38B6FF'; status.textContent='Generando con IA… (10-25s)'; }

  // Intenta descargar la imagen a dataURL (con 1 reintento; Pollinations a veces 403 y luego responde)
  async function intentar(){
    const res = await fetch(url);
    if(!res.ok) throw Object.assign(new Error('HTTP '+res.status), {status:res.status});
    const blob = await res.blob();
    if(blob.size < 800) throw new Error('respuesta vacía');
    return await new Promise((r,rej)=>{ const rd=new FileReader(); rd.onload=e=>r(e.target.result); rd.onerror=rej; rd.readAsDataURL(blob); });
  }

  let ultimoErr;
  for(let intento=1; intento<=2; intento++){
    try{
      const dataUrl = await intentar();
      const id = ++mediaIdCounter;
      MEDIA.push({id, url:dataUrl, name:`IA · ${prompt.slice(0,24)}`});
      renderMediaGrid();
      if(status){ status.style.color='#38B6FF'; status.textContent='✓ Imagen creada — clic en ella para usarla'; }
      if(asignandoTarget) asignarImagen(id, asignandoTarget);
      if(btn){ btn.disabled=false; btn.textContent='✨'; }
      return;
    }catch(e){ ultimoErr=e; if(intento===1) await delay(2500); }
  }

  // Falló las 2 veces
  if(status){
    status.style.color='#ff9f43';
    if(ultimoErr?.status===403){
      status.textContent='⚠ El servicio de IA rechazó la petición (403). Reintenta en 1 min; si sigue, tu red puede estar bloqueada.';
    }else if(!esLocalhost()){
      status.textContent='⚠ Abre con iniciar.py (localhost) para crear imágenes IA.';
    }else{
      status.textContent='No se pudo generar: '+(ultimoErr?.message||'error');
    }
  }
  if(btn){ btn.disabled=false; btn.textContent='✨'; }
}

async function importarFotoPexels(url, autor){
  toast2('Descargando foto...');
  try{
    const res = await fetch(url);
    const blob = await res.blob();
    const reader = new FileReader();
    reader.onload = e=>{
      const id = ++mediaIdCounter;
      MEDIA.push({id, url: e.target.result, name:`Pexels · ${autor}`});
      renderMediaGrid();
      toast2(`✓ Foto de ${autor} añadida a tu biblioteca`);
      // Asignar automáticamente si hay target activo
      if(asignandoTarget) asignarImagen(id, asignandoTarget);
    };
    reader.readAsDataURL(blob);
  }catch(e){
    toast2('Error al descargar la foto');
  }
}

function copiar(txt){
  navigator.clipboard.writeText(txt.trim()).then(toast).catch(()=>{
    const ta=document.createElement('textarea');
    ta.value=txt.trim();document.body.appendChild(ta);ta.select();
    document.execCommand('copy');document.body.removeChild(ta);toast();
  });
}

function copiarTodo(angulo, hookEnc){
  const copyData = BANCO.instagramCopy[angulo] || BANCO.instagramCopy.default;
  const full = decodeURIComponent(hookEnc) + '\n\n' + copyData.caption + '\n\n' + copyData.hashtags;
  copiar(full);
}

function toast(){
  const t=document.getElementById('toast');
  t.classList.add('on');
  setTimeout(()=>t.classList.remove('on'),1800);
}

/* ═══════════════════════════════════════════
   ESCALA STAGE
   ═══════════════════════════════════════════ */
function scaleStage(){
  const stage=document.getElementById('stage');
  const inner=document.getElementById('stageInner');
  if(!stage||!inner) return;
  const w=stage.offsetWidth;
  const scale=w/1080;
  const H=stageH();
  inner.style.transform=`scale(${scale})`;
  inner.style.width='1080px';
  inner.style.height=H+'px';
  stage.style.height=(H*scale)+'px';
}

/* ═══════════════════════════════════════════
   MODO POST / CARRUSEL  (ambos 1080×1350)
   Post = 1 slide  ·  Carrusel = varios slides
   ═══════════════════════════════════════════ */
function setModo(m){
  modo = m;
  const uno = (m==='post' || m==='reel'); // formatos de 1 sola pieza
  document.getElementById('mPost').classList.toggle('on', m==='post');
  document.getElementById('mCarr').classList.toggle('on', m==='carrusel');
  const mr=document.getElementById('mReel'); if(mr) mr.classList.toggle('on', m==='reel');
  // Formatos de 1 pieza: ocultar miniaturas, navegación y selector de slides
  document.getElementById('sideL').style.display = uno ? 'none' : '';
  document.getElementById('navRow').style.display = uno ? 'none' : 'flex';
  const sp=document.getElementById('slidesPicker'); if(sp) sp.style.display = uno ? 'none' : 'flex';
  const gb=document.getElementById('btnGuionReel'); if(gb) gb.style.display = m==='reel' ? '' : 'none';
  // Si pasamos a 1 pieza y hay varios slides, quedarnos solo con el actual
  if(uno && SLIDES.length>1){
    const actual = SLIDES[cur];
    SLIDES.length = 0;
    SLIDES.push(actual);
    cur = 0;
  }
  buildThumbs();
  show(cur);
  scaleStage();
}

// Descargar el guión del reel como .txt
function descargarGuionReel(){
  if(!ULTIMO_GUION){ toast2('Genera un reel primero'); return; }
  const blob=new Blob([ULTIMO_GUION],{type:'text/plain;charset=utf-8'});
  const a=document.createElement('a');
  a.href=URL.createObjectURL(blob);
  a.download='guion_reel_rm.txt';
  a.click();
  setTimeout(()=>URL.revokeObjectURL(a.href),1000);
  toast2('✓ Guión descargado');
}

// Cambiar nº de slides del carrusel actual al vuelo
function cambiarNumSlides(n){
  n = parseInt(n);
  // Sincronizar con el selector del tab Generar
  const gen=document.getElementById('cNumSlides'); if(gen) gen.value = (n>=5&&n<=7)?n:7;
  if(modo==='post' || !SLIDES.length) return;

  const actual = SLIDES.length;
  if(n === actual) return;

  if(n < actual){
    // Recortar: mantener hook (primero) y CTA (último), quitar intermedios
    const primero = SLIDES[0];
    const ultimo  = SLIDES[actual-1];
    const medios  = SLIDES.slice(1, actual-1).slice(0, n-2);
    SLIDES.length = 0;
    SLIDES.push(primero, ...medios, ultimo);
  } else {
    // Añadir slides nuevos antes del último (CTA)
    const ultimo = SLIDES.pop();
    const tiposExtra = ['frase','lista','stats','servicio','debate','proceso'];
    const fondos = ['dark','light','blue'];
    while(SLIDES.length < n-1){
      const t = rnd(tiposExtra);
      SLIDES.push({
        tipo: t, fondo: rnd(fondos),
        eye: rnd(BANCO.eyebrows),
        head: t==='frase' ? rnd(BANCO.frases) : 'Edita este slide',
        body: '', items: t==='lista'||t==='servicio' ? rnd(BANCO.listas.default) : (t==='stats'?rnd(BANCO.stats):[]),
        cta: rnd(BANCO.ctas)+' →'
      });
    }
    SLIDES.push(ultimo);
  }
  cur = Math.min(cur, SLIDES.length-1);
  buildThumbs();
  show(cur);
  toast2(`Carrusel ajustado a ${n} slides`);
}

/* ═══════════════════════════════════════════
   MOSTRAR SLIDE
   ═══════════════════════════════════════════ */
function show(i){
  if(!SLIDES.length) return;
  cur=Math.max(0,Math.min(i,SLIDES.length-1));
  document.getElementById('stageInner').innerHTML=render(SLIDES[cur],cur);
  scaleStage();
  const total=SLIDES.length;
  document.getElementById('navCnt').textContent=`${cur+1} / ${total}`;
  document.getElementById('bPrev').disabled=cur===0;
  document.getElementById('bNext').disabled=cur===total-1;
  document.querySelectorAll('.thumb').forEach((el,j)=>el.classList.toggle('active',j===cur));
  const d=SLIDES[cur];
  document.getElementById('cTipo').value=d.tipo;
  document.getElementById('cFondo').value=d.fondo;
  document.getElementById('cEye').value=d.eye||'';
  document.getElementById('cHead').value=d.head||'';
  document.getElementById('cBody').value=d.body||'';
  document.getElementById('cCta').value=d.cta||'';
  renderItemsList();
  sincronizarPanelImg(d);
  sincronizarTextoSlide(d);
}
function nav(dir){show(cur+dir)}

function moverSlide(dir){
  if(!SLIDES.length) return;
  const nueva = cur + dir;
  if(nueva < 0 || nueva >= SLIDES.length) return;
  // Intercambiar posiciones
  [SLIDES[cur], SLIDES[nueva]] = [SLIDES[nueva], SLIDES[cur]];
  cur = nueva;
  buildThumbs();
  show(cur);
}

function ed(f,v){
  if(!SLIDES.length) return;
  const d=SLIDES[cur];
  if(f==='tipo')    d.tipo=v;
  if(f==='fondo')   d.fondo=v;
  if(f==='eye')     d.eye=v;
  if(f==='head')    d.head=v;
  if(f==='body')    d.body=v;
  if(f==='cta')     d.cta=v;
  if(f==='overlay')   { d.overlay=v; sincronizarPanelImg(d); }
  if(f==='imgX')      d.imgX=parseInt(v);
  if(f==='imgY')      d.imgY=parseInt(v);
  if(f==='imgZoom')   d.imgZoom=parseInt(v);
  if(f==='ovOpacity') d.ovOpacity=parseInt(v);
  if(f==='txtPos')    d.txtPos=v;
  if(f==='imgLayout') d.imgLayout=v;
  if(f==='txtScale')  d.txtScale=parseInt(v);
  if(f==='txtDX')     d.txtDX=parseInt(v);
  if(f==='txtDY')     d.txtDY=parseInt(v);
  if(f==='imgX2')     d.imgX2=parseInt(v);
  if(f==='imgY2')     d.imgY2=parseInt(v);
  if(f==='imgZoom2')  d.imgZoom2=parseInt(v);
  show(cur);
  refreshThumb(cur);
}

/* ═══════════════════════════════════════════
   ITEMS DINÁMICOS
   ═══════════════════════════════════════════ */
function addItem(txt=''){
  if(!SLIDES.length) return;
  const d=SLIDES[cur];
  if(!d.items) d.items=[];
  if(d.items.length>=6) return;
  d.items.push(txt);
  renderItemsList();
  show(cur);
  refreshThumb(cur);
  // foco en el nuevo campo
  const rows=document.querySelectorAll('.item-row textarea');
  if(rows.length) rows[rows.length-1].focus();
}

function removeItem(i){
  if(!SLIDES.length) return;
  const d=SLIDES[cur];
  d.items.splice(i,1);
  renderItemsList();
  show(cur);
  refreshThumb(cur);
}

function editItemTxt(i,v){
  if(!SLIDES.length) return;
  SLIDES[cur].items[i]=v;
  show(cur);
  refreshThumb(cur);
}

function renderItemsList(){
  const d=SLIDES[cur];
  const items=d?d.items||[]:[];
  const list=document.getElementById('itemsList');
  const count=document.getElementById('itemsCount');
  if(!list) return;
  count.textContent=`${items.length}/6`;
  list.innerHTML=items.map((it,i)=>`
    <div class="item-row">
      <span class="item-num">${i+1}</span>
      <textarea rows="2" oninput="editItemTxt(${i},this.value)">${it}</textarea>
      <button class="item-del" onclick="removeItem(${i})">✕</button>
    </div>`).join('');
}
function setV(k,v){document.documentElement.style.setProperty(k,v);show(cur);buildThumbs()}

/* ── Controles del modo dos fotos ── */
function setDuo(prop, val){
  if(!SLIDES.length) return;
  SLIDES[cur][prop] = val;
  if(prop==='duoDir'){
    document.getElementById('duoH')?.classList.toggle('on', val==='h');
    document.getElementById('duoV')?.classList.toggle('on', val==='v');
  }
  if(prop==='duoTxt'){
    document.getElementById('duoTxtB')?.classList.toggle('on', val==='bottom');
    document.getElementById('duoTxtT')?.classList.toggle('on', val==='top');
  }
  show(cur); refreshThumb(cur);
}

/* ── Controles de texto por slide ── */
function setTxtAlign(a){
  if(!SLIDES.length) return;
  SLIDES[cur].txtAlign=a;
  ['L','C','R'].forEach(k=>document.getElementById('al'+k)?.classList.remove('on'));
  document.getElementById('al'+(a==='left'?'L':a==='center'?'C':'R'))?.classList.add('on');
  show(cur); refreshThumb(cur);
}
function setTxtVPos(v){
  if(!SLIDES.length) return;
  SLIDES[cur].txtVPos=v;
  ['T','C','B'].forEach(k=>document.getElementById('vp'+k)?.classList.remove('on'));
  document.getElementById('vp'+(v==='top'?'T':v==='bottom'?'B':'C'))?.classList.add('on');
  show(cur); refreshThumb(cur);
}
function resetTextoSlide(){
  if(!SLIDES.length) return;
  const d=SLIDES[cur];
  d.txtScale=100; d.txtAlign='left'; d.txtVPos='center'; d.txtDX=0; d.txtDY=0;
  sincronizarTextoSlide(d);
  show(cur); refreshThumb(cur);
}
function sincronizarTextoSlide(d){
  const sc=document.getElementById('rTxtScale'); if(sc){sc.value=d.txtScale??100; document.getElementById('vTxtScale').textContent=(d.txtScale??100)+'%'}
  const dx=document.getElementById('rTxtDX'); if(dx){dx.value=d.txtDX??0; document.getElementById('vTxtDX').textContent=(d.txtDX??0)+'px'}
  const dy=document.getElementById('rTxtDY'); if(dy){dy.value=d.txtDY??0; document.getElementById('vTxtDY').textContent=(d.txtDY??0)+'px'}
  const al=d.txtAlign||'left';
  ['L','C','R'].forEach(k=>document.getElementById('al'+k)?.classList.remove('on'));
  document.getElementById('al'+(al==='left'?'L':al==='center'?'C':'R'))?.classList.add('on');
  const vp=d.txtVPos||'center';
  ['T','C','B'].forEach(k=>document.getElementById('vp'+k)?.classList.remove('on'));
  document.getElementById('vp'+(vp==='top'?'T':vp==='bottom'?'B':'C'))?.classList.add('on');
}

/* ═══════════════════════════════════════════
   THUMBNAILS
   ═══════════════════════════════════════════ */
const TIPO_L={hook:'Hook',frase:'Frase',ba:'BA Texto',lista:'Lista',
  stats:'Stats',proceso:'Proceso',servicio:'Servicio',debate:'Debate',
  cta:'CTA',post:'Post',foto:'Foto BG',bafoto:'BA Foto',
  fototxt:'Foto+Txt',autoridad:'Autoridad'};

function buildThumbs(){
  const panel=document.getElementById('sideL');
  const lbl=panel.querySelector('.sl-lbl');
  panel.innerHTML='';panel.appendChild(lbl);
  if(modo==='post'){return}
  SLIDES.forEach((d,i)=>{
    const wrap=document.createElement('div');
    wrap.className='thumb'+(i===cur?' active':'');
    wrap.onclick=()=>show(i);
    const inner=document.createElement('div');
    inner.className='thumb-inner';
    const host=document.createElement('div');
    host.className='thumb-host';
    host.innerHTML=render(d,i);
    inner.appendChild(host);
    requestAnimationFrame(()=>{
      const w=inner.offsetWidth||128;
      const s=w/1080;
      host.style.transform=`scale(${s})`;
      inner.style.height=(stageH()*s)+'px';
    });
    const numEl=document.createElement('div');
    numEl.className='thumb-num';
    numEl.textContent=String(i+1).padStart(2,'0');
    const chipEl=document.createElement('div');
    chipEl.className='thumb-chip';
    chipEl.textContent=TIPO_L[d.tipo]||d.tipo;
    wrap.appendChild(inner);wrap.appendChild(numEl);wrap.appendChild(chipEl);
    panel.appendChild(wrap);
  });
}
function refreshThumb(i){
  const ts=document.querySelectorAll('.thumb');
  if(!ts[i]) return;
  const host=ts[i].querySelector('.thumb-host');
  if(!host) return;
  const inner=ts[i].querySelector('.thumb-inner');
  host.innerHTML=render(SLIDES[i],i);
  const w=inner.offsetWidth||128;
  host.style.transform=`scale(${w/1080})`;
}

/* ═══════════════════════════════════════════
   BIBLIOTECA TOGGLE
   ═══════════════════════════════════════════ */
function toggleMedia(){
  const lib = document.getElementById('mediaLib');
  const btn = document.getElementById('btnMedia');
  const hidden = lib.classList.toggle('hidden');
  btn.classList.toggle('on', !hidden);
}

/* ═══════════════════════════════════════════
   GUÍAS
   ═══════════════════════════════════════════ */
function toggleExpMenu(){
  document.getElementById('expMenu').classList.toggle('on');
}
// Cerrar dropdown al clicar fuera
document.addEventListener('click', e=>{
  const wrap = document.getElementById('expWrap');
  if(wrap && !wrap.contains(e.target)){
    document.getElementById('expMenu').classList.remove('on');
  }
});

function toggleGuias(){
  guias=!guias;
  document.getElementById('safeRing').classList.toggle('on',guias);
  ['btnG','btnG2'].forEach(id=>{
    const el=document.getElementById(id);
    if(el){el.classList.toggle('on',guias);el.textContent=guias?'Guías ✓':'Guías'}
  });
  document.getElementById('btnG2').textContent=guias?'On':'Off';
}

/* ═══════════════════════════════════════════
   EXPORTAR
   ═══════════════════════════════════════════ */
async function capture(i){
  const d=SLIDES[i];
  const H=stageH(); // 1350 (4:5) o 1920 (reel 9:16)
  const root=getComputedStyle(document.documentElement);
  const vars=['--C-DARK','--C-LIGHT','--C-BLUE']
    .map(k=>`${k}:${root.getPropertyValue(k).trim()}`).join(';');
  const wrap=document.createElement('div');
  wrap.style.cssText=`position:fixed;top:-9999px;left:-9999px;width:1080px;height:${H}px;overflow:hidden;`;
  wrap.innerHTML=render(d,i);
  const st=document.createElement('style');
  st.textContent=`
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;1,300&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');
    :root{${vars};--C-BLUE2:#1A9AE8;--F-SER:'Playfair Display',Georgia,serif;--F-SAN:'Montserrat',system-ui,sans-serif}`;
  wrap.appendChild(st);
  document.body.appendChild(wrap);
  // Esperar a que las fuentes carguen antes de capturar
  try{ await document.fonts.ready; }catch(e){}
  try{
    const cv=await html2canvas(wrap,{width:1080,height:H,scale:1,
      useCORS:true,allowTaint:true,backgroundColor:null,logging:false});
    document.body.removeChild(wrap);return cv;
  }catch(e){document.body.removeChild(wrap);throw e}
}

async function expActual(){
  if(!SLIDES.length) return;
  const ov=document.getElementById('expOv');
  const msg=document.getElementById('expMsg');
  const bar=document.getElementById('expBar');
  ov.classList.add('on');bar.style.width='0%';
  msg.textContent=`Exportando ${modo==='post'?'post':'slide '+(cur+1)}...`;
  try{
    const cv=await capture(cur);bar.style.width='100%';
    await delay(250);
    const a=document.createElement('a');
    a.download=`rm-${modo}-${String(cur+1).padStart(2,'0')}.png`;
    a.href=cv.toDataURL('image/png');a.click();
  }catch(e){alert('Error al exportar.');}
  ov.classList.remove('on');
}

async function expTodos(){
  if(!SLIDES.length) return;
  const ov=document.getElementById('expOv');
  const msg=document.getElementById('expMsg');
  const bar=document.getElementById('expBar');
  ov.classList.add('on');

  // Usar JSZip si está disponible
  if(typeof JSZip !== 'undefined'){
    const zip = new JSZip();
    for(let i=0;i<SLIDES.length;i++){
      bar.style.width=Math.round(i/SLIDES.length*100)+'%';
      msg.textContent=`Generando ${i+1} de ${SLIDES.length}...`;
      try{
        const cv=await capture(i);
        const blob=await new Promise(r=>cv.toBlob(r,'image/png'));
        zip.file(`rm_slide_${String(i+1).padStart(2,'0')}_1080x1350.png`,blob);
        await delay(80);
      }catch(e){console.error(e)}
    }
    bar.style.width='100%';
    msg.textContent='Empaquetando ZIP...';
    const content=await zip.generateAsync({type:'blob'});
    const a=document.createElement('a');
    a.href=URL.createObjectURL(content);
    a.download=`rm_carrusel_${SLIDES.length}_slides.zip`;
    a.click();
    setTimeout(()=>URL.revokeObjectURL(a.href),1000);
    msg.textContent=`✓ ${SLIDES.length} slides en ZIP`;
  } else {
    // Fallback: descargar uno a uno
    for(let i=0;i<SLIDES.length;i++){
      bar.style.width=Math.round(i/SLIDES.length*100)+'%';
      msg.textContent=`Exportando ${i+1} de ${SLIDES.length}...`;
      try{
        const cv=await capture(i);
        const a=document.createElement('a');
        a.download=`rm-carrusel-${String(i+1).padStart(2,'0')}.png`;
        a.href=cv.toDataURL('image/png');a.click();
        await delay(700);
      }catch(e){console.error(e)}
    }
    bar.style.width='100%';
    msg.textContent=`✓ ${SLIDES.length} archivos exportados`;
  }
  await delay(1200);
  ov.classList.remove('on');
}

/* ═══════════════════════════════════════════
   FÁBRICA — GENERAR MES COMPLETO (batch ZIP)
   Recorre ideas NO usadas del banco de 365, genera cada pieza
   con el motor de feed P1-P9 y lo empaqueta todo en un ZIP:
   dia_XX_carrusel_Pn/ (imágenes + copy.txt) + calendario_mes.csv
   ═══════════════════════════════════════════ */
async function generarMes(dias){
  if(typeof JSZip==='undefined'){ alert('JSZip no disponible. Revisa tu conexión.'); return; }
  if(!dias){
    const v=prompt(
      '¿Cuántos días de contenido genero?\n(7 = semana · 15 = quincena · 30 = mes)\n\n'+
      'Cada día usa una idea NUEVA del banco de 365 y avanza la posición del feed automáticamente.\n'+
      'Los días de Reel generan la PORTADA + guion en copy.txt.','30');
    if(v===null) return;
    dias=parseInt(v)||0;
  }
  dias=Math.max(1,Math.min(dias,31));

  const usadas=getUsadas();
  let pendientes=BANCO_IDEAS.filter(i=>!usadas[i.dia]);
  if(!pendientes.length) pendientes=BANCO_IDEAS.slice();
  if(!pendientes.length){ alert('No hay ideas en el banco.'); return; }

  const ov=document.getElementById('expOv'), msg=document.getElementById('expMsg'), bar=document.getElementById('expBar');
  ov.classList.add('on'); bar.style.width='0%';

  // Guardar lo que hay en pantalla para restaurarlo al final
  const bakSlides=SLIDES.slice(), bakCur=cur;

  const zip=new JSZip();
  const numSlides=parseInt(document.getElementById('cNumSlidesTop')?.value||document.getElementById('cNumSlides')?.value)||7;
  const cal=[['Dia idea','Formato','Pilar','Posicion feed','Hook','CTA','Busqueda visual','Carpeta']];
  let totalImgs=0;
  const usarIA = !!getGroqKey();   // si hay key de Groq, cada día lleva copy único

  try{
    for(let d=0; d<dias; d++){
      const idea=pendientes[d % pendientes.length];
      const angulo=anguloDesdeIdea(idea);
      const esCarrusel=idea.formato==='Carrusel';
      const pos=getFeedPos();

      // Copy con IA (Groq) si hay key; si falla/limita, se usa el banco de la idea
      let aiDia=null;
      if(usarIA){
        msg.textContent=`Día ${d+1}/${dias} — escribiendo copy con IA...`;
        try{ aiDia=await fetchAI(angulo); }
        catch(e){ aiDia=null; /* 429/red → banco para este día */ }
      }

      // Construir contenido (sembrado con IA o con la idea del banco)
      const slides=esCarrusel?buildCarrusel(angulo,aiDia,numSlides):buildPost(angulo,aiDia);
      if(slides[0]){ slides[0].head=(aiDia&&aiDia.hook)||idea.hook; slides[0].eye=idea.objetivo||idea.pilar; }
      const ult=slides[slides.length-1];
      if(ult){
        ult.cta = (aiDia&&aiDia.cta_word) ? `Escríbeme ${aiDia.cta_word}`
                : (idea.cta && idea.cta.length>40 ? 'Escríbeme REFORMAS' : (idea.cta||ult.cta));
      }
      SLIDES.length=0; slides.forEach(s=>SLIDES.push(s));
      if(esCarrusel) avanzarFeedPos();

      const tipoCarpeta=idea.formato==='Reel'?'reel_portada':esCarrusel?'carrusel':'post';
      const carpeta=`dia_${String(d+1).padStart(2,'0')}_${tipoCarpeta}${esCarrusel?'_P'+pos:''}`;

      for(let i=0;i<SLIDES.length;i++){
        msg.textContent=`Día ${d+1}/${dias} — slide ${i+1}/${SLIDES.length}...`;
        bar.style.width=Math.round((d+i/SLIDES.length)/dias*95)+'%';
        const cv=await capture(i);
        const blob=await new Promise(r=>cv.toBlob(r,'image/jpeg',.92));
        zip.file(`${carpeta}/rm_${String(i+1).padStart(2,'0')}_1080x1350.jpg`,blob);
        totalImgs++;
        await delay(30);
      }
      zip.file(`${carpeta}/copy.txt`, copyDeIdea(idea, aiDia));
      const kw=((PEXELS_SUGERIDAS[angulo]||PEXELS_SUGERIDAS.default||[])[0])||'';
      const hookFinal = (aiDia&&aiDia.hook)||idea.hook;
      const ctaFinal  = (aiDia&&aiDia.cta_word) ? `Escríbeme ${aiDia.cta_word}`
                      : ((idea.cta&&idea.cta.length<=40)?idea.cta:'Escríbeme REFORMAS');
      // Para días de Reel: datos estructurados que consume reel-video/reel_video.py --mes
      if(idea.formato==='Reel'){
        zip.file(`${carpeta}/reel.json`, JSON.stringify({
          dia: idea.dia, hook: hookFinal,
          sub: (aiDia&&aiDia.hook_sub) || (idea.deseo ? `Para ${idea.deseo}` : ''),
          cta: ctaFinal, busqueda: kw, orden: d+1
        }, null, 2));
      }
      cal.push([idea.dia,idea.formato,idea.pilar,esCarrusel?'P'+pos:'—',hookFinal,ctaFinal,kw,carpeta]);
      marcarUsada(idea.dia);
    }

    msg.textContent='Empaquetando ZIP...'; bar.style.width='97%';
    const csv='﻿'+cal.map(r=>r.map(c=>`"${String(c==null?'':c).replace(/"/g,'""')}"`).join(';')).join('\r\n');
    zip.file('calendario_mes.csv',csv);
    zip.file('LEEME.txt',
`CONTENIDO GENERADO — ${MARCA}
${dias} días · ${totalImgs} imágenes (1080x1350)

- Cada carpeta dia_XX contiene las imágenes + copy.txt (texto listo para pegar).
- Los carruseles llevan _P1.._P9: su posición en el grid del feed (plantilla 9 tiles).
- Los días "reel_portada" son la PORTADA del reel: graba el vídeo siguiendo el guion del copy.txt.
  Llevan ademas un reel.json que el modulo reel-video puede usar para montar el video automatico:
      py reel_video.py --mes "ruta a esta carpeta"
- calendario_mes.csv: ábrelo en Excel para planificar (separador ;).

Publica con Meta Business Suite Planner (gratis) y programa todo el mes en una sentada.`);

    const content=await zip.generateAsync({type:'blob'});
    const a=document.createElement('a');
    a.href=URL.createObjectURL(content);
    a.download=`rm_contenido_${dias}dias.zip`;
    a.click();
    setTimeout(()=>URL.revokeObjectURL(a.href),1500);
    bar.style.width='100%';
    msg.textContent=`✓ ${dias} días · ${totalImgs} imágenes en ZIP`;
  }catch(e){
    console.error(e);
    msg.textContent='Error generando el mes: '+e.message;
  }

  // Restaurar el trabajo que había en pantalla
  SLIDES.length=0; bakSlides.forEach(s=>SLIDES.push(s));
  cur=Math.min(bakCur,Math.max(0,SLIDES.length-1));
  if(SLIDES.length){ buildThumbs(); show(cur); scaleStage(); }
  renderBanco(); actualizarFeedLabel();
  await delay(1800);
  ov.classList.remove('on');
}

// Texto listo para pegar en Instagram (+ guion si es Reel). Usa copy de IA si se pasa.
function copyDeIdea(idea, ai){
  const esReel=idea.formato==='Reel';
  const hook = (ai&&ai.hook)||idea.hook;
  const cuerpo = (ai&&ai.cta_body)||idea.idea;
  const cta = (ai&&ai.cta_word)?`Escríbeme ${ai.cta_word}`:idea.cta;
  const guion=esReel?`\n\n— GUION REEL —\nEstructura: ${idea.estructura}\nIdea visual: ${idea.visual}\nÁngulo: ${idea.angulo}`:'';
  return `${hook}\n\n${cuerpo}\n\n${cta}${guion}\n\n#reformas #empresadereformas #marketingparareformas #metaads #googleads`;
}

/* ═══════════════════════════════════════════
   BANCO DE 365 IDEAS
   ═══════════════════════════════════════════ */
const BANCO_IDEAS = window.IDEAS_365 || [];

function getUsadas(){
  try{ return JSON.parse(localStorage.getItem('ideas_usadas')||'{}'); }
  catch(e){ return {}; }
}
function setUsadas(obj){
  localStorage.setItem('ideas_usadas', JSON.stringify(obj));
}
function marcarUsada(dia){
  const u=getUsadas(); u[dia]={fecha:Date.now()}; setUsadas(u);
}
function desmarcarUsada(dia){
  const u=getUsadas(); delete u[dia]; setUsadas(u);
}

// Mapeo pilar del banco → pilar/ángulo del generador
const MAP_PILAR_ANGULO = {
  'dependencia del boca a boca':'bocaboca',
  'meses llenos y meses vacios':'estabilidad',
  'ingresos inestables':'estabilidad',
  'clientes que regatean':'regateo',
  'saturacion':'saturacion',
  'falta de tiempo':'tiempo',
  'competir por precio':'precio',
};

function anguloDesdeIdea(idea){
  const dolor=(idea.dolor||'').toLowerCase();
  for(const k in MAP_PILAR_ANGULO){ if(dolor.includes(k.split(' ')[0])) return MAP_PILAR_ANGULO[k]; }
  const pil=(idea.pilar||'').toLowerCase();
  if(pil.includes('dolor'))      return 'bocaboca';
  if(pil.includes('educativo'))  return 'sistema';
  if(pil.includes('autoridad'))  return 'autoridad';
  if(pil.includes('conversion')) return 'sistema';
  if(pil.includes('reframe'))    return 'objecion';
  if(pil.includes('servicio'))   return 'sistema';
  if(pil.includes('objecion'))   return 'objecion';
  return rnd(Object.keys(BANCO.angulos));
}

function renderBanco(){
  const list=document.getElementById('bancoList');
  if(!list || !BANCO_IDEAS.length){
    if(list) list.innerHTML='<div class="banco-empty">No se cargó el banco de ideas.<br>El banco va incrustado en el HTML; recarga la página.</div>';
    return;
  }
  const usadas=getUsadas();
  const q=(document.getElementById('bancoSearch')?.value||'').toLowerCase();
  const fFmt=document.getElementById('bancoFiltroFormato')?.value||'';
  const fPil=document.getElementById('bancoFiltroPilar')?.value||'';
  const ocultar=document.getElementById('bancoOcultarUsadas')?.checked;

  // Contador
  const totalUsadas=Object.keys(usadas).length;
  document.getElementById('bancoCount').textContent=`${totalUsadas}/365`;
  document.getElementById('bancoBar').style.width=(totalUsadas/365*100)+'%';

  let filtradas=BANCO_IDEAS.filter(it=>{
    if(fFmt && it.formato!==fFmt) return false;
    if(fPil && it.pilar!==fPil) return false;
    if(ocultar && usadas[it.dia]) return false;
    if(q){
      const txt=`${it.idea} ${it.hook} ${it.dolor} ${it.deseo} ${it.avatar} ${it.objetivo}`.toLowerCase();
      if(!txt.includes(q)) return false;
    }
    return true;
  });

  if(!filtradas.length){
    list.innerHTML='<div class="banco-empty">Sin ideas que coincidan.<br>'+(ocultar&&totalUsadas>0?'¡Has usado todas las de este filtro! 🎉':'Prueba otro filtro.')+'</div>';
    return;
  }

  // Limitar a 40 visibles para rendimiento
  const visibles=filtradas.slice(0,40);
  list.innerHTML=visibles.map(it=>{
    const usada=!!usadas[it.dia];
    return `<div class="idea-card ${usada?'usada':''}">
      <div class="idea-head">
        <span class="idea-dia">${String(it.dia).padStart(3,'0')}</span>
        <span class="idea-tag fmt">${it.formato}</span>
        <span class="idea-tag pil">${it.pilar}</span>
        ${usada?'<span class="idea-tag" style="background:rgba(56,182,255,.2);color:var(--UI-A)">✓ usada</span>':''}
      </div>
      <div class="idea-titulo">${it.idea}</div>
      <div class="idea-hook">"${it.hook}"</div>
      <div class="idea-actions">
        ${usada
          ? `<button class="idea-btn repost" onclick="repostIdea(${it.dia})">↻ Repost</button>`
          : `<button class="idea-btn primary" onclick="usarIdeaBanco(${it.dia})">⚡ Usar idea</button>`}
        <button class="idea-btn" onclick="verIdeaCompleta(${it.dia})">👁 Ver</button>
      </div>
    </div>`;
  }).join('') + (filtradas.length>40?`<div class="banco-empty">+${filtradas.length-40} ideas más. Usa el buscador para afinar.</div>`:'');
}

function usarIdeaBanco(dia){
  const idea=BANCO_IDEAS.find(i=>String(i.dia)===String(dia));
  if(!idea) return;
  const angulo=anguloDesdeIdea(idea);
  // Construir carrusel base
  const numSlides=parseInt(document.getElementById('cNumSlides')?.value)||7;
  const slides=buildCarrusel(angulo,null,numSlides);
  // Sobrescribir con contenido REAL de la idea
  if(slides[0]){
    slides[0].head=idea.hook;
    slides[0].eye=idea.objetivo||idea.pilar;
  }
  // Último slide = CTA real de la idea
  const ult=slides[slides.length-1];
  if(ult && idea.cta){
    ult.cta=idea.cta.length>40?'Escríbeme REFORMAS':idea.cta;
    ult.body=idea.cta;
  }
  SLIDES.length=0;
  slides.forEach(s=>SLIDES.push(s));
  cur=0;
  buildThumbs();
  show(0);
  scaleStage();
  actualizarCopy(angulo,null);
  // Marcar como usada
  marcarUsada(dia);
  renderBanco();
  toast2(`✓ Idea ${String(dia).padStart(3,'0')} cargada y marcada como usada`);
  // Saltar a Editar
  abrirTabEditar();
}

function repostIdea(dia){
  desmarcarUsada(dia);
  renderBanco();
  toast2(`↻ Idea ${String(dia).padStart(3,'0')} disponible de nuevo para repost`);
}

function verIdeaCompleta(dia){
  const it=BANCO_IDEAS.find(i=>String(i.dia)===String(dia));
  if(!it) return;
  alert(`DÍA ${it.dia} · ${it.formato} · ${it.pilar}\n`+
    `\n▸ AVATAR: ${it.avatar}`+
    `\n▸ DOLOR: ${it.dolor}`+
    `\n▸ DESEO: ${it.deseo}`+
    `\n\n▸ IDEA:\n${it.idea}`+
    `\n\n▸ HOOK:\n${it.hook}`+
    `\n\n▸ ÁNGULO:\n${it.angulo}`+
    `\n\n▸ ESTRUCTURA:\n${it.estructura}`+
    `\n\n▸ IDEA VISUAL:\n${it.visual}`+
    `\n\n▸ CTA:\n${it.cta}`+
    `\n\n▸ TEMPERATURA: ${it.temp}  ·  OBJETIVO: ${it.objetivo}`);
}

function usarSiguienteIdea(){
  const usadas=getUsadas();
  const fFmt=document.getElementById('bancoFiltroFormato')?.value||'';
  const fPil=document.getElementById('bancoFiltroPilar')?.value||'';
  const sig=BANCO_IDEAS.find(it=>{
    if(usadas[it.dia]) return false;
    if(fFmt && it.formato!==fFmt) return false;
    if(fPil && it.pilar!==fPil) return false;
    return true;
  });
  if(!sig){ toast2('🎉 No quedan ideas sin usar con este filtro'); return; }
  usarIdeaBanco(sig.dia);
}

function resetBanco(){
  if(confirm('¿Reiniciar todas las marcas? Todas las ideas volverán a estar disponibles.')){
    localStorage.removeItem('ideas_usadas');
    renderBanco();
    toast2('↺ Banco reiniciado — 365 ideas disponibles');
  }
}

/* ═══════════════════════════════════════════
   EXPORT PPTX — editable en Canva
   ═══════════════════════════════════════════ */
async function expPPTX(){
  if(!SLIDES.length){ alert('Genera contenido primero.'); return; }
  if(typeof PptxGenJS === 'undefined'){ alert('Cargando librería PPTX, espera un momento y vuelve a intentarlo.'); return; }

  const ov = document.getElementById('expOv');
  const msg = document.getElementById('expMsg');
  const bar = document.getElementById('expBar');
  ov.classList.add('on');
  msg.textContent = 'Generando PPTX...';
  bar.style.width = '0%';

  const pptx = new PptxGenJS();
  // Formato 4:5 Instagram (en pulgadas)
  pptx.defineLayout({ name:'IG45', width:10.8, height:13.5 });
  pptx.layout = 'IG45';

  // Colores de marca
  const CDARK  = '1A1A1A';
  const CLIGHT = 'F5F1EA';
  const CBLUE  = '38B6FF';

  // Escala px→pulgadas (1080px = 10.8in)
  const sc = v => parseFloat((v / 100).toFixed(4));

  for(let i=0;i<SLIDES.length;i++){
    const d = SLIDES[i];
    bar.style.width = Math.round((i/SLIDES.length)*80)+'%';
    msg.textContent = `Slide ${i+1} de ${SLIDES.length}...`;
    await delay(30);

    const slide = pptx.addSlide();
    const bgColor = d.fondo==='light' ? CLIGHT : d.fondo==='blue' ? CBLUE : CDARK;
    slide.background = { color: bgColor };

    const txtC = d.fondo==='dark' ? 'F5F1EA' : '1A1A1A';
    const subC = d.fondo==='dark' ? 'A0A0A0' : '555555';
    const accC = CBLUE;

    // Imagen de fondo (slides con foto)
    if(['foto','fototxt','autoridad','bafoto'].includes(d.tipo)){
      const url = getImgUrl(d.imgFondo || d.imgAntes);
      if(url){
        try{
          slide.addImage({ data: url, x:0, y:0, w:10.8, h:13.5, sizing:{type:'cover',w:10.8,h:13.5} });
          // Overlay oscuro
          slide.addShape(pptx.ShapeType.rect, { x:0, y:0, w:10.8, h:13.5,
            fill:{ color:'000000', transparency:45 }, line:{color:'000000',transparency:100} });
        }catch(e){}
      }
    }

    // Barra de acento superior
    slide.addShape(pptx.ShapeType.rect, { x:sc(90), y:sc(86), w:sc(44), h:sc(3), fill:{color:CBLUE}, line:{color:CBLUE,transparency:100} });

    // Eyebrow
    if(d.eye){
      slide.addText(d.eye.toUpperCase(), {
        x:sc(148), y:sc(82), w:sc(800), h:sc(40),
        fontSize:10, color:subC, fontFace:'Montserrat',
        charSpacing:3, bold:true,
      });
    }

    // Headline
    if(d.head){
      const headTxt = d.head.replace(/\*\*(.+?)\*\*/g,'$1').replace(/\*(.+?)\*/g,'$1');
      slide.addText(headTxt, {
        x:sc(90), y:sc(200), w:sc(900), h:sc(700),
        fontSize:Math.round(T.head*0.72), color:txtC,
        fontFace:'Montserrat', bold:false,
        valign:'middle', wrap:true, lineSpacingMultiple:1.15,
      });
    }

    // Cuerpo
    if(d.body){
      slide.addText(d.body, {
        x:sc(90), y:sc(920), w:sc(900), h:sc(200),
        fontSize:Math.round(T.body*0.72), color:subC,
        fontFace:'Montserrat', wrap:true, lineSpacingMultiple:1.4,
      });
    }

    // Items (lista)
    if(d.items?.length && ['lista','servicio','proceso'].includes(d.tipo)){
      const itemY = 820;
      const itemH = Math.floor(900/d.items.length);
      d.items.forEach((it,j)=>{
        const txt = it.replace(/\*\*(.+?)\*\*/g,'$1').replace(/\*(.+?)\*/g,'$1');
        slide.addText(`${String(j+1).padStart(2,'0')}  ${txt}`, {
          x:sc(90), y:sc(itemY+(j*itemH)), w:sc(900), h:sc(itemH-10),
          fontSize:Math.round(T.items*0.65), color:txtC,
          fontFace:'Montserrat', wrap:true,
        });
      });
    }

    // Footer: handle + CTA
    slide.addText(HANDLE, {
      x:sc(90), y:sc(1260), w:sc(400), h:sc(30),
      fontSize:9, color:subC, fontFace:'Montserrat', charSpacing:2, bold:true,
    });
    if(d.cta){
      slide.addText(d.cta, {
        x:sc(590), y:sc(1255), w:sc(400), h:sc(40),
        fontSize:10, color:accC, fontFace:'Montserrat',
        align:'right', bold:true, charSpacing:1,
      });
    }
  }

  bar.style.width = '95%';
  msg.textContent = 'Guardando archivo...';
  await pptx.writeFile({ fileName:`RM_carrusel_${SLIDES.length}_slides.pptx` });

  bar.style.width = '100%';
  msg.textContent = '✓ PPTX listo — importa en Canva';
  await delay(1800);
  ov.classList.remove('on');
}

/* ═══════════════════════════════════════════
   INIT
   ═══════════════════════════════════════════ */
document.addEventListener('DOMContentLoaded',async()=>{
  const ns=document.getElementById('nichoSel'); if(ns) ns.value=getNicho();
  actualizarAngulos();
  actualizarFeedLabel(); // Mostrar posición actual del feed
  setLogoTam(getLogoTam()); // Restaurar tamaño de logo guardado
  // Restaurar API key (guardada o por defecto)
  const ki=document.getElementById('pexelsKey');
  if(ki) ki.value = localStorage.getItem('pexels_key') || PEXELS_KEY_DEFAULT;
  // Sembrar keys desde config.local.js (fijas, no en el repo) si no hay guardadas
  if(window.RM_CONFIG){
    if(RM_CONFIG.groq_key && !localStorage.getItem('groq_key')) localStorage.setItem('groq_key', RM_CONFIG.groq_key);
    if(RM_CONFIG.pixabay_key && !localStorage.getItem('pixabay_key')) localStorage.setItem('pixabay_key', RM_CONFIG.pixabay_key);
    if(RM_CONFIG.jamendo_key && !localStorage.getItem('jamendo_key')) localStorage.setItem('jamendo_key', RM_CONFIG.jamendo_key);
  }
  const jk=document.getElementById('jamendoKey');
  if(jk){ jk.value=getJamendoKey(); guardarKeyJamendo(jk.value); }
  // Restaurar key de Groq y reflejar estado
  const gk=document.getElementById('groqKey');
  if(gk){ gk.value = getGroqKey(); guardarKeyGroq(gk.value); }
  const angulo=rnd(Object.keys(BANCO.angulos));
  const slides=buildCarrusel(angulo,null,7);
  slides.forEach(s=>SLIDES.push(s));
  buildThumbs();
  show(0);
  scaleStage();
  actualizarCopy(angulo, null);
  actualizarTagsPexels(angulo);
  renderBanco();
  window.addEventListener('resize',scaleStage);

  // Pre-cargar foto de perfil profesional en la biblioteca
  precargarImagen('FOTO PERFIL PROFESIONAL.png', 'Rosa María — Foto perfil');
  // Pre-cargar feed principal como referencia visual
  precargarImagen('FEED ROSA PRINCIPAL.png', 'Feed principal RM');
  // Auto-cargar TODAS las imágenes de la carpeta FOTOS PROFESIONALES (requiere servidor http)
  precargarCarpeta('FOTOS PROFESIONALES');

  // ── Drag & drop de fotos ──────────────────────────────
  // 1) Evitar que el navegador ABRA la imagen si se suelta fuera de la zona
  //    (comportamiento por defecto que sacaba de la app).
  ['dragover','drop'].forEach(ev =>
    window.addEventListener(ev, e=>{ e.preventDefault(); }, false));

  // 2) Todo el panel de fotos es zona de soltado (no solo la etiqueta pequeña).
  const panel = document.getElementById('mediaLib');
  const drop  = document.getElementById('mlibDrop');
  const marcar   = ()=>{ drop.classList.add('drag'); panel.classList.add('drag'); };
  const desmarcar= ()=>{ drop.classList.remove('drag'); panel.classList.remove('drag'); };

  panel.addEventListener('dragenter', e=>{ e.preventDefault(); marcar(); });
  panel.addEventListener('dragover',  e=>{ e.preventDefault(); e.dataTransfer.dropEffect='copy'; marcar(); });
  panel.addEventListener('dragleave', e=>{ if(!panel.contains(e.relatedTarget)) desmarcar(); });
  panel.addEventListener('drop', e=>{
    e.preventDefault(); desmarcar();
    const files = e.dataTransfer.files;
    if(files && files.length) cargarImagenes(files);
  });
});

// Descarga una imagen a dataURL. Devuelve {url, blobUrl} o null si falla.
// Silencioso en file:// (fetch bloqueado por CORS).
async function fetchDataURL(src){
  try{
    const res = await fetch(src);
    if(!res.ok) return null;
    const blob = await res.blob();
    const url = await new Promise(r=>{ const rd=new FileReader(); rd.onload=e=>r(e.target.result); rd.onerror=()=>r(null); rd.readAsDataURL(blob); });
    return url;
  }catch(e){ return null; }
}

// Añade una imagen ya descargada a la biblioteca.
function pushMedia(url, name){
  const id = ++mediaIdCounter;
  MEDIA.push({id, url, name});
  return id;
}

// Precarga simple (perfil, feed): descarga y añade a la biblioteca.
async function precargarImagen(src, name){
  const url = await fetchDataURL(src);
  if(url){ pushMedia(url, name); renderMediaGrid(); }
}

// ¿El nombre parece un logo? (para exigirle fondo transparente)
function pareceLogo(nombre){
  return /logo|propuesta|meta y google|removebg/i.test(nombre);
}

// ¿La imagen (dataURL) tiene fondo transparente? Muestrea el borde: si algún
// punto del borde es casi transparente, la consideramos con fondo transparente.
// Los .jpg nunca son transparentes → devuelve false sin cargar canvas.
function tieneTransparencia(url){
  if(/^data:image\/jpe?g/i.test(url)) return Promise.resolve(false);
  return new Promise(resolve=>{
    const img = new Image();
    img.onload = ()=>{
      try{
        const w=64, h=64;
        const cv=document.createElement('canvas'); cv.width=w; cv.height=h;
        const ctx=cv.getContext('2d'); ctx.drawImage(img,0,0,w,h);
        const d=ctx.getImageData(0,0,w,h).data;
        const pts=[[0,0],[w-1,0],[0,h-1],[w-1,h-1],[w>>1,0],[0,h>>1]]; // esquinas + medios de borde
        for(const [x,y] of pts){ if(d[(y*w+x)*4+3] < 40){ resolve(true); return; } }
        resolve(false);
      }catch(e){ resolve(false); }
    };
    img.onerror = ()=> resolve(false);
    img.src = url;
  });
}

/* Auto-carga imágenes de una carpeta leyendo su listado http (en paralelo).
   Carga TODAS las fotos + solo los logos con fondo transparente.
   Funciona con el listado de directorios de `python -m http.server` (y similares).
   Silencioso en file:// (fetch bloqueado por CORS). */
async function precargarCarpeta(carpeta){
  let res;
  try{ res = await fetch(carpeta + '/'); }catch(e){ return; }
  if(!res || !res.ok) return;
  const html = await res.text();
  const doc = new DOMParser().parseFromString(html, 'text/html');
  const yaCargadas = new Set(MEDIA.map(m => m.name));
  const items = Array.from(doc.querySelectorAll('a[href]'))
    .map(a => a.getAttribute('href'))
    .filter(h => h && /\.(png|jpe?g|webp|gif)$/i.test(h))
    .map(href => ({ href, nombre: decodeURIComponent(href.replace(/\/$/, '').split('/').pop()) }))
    .filter(it => !yaCargadas.has(it.nombre));       // evita duplicar perfil/feed ya precargados

  const load = document.getElementById('mlibLoad');
  let hechas = 0, añadidas = 0;
  const total = items.length;
  const setProg = ()=>{ if(load){ load.style.display='block'; load.textContent = `Cargando fotos… ${hechas}/${total}`; } };
  setProg();

  // Descarga + filtrado en paralelo; render incremental.
  await Promise.all(items.map(async ({href, nombre})=>{
    const url = await fetchDataURL(carpeta + '/' + href);
    if(url){
      // Fotos: siempre. Logos: solo si tienen fondo transparente.
      const ok = !pareceLogo(nombre) || await tieneTransparencia(url);
      if(ok){ pushMedia(url, nombre); añadidas++; renderMediaGrid(); }
    }
    hechas++; setProg();
  }));

  if(load){ load.textContent = `${añadidas} fotos cargadas`; setTimeout(()=>{ load.style.display='none'; }, 2500); }
}
document.addEventListener('keydown',e=>{
  if(e.key==='ArrowRight'||e.key==='ArrowDown') nav(1);
  if(e.key==='ArrowLeft' ||e.key==='ArrowUp')   nav(-1);
});
