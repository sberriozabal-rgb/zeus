# Anexo A — Ficha comercial

| Campo | Valor |
|---|---|
| Nombre técnico | `respaldo-proyecto-ia-cl` |
| Nombre comercial | Respaldo cifrado de proyecto de IA |
| Peldaño | P1 · SKILL |
| Línea / Paquete | Neutra · sin oficio específico |
| Comprador nombrado | Quien administra un Proyecto de Claude con **contenido que le costaría rehacer**: consultor, despacho, agencia o equipo pequeño con base de conocimiento propia, adjuntos de cliente y meses de conversación. Decide y paga quien administra el proyecto. |
| Quien NO es comprador | Quien espere una **migración automática entre cuentas**: no existe, Anthropic no la soporta, y esta skill no la inventa. Vender esto como "mover tu cuenta" es vender humo. Tampoco quien necesite un archivo con validez legal o de cumplimiento normativo: esto es un respaldo operativo. |
| Trabajo que quita | Perder meses de trabajo al cerrar o cambiar de cuenta, o hacer un `zip -r` de la carpeta y descubrir al restaurar que faltan las conversaciones, que los adjuntos citan documentos que no viajaron, o que dentro iba una clave API. |
| Umbral que aporta | Las **cuatro clases excluyentes C0-C3** leídas de C3 hacia C0, con dos reglas duras: un archivo con una clave es **C3 aunque el otro 99 % sea público** (se parte el archivo, no se rebaja la clase), y **clase desconocida = C2, nunca C0**. Más la **restauración en frío firmada y fechada otro día**, que es lo único que distingue un respaldo verificado de un comando que terminó sin error. |
| Límite declarado | **No migra nada.** Anthropic no soporta migrar datos entre cuentas personales: lo que produce es un paquete de **reconstrucción manual**. El borrador de chats **cita y cuenta, no interpreta**. Sin `pyzipper` el paquete se entrega **sin cifrar y se declara**. |
| Precio propuesto | **49 €** suelta · **89 €** en PACK CONTEXTO. **Ratificado 15-sep-2026.** |
| Razón del precio | Tramo 30-49 € de mejor conversión. El comprador llega con urgencia —va a cerrar una cuenta o a cambiar de plan— y el coste de no tenerlo es la pérdida total del contenido, así que la disposición a pagar es alta, pero es un producto de **uso puntual** y no de serie: no sostiene una suscripción. |
| Canal | Gumroad · catálogo (Motor A). Entrega por descarga (`venta/GUMROAD-ALTA.md`); decisión 8 del 15-sep-2026. |
| Motor | A · Catálogo |
| Frase de anuncio | «Te llevas tu proyecto entero cifrado, con el guion para rehacerlo y la lista de lo que no cabía. Probado en frío antes de que borres nada.» |
| Estado / Versión | ACORDADO / v2.1.0 |
| Auditoría | **19/20** (`validar_skill.py`, 15-sep-2026). El validador devuelve 20/20 mecánico; **no se firma el 20** porque el punto 19 exige URLs verificadas y no se han reconfirmado una a una. Antes de esta revisión medía **3/20** frente al 18/20 de autoevaluación que declaraba. |
| Gates | G1 [x] G2 [ ] G3 [x] G4 [x] G5 [x] |

## Notas de gates

- **G1 (producto)** levantado el 15-sep-2026: 19/20 desde **3/20** medido. La nota baja era de
  estructura. El contenido —las cuatro clases, el ZIP anidado, la restauración en frío, los nueve
  SIEMPRE y los nueve NUNCA— ya estaba y se conserva íntegro.
- **G2 (prueba)** pendiente: los casos son de fabricación.
- **G3 (precio)** pendiente: comprador nombrado y canal definidos, cifra `[A VALIDAR]`.
- **G4 (legal)** en orden, y es el gate con más peso propio de esta pieza. Declara sin adornos el
  límite de plataforma con **cita literal del Centro de Ayuda** y su artículo; trata las
  credenciales como C3 que **se rotan y no se respaldan**; y no promete cifrado cuando `pyzipper`
  no está disponible.
- **G5 (público)** pendiente. Al publicar, **nunca presentar esto como migración de cuenta**: es
  la afirmación que la propia documentación de la plataforma desmiente, y sería una cifra huérfana
  en forma de promesa.
