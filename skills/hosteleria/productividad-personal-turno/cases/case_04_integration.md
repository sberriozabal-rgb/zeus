# Caso de prueba · Integration — encadenado con otro activo

**Activo:** `productividad-personal-turno` v1.1.0  
**Línea:** hosteleria  
**Para qué sirve este caso:** La prueba de sistema: la salida de otra skill de la casa entra como entrada de esta.

---

## El encargo y lo que debe salir

**Integration (encadenado con otro activo)**: `escandallo-ingenieria-menu` ha dejado el coste de materia prima en el 34% de la venta sin IVA y el dueño pregunta por qué sigue sin ganar dinero. → Esta skill calcula el coste de personal del mismo periodo, suma el prime cost y devuelve el reparto entre las dos partidas; si el personal está dentro de rango y el prime cost sigue disparado, lo dice y devuelve el trabajo a la otra skill en vez de apretar más al equipo. La escalera resultante se cruza con `apertura-cierre-turno` para colocar las tareas fijas de apertura y cierre en las franjas que la escalera deja cubiertas. Ver `cases/case_04_integration.md`.

---

## Qué se comprueba al ejecutarlo

Que NO recalcule lo que la skill anterior ya calculó, que nombre explícitamente el activo con el que encadena, y que respete el umbral que la otra ya fijó en vez de producir uno nuevo que lo contradiga.

## Criterio de paso

El caso pasa si un desconocido del oficio puede leer la salida y ejecutarla sin preguntar nada al autor, y si ninguna cifra de la salida carece de fuente nombrada o de la marca `[A VALIDAR]`. Si falla cualquiera de las dos condiciones, el activo no sale de la fábrica: vuelve a BORRADOR y se corrige la sección que originó el fallo, no el caso.
