# Caso de prueba · Happy path

**Activo:** `productividad-personal-turno` v1.1.0  
**Línea:** hosteleria  
**Para qué sirve este caso:** El camino normal: el cliente aporta los datos que la skill pide y en el formato esperable.

---

## El encargo y lo que debe salir

**Happy path**: export del TPV de 28 días con fecha, franja, ventas sin IVA, horas y comensales; el dueño aporta coste hora total de 14,50 € y explica que de 11:00 a 12:00 se hace producción. → Informe completo: media 48,55 €/hora y 29,9% de coste de personal, cuatro franjas por encima del 40% con 2.927,82 € de exceso en el periodo, la franja de producción etiquetada FIJA y fuera de la propuesta, y una escalera de entradas con las horas recuperadas por franja. Ver `cases/case_01_happy_path.md`.

---

## Qué se comprueba al ejecutarlo

Que la salida use la plantilla exacta de la sección Salida, que toda cifra lleve fuente o [A VALIDAR], y que el informe cierre en la sección 'Supuestos de esta versión' aunque no haya supuestos que declarar.

## Criterio de paso

El caso pasa si un desconocido del oficio puede leer la salida y ejecutarla sin preguntar nada al autor, y si ninguna cifra de la salida carece de fuente nombrada o de la marca `[A VALIDAR]`. Si falla cualquiera de las dos condiciones, el activo no sale de la fábrica: vuelve a BORRADOR y se corrige la sección que originó el fallo, no el caso.
