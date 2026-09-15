# Caso 3 · Failure (el enlace del export caducó)

## Situación

El export se solicitó el lunes. Nadie lo descargó. El viernes, al ir a por él, **el enlace ha
caducado** y hay que volver a solicitarlo — pero el proyecto se borra mañana.

## Lo que se pierde

**La capa 6 entera: el historial de chats.** Es la única vía a las conversaciones y no hay otra.
Sin export no hay chats, y no se puede fabricar.

## Lo que NO se hace

No se detiene el respaldo. Perder una capa de seis no es perder el respaldo: es perder una capa
de seis, y las otras cinco siguen ahí y siguen siendo recuperables **solo mientras haya acceso**,
que es hoy.

Tampoco se reconstruyen los chats "de memoria" ni a partir de lo que digan las instrucciones del
proyecto. Sería inventar la capa que falta.

## Salida real — cinco capas de seis, y el hueco declarado

```
paquete-[proyecto]-2026-09-15.zip   Estado: COMPLETO SALVO 1 ELEMENTO DECLARADO

01-instrucciones/ .... OK   (3 archivos)
02-conocimiento/ ..... OK   (22 documentos)
03-adjuntos/ ......... OK   (4 adjuntos)
04-descargas/ ........ OK   (7 descargas)
05-skills/ ........... OK   (2 skills)
06-chats/ ............ VACIA -> ver HUECOS.md
```

```markdown
## HUECOS.md

### L5 · Historial de chats — NO VIAJA
**Qué falta:** las 61 conversaciones del proyecto.
**Por qué:** el export oficial se solicitó el 2026-09-08 y su enlace caducó antes de
descargarse. Es la única vía al historial y no existe otra.
**¿Recuperable?** Solo si se vuelve a solicitar el export ANTES de borrar la cuenta o
el proyecto, y se descarga en menos de 24 h.
**Qué hacer ahora, por orden:**
  1. Solicitar de nuevo el export AHORA: support.claude.com/en/articles/9450526
  2. NO borrar el proyecto hasta tenerlo descargado.
  3. Cuando llegue, ejecutar solo los pasos 2 y 3 sobre este mismo paquete y
     re-sellar. El resto no hay que repetirlo.
```

## Los supuestos declarados

> **Asumido**: sin historial de chats. El paquete **no se declara COMPLETO**, sino *"completo
> salvo 1 elemento declarado"*. Las otras cinco capas están verificadas en frío y firmadas.
>
> El `RESUMEN-CHATS.md` **no existe** en este paquete, y `RESTAURAR-TODO.md` lo dice en su
> primera línea: quien reconstruya sabrá desde el principio que no hay conversaciones, en lugar
> de descubrirlo buscándolas.

## La recomendación que acompaña a la entrega

> **No borres el proyecto mañana.** Vuelve a pedir el export hoy, descárgalo en cuanto llegue y
> te añado la capa que falta en veinte minutos sobre este mismo paquete. Borrar mañana con la
> capa 6 vacía es irreversible; esperar dos días no cuesta nada.

## Por qué es el caso decisivo

El antipatrón sería responder "no se puede hacer el respaldo sin el export" y dejar que se
borren las otras cinco capas con el proyecto. Aquí el usuario se lleva **el 83 % del respaldo
hecho y verificado**, el hueco escrito con nombre y motivo, y las tres acciones concretas para
cerrarlo antes de que sea tarde.
