# PLANTILLAS · respaldo-proyecto-ia-cl v2.0.0

Cinco plantillas. RESTAURAR-TODO.md, RESUMEN-CHATS.md e INDICE-ADJUNTOS.md no están aquí porque los genera `scripts/respaldo.py`; estas son las que se rellenan a mano. Se copian tal cual y se rellenan. Todo lo que va entre `<>` es
un hueco que hay que sustituir; si queda un `<` en el archivo final, el paquete no
está terminado.

---

## 1 · MANIFIESTO.md

```markdown
# RESPALDO · <nombre del proyecto>

**Estado:** COMPLETO | **PARCIAL — <n> elementos declarados en HUECOS.md**
**Origen:** cuenta <alias, no el correo> · plan <Free|Pro|Max|Team|Enterprise>
**Sellado:** <AAAA-MM-DD HH:MM UTC> por <alias>
**Verificado (P7):** <AAAA-MM-DD HH:MM UTC> por <alias> · <PENDIENTE> hasta que se haga
**Paquete:** <nombre>.zip · SHA-256 `<huella>` · cifrado <AES-256|NINGUNO>
**Diccionario de redacción:** <fuera del paquete, entregado por: canal B | no aplica>

## Contenido por capa

| Capa | Carpeta | Elementos | Clase predominante |
|---|---|---|---|
| L1 Instrucciones | 01-instrucciones/ | <n> | <C0-C2> |
| L2 Conocimiento  | 02-conocimiento/  | <n> | <C0-C2> |
| L3 Adjuntos      | 03-adjuntos/      | <n> | <C0-C2> |
| L4 Skills        | 04-skills/        | <n> | <C0-C2> |
| L5 Chats         | 05-chats/         | <n> de <total> | <C0-C2> |

## Inventario

| Archivo | Capa | Clase | Redactado | SHA-256 (8 primeros) |
|---|---|---|---|---|
| <ruta> | L<n> | C<n> | sí/no | <8 chars> |

## Prueba de humo (se redacta AQUÍ, en el origen)

**Pregunta:** <una pregunta que solo se responde bien si el proyecto se reconstruyó>
**Respuesta correcta:** <la respuesta, con el dato exacto que debe aparecer>
**Dónde vive ese dato:** <archivo>

## Declaración

Este respaldo es una copia de reconstrucción manual. **No es una migración
soportada por la plataforma** — Anthropic no admite importar datos entre cuentas
personales. Reconstruir exige seguir RECONSTRUIR.md a mano.
```

---

## 2 · HUECOS.md

```markdown
# HUECOS DECLARADOS · <proyecto> · <fecha>

Total: <n>. **Mientras este archivo no esté vacío, el respaldo se declara PARCIAL.**

| # | Tipo | Nombre | Descripción | Procedencia | Acción y fecha | Marca |
|---|---|---|---|---|---|---|
| 1 | adjunto | <archivo> | <qué era, tamaño aprox> | <quién lo subió, cuándo> | <a quién pedirlo, antes de cuándo> | `[NO EXPORTABLE: <motivo>]` |
| 2 | chat | <título> | <qué decisión contiene> | <fecha> | <resumirlo a mano> | `[CHAT NO INCLUIDO]` |

## Si no hay huecos

> Sin huecos declarados. Las cinco capas viajaron íntegras.
> Comprobado en P5 contra el listado de P1 el <fecha> por <alias>.
```

---

## 3 · RECONSTRUIR.md

```markdown
# RECONSTRUIR · <proyecto>

Para quien abre este paquete en la cuenta destino. No hace falta conocer el origen.

**Antes de empezar:** verifica el paquete.
`python3 scripts/respaldo.py --verificar <paquete>.zip`
Si la huella no coincide con la que te dieron por el canal B, **para y avisa**.

1. **Crear el proyecto.** Nombre: `<nombre>`. Descripción: `<descripción>`.
2. **Pegar L1.** Contenido íntegro de `01-instrucciones/INSTRUCCIONES.md` en el
   campo de instrucciones del proyecto. Pégalo entero y de una vez.
3. **Subir L3 antes que L2.** Los adjuntos primero: si un documento de L2 los
   cita, la referencia ya existe cuando se crea.
4. **Crear L2.** Un documento por archivo de `02-conocimiento/`, respetando el
   nombre exacto. El nombre importa: L1 cita archivos por su nombre.
5. **Instalar L4.** Cada `.skill` de `04-skills/` en la cuenta destino.
6. **Pegar L5.** Solo si los chats de `05-chats/` aportan contexto que no está en
   L2. Normalmente no hace falta.
7. **Deshacer la redacción.** Sustituir cada `[REDACTADO:tipo]` usando
   `DICCIONARIO.md`, **que llega por separado**. Si no lo tienes, el proyecto
   funciona igual con las marcas puestas — solo pierde los nombres propios.
8. **Prueba de humo.** Abre un chat nuevo y haz la pregunta del MANIFIESTO.
   Si la respuesta no contiene el dato esperado, algo de L2 no subió: revisa el
   inventario del MANIFIESTO contra lo que hay en el proyecto.

## Lo que NO se reconstruye, y no es un fallo

- El historial completo de chats del proyecto original.
- Los permisos y miembros, si el origen era Team o Enterprise.
- El comportamiento idéntico: en proyectos grandes la recuperación puede
  seleccionar fragmentos distintos. El contenido es el mismo; la respuesta
  literal puede variar.

## Acta

Reconstruido el <fecha> por <alias>. Prueba de humo: <superada|fallida>.
Huecos que siguen abiertos: <n>.
```

---

## 4 · Cabecera de archivo redactado

Al principio de cualquier archivo tocado en P4:

```markdown
<!-- REDACTADO en P4 el <fecha>. <n> sustituciones.
     Tipos: <cliente, importe, correo…>
     Reversión: DICCIONARIO.md, entregado por canal separado.
     Este archivo es utilizable tal cual; la redacción no altera el método. -->
```

---

## 5 · LECTURA DE UNA PERSONA (por chat, en RESUMEN-CHATS.md)

Sustituye cada `_[pendiente de escribir]_` del borrador por este bloque:

```markdown
**LECTURA DE UNA PERSONA:** <qué se decidió de verdad, en una frase con verbo>.
<Qué quedó abierto, si algo>. <La cifra o el umbral que hay que defender, con su
marca [A VALIDAR] si nadie la firmó>. — <alias>, <AAAA-MM-DD>
```

Regla de paso: si la lectura repite la cita literal del borrador, no es lectura,
es eco. Se escribe lo que la cita significa para el proyecto, no lo que dice.

---

## Nombres de archivo: la regla de una línea

**El nombre de un archivo es un dato.** `03-adjuntos/03-propuesta-cliente-A.pdf`
en lugar de `03-adjuntos/propuesta-Ferretería-Sánchez-450000.pdf`. La
correspondencia va en el MANIFIESTO, que viaja dentro del cifrado; el nombre no.
Ver antipatrón 2 y `references/fuentes.md` B4.
