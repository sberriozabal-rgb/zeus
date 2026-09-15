# Caso 1 · Happy path (proyecto Pro, export con campo de proyecto)

## Entrada

- Proyecto Pro con **22 documentos** en base de conocimiento, **4 adjuntos**, **2 skills**
  asociadas y 61 chats.
- Export oficial solicitado el lunes, **descargado el mismo día** (el enlace caduca).
- El export **sí trae campo de proyecto**: el filtrado es prueba, no indicio.

## Ejecución

```
P1 inventario ..... 22 docs · 4 adjuntos · 2 skills · 61 chats
P2 arbol .......... 6 capas creadas
P3 chats .......... 61/61 por campo de proyecto (sin [INDICIO])
P4 descargas ...... 4/4 · referencias cruzadas OK
P5 clases ......... C0:9  C1:12  C2:5  C3:0
P6 redactado ...... 5 archivos C2 redactados · escaneo de credenciales: limpio
P7 lectura ........ RESUMEN-CHATS.md completo, 0 [pendiente de escribir]
P8 maestro ........ RESTAURAR-TODO.md generado
P9 sellado ........ AES-256, ZIP anidado, nombres neutros, SHA-256 calculados
P10 restauracion .. carpeta vacia distinta, 3 archivos de 3 carpetas: OK
P11 entrega ....... paquete por correo · clave + huella SHA-256 por WhatsApp
```

## Clasificación (paso 4), que es donde está el criterio

De los 22 documentos, cinco resultan **C2** por nombrar clientes con precios. Uno de ellos es un
documento que el dueño habría marcado público: un índice de catálogo que en su tercera tabla
lleva tarifas de tres clientes nombrados.

**No se rebaja la clase por el 90 % público**: entra cifrado y redactado, con la correspondencia
en `INDICE-ADJUNTOS.md`, dentro del cifrado.

Los 61 chats entran como **C2 por defecto**, sin excepción. Es donde vive el dato personal que
nadie recuerda haber escrito.

## Verificación en frío (paso 8)

```
MANIFIESTO.md
  Creado:      2026-09-15 10:42
  Verificado:  2026-09-16 09:15  por [nombre]
  Restauracion en frio: /tmp/prueba-restauracion (carpeta vacia)
  Abiertos: 02-conocimiento/doc-07.md, 03-adjuntos/adj-02.pdf, 06-chats/chat-034.md
  Resultado: los 3 abren y su contenido coincide con el origen
```

**La fecha de verificación es del día siguiente**, no del mismo minuto. Es la diferencia entre
haber probado el paquete y haber visto que el comando terminó sin error.

## Salida

```
Estado del paquete: COMPLETO
HUECOS.md: vacio
[pendiente de escribir]: 0
Secretos detectados: 0 (C3 vacio)
```

## Por qué es el caso central

Es el único escenario en que el paquete se puede declarar **COMPLETO** sin salvedades, y muestra
las dos decisiones que separan este respaldo de un `zip -r`: **la clase se sube y no se baja**
—el índice de catálogo acabó en C2— y **la verificación se hace otro día y la firma una persona**.
