# Plantillas de las piezas de síntesis

## RESUMEN_CONTEXTO.md (una página, exacta)

```
# RESUMEN DE CONTEXTO — <PROYECTO> · <AAAA-MM-DD> · v<x.y>

## Qué contiene este paquete
<3–5 líneas: fuente usada (ordenador/Drive/ZIP, nº archivos), ruta de chats (A parcial / B export) y nº de chats, versión anterior comparada, taxonomía derivada en una línea.>

## Qué está DECIDIDO (con fuente que lo confirma)
- <decisión> — <archivo o chat, fecha>

## Qué está A VALIDAR (propuestas sin aprobación)
- <propuesta> — <dónde vive>

## Conflictos abiertos
- <A vs B> — ver 00_INDICE_MAESTRO

## Huecos (lo que no existe en ninguna fuente)
- <hueco>

## Dónde está cada cosa
| Tema | Documento del paquete |
|---|---|

## Próxima recompilación
<qué la dispara>
```

## RESUMEN_CHATS.md (final, sobre el borrador del script)

```
# RESUMEN DE CHATS — <PROYECTO> · <fecha>
Ruta: <A: sesión, N chats leídos de M listados | B: export oficial, filtro FIABLE/INDICIO> · Alcance: <completo | parcial: qué falta>

## Índice de chats
| # | Fecha | Chat | Lectura (2–4 líneas: qué se decidió, qué quedó abierto, qué cifra defender) |

## Decisiones confirmadas por el usuario
| Decisión | Chat | Fecha | Maestro donde vive |

## Propuestas de Claude sin confirmar
| Propuesta | Chat | Fecha |

## Pendientes y bloqueos
| Pendiente | Chat | Quién lo cierra (si consta) |

## Documentos producidos en los chats
(remite a INVENTARIO_DOCUMENTOS.md; aquí solo los que cambiaron de versión)
```

## 00_INDICE_MAESTRO.md — secciones obligatorias
1. Taxonomía derivada (dominio · nº de fuentes · palabras)
2. Manifest fuente → destino
3. Descartes con motivo
4. Ilegibles con motivo y tema probable
5. Conflictos abiertos (A · B · fechas · qué prevalece · quién decide)
6. Huecos
7. Documentos `[NO LOCALIZADO]` citados en chats
8. Diff de versión respecto a la compilación anterior
9. Método de chats usado y alcance
10. Parámetros fijados (proyecto, idioma, marcas de estado)
