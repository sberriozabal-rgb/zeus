# Taxonomía: cómo derivarla del material

## Regla de derivación (F3)
1. Lee los títulos, cabeceras y primeras 300 palabras de cada extracción.
2. Agrupa por tema hasta obtener **entre 5 y 12 dominios** que cubran el 100 % de los
   archivos que entraron. Criterio de corte: un dominio con menos de 2 fuentes se funde
   con su vecino; un dominio con más de ~7.000 palabras se divide (04a, 04b).
3. «Anexos» existe solo para lo que de verdad no encaja y no puede superar el 15 % de los
   archivos; si lo supera, falta un dominio.
4. Nombra cada dominio con sustantivos del propio material (usa su léxico, no el tuyo).
5. Declara la taxonomía en el índice con una línea por dominio y su nº de fuentes.

## Plantilla genérica (punto de partida, no obligación)

| Nº | Dominio genérico | Suele contener |
|---|---|---|
| 00 | INDICE_MAESTRO | Mapa · manifest fuente→destino · descartes · ilegibles · conflictos · huecos · `[NO LOCALIZADO]` · diff de versión · método de chats · taxonomía derivada |
| 01 | QUE_ES_Y_ESTRATEGIA | Definición del proyecto, objetivo, tesis, destinatario, ventaja, decisiones pendientes, hoja de ruta |
| 02 | PRODUCTO_O_MATERIA | Qué se produce o estudia: producto, servicio, obra, tema; componentes y módulos |
| 03 | METODO_Y_PROCESO | Cómo se hace: fases, entregables, hitos, controles, criterios de terminación |
| 04 | ECONOMIA | Precios, costes, presupuesto, modelo económico, condiciones de pago — `PROPUESTA A VALIDAR` por defecto |
| 05 | MERCADO_Y_RELACIONES | Clientes, público, canales, competidores, alianzas, argumentario |
| 06 | IDENTIDAD_Y_COMUNICACION | Voz, léxico, identidad visual, reglas editoriales, publicación |
| 07 | LEGAL_Y_ORGANIZACION | Estructura, socios, contratos, propiedad intelectual, cumplimiento — `PROPUESTA A VALIDAR` |
| 08 | EVIDENCIA_Y_RESULTADOS | Pilotos, datos, métricas, casos, autorizaciones de uso — `[CONFIDENCIAL]` si hay terceros |
| 09 | ANEXOS | Lo valioso que no encaja arriba (≤15 % de los archivos) |
| — | RESUMEN_EJECUTIVO / RESUMEN_CONTEXTO / RESUMEN_CHATS / INVENTARIO_DOCUMENTOS | Piezas de síntesis (plantillas en assets) |

Ejemplos de taxonomías derivadas, para calibrar: una tesis → Estado del arte · Método ·
Datos · Resultados · Borradores de capítulos · Bibliografía. Un despacho → Clientes ·
Procedimientos · Plantillas · Honorarios · Normativa · Correspondencia. Una obra → Proyecto
· Licencias · Presupuesto · Contratistas · Actas de obra · Planos.

## Formato obligatorio de cada documento maestro

```
# <Título descriptivo>
Dominio: <nº y nombre> · Proyecto: <PROYECTO> · Compilado: <AAAA-MM-DD> · Versión: v1.0 · Estado: <COMPILADO | PARCIAL | HUECO>
Archivos fuente: <nombre (fecha)>, … · Chats fuente: <títulos>

## <H2 por tema> … ### <H3>

---
## Notas de compilación
- [CONFLICTO] <fuente A dice X (fecha) · fuente B dice Y (fecha) · en el cuerpo prevalece Y>
- [DESCARTE] <archivo · motivo>
- [HUECO] <qué falta>
- [CONFIDENCIAL] <qué se anonimizó o excluyó>
```

Cada sección se entiende sola: el buscador del proyecto recupera fragmentos, no
carpetas. Siglas explicadas la primera vez que aparecen en cada documento.
