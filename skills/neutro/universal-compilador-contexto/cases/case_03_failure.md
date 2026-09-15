# Caso 3 · Failure (sin chats y con 18 PDF ilegibles)

## Situación

- **Sin acceso al historial de chats**: no hay export descargado y las herramientas de sesión no
  devuelven nada útil para este proyecto.
- De los 94 archivos de la carpeta, **18 son PDF escaneados** de muy baja calidad: el OCR
  devuelve texto inservible (columnas mezcladas, caracteres corruptos).

Entre los 18 hay, por el nombre, contratos y actas: material probablemente importante.

## Lo que NO se hace

No se bloquea la entrega. **Bloquear es el fallo más caro** de esta skill: el dueño se queda sin
nada cuando podría tener el 81 % ordenado.

Tampoco se acepta el OCR malo como si fuera texto. Meter una transcripción corrupta en un maestro
es peor que declarar el hueco: nadie vuelve a comprobarla y el error se propaga con aspecto de
dato.

Y **no se infiere el contenido por el nombre del archivo**. Que un PDF se llame
`acta-reunion-socios-marzo.pdf` no autoriza a escribir en ningún maestro qué se acordó en esa
reunión.

## Salida real — el ZIP sale con el 81 % y los huecos escritos

```
PROYECTO_CONTEXTO_2026-09-15.zip
  Archivos procesados: 76 de 94  (81%)
  Dominios derivados: 5  (todos con >=2 fuentes)
  Anexos: 9 archivos = 11,8% (tope 15%) OK

  RESUMEN_CHATS.md ....... NO EXISTE -> ver HUECOS.md
  CONFLICTOS.md .......... 1 entrada
  HUECOS.md .............. 2 entradas
```

```markdown
## HUECOS.md

### H1 · Historial de chats — NO INGERIDO
**Qué falta:** todas las conversaciones del proyecto.
**Por qué:** sin export oficial descargado. La Ruta A no devolvió material utilizable.
**Consecuencia:** no hay `RESUMEN_CHATS.md`. La biblioteca sale **solo de documentos**,
así que **la ausencia de una decisión en los maestros no prueba que no se tomara**:
puede estar en una conversación que no se ingirió.
**Cómo cerrarlo:** solicitar el export en support.claude.com/en/articles/9450526 y
descargarlo en menos de 24 h. Con él, se re-ejecutan solo los pasos 3 y 4.

### H2 · 18 PDF escaneados ilegibles
**Qué falta:** el contenido de 18 archivos, listados uno a uno abajo con su ruta.
**Por qué:** escaneados sin capa de texto y con OCR de calidad inservible.
**Consecuencia:** por su nombre, al menos 6 parecen contratos o actas. **No se ha
inferido nada de ellos.** Si contienen decisiones, no están en esta compilación.
**Cómo cerrarlo:** reescanear a mayor resolución, o transcribir a mano los 6 críticos.
```

## La frase que hace útil el hueco

Está en el `RESUMEN_EJECUTIVO.md`, arriba del todo, y es la que evita el malentendido caro:

> **Esta compilación sale solo de documentos legibles: el 81 % de la carpeta y ningún chat.**
> Cuando un tema no aparezca aquí, eso significa *"no consta en lo compilado"*, **no**
> *"no se decidió"*. Los dos huecos que lo explican están en `HUECOS.md` con su lista de archivos.

## Los supuestos declarados

> **Asumido**: sin historial de chats y con 18 archivos ilegibles, listados con ruta en
> `HUECOS.md`. **No se ha inferido contenido de ningún archivo por su nombre.** Los 5 dominios
> derivados cumplen el mínimo de 2 fuentes y "Anexos" queda en el 11,8 %, por debajo del tope.

## Por qué es el caso decisivo

El dueño se lleva **76 archivos ordenados, cinco dominios y un inventario trazable** en lugar de
un mensaje de error. Y, sobre todo, se lleva escrita la diferencia entre *ausencia de dato* y
*ausencia de decisión*, que es lo único que impide que use esta biblioteca como si fuera completa.
