# Caso de prueba · Failure — encargo de una línea sin contexto

**Activo:** `productividad-personal-turno` v1.1.0  
**Línea:** hosteleria  
**Para qué sirve este caso:** La prueba dura: una sola frase, sin datos, sin sector, sin cifras.

---

## El encargo y lo que debe salir

**Failure (encargo de una línea sin contexto)**: "dime si me sobra gente". → No se rinde ni pide todos los datos antes de producir. Entrega la plantilla de recogida (`assets/plantilla-turnos.csv`), el método de las tres cifras, la tabla de lectura por franja y el factor de coste hora del país, con un ejemplo numérico marcado como ilustrativo, y cierra con la única pregunta bloqueante: "pásame ventas por franja y horas del mismo periodo, aunque sean cuatro semanas a mano, y te lo calculo". Ver `cases/case_03_failure.md`.

---

## Qué se comprueba al ejecutarlo

Que NO se rinda ni pida todos los datos antes de producir. Debe entregar el producto parcial con los valores por defecto más defendibles, marcar los huecos entre corchetes y cerrar declarando en una línea qué se asumió.

## Criterio de paso

El caso pasa si un desconocido del oficio puede leer la salida y ejecutarla sin preguntar nada al autor, y si ninguna cifra de la salida carece de fuente nombrada o de la marca `[A VALIDAR]`. Si falla cualquiera de las dos condiciones, el activo no sale de la fábrica: vuelve a BORRADOR y se corrige la sección que originó el fallo, no el caso.
