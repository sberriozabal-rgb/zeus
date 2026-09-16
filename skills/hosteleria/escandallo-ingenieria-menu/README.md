# escandallo-ingenieria-menu

Skill de la línea Hostelería (Agent Skills, estándar abierto). Calcula el escandallo real de
una carta —con rendimiento de limpieza, merma de cocción y los costes que nadie imputa— y
clasifica cada plato en la matriz de Kasavana-Smith para decir qué proteger, qué abaratar,
qué reposicionar y qué retirar. Cierra en euros al año.

## Instalación

Copia esta carpeta completa (o el archivo `.skill` empaquetado) en el directorio de skills
del agente que la va a ejecutar, o instálala desde el repositorio privado si el cliente
tiene acceso de suscripción vigente.

Requiere Python 3.9 o superior. Sin dependencias externas.

## Estructura

```
escandallo-ingenieria-menu/
├── SKILL.md                          — método completo, reglas, antipatrones, casos
├── README.md                         — este archivo
├── metadata.json                     — metadatos de empaque
├── CHANGELOG.md                      — historial de versiones
├── LICENSE.txt                       — licencia de uso comercial
├── ANEXO-A-ficha-comercial.md        — a quién se vende y a qué precio
├── assets/
│   └── plantilla-datos.json          — carta de prueba, 9 platos, formato de entrada
├── references/
│   ├── rendimientos-y-umbrales.md    — rendimientos, mermas, umbrales, señales de alarma
│   └── FUENTES.md                    — fuentes externas verificadas y lo que queda [A VALIDAR]
├── scripts/
│   └── escandallo.py                 — motor de cálculo determinista
└── cases/
    ├── case_01_happy_path.md         — carta completa con inventarios
    ├── case_02_edge_case.md          — sin rendimientos, sin inventarios, datos sucios
    ├── case_03_failure.md            — "¿cuánto me cuesta el arroz?", una línea
    └── case_04_integration.md        — encadenado con comparativa-proveedores
```

## Verificar antes de entregar a un cliente

```bash
python3 scripts/escandallo.py assets/plantilla-datos.json
```

Debe devolver, sobre la carta de prueba: food cost teórico **32,35%**, real **36,20%**,
desviación **3,85 puntos**, y la merluza a la plancha en **30,4%** de food cost. Si alguno
de esos cuatro números no sale, algo se ha tocado en el motor y no se entrega.

Otras opciones del script:

```bash
python3 scripts/escandallo.py --ejemplo             # imprime un JSON de entrada válido
python3 scripts/escandallo.py datos.json --json out.json
python3 scripts/escandallo.py datos.json --csv tabla.csv
```

## Lo que hay que decirle al cliente antes de empezar

1. **Sin inventarios no hay desviación.** El informe sale igual, pero abre con "análisis sin
   contraste" y no puede afirmar si el problema es de carta o de control.
2. **Los rendimientos de esta cocina mandan.** Los de `references/` son orientativos y
   cualquier plato calculado con ellos sale marcado como estimado.
3. **El reparto a domicilio se analiza aparte.** La comisión de plataforma convierte en
   pérdida platos que en sala son rentables.

## Soporte

Pieza 1 de 7 del sistema instalable de hostelería (Motor B). No se vende suelta salvo
decisión explícita de Sergio. Ver `ANEXO-A-ficha-comercial.md`.
