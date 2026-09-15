# Caso 2 · Edge case

## Encargo real que escribiría un dueño

> "Somos dos. Mi mujer y yo. Tenemos un bar con cocina en Puebla, abrimos de
> 8 de la mañana a 6 de la tarde de corrido y hacemos de todo los dos: yo cocino
> y saco, ella cobra y atiende, y cuando entra gente cocinamos los dos. No hay
> turnos. ¿Me sirve esto de todos modos?"

## Entrada

| Dato | Valor aportado | Estado |
|---|---|---|
| Tipo de local | Bar con cocina limitada | CONFIRMADO |
| Horario | 08:00 – 18:00, jornada corrida, **sin cambio de turno** | CONFIRMADO |
| Plantilla por puesto | 2 personas sin separación de puesto | CONFIRMADO — y rompe el modelo |
| Puntos de fricción | Ninguno declarado | FALTA |
| País de operación | México | CONFIRMADO |

**Lo que hace raro este caso:** la skill está construida sobre "un responsable
por puesto y por tarea", y aquí no hay puestos. Un motor ingenuo haría una de
dos cosas malas: forzar la plantilla sala/cocina/encargado sobre dos personas
que no la tienen (documento que el cliente descarta en la primera lectura), o
declarar que la skill no aplica y devolver el encargo.

## Salida esperada — completa

Plantilla seleccionada: **nº1, bar / barra con cocina limitada**. Bloque de
cambio de turno: **suprimido, no vaciado.**

### Lo que la skill hace y hay que ver en la salida

1. **No fuerza los puestos.** La columna "Responsable" se sustituye por
   **"Quién"** con dos valores reales del local: `Cocina (él)` y `Barra (ella)`,
   asignados una sola vez al inicio y no por tarea. Donde una tarea puede hacerla
   cualquiera, pone `El primero que llega` — que en un local de dos personas es
   un responsable perfectamente identificable, no una ambigüedad.
2. **Suprime el bloque de cambio de turno y lo dice.** No entrega una tabla
   vacía con un guion. Entrega en su lugar un bloque nuevo de **cierre parcial de
   media jornada** con dos tareas: temperatura de cámara a mitad de servicio y
   arqueo intermedio de caja. Razón declarada en la entrega: en una jornada
   corrida de 10 horas, el momento de mayor riesgo de temperatura y de descuadre
   no está en la apertura ni en el cierre, está en el medio, y sin cambio de
   turno nadie lo mira.
3. **Recorta la longitud.** Apertura 8 tareas, cierre 7 (rangos de plantilla nº1:
   8-12). Con dos personas y diez horas seguidas, una lista de 15 puntos no se
   ejecuta.
4. **Ajusta la cifra de temperatura al país.** El criterio de "hecho" de cámara
   sale con el máximo mexicano: **7 °C (NOM-251-SSA1-2009, §5.5.2)**, no con el
   0-4 °C de oficio por defecto, y lo cita. Un dueño en Puebla defiende una cifra
   ante verificación con la norma que le aplica, no con la de otro continente.

### Bloque nuevo — cierre parcial de media jornada (13:00)

| # | Tarea | Quién | Criterio de "hecho" |
|---|---|---|---|
| 1 | Anotar temperatura de cámara y vitrina | Cocina (él) | Cifra anotada. Máximo 7 °C en refrigeración (NOM-251, §5.5.2). Por encima: se retira el producto de riesgo antes de seguir vendiendo |
| 2 | Arqueo intermedio de caja | Barra (ella) | Cifra anotada y cotejada contra ventas registradas hasta esa hora |

### Supuestos declarados en la entrega

- Puntos de fricción: no aportados. Se usan los de la plantilla base de bar
  (café, cámara de bebidas, arqueo), sin inventar ninguno específico del local.
- Reparto Cocina/Barra: tomado literalmente de la frase del cliente. Si en la
  práctica se cruzan, se cambia a `El primero que llega` sin tocar el criterio
  de "hecho", que es lo que no se negocia.

## Por qué importa

Es el caso que separa una plantilla rellenable de un producto con criterio. La
tentación es entregar la estructura de tres bloques porque es la que la skill
tiene escrita. Lo que hace aquí es **quitar** un bloque que no existe en ese
local y **añadir** uno que sí hace falta, explicando por qué — y regionalizar la
única cifra que el cliente podría tener que defender ante un inspector.

Misma disciplina que `respuesta-resenas` aplica cuando faltan fechas: cuando el
dato real del cliente contradice el modelo de la skill, manda el dato del
cliente y se declara el cambio. El modelo no se le impone al local.
