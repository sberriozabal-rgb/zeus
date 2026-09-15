# Caso 1 · Happy path

## Encargo real que escribiría un dueño

> "Somos un restaurante de mesa y mantel en Valencia, 42 cubiertos. Abrimos a las
> 13:00 y cerramos a las 23:30, con turno partido: mañana entra a las 11:00 y sale
> a las 16:30, tarde entra a las 19:00. Somos 3 en sala, 3 en cocina y yo, que soy
> el encargado. Lo que siempre se nos olvida es mirar que la cámara del pescado
> esté a temperatura antes de sacar género, y el cambio de turno es un desastre:
> el de tarde nunca se entera de lo que pasó a mediodía."

## Entrada

| Dato | Valor aportado | Estado |
|---|---|---|
| Tipo de local | Restaurante de mesa y mantel, 42 cubiertos | CONFIRMADO |
| Horario | Apertura 13:00 · cierre 23:30 · turno partido 11:00-16:30 / 19:00-cierre | CONFIRMADO |
| Plantilla por puesto | 3 sala · 3 cocina · 1 encargado | CONFIRMADO |
| Puntos de fricción | (a) temperatura de cámara de pescado sin verificar · (b) traspaso de turno sin información | CONFIRMADO |
| País de operación | España | CONFIRMADO |

Ningún dato falta. Es el camino esperado en una instalación con el dueño delante.

## Salida esperada — completa

Plantilla seleccionada: **nº2, restaurante de mesa y mantel** (`references/plantillas-por-tipo.md`),
sin combinación. Los tres bloques salen con hora real, no con `[hora local]`.

### Apertura (11:00 – 13:00)

| # | Tarea | Responsable | Criterio de "hecho" | Crítico |
|---|---|---|---|---|
| 1 | Leer el parte de incidencias del cierre anterior | Encargado | Firmado como leído antes de cualquier otra tarea | ● |
| 2 | Anotar temperatura de las tres cámaras (pescado, carne, congelación) | Cocina | Tres cifras anotadas en el registro. Frío positivo 0-4 °C; congelación ≤ −18 °C. **Si la de pescado supera 4 °C, no se saca género y se avisa al encargado antes de continuar** | ● |
| 3 | Cotejar albarán del género recibido contra pedido | Cocina | Albarán firmado; toda discrepancia anotada con cantidad, no "faltaba algo" | ● |
| 4 | Contar fondo de caja | Encargado | Importe anotado y coincide con el cierre anterior; descuadre registrado con su cifra exacta | ● |
| 5 | Mise en place por partida (frío, caliente, postres) | Cocina | Cada partida con su lista de producto preparado visible, sin faltantes sin anotar | |
| 6 | Montaje de las 42 plazas de sala | Sala | Todas las mesas del turno montadas antes de las 12:45 | |
| 7 | Revisar reservas del día | Sala | Lista visible con alergias y peticiones especiales marcadas en rojo | ● |
| 8 | Revisar carta contra agotados | Sala + Cocina | Cada plato de carta disponible o marcado como 86 antes de abrir puertas | |
| 9 | Encender TPV y comprobar impresora de comandas | Encargado | Comanda de prueba impresa en cocina | |
| 10 | Personal de apertura presente y uniformado | Encargado | Presentes cotejados contra cuadrante del turno | |

10 tareas: dentro del rango de 12-20 declarado para esta plantilla — por debajo,
porque el local tiene una sola sala y no hay delivery. No se rellena hasta 12
con tareas de adorno.

### Cambio de turno (16:30)

| # | Tarea | Resp. (sale) | Resp. (entra) | Criterio de "hecho" |
|---|---|---|---|---|
| 1 | Traspasar y firmar el parte de incidencias del turno de mañana | Encargado | Encargado | Firma de quien entra, **antes** de que salga quien sale. No se deja sobre la barra |
| 2 | Anotar stock restante de los 3 productos de mayor rotación | Cocina | Cocina | Tres cifras anotadas, no "queda poco" |
| 3 | Contar caja intermedia | Encargado | Encargado | Cifra anotada y coincide con ventas del TPV hasta las 16:30 |
| 4 | Comunicar mesas abiertas o incidencias de sala | Sala | Sala | Verbal **y** anotado en el parte si queda algo abierto |
| 5 | Revisar reservas restantes de la noche | Sala | Sala | Lista actualizada con las de mediodía tachadas |
| 6 | Anotar temperatura de cámara de pescado | Cocina | Cocina | Cifra anotada. Es el punto de fricción declarado: se verifica dos veces al día, no una |

6 tareas: mínimo del rango 6-10. El punto de fricción (b) del cliente queda
resuelto por las tareas 1 y 4, que son las únicas que convierten "el de tarde no
se entera" en una firma que alguien tiene que estampar.

### Cierre (23:30 – 00:30)

| # | Tarea | Responsable | Criterio de "hecho" | Crítico |
|---|---|---|---|---|
| 1 | Arqueo de caja final | Encargado | Cifra de cierre anotada; descuadre registrado con importe exacto, aunque sea de 2 € | ● |
| 2 | Anotar temperatura de las tres cámaras al cierre | Cocina | Tres cifras anotadas; fuera de rango abre incidencia con número | ● |
| 3 | Registrar merma del día | Cocina | Producto perdido anotado con cantidad y motivo. Tirar sin anotar cuenta como tarea no hecha | |
| 4 | Limpieza de línea caliente y fría | Cocina | Superficies y equipos según el listado del local; pendientes anotados en el parte | |
| 5 | Dejar lista de reposición para mañana | Cocina + Encargado | Pedido enviado o lista visible en la puerta de cámara | |
| 6 | Recoger sala y dejarla lista para el montaje siguiente | Sala | Mesas limpias, mantelería recogida, nada de la última mesa servida sin retirar | |
| 7 | Completar el parte de incidencias del día | Encargado | Todas las incidencias anotadas antes de salir. Ninguna "se cuenta mañana de palabra" | ● |
| 8 | Asegurar puertas y accesos | Encargado | Verificación física puerta por puerta, no "se cerró" | ● |

### Parte de incidencias

Se entrega la plantilla de `assets/plantilla-parte-incidencias.md`, en blanco,
con las tres primeras filas rellenas como ejemplo de redacción.

### Supuestos de esta versión

- Ninguno. El cliente aportó los cuatro bloques de entrada.
- Rango de frío positivo 0-4 °C: criterio de oficio conservador, no máximo legal
  (ver `references/FUENTES.md`, fuente 4). En España rige la temperatura del
  fabricante o la específica del producto.

## Por qué es el caso central

Es el flujo con los cuatro bloques de entrada completos y dos puntos de fricción
reales del cliente. Demuestra lo único que un modelo genérico no hace: convertir
"siempre se nos olvida mirar la cámara" en una tarea numerada, con responsable
por puesto, cifra de corte y una instrucción de qué hacer cuando la cifra se
pasa — dos veces al día, porque el cliente dijo que se le olvida.
