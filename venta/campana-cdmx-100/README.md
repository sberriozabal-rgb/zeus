# campana-cdmx-100 · generadores

Dos scripts de la biblioteca estándar más `openpyxl` (solo el segundo). Los datos de terceros
no entran en el repositorio: se leen y se escriben en `dist/`, que git ignora. Método, calendario y
textos en [`../CAMPANA-CDMX-100.md`](../CAMPANA-CDMX-100.md).

```bash
# 1 · correos (uno por local) + seguimientos + índice de envíos
python3 venta/campana-cdmx-100/generar_correos.py \
    --entrada dist/campana-cdmx-100/prospectos.json --salida dist/campana-cdmx-100

# 2 · base de datos v2.1: conserva las 21 cuentas y añade las nuevas
python3 venta/campana-cdmx-100/actualizar_cartera.py \
    --base "dist/OCTAVA_Base_de_Datos_Cartera_Prospectos_20260904.xlsx" \
    --prospectos dist/campana-cdmx-100/prospectos.json \
    --indice dist/campana-cdmx-100/indice_envios.csv \
    --salida "dist/OCTAVA_Base_de_Datos_Cartera_Prospectos_20260917.xlsx"
```

## Formato de `prospectos.json`

Array de objetos. Campos que usa el generador (los demás pasan a la base tal cual):

| Campo | Uso |
|---|---|
| `id`, `nombre`, `zona` | numeración, nombre del local y colonia |
| `perfil` | uno de los catorce perfiles de `PERFILES` en `generar_correos.py` |
| `atencion` | línea «Atención: …» (persona y cargo si es pública; si no, «Dirección · Local») |
| `trato` | cómo se le nombra en el titular de la visita («Chef Chiu», «Elizabeth»); vacío si no hay persona |
| `reputacion` | «Plataforma X.X/5 · N reseñas · fecha (url)»; si no tiene cifra, no se muestra |
| `detalle_para_el_correo` | un hecho público del local, una línea |
| `correo_verificado`, `correo_secundario`, `telefono` | deciden el estado del envío en el índice; nunca se inventan |
| `ola`, `fecha_envio` | calendario |

Regla de la casa: si un dato no está, se escribe `[SIN DATO]`. El generador no rellena huecos.
