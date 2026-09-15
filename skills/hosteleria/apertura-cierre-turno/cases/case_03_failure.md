# Caso 3 · Failure (encargo de una línea, sin contexto)

## Encargo real que escribiría un dueño

> "hazme un checklist de cierre"

Sin tipo de local, sin horario, sin plantilla, sin puntos de fricción. Cuatro
palabras. Es el encargo más frecuente que llega por WhatsApp un martes a las
once de la noche.

## Entrada mínima construible

```
tipo_local:        [FALTA]
horario:           [FALTA]
plantilla_puesto:  [FALTA]
puntos_friccion:   [FALTA]
pais:              [FALTA]
bloque_pedido:     cierre   ← lo único que hay
```

## Salida esperada — lo que se entrega igual, sin rendirse

**El antipatrón que aquí sería un suspenso:** responder *"para hacerte el
checklist necesito saber qué tipo de local tienes, tu horario, tu plantilla y
qué se os suele olvidar"* y detenerse. El dueño no vuelve a escribir. Se entrega
el producto y se declara lo asumido.

Se entrega **el checklist de cierre completo y usable esta misma noche**:

### Checklist de cierre — [nombre del local]

Plantilla base: restaurante de mesa y mantel, tamaño medio (la nº2, por defecto).

| # | Tarea | Responsable | Criterio de "hecho" | Crítico |
|---|---|---|---|---|
| 1 | Arqueo de caja final | Encargado | Cifra de cierre anotada; descuadre registrado con su importe exacto | ● |
| 2 | Anotar temperatura de cámaras | Cocina | Una cifra por cámara. Frío positivo 0-4 °C · congelación ≤ −18 °C. Fuera de rango: abre incidencia numerada | ● |
| 3 | Registrar merma del día | Cocina | Producto perdido anotado con cantidad y motivo. Tirarlo sin anotarlo no cuenta | |
| 4 | Limpieza de línea caliente y fría | Cocina | Superficies y equipos del listado del local; lo pendiente se anota, no se deja | |
| 5 | Dejar lista de reposición para el día siguiente | Cocina | Pedido enviado o lista visible en puerta de cámara antes de salir | |
| 6 | Recoger sala y prepararla para el montaje siguiente | Sala | Mesas limpias, mantelería recogida, nada de la última mesa sin retirar | |
| 7 | Apagar y desconectar equipos según su orden | Cocina | Lista de equipos recorrida; los que quedan encendidos por diseño (cámaras) anotados aparte | |
| 8 | Completar el parte de incidencias del día | Encargado | Todas las incidencias anotadas antes de salir. Ninguna "se cuenta mañana de palabra" | ● |
| 9 | Asegurar puertas y accesos | Encargado | Verificación física puerta por puerta, no "se cerró" | ● |
| 10 | Última pasada de basura y residuos a su punto | Sala/Cocina | Contenedores fuera y zona de residuos sin bolsa abierta dentro del local | |

**Horarios:** el bloque sale encabezado como
`## Cierre ([hora local] – [hora local])`. **No se inventa "23:30".** Un horario
falso en un documento operativo se copia y se usa por error.

### Línea final de la entrega, literal

> **Asumido:** restaurante de mesa y mantel de tamaño medio, sin datos de
> horario, plantilla ni puntos de fricción. Los responsables van por puesto
> genérico (sala / cocina / encargado). Rellena las horas entre corchetes y
> dime dos cosas que se os olviden siempre al cerrar: con eso la lista pasa de
> genérica a vuestra en un minuto.

## Por qué es el caso decisivo

Dos cosas se juegan aquí a la vez, y la mayoría de los generadores fallan una:

1. **No se rinde.** Diez tareas ejecutables hoy, con criterio de terminación
   verificable en cada una.
2. **No inventa donde no sabe.** Las horas quedan en `[hora local]`. Un horario
   de ejemplo presentado como real es peor que un hueco, porque el hueco se ve
   y el número falso no.

Y la última línea no pide "todos los datos": pide **dos**. Es la petición que un
dueño cansado sí contesta, y es la que convierte la plantilla genérica en el
producto por el que paga.
