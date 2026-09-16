# comparativa-proveedores

Skill de FORJA (Agent Skills, estándar abierto). Convierte los albaranes y facturas de varios proveedores de un local de hostelería en la alerta de subidas —qué producto subió, cuánto, desde cuándo y quién lo tiene hoy más barato— y en el impacto de esas subidas sobre el margen de los platos de la carta, cerrado en tres o cuatro acciones de compra con su euro anual al lado.

## Instalación

Copia esta carpeta completa (o el archivo `.skill` empaquetado) en el directorio de skills del agente que la va a ejecutar, o desde el paquete entregado en la instalación contratada.

## Estructura

```
comparativa-proveedores/
├── SKILL.md                       — método completo, reglas, antipatrones, casos
├── README.md                      — este archivo
├── metadata.json                  — metadatos de empaque
├── CHANGELOG.md                   — historial de versiones
├── LICENSE.txt                    — licencia de uso comercial
├── ANEXO-A-ficha-comercial.md     — a quién se vende y a qué precio
├── references/
│   ├── FUENTES.md                 — cada cifra con URL, límite de uso y huecos declarados
│   └── familias-y-volatilidad.md  — volatilidad por familia, formatos, IVA, trucos, umbrales
├── assets/
│   └── plantilla-informe.md       — el informe de control de compras en 7 apartados
├── scripts/
│   └── proveedores.py             — motor determinista, con --ejemplo y --autotest
└── cases/
    ├── case_01_happy_path.md
    ├── case_02_edge_case.md
    ├── case_03_failure.md
    └── case_04_integration.md
```

## Uso

```bash
python3 scripts/proveedores.py --ejemplo      # formato de entrada
python3 scripts/proveedores.py datos.json     # análisis completo
python3 scripts/proveedores.py --autotest     # comprobación aritmética
```

## Verificar antes de entregar a un cliente

```bash
python3 scripts/proveedores.py --autotest
```

Debe imprimir **"AUTOTEST OK — 6 comprobaciones aritméticas pasadas"**. Si no, no se entrega.

Las dos primeras comprobaciones son las que impiden el error de compras más caro: la nº 1 verifica que una garrafa de 5 L a 42,50 € se lee como **8,50 €/L** —más barata que el litro suelto a 8,90 €, aunque el número grande asuste— y la nº 2, que un precio de 11,00 € con 10% de IVA incluido se compara como **10,00 €** de base imponible. Sin esas dos capas, la recomendación de compra sale invertida.

## Lo que hay que revisar a mano, siempre

El motor no ve tres cosas que cambian qué proveedor es más barato de verdad: **portes** que aparecen en unas facturas y no en otras, **precio pactado** que se olvida de aplicarse en algunas líneas, y **mínimo de pedido** que obliga a comprar más de lo que se gasta antes de que caduque. Están en `references/familias-y-volatilidad.md` §4 y se revisan en el paso 7 del procedimiento.

## Lo que esta skill NO hace

No renegocia por el cliente, no pide ofertas, no cambia pedidos en ningún sistema, no detecta fraude ni lo afirma, y no calcula el escandallo de un plato desde cero (eso es `escandallo-ingenieria-menu`). Tampoco decide de proveedor: el precio por kilo no incluye calidad, calibre, plazo, servicio ni crédito comercial. Ver la sección "Límites" de `SKILL.md`.

## Soporte

Parte del sistema instalable de 6 skills de hostelería (Motor B). No se vende suelta salvo decisión explícita de Sergio.
