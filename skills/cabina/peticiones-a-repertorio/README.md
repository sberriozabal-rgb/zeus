# peticiones-a-repertorio

Skill de la línea **CABINA**, paquete **CABINA EVENTOS** (Agent Skills, estándar abierto).

Convierte la lista de canciones que manda el cliente en texto sucio —WhatsApp, email, Excel mal
escrito, audio transcrito— en un informe accionable cruzado contra la biblioteca real del DJ.

## Los cuatro cubos

| Cubo | Qué es | Destino |
|---|---|---|
| **TENGO** | Coincidencia > 0.86 | Playlist directa |
| **NO TENGO** | Sin coincidencia | Lista de compra por criticidad |
| **DUDOSO** | Entre 0.62 y 0.86, o varias versiones | Confirmación del cliente |
| **PROHIBIDO** | Vetado por el cliente | Se repite literal por escrito |

## Uso

```bash
python3 scripts/cruzar.py <biblioteca.xml|csv> <peticiones.txt> --formato texto
python3 scripts/cruzar.py <biblioteca.xml|csv> <peticiones.txt> --formato json
```

**No limpies la lista del cliente antes de pegarla.** Limpiarla es el trabajo.

## Las dos reglas que evitan el incidente

1. **Todo lo que no supere 0.86 sube al cliente.** Un falso positivo no se descubre
   preparando: se descubre en el evento.
2. **Cero dudosos es señal de fallo, no de éxito.** Una lista real de 25 peticiones produce
   entre 2 y 6. Si salen cero, se bajó un umbral o se cruzó a ojo.

`--umbral-duda` se puede bajar si el cliente escribe muy mal. **Subir los umbrales nunca.**

## Lo que entrega al cliente

Un documento en su idioma, sin jerga, con tres bloques: **Confirmado**, **Necesito que me
confirmes** y **Anotado como no poner**. Ese último bloque repite los prohibidos literalmente,
porque es la parte que genera conflicto y tiene que constar por escrito.

## Ficheros

- `references/formato-biblioteca.md` — cómo exportar de cada software y sus límites.
- `references/momentos-evento.md` — momentos críticos por tipo de evento.
- `assets/plantilla-confirmacion.md` — plantilla del documento de cliente.
- `scripts/cruzar.py` — el motor del cruce.
- `cases/` — los 4 casos de prueba.

## Licencia

Propietaria. Uso permitido al comprador; prohibida la redistribución. Ver `LICENSE.txt`.
