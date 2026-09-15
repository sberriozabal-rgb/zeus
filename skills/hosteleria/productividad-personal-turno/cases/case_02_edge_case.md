# Caso de prueba · Edge case

**Activo:** `productividad-personal-turno` v1.1.0  
**Línea:** hosteleria  
**Para qué sirve este caso:** El límite del perímetro: un encargo real que la plantilla base no cubre tal cual.

---

## El encargo y lo que debe salir

**Edge case**: local de dos personas con turno partido, sin fichajes digitales y con las horas dictadas de memoria, sin comensales por franja y con dos semanas de obras dentro del periodo. → No se fuerza la plantilla: se calcula con las horas declaradas, se excluyen los días de obra del cálculo y se listan aparte, se omite la columna de venta por comensal advirtiendo qué conclusión no se puede sacar sin ella, y se propone únicamente escalonar la entrada del segundo turno porque con mínimo de seguridad de dos personas no hay más margen. Ver `cases/case_02_edge_case.md`.

---

## Qué se comprueba al ejecutarlo

Que la skill NO fuerce la plantilla base sobre un caso que no encaja, que diga con qué palabras no aplica, y que entregue igualmente la parte que sí es ejecutable.

## Criterio de paso

El caso pasa si un desconocido del oficio puede leer la salida y ejecutarla sin preguntar nada al autor, y si ninguna cifra de la salida carece de fuente nombrada o de la marca `[A VALIDAR]`. Si falla cualquiera de las dos condiciones, el activo no sale de la fábrica: vuelve a BORRADOR y se corrige la sección que originó el fallo, no el caso.
