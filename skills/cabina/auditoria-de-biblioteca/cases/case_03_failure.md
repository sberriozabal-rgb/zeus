# Caso 3 · Failure (XML de otra máquina, 100% de rutas rotas)

## Encargo real

> "Te mando el XML desde el portátil del curro que es donde lo tenía a mano."

## Entrada

- `collection.xml` de 5.200 tracks.
- Ejecutado con `--comprobar-rutas` **desde una máquina que no es la del DJ**.
- La música vive en un disco externo que no está montado aquí.

## Lo que sale si no se detecta el artefacto

```
ruta_rota          5.200  100.0%   CRITICO
Indice de salud:   12/100
```

Un parte que diga "tienes la biblioteca destruida" sería **falso** y además alarmante.

## Salida real — lo que se entrega igual, sin rendirse

Se detecta el artefacto por la regla de que un 100% de rutas rotas con el resto de metadatos
sanos es casi siempre máquina equivocada, se reejecuta sin `--comprobar-rutas`, y **se entrega
el parte de todo lo demás**, que sigue siendo válido porque no depende del disco:

```
Indice de salud: 74/100    (5.200 tracks)   [rutas NO comprobadas]

CATEGORIA              N       %   RIESGO
sin_beatgrid         180    3.5%   CRITICO
sin_clave            890   17.1%   ALTO
bitrate_bajo          41    0.8%   ALTO
duplicados           310    6.0%   MEDIO
genero_inconsistente 620   11.9%   MEDIO
```

## Los supuestos declarados

> **Asumido**: el XML se exportó desde una máquina distinta a la que aloja la música, porque
> el 100% de rutas rotas convive con metadatos sanos. **No se ha comprobado ni una sola ruta
> en disco**: esa parte del parte no existe en esta entrega. Todo lo demás —beatgrid, clave,
> bitrate, duplicados, géneros— se lee del XML y es válido con independencia del disco.
>
> Para cerrar el hueco: reexporta el XML desde tu máquina y vuelve a lanzarlo con
> `--comprobar-rutas`. Son dos minutos y es lo único que falta.

## Lo que NO se hace

No se responde "necesito que lo ejecutes desde tu ordenador" y se acaba ahí. El DJ recibe el
80% del parte —que es real, accionable y contiene los 180 sin beatgrid que sí le importan— y
una instrucción concreta de dos minutos para completar el 20% restante.

Tampoco se entrega el dato de rutas con una nota al pie. Se retira del parte entero, porque
una cifra falsa con asterisco sigue siendo una cifra falsa y es la que el DJ va a recordar.
