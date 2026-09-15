# Reglas de calidad (innegociables) — desarrollo

## 1 · Nada inventado
Cada afirmación proviene de un archivo de la carpeta o de un chat. Lo que falta se
declara `[HUECO]`; no se rellena de memoria ni desde el conocimiento general del modelo
sobre el sector.

## 2 · Trazabilidad
Cada maestro cierra con archivos fuente (nombre y fecha) y chats fuente. El índice lleva
el manifest completo archivo → maestro. Un archivo que entró y no aparece en ningún
maestro es un descarte no declarado: corrígelo.

## 3 · Decidido ≠ propuesto
`PROPUESTA A VALIDAR` en cifras, precios, contratos, reparto, estructura legal y todo
compromiso con terceros, salvo fuente que lo levante: documento marcado aprobado/firmado
o turno del **usuario** confirmándolo en un chat. Un turno del asistente nunca lo levanta.

## 4 · Conflictos a la vista
Dos fuentes que se contradicen: prevalece la más reciente en el cuerpo; la divergencia
en `[CONFLICTO]` al pie y en el índice con ambas fechas. Excepción: si la antigua está
marcada aprobada y la nueva no, prevalece la aprobada y se anota. Nunca en silencio.

## 5 · Marcos alternativos
Dos planteamientos incompatibles del mismo tema se etiquetan Marco A / Marco B (o con el
nombre que la carpeta les dé) y conviven. Un tercero se etiqueta C. Nunca se promedian.

## 6 · Confidencialidad
Datos de terceros identificables (clientes, pacientes, empleados, proveedores, alumnos):
`[CONFIDENCIAL]`, anonimizados salvo autorización escrita dentro de la carpeta (cítala).
Credenciales, tokens, claves, cuentas bancarias, documentos de identidad: **no entran**
al paquete; se avisa al usuario para que rote o custodie aparte. Ante la duda, marca.

## 7 · Autonomía de fragmento
Cada H2 se entiende solo. Títulos descriptivos, no genéricos. Sin «ver arriba».

## 8 · Tamaño útil
Referencia densa. >~7.000 palabras por dominio → divide con títulos propios. Tablas
donde el original era tabla.

## 9 · El conocimiento del proyecto no es fuente primaria
`/mnt/project` es la compilación anterior o material previo. Sirve para el diff de
versión y para no perder un dato cuya fuente ya no está en la carpeta —citado entonces
como `[FUENTE: compilación anterior, archivo original no localizado]`.

## 10 · La carpeta original queda intacta
Todo lo nuevo vive en CONTEXTO, junto a la original; nunca dentro, nunca reemplazándola.

## 11 · Sin sesgo de sector
No asumas país, moneda, normativa, idioma ni jerga. Si la carpeta no lo dice, es hueco.
