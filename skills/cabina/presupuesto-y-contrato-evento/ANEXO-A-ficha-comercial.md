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
| Canal | Gumroad · catálogo (Motor A). Entrega por descarga (`venta/GUMROAD-ALTA.md`); decisión 8 del 15-sep-2026. |
| Motor | A · Catálogo |
| Frase de anuncio | «Las seis cláusulas que se pagan cuando faltan, y el presupuesto desglosado para que negociar no sea bajar el margen.» |
| Estado / Versión | ACORDADO / v1.1.0 |
| Auditoría | **19/20**. El validador de la casa (`validar_skill.py`, 15-sep-2026) devuelve 20/20 mecánico, frente al **1/20** de la v1.0.0. **No se firma el 20**: el punto 19 exige URLs verificadas, no solo presentes, y en esta pasada no se han reverificado una a una. La casa no redondea al alza. |
| Gates | G1 [x] G2 [ ] G3 [x] G4 [x] G5 [x] |

## Notas de gates

- **G1 (producto)** **levantado** el 15-sep-2026: 19/20 declarado, por encima del 16 que exige P1. Venía de 1/20. Se cerró el envoltorio —13 secciones del ADN, 6 pasos atómicos, 10 reglas SIEMPRE y 9 NUNCA, 5 antipatrones, los 4 casos de prueba, CHANGELOG, README, LICENSE y metadata—. El contenido de oficio ya estaba; faltaba la forma.
- **G3 (precio)** levantado el 15-sep-2026 por instrucción del dueño. Cifra cerrada: 49 €.
- **G2 (prueba)** pendiente.
- **G4 (legal)** es el gate delicado de esta pieza y está en orden: el aviso legal de que no es asesoramiento jurídico es no negociable y va en la propia skill, además de en la licencia. Los baremos citan fuente (Cronoshare, Fixando, coste medio de boda con tamaño de muestra).
- **G5 (público)** pendiente. Al publicar, la cifra de baremo debe ir siempre con su fuente y su límite de país: el precedente de la casa es la frase retirada de `respuesta-resenas` por afirmar una política que ninguna plataforma publicaba.
