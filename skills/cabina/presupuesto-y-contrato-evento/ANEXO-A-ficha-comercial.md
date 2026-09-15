# Anexo A — Ficha comercial

| Campo | Valor |
|---|---|
| Nombre técnico | `presupuesto-y-contrato-evento` |
| Nombre comercial | Presupuesto y contrato de evento |
| Peldaño | P1 · SKILL |
| Línea / Paquete | CABINA · **CABINA EVENTOS** |
| Comprador nombrado | DJ móvil y de eventos que cierra condiciones por su cuenta, sin manager ni agencia, en España o México. Decide y paga el propio DJ. |
| Quien NO es comprador | El DJ con agencia que le pasa el contrato hecho, y quien busque asesoramiento jurídico: **esta skill no lo es y lo declara.** |
| Trabajo que quita | Improvisar el presupuesto por WhatsApp y descubrir después que faltaba la cláusula de cancelación, la de horas extra o la de potencia eléctrica. |
| Umbral que aporta | Las **seis cláusulas críticas** —depósito, cancelación, horas extra, potencia eléctrica, superficie, comida de proveedor y limitador de sonido— clasificadas por nivel: CRÍTICA es aquella sin la cual el DJ asume una pérdida real y previsible. Más los baremos de mercado con fuente: media nacional 350–500 €, boda completa 400–1.500 €, **escalón medio real 1.000–1.500 €**, hora extra 75–250 €, y el contexto de que 1.200 € sobre una boda de 25.183 € es menos del 5 % del presupuesto. |
| Límite declarado | **No es asesoramiento jurídico** y lleva aviso legal no negociable. Los baremos son contexto de mercado para saber si estás fuera de precio, no una tarifa: el precio lo decide el DJ según su coste, su agenda y su posicionamiento. Regla dura: no aplicar el baremo de un país a otro. |
| Precio propuesto | **49 €** pago único |
| Razón del precio | Es la pieza que más dinero protege del catálogo y la que más arriba podría ir del tramo. Se mantiene en 49 € por coherencia de la línea: **una sola cancelación sin cláusula de depósito cuesta entre 1.000 y 1.500 €**, y una hora extra recuperada (75–250 €) ya paga la skill varias veces. |
| Canal | Polar · catálogo (Motor A). Entrega por acceso revocable a repositorio privado. |
| Motor | A · Catálogo |
| Frase de anuncio | «Las seis cláusulas que se pagan cuando faltan, y el presupuesto desglosado para que negociar no sea bajar el margen.» |
| Estado / Versión | ACORDADO / v1.0.0 |
| Auditoría | **1/20** contra la rúbrica de 20 puntos de la casa (`validar_skill.py`, 15-sep-2026). Faltan: cases/ (4 casos), CHANGELOG.md, tabla de reglas NUNCA, 5 antipatrones. La nota se declara sin redondear: **por debajo de 16 no se vende**. |
| Gates | G1 [ ] G2 [ ] G3 [x] G4 [x] G5 [ ] |

## Notas de gates

- **G1 (producto)** **NO levantado**: 1/20 frente al 16/20 que exige el peldaño P1. Es el bloqueo real de esta pieza: el precio está cerrado pero el producto no pasa todavía la rúbrica de la casa.
- **G3 (precio)** levantado el 15-sep-2026 por instrucción del dueño. Cifra cerrada: 49 €.
- **G2 (prueba)** pendiente.
- **G4 (legal)** es el gate delicado de esta pieza y está en orden: el aviso legal de que no es asesoramiento jurídico es no negociable y va en la propia skill, además de en la licencia. Los baremos citan fuente (Cronoshare, Fixando, coste medio de boda con tamaño de muestra).
- **G5 (público)** pendiente. Al publicar, la cifra de baremo debe ir siempre con su fuente y su límite de país: el precedente de la casa es la frase retirada de `respuesta-resenas` por afirmar una política que ninguna plataforma publicaba.
