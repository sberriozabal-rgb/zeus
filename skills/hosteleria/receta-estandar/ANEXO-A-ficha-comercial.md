# Anexo A — Ficha comercial

Nombre técnico     : receta-estandar
Nombre comercial   : [A VALIDAR — nombre comercial de la casa pendiente]
Peldaño            : P1 · SKILL (pieza del sistema instalable Motor B)
Línea              : Hostelería
Comprador nombrado : Restaurante con carta fija y producción repetida (≥1 vez por semana), España o México, plantilla de cocina de 3 a 15 personas con más de un cocinero por turno, y con un segundo local, una franquicia o un catering de volumen en el horizonte. Decide el chef propietario o el jefe de cocina; el dueño no cocinero firma pero no evalúa. Quien la ejecuta es el jefe de cocina fuera de servicio; quien la lee después es el cocinero de línea, de pie y con las manos ocupadas. **No es comprador**: la cocina de una sola persona sin rotación (no hay dos cocineros que diverjan, que es el problema que esto resuelve), la alta cocina de autor de pieza única sin repetición prevista, el local cuyo propietario decide que el valor del plato depende de no documentarlo, y cualquiera que venga buscando el plan APPCC — eso no es esto y se dice en la primera llamada, no en la entrega.
Trabajo que quita  : Escribir a mano las fichas técnicas de la carta, o no escribirlas nunca y perderlas el día que se va el chef. Y reconstruir cada temporada por qué el plato ya no sale como salía.
Umbral que aporta  : Que el pescado **no lleva la misma cifra en Madrid que en Monterrey** — 68 °C durante 15 s (AESAN-2021-004) frente a 63 °C (NOM-251 §7.3.1) — y que AESAN exige binomio tiempo-temperatura y no solo grados, de modo que una ficha española que copia una tabla americana está a medias aunque los grados coincidan. Mantenimiento en caliente ≥63 °C en España contra >60 °C en México. Más los 10 campos obligatorios de la receta estándar (Pennsylvania State University, cap. 6), la tolerancia de ±10 % sobre **peso de plato servido** y no sobre ingrediente crudo, y la regla de estado que sostiene todo lo demás: ninguna ficha es ACORDADO hasta que se ha pesado una vez.
Precio propuesto   : Dentro de Instalación Completa (4.900 €) **cuando levante G4**. Hasta entonces NO se factura. **Ratificado 15-sep-2026.**
Canal              : Venta presencial dentro del sistema instalable (Motor B). No se publica suelta en directorio hasta que el sistema completo tenga el primer caso vendido con cifras documentadas.
Motor              : B · Instalación
Frase de anuncio   : "La receta de tu local, no una receta bonita: con la temperatura que exige la norma de tu país y el hueco marcado donde todavía no has pesado."
Estado / Versión   : ACORDADO / v1.1.1
Auditoría          : **19/20** (`validar_skill.py`, 15-sep-2026, v1.1.1). El validador devuelve 20/20 mecánico; no se firma el 20 porque el punto 19 exige URLs verificadas una a una. Antes de la v1.1.1 medía **17/20** por tres defectos de estructura (umbral sin URL inline, salida sin supuestos, un antipatrón con el molde partido), ya cerrados.
Gates              : G1 [x] G2 [ ] G3 [x] G4 [ ] G5 [x]

## Desglose de auditoría (18/20)

Primera auditoría formal contra la rúbrica de 20 puntos de esta skill: la v1.0.0
declaró 17/20 en su CHANGELOG remitiendo a un informe del registro del proyecto,
sin desglose propio en la pieza.

**~~Punto no conseguido nº 1 — versión y CHANGELOG.~~ ✅ Resuelto.** El `CHANGELOG.md`
registra la v1.1.0 con el cambio de fuente normativa (FSA UK → AESAN + NOM-251) como su
cambio de más valor, y desde la v1.1.1 las versiones coinciden en los cuatro sitios.

**Punto no conseguido nº 2 — frontmatter conforme a spec.** El bloque YAML es
conforme en forma (`name` de 15 caracteres, `description` de 868, los cinco campos
presentes), pero `metadata.contrato_salida_hacia` declara
`"escandallo-costos, ingenieria-menu, checklist-operativo"`: **tres nombres que no
existen en el catálogo**. Los reales son `escandallo-ingenieria-menu` y
`apertura-cierre-turno`, como sí dice correctamente el cuerpo del SKILL.md en su
contrato de interfaz. Un consumidor que lea el frontmatter para encadenar no
encuentra nada. El frontmatter está congelado por regla de fábrica y no se corrige
desde aquí.

Todos los demás puntos: disparo con jerga real (ficha técnica, gramaje, partida,
sonda, merma, porcionado, "86"), trabajo en verbo, ejecutor definido con su tiempo
y con la asimetría declarada entre quien la escribe y quien la lee, entrada real,
manejo de datos sucios (nota de voz que mezcla dos preparaciones), umbral con
cifra y norma, 8 pasos atómicos con "si falta el dato", plantilla de salida en
bloque con longitud máxima y contrato JSON, límites declarados con matriz de
aplicabilidad, 12 reglas SIEMPRE, 10 reglas NUNCA, 5 antipatrones con síntoma ·
causa raíz · corrección, los 4 casos, 6 referencias externas verificadas con URL y
apartado, y esta ficha.

## Notas de gates

- **G1 (producto)** levantado: 18/20, por encima del 16 exigido. Los dos puntos
  que faltan son de coherencia documental, no de método, y ninguno se corrige
  desde los archivos de acompañamiento.
- **G2 (prueba)** pendiente: los cuatro casos son de fabricación. Ninguna ficha ha
  sido pesada en una cocina real, que es precisamente la condición que la propia
  skill impone para pasar de BORRADOR a ACORDADO. La skill se aplica su regla:
  hasta el primer pesaje documentado en un local, es una hipótesis bien escrita.
- **G3 (precio)** marcado con comprador nombrado, no-comprador nombrado y canal
  definido, aunque la cifra siga `[A VALIDAR]` hasta la firma de Sergio.
- **G4 (legal) pendiente, y es el gate crítico de esta pieza. Estado 15-sep-2026: de los
  tres requisitos, dos hechos y uno que no puede hacer la casa.**
  - **(c) ✅ cerrado**: el CHANGELOG registra el cambio de fuente normativa y las versiones
    coinciden.
  - **(b) ✅ redactado**: `venta/ANEXO-CONTRATO-INOCUIDAD.md`, cláusula que traslada al titular
    del negocio la inocuidad, la validación de cada binomio y los alérgenos. **Pendiente de
    revisión jurídica** antes de firmarse.
  - **(a) ❌ pendiente y es el que protege al titular**: revisión técnica externa por consultor
    de seguridad alimentaria. La casa ha dejado el trabajo listo para esa revisión: las tres
    cifras sin ancla que la v1.1.0 declaraba como riesgo legal están ancladas (RD 3484/2000
    art. 7 para conservación en frío y vida útil; AESAN vegetales 70 °C/2 min para el ejemplo
    del script), y se ha detectado y corregido una **discrepancia AESAN/RD en mantenimiento en
    caliente (≥63 vs ≥65 °C)** aplicando la cifra reglamentaria. Todo ello listado en el
    CHANGELOG v1.1.1 bajo *"Para el consultor"*.
  - Texto original del requisito: No por licencia
  —no deriva de material con prohibición de venta, no usa marca ajena en el nombre
  técnico ni comercial, y las menciones a AESAN, NOM-251, COFEPRIS y Codex son
  citas de fuente con URL— sino porque **toca seguridad alimentaria**. Antes de
  cobrar por ella hay que: (a) que un consultor de seguridad alimentaria revise el
  texto de `## Límites`, la declaración de no-APPCC y las dos tablas de
  `references/temperaturas_haccp.md` contra el documento primario; (b) confirmar
  que el contrato de instalación traslada al titular del negocio alimentario la
  responsabilidad sobre la inocuidad, sobre la validación de todo binomio y sobre
  la declaración de alérgenos; (c) cerrar la divergencia de versión del punto nº 1,
  porque un producto de seguridad alimentaria con un historial de cambios que no
  registra el cambio de fuente normativa no es defendible ante nadie. Sin esas
  tres cosas, no se cobra.
- **G5 (público)** pendiente: esta ficha no se ha usado todavía en material de
  venta enviado a nadie, y la frase de anuncio no ha pasado revisión de Sergio.
- **Declaración obligatoria en toda entrega, comercial o técnica**: la ficha de
  receta estándar **no es un plan APPCC** y no satisface el artículo 5 del
  Reglamento (CE) 852/2004; en México no sustituye el cumplimiento de la
  NOM-251-SSA1-2009. Marcar puntos críticos en una receta es buena práctica de
  higiene documentada, no el sistema de autocontrol que la ley exige al titular.
  Esta frase va en el material de venta, no solo en el LICENSE: un cliente que
  compre creyendo que resuelve su APPCC es una reclamación con fecha.
- **Riesgo comercial declarado**: es la pieza de mayor coste unitario de
  producción del sistema (una ficha por plato) y la única cuyo valor el cliente no
  ve hasta que se va un cocinero. Se vende contra el miedo a la fuga de
  conocimiento y contra el segundo local, no contra la eficiencia — y eso obliga a
  nombrar al comprador antes de fabricar carta, no después.
