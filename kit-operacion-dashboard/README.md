# Tablero del Kit de operación

Complemento web del archivo `Kit_de_operacion.xlsx` del libro *Historia de la hostelería y la
gastronomía*, de Sergio Berriozábal Serrano. El Excel es donde metes tus números; esta página es
donde los ves: en diez segundos sabes si tu semana va bien o mal y qué mejora toca instalar después.

## Cómo abrirlo

- **En tu computadora:** haz doble clic en `index.html`. Se abre en el navegador.
- **En internet:** publica esta carpeta en GitHub Pages (Settings → Pages → rama y carpeta). No hay
  que tocar nada: es una sola página estática, sin servidor, sin base de datos y sin cuentas.

La primera vez verás el **restaurante de referencia** del capítulo 19, marcado con la etiqueta
«Ejemplo», para que veas la aritmética funcionando antes de poner la tuya.

## Cómo cargar tu Excel

1. Llena las celdas azules de tu `Kit_de_operacion.xlsx` y guárdalo.
2. En la página, pulsa **Cargar mi Excel** y elige el archivo.
3. La etiqueta «Ejemplo» desaparece y en la cabecera salen el nombre del archivo y la hora de carga.

El archivo **nunca sale de tu computadora**: se lee dentro del navegador. La última carga se queda
guardada en ese navegador, así que al volver a abrir la página sigue ahí, también sin internet.
«Volver al ejemplo» borra lo guardado y regresa al restaurante de referencia.

El nombre del restaurante se cambia haciendo clic sobre él. Las casillas de los doce quick wins
también se guardan en el navegador.

## Qué lee del Excel

Lee solo los datos que escribes tú (las celdas azules) y recalcula todo con las mismas fórmulas del
kit, así que no importa si el Excel se recalculó o no. Las tablas se localizan por el texto de sus
encabezados: puedes añadir filas. Se ignoran las filas vacías y las de «Total».

| Pestaña | Lo que usa |
| --- | --- |
| `01 Diez referencias` | Artículo, inventario inicial, compras, inventario final, unidades vendidas, porción, costo unitario |
| `03 Ingeniería de menú` | Plato, unidades 90 días, precio, costo |
| `04 Estado de resultados` | Las ocho entradas de la columna B (filas 5 a 12); los costos pueden ir en % de su venta o en pesos |
| `05 Los cinco números` | Una fila por semana: ventas, costos, nómina, merma, compras, comensales |
| `06 Control de barra` | Producto, contenido, servicio, envases abiertos, servicios vendidos, precio de venta |
| `07 Tiempo del pase` | Franja, plato, hora de comanda, hora de salida |
| `10 Reservas y no-show` | Objetivo de no-show, y por mes: reservas, no-shows, personas por reserva, ticket |

Si una pestaña falta o está vacía, esa sección dice «Sin datos en esta pestaña del Excel» y el resto
sigue funcionando.

## Archivos

- `index.html`: la página completa (HTML, CSS y JavaScript).
- `vendor/`: copias locales de SheetJS 0.18.5 y Chart.js 4.4.1. La página las toma de la CDN con
  versión fija y, si no hay conexión, usa estas.
- `pruebas/verificar.js`: comprobación automática de los criterios de aceptación con Playwright.
  Uso: `node pruebas/verificar.js ruta/a/Kit_de_operacion.xlsx`. Necesita Node, Playwright con
  Chromium y Python con `openpyxl`.

## Licencia

El código de esta carpeta es MIT (ver `LICENSE`). SheetJS y Chart.js conservan sus licencias en
`vendor/`. El libro, el Excel del kit y sus textos no están cubiertos por esta licencia.

Kit de operación · *Historia de la hostelería y la gastronomía* · Sergio Berriozábal Serrano ·
WhatsApp +52 984 187 8284
