# CHANGELOG — respaldo-proyecto-ia-cl

## [2.1.0] — 2026-09-15

**Cierre del envoltorio de venta.** La auditoría mecánica del 15-sep-2026 (`validar_skill.py`)
dio **3/20** frente al **18/20 (autoevaluación)** que declaraba el frontmatter. La autoevaluación
era honesta en sustancia y estaba marcada como tal, pero **una nota que nadie puede reproducir con
el validador no sirve para vender**.

Añadido:

- Estructura de **13 secciones del ADN**, con los 12 pasos P0-P11 comprimidos a **8 pasos
  atómicos** con el molde en línea Entrada → Acción → Salida → Si falta el dato.
- Reglas convertidas de lista numerada a tabla: **10 SIEMPRE y 9 NUNCA** con su porqué.
- Antipatrones de 6 a **5 con el molde de serie**, fusionando "el respaldo que nadie abrió nunca"
  y "la instrucción que apunta a un archivo que no viajó": son el mismo fallo —nadie probó la
  restauración— visto desde dos síntomas distintos.
- Los **4 casos de prueba** en `cases/`, extraídos de `references/casos.md`, que conserva el
  quinto (datos sucios) y el detalle de todos.
- Viñeta de **dato sucio típico** en `Entrada`: el export sin campo de proyecto y el secreto
  pegado dentro de un chat.
- `ANEXO-A-ficha-comercial.md`, `README.md` y `metadata.json`.

**El contenido de oficio no se ha tocado**: las cuatro clases C0-C3 con sus dos reglas duras, el
ZIP anidado contra el índice en claro, la restauración en frío firmada y fechada, la rotación de
credenciales y el límite de plataforma con cita literal están exactamente como estaban.

Resultado: **19/20** declarado (20/20 mecánico, menos el punto 19 de criterio).

Versionado semántico: MAYOR cambia el protocolo · MENOR añade capacidad ·
PARCHE corrige referencias, ejemplos y redacción.

---

Versionado semántico: MAYOR cambia el protocolo · MENOR añade capacidad ·
PARCHE corrige referencias, ejemplos y redacción.

---

## v2.0.0 — 2026-08-16

Estado **ACORDADO**. Autoevaluación **18/20**. Motor de la sesión de
fabricación: `claude-fable-5` (Cowork). MAYOR porque el protocolo cambia: de 9
pasos a 12 (P0–P11), y quien usaba la v1 debe releer.

### Añadido

- **P0 · Export oficial como vía a los chats.** El historial completo solo
  existe en el ZIP de Ajustes → Privacidad → Exportar datos; el enlace caduca a
  las 24 h (fuente A6). La skill ya no pide "seleccionar chats a mano": digiere
  el export.
- **`--ingerir`**: reconoce el volcado por estructura (no por nombre de
  archivo), acepta ZIP / carpeta / JSON, tolera tres formas de mensaje
  observadas (`text`, `content` en bloques, `parts`), filtra por proyecto
  declarando el método (`[FIABLE]` con campo de proyecto, `[INDICIO, NO
  PRUEBA]` por coincidencia de texto), transcribe un .md por chat y genera
  `RESUMEN-CHATS.md` con índice, temas, citas candidatas a decisión, cifras y
  pendientes. Deja `chats.jsonl` para encadenar con otras skills.
- **`--recolectar`**: barrido de carpetas locales de descargas con deduplicado
  por SHA-256 en dos pasadas — de cada grupo de duplicados conserva la copia
  que citan L1/L2, no la primera alfabética —, corte por fecha `--desde`,
  renombrado neutro e `INDICE-ADJUNTOS.md` con lo citado-que-falta y lo
  recolectado-que-nadie-cita.
- **`--restaurar-todo`**: genera `RESTAURAR-TODO.md`, archivo maestro
  autosuficiente con L1 íntegra, índice y extracto de L2, inventario de L3/L4,
  resumen de chats completo, los 10 pasos de restauración, la prueba de humo,
  los huecos y el acta.
- **`--auto`**: encadena preparar → ingerir → recolectar → escanear → maestro →
  sellar → verificar y emite `ACTA-<carpeta>-<fecha>.json`. Se detiene ante C3.
  No automatiza lo que no debe: clasificar, redactar, la lectura humana ni la
  entrega.
- **P7 · Lectura humana obligatoria**: el borrador automático cita, cuenta y
  ordena, y termina cada chat con `LECTURA DE UNA PERSONA: [pendiente]` que se
  rellena antes de sellar. Plantilla 5 en `assets/plantillas.md`.
- Antipatrón 6: el borrador que se vendió como resumen.
- Caso 05 (datos sucios) **ejecutado en real** contra un export simulado, con
  salida observada literal en `references/casos.md`.
- Patrón C3 nuevo: tokens de Stripe (`sk_live_` / `rk_live_`).

### Corregido

- **G-1 (gotcha de v1.0.0, registrado en `claude/registro-respaldos.md`):** el
  marcador `[REDACTADO:tipo]` en forma de asignación
  (`password=[REDACTADO:...]`) volvía a disparar el patrón C3 de contraseñas y
  el sellado entraba en bucle: redactabas y el escáner seguía viendo un
  secreto. Los patrones de asignación y Bearer ahora excluyen los marcadores
  `[REDACTADO:`, `[NO EXPORTABLE:`, huecos `<...>` y ofuscados (`***`,
  `xxxx...`). Verificado en el caso 05.
- La regex de rutas citadas en L1/L2 aceptaba espacios dentro del nombre y
  capturaba frases enteras ("Ver informe.pdf" entero) que ningún barrido
  encontraba después. Sin espacio en la clase de caracteres.
- `--verificar` tras `--auto` ahora recibe la ruta absoluta del paquete
  (`ruta` en el JSON de sellado); antes fallaba si `--salida` apuntaba fuera
  del directorio de trabajo.
- El escáner excluye `chats.jsonl` (duplicaba cada hallazgo de las
  transcripciones) y `CHECKSUMS.txt`.

### Decisiones de diseño que conviene no revertir

1. **El maestro no contiene la huella SHA-256 de su propio paquete, y lo
   declara.** Un archivo no puede contener la huella del contenedor que lo
   contiene; el primer diseño de `--auto` resellaba para "inyectarla" y
   producía una huella que ya no era la del paquete final. La huella viaja solo
   por el canal B.
2. **`--ingerir` identifica el export por estructura, nunca por nombre de
   archivo.** Anthropic no documenta la estructura interna del ZIP (hueco
   declarado en A6) y ya ha cambiado antes. Si no reconoce nada, lo dice y L5
   va a HUECOS.md: nunca inventa conversaciones.
3. **El resumen automático no interpreta.** Extrae citas con señales de
   decisión, cifras y pendientes; la lectura la firma una persona. Un resumen
   generado que opina es una cifra huérfana con párrafos.
4. Se conservan las tres decisiones de v1.0.0: el script propone y la persona
   clasifica; el sellado se detiene ante C3; doble ZIP obligatorio.

### Deuda declarada

- Las referencias criptográficas B1–B3 siguen citadas por ficha, no por lectura
  del texto completo.
- El filtro `[INDICIO]` por coincidencia de texto no tiene medida de precisión:
  la revisión manual es la mitigación, no un lujo.
- Sin ejecución aún contra un export real de cuenta (solo simulado). Primer
  export real de Sergio = primer caso de PRODUCCIÓN.

---

## v1.0.0 — 2026-08-15

Primera versión. Estado **ACORDADO**. Autoevaluación **18/20**.

> **Nota de nomenclatura.** La pieza se fabricó el mismo día bajo el nombre
> `respaldo-proyecto-claude` y se renombró a `respaldo-proyecto-ia-cl` antes de
> cualquier distribución. **No hubo versión publicada con el nombre anterior**, así
> que el cambio no consume número de versión ni deja artefacto DEPRECADO. Si
> alguien tiene un `.skill` con el nombre viejo, es el mismo contenido y puede
> sustituirlo sin releer nada.

### Añadido

- Protocolo de 9 pasos, de inventariar el perímetro a reconstruir en destino.
- Modelo de 5 capas (L1 instrucciones · L2 conocimiento · L3 adjuntos ·
  L4 skills · L5 chats) con orden de extracción justificado.
- 4 clases de sensibilidad excluyentes (C0–C3) con regla de asignación
  determinista: se lee de C3 hacia C0 y se para en la primera que se cumple.
- 8 reglas SIEMPRE y 8 NUNCA, todas con su porqué de una línea.
- 5 antipatrones con síntoma observable desde la salida.
- 4 casos de prueba en `references/casos.md`, con la trampa que comprueba cada uno.
- `scripts/respaldo.py` con cuatro modos: `--escanear`, `--empaquetar`,
  `--verificar`, `--ejemplo`.
- 4 plantillas en `assets/plantillas.md`: MANIFIESTO, HUECOS, RECONSTRUIR y
  cabecera de archivo redactado.
- 7 fuentes externas en `references/fuentes.md`, cada una anclada a la línea que
  sostiene, con su estatus de verificación declarado.
- Debate abierto documentado con ambas posiciones: ¿basta un ZIP AES-256, o hace
  falta GnuPG/age? Con la resolución de diseño y lo que esa resolución sacrifica.

### Decisiones de diseño que conviene no revertir

1. **El script no asigna clases de sensibilidad; propone hallazgos.** Marcar un
   archivo como confidencial tiene consecuencias sobre personas. Una máquina
   señala patrones; la clasificación la firma alguien.
2. **El sellado se detiene ante un hallazgo C3.** Es la única condición
   bloqueante del script. Un secreto respaldado es un secreto filtrado en cuanto
   el paquete se copia una vez de más.
3. **ZIP anidado obligatorio.** No es preferencia: el formato ZIP deja el
   directorio central en claro. Verificado por ejecución propia (`fuentes.md` B4).
4. **`verificado_en` nace `null` y solo lo rellena una persona.** El script no se
   autocertifica: eso convierte el antipatrón 3 en un campo auditable desde fuera.
5. **La contraseña no se acepta como argumento.** Queda en el historial del shell
   y en la lista de procesos.

### Limitaciones declaradas de esta versión

- **Ningún proyecto real respaldado.** Los 4 casos usan datos sintéticos. Es lo
  único que sube esta pieza de ACORDADO a PRODUCCIÓN, y no lo arregla redactar más.
- **Antipatrones `[DERIVADOS]`** de dónde puede romperse el protocolo, no
  observados en campo. Excepción parcial: el antipatrón 2 sí está verificado
  técnicamente, aunque no observado en un respaldo real.
- **Tres referencias criptográficas citadas por ficha bibliográfica**, no por
  lectura del texto completo (B1, B2, B3).
- **No cubre no repudio.** La huella SHA-256 por canal separado es un control más
  débil que una firma criptográfica, y se declara como tal.
- **Compatibilidad de apertura no comprobada** con 7-Zip, WinZip ni Keka: el
  anidado se verificó con `pyzipper` en Linux.

---

## Roadmap v1.1.0

Por orden de lo que más sube la nota:

1. **Tres respaldos reales documentados**, con cronometraje real de P2 y volumen
   real. Cierra el criterio 9 y sustituye los antipatrones `[DERIVADOS]`.
2. **Probar el paquete anidado en 7-Zip, WinZip, Keka y el explorador de Windows.**
   Si alguno no abre el anidado con comodidad, el diseño cambia. Es barato y
   decide si la pieza es usable por un no técnico.
3. **Leer B1–B3 en texto completo** y sustituir las fichas por citas ancladas.
4. **Modo `--age` / `--gpg`** para quien necesite firma del remitente y cifrado de
   nombres sin anidado. Resuelve el "en contra" del debate en lugar de rodearlo.
5. **Detección de dato personal por idioma.** Los patrones actuales (correo,
   IBAN, teléfono) son razonablemente universales; nombres propios, documentos de
   identidad y direcciones no lo son.
6. **Módulo de respaldo incremental.** Hoy cada paquete es completo. Con proyectos
   que cambian a diario, eso multiplica el volumen y desanima el hábito.
7. **Comprobar si la exportación nativa incluye la base de conocimiento** y en qué
   formato. Si la incluyera, P2 se acorta mucho para las capas L1 y L2.

## Roadmap v2.0.0 (cambiaría el protocolo)

- Si Anthropic publica en algún momento una ruta de duplicación o transferencia de
  proyectos, P9 deja de ser reconstrucción manual y el protocolo se reescribe.
  **Comprobar en cada revisión antes de dar por buena la afirmación de A1.**
