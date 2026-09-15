# Temperaturas mínimas de seguridad — puntos críticos de control

**Toda cifra de esta tabla está anclada a una norma o a un informe oficial de la
autoridad competente del país, con su número de apartado o de informe.** Las
cifras que no se pueden anclar no están aquí: están en la lista del final,
marcadas `[A VALIDAR]`.

Cambio respecto de la v1.0.0 de esta skill: la versión anterior tomaba las
temperaturas de un blog comercial que a su vez citaba a la Food Standards Agency
británica. Se ha sustituido por las dos fuentes oficiales de los mercados donde
opera la casa — **España (AESAN) y México (NOM-251)** —, que **no coinciden entre
sí** en varias categorías. Usar la cifra del país equivocado es exactamente el
fallo que hace que una ficha no sirva ante una inspección.

Fuentes completas con URL: `FUENTES.md`.

---

## Tabla A · España — informe AESAN-2021-004

Informe del Comité Científico de la Agencia Española de Seguridad Alimentaria y
Nutrición sobre combinaciones tiempo-temperatura para el cocinado seguro de los
alimentos, aprobado el 17-feb-2021.

| Categoría | Temperatura interna mínima | Tiempo mínimo a esa temperatura |
|---|---|---|
| Carne (no ave) | **70 °C** | 1 segundo en el centro del producto |
| Aves | **74 °C** | 1 segundo |
| Pescado | **68 °C** | 15 segundos en el centro |
| Pescado relleno | **74 °C** | 15 segundos |
| Moluscos bivalvos crudos | **90 °C** | 90 segundos en agua hirviendo |
| Platos con huevo, consumo NO inmediato | **70 °C** | 2 segundos |
| Platos con huevo, consumo inmediato | **63 °C** | 20 segundos |
| Vegetales | **70 °C** | 2 minutos en el centro |
| **Mantenimiento en caliente** (AESAN) | **≥63 °C** | mientras dure el servicio — **ver discrepancia con RD 3484/2000 abajo** |
| **Recalentamiento** | **≥74 °C** | 15 segundos en el centro |

### Tabla A-bis · España — Real Decreto 3484/2000, artículo 7 (norma reglamentaria)

Conservación y servicio de comidas preparadas. Es la norma que aplica la inspección; AESAN
es opinión científica. Fuente 7 de `FUENTES.md`.

| Comida preparada | Temperatura |
|---|---|
| Congelada | **≤ −18 °C** |
| Refrigerada, duración **< 24 h** | **≤ 8 °C** |
| Refrigerada, duración **> 24 h** | **≤ 4 °C** |
| **Caliente** | **≥ 65 °C** |

El RD **no** regula temperaturas de cocinado: para eso sigue valiendo AESAN.

AESAN expresa siempre **binomio tiempo-temperatura**, no solo la temperatura. Una
ficha que dice "74 °C" sin el tiempo está incompleta según esta fuente, aunque el
número de grados coincida.

## Tabla B · México — NOM-251-SSA1-2009

Norma Oficial Mexicana de prácticas de higiene para el proceso de alimentos,
bebidas o suplementos alimenticios, publicada en el DOF.

| Categoría | Temperatura | Apartado |
|---|---|---|
| Pescado · trozos de res · huevo con cascarón roto | **63 °C** (145 °F) | §7.3.1 |
| Cerdo en trozo · carnes molidas · carnes inyectadas · huevo roto para buffet | **68 °C** (154 °F) | §7.3.1 |
| Aves · emulsiones de pescado · alimentos rellenos | **74 °C** (165 °F) | §7.3.1 |
| Recalentamiento | **≥74 °C** (165 °F) | §7.3.2 |
| Mantenimiento en caliente | **>60 °C** (140 °F) | §7.3.3 |
| Mantenimiento en frío | **≤7 °C** (45 °F) | §7.3.3 |
| Equipos de refrigeración | **máximo 7 °C** | §5.5.2 |
| Recepción de pescados y mariscos frescos | **máximo 4 °C** | §7.4.2 |
| Recepción de pescados y mariscos congelados | **máximo 9 °C** | §7.4.2 |
| Recepción de producto vivo | **7 °C** | §7.4.2 |

## Dónde discrepan las dos tablas — mirar antes de escribir una ficha

Es la parte que un generador genérico no da, y la razón por la que la tabla está
partida en dos y no promediada:

| Categoría | España (AESAN) | México (NOM-251) | Consecuencia práctica |
|---|---|---|---|
| Pescado en trozo | 68 °C / 15 s | 63 °C | Una ficha de merluza escrita para Madrid queda 5 °C por encima de lo exigido en Monterrey. Cocinar de más no es ilegal, pero es un pescado peor: si la ficha viaja, se reescribe el binomio, no se copia |
| Carne (molida / trozo) | 70 °C / 1 s (carne, genérico) | 68 °C molida · 63 °C trozo de res | Cifras cercanas, categorías distintas. La defendible ante inspección es la del país de operación |
| Mantenimiento en caliente | ≥63 °C (AESAN) · **≥65 °C (RD 3484/2000)** | >60 °C | Dentro de España, el informe AESAN y el Real Decreto no coinciden: **prevalece el RD, que es la norma reglamentaria**. Las fichas españolas usan ≥65 °C desde la v1.1.1 |
| Conservación en frío | ≤8 °C si <24 h · ≤4 °C si >24 h (RD 3484/2000 art. 7) | ≤7 °C conservación (§7.3.3) · ≤4 °C recepción de pescado fresco (§7.4.2) | **El 4 °C significa cosas distintas en cada país**: en España es conservación de más de 24 h; en México es recepción de pescado. Una ficha que ponga "≤4 °C" sin decir cuál de las dos es, no sirve en ninguno de los dos |

**Regla de la casa:** una ficha declara **el país de operación en la cabecera** y
usa la tabla de ese país. Una ficha sin país declarado no pasa de BORRADOR. No se
promedian las dos normas ni se toma "la más alta por si acaso" en silencio: si se
opta deliberadamente por el criterio más estricto, se escribe por qué.

---

## Reglas de uso de estas tablas

1. **Ningún punto crítico se cierra con verificación visual.** Termómetro de
   sonda en la parte más gruesa, sin tocar hueso. Si no hay sonda en el puesto,
   la ficha lo declara como **carencia de equipo**, no como "verificado al ojo"
   disfrazado de cumplido.
2. **El tiempo forma parte del umbral.** AESAN expresa binomios. Una ficha
   española que solo copia los grados está a medias.
3. **Categorías fuera de estas tablas** (caza, embutidos artesanales, conservas,
   fermentados, sous-vide a baja temperatura, cocciones prolongadas por debajo de
   estos umbrales) se marcan
   `[A VALIDAR — CONSULTAR AUTORIDAD SANITARIA LOCAL]`. **No se extrapola por
   analogía desde estas tablas.** El sous-vide en particular trabaja con binomios
   largos que no aparecen en ninguna de las dos fuentes y que exigen validación
   específica documentada del establecimiento.
4. **Otros países.** Estas dos tablas cubren España y México. Para cualquier otro
   mercado la cifra sale de la autoridad local (FDA Food Code en EE. UU.,
   INAL/SENASA en Argentina, ANVISA en Brasil) y hasta entonces la ficha lleva
   `[A VALIDAR]`. El marco internacional de referencia es el Codex Alimentarius
   CXC 1-1969 *General Principles of Food Hygiene*, rev. 2020, que fija los
   principios APPCC pero **no** una tabla universal de temperaturas de cocinado:
   no sirve para rellenar un hueco de esta tabla.

## Cifras usadas por esta skill que NO están normadas

- **Tolerancia de porción ±10 %** sobre peso de plato servido: criterio de oficio,
  valor por defecto de la casa. `[A VALIDAR]` — no procede de ninguna norma ni
  estudio publicado. Se declara como tal en cada ficha.
- **Umbral "más de 4 de los 10 campos faltantes → no pasa de BORRADOR"**:
  criterio de oficio de la casa. `[A VALIDAR]`.
- **20-40 minutos por receta**: estimación de tiempo de trabajo procedente de una
  fuente sectorial única (ProChefDesk, ver `FUENTES.md`), no medida por la casa.
  `[A VALIDAR]`.
- **~25 % de costes indirectos sobre coste de ingredientes**: práctica sectorial
  de una sola fuente. `[A VALIDAR]`. Y además **no es trabajo de esta skill**: el
  coste lo calcula `escandallo-ingenieria-menu` con la estructura real del
  negocio, no una regla de tres sectorial.
