#!/usr/bin/env python3
"""OCTAVA · Campaña CDMX-100 · añade los prospectos verificados a la Cartera Documentada (xlsx v2.0 → v2.1).

Toma el libro vigente (OCTAVA_Base_de_Datos_Cartera_Prospectos_<corte>.xlsx), conserva las cuentas
existentes y añade una fila por prospecto nuevo en «Cartera», su ficha en «Fichas», actualiza los
rangos del «Tablero», anota la pasada en «Diccionario» y crea la hoja «Campaña CDMX-100» con el
estado de envío de cada correo.

Uso:
  python3 actualizar_cartera.py --base OCTAVA_Base_..._20260904.xlsx --prospectos prospectos.json \
      --indice indice_envios.csv --salida OCTAVA_Base_de_Datos_Cartera_Prospectos_20260917.xlsx

Los datos de terceros (prospectos.json, indice_envios.csv, el xlsx) viven fuera del repositorio.
"""
import argparse, csv, json, re
from copy import copy
import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

CORTE = "17-sep-2026"
MARINO = "FF17323C"; CREMA = "FFF6F1E7"; VERDE = "FFE4EFE6"; ARENA = "FFE9E6DF"; COBRE = "FFA6642A"

CAMPOS = ["Razón social", "Categoría", "Plaza", "Unidades", "¿Estudio?", "Tipo de estudio", "Fecha del estudio",
          "¿Informe / pieza comercial?", "Documentos en el archivo", "¿Visitada?", "Fecha de visita", "¿Contactada?",
          "Canal de entrada", "Decisor 1 · nombre y cargo", "Decisor 2 · nombre y cargo", "Teléfono",
          "Correo VERIFICADO", "Correo secundario / canal alterno", "Sitio web", "Redes (IG · FB · LinkedIn)",
          "Dirección corporativa", "Reputación (con corte)", "Encuadre Baremo A", "Prioridad", "Estado en el embudo",
          "Siguiente acción", "Fecha objetivo", "Asiento dueño", "Grado de verificación", "Notas / riesgo"]

def sd(v):
    v = (v or "").strip()
    return v if v else "[SIN DATO]"

def fila_cartera(p, idx):
    tiene_correo = not sd(p.get("correo_verificado")).startswith("[SIN")
    tiene_alt = not sd(p.get("correo_secundario")).startswith("[SIN")
    tiene_tel = not sd(p.get("telefono")).startswith("[SIN")
    if tiene_correo: canal = "Correo frío M·2 al buzón oficial → WhatsApp para agendar"
    elif tiene_alt: canal = "Correo frío M·2 a buzón de tercero [SIN CONFIRMAR] → si rebota, teléfono"
    elif tiene_tel: canal = "WhatsApp / teléfono (M·1) antes del servicio de comida; carta en mano si no contesta"
    else: canal = "Carta en mano en el local (correo impreso) + Instagram"
    siguiente = {"Ola 1": "Enviar M·2 el lun 21-sep; M·6 vie 25-sep; M·7 vie 2-oct; M·8 lun 12-oct",
                 "Ola 2": "Enviar M·2 el lun 28-sep; M·6 vie 2-oct; M·7 vie 9-oct; M·8 lun 19-oct",
                 "Ola 3": "Enviar M·2 el lun 5-oct; M·6 vie 9-oct; M·7 vie 16-oct; M·8 lun 26-oct",
                 "Ola 4": "Enviar M·2 el lun 12-oct; M·6 vie 16-oct; M·7 vie 23-oct; M·8 lun 2-nov",
                 "Ola 5": "Enviar M·2 el lun 19-oct; M·6 vie 23-oct; M·7 vie 30-oct; M·8 lun 9-nov"}.get(p.get("ola", ""), "Programar en la siguiente ola")
    return [idx, p.get("nombre_cartera") or p["nombre"], sd(p.get("razon_social")), sd(p.get("categoria")), f"CDMX · {p.get('zona','')}",
            sd(p.get("unidades")), "No", "Ficha de campaña CDMX-100 · verificación de contacto en fuentes públicas",
            "2026-09-17", "Sí", f"Correo M·2 personalizado (HTML) · seguimientos M·6/M·7/M·8 · campana-cdmx-100/{int(idx)-21:03d}",
            "No", "—", "No", canal, sd(p.get("decisor_1")), sd(p.get("decisor_2")), sd(p.get("telefono")),
            sd(p.get("correo_verificado")), sd(p.get("correo_secundario")), sd(p.get("sitio_web")), sd(p.get("redes")),
            sd(p.get("direccion")), sd(p.get("reputacion")), p.get("baremo", "[A CORRER] en llamada"),
            p.get("prioridad", "CDMX-100 · " + p.get("ola", "")), "Correo listo · sin contacto",
            siguiente, p.get("fecha_envio", ""), "A·3 Ventas", sd(p.get("grado_verificacion")), sd(p.get("riesgo_nota") or p.get("riesgo"))]

def copiar_estilo(src, dst):
    dst.font = copy(src.font); dst.fill = copy(src.fill); dst.alignment = copy(src.alignment); dst.border = copy(src.border); dst.number_format = src.number_format

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True); ap.add_argument("--prospectos", required=True)
    ap.add_argument("--indice", required=True); ap.add_argument("--salida", required=True)
    a = ap.parse_args()
    prospectos = json.load(open(a.prospectos, encoding="utf-8"))
    indice = {r["local"]: r for r in csv.DictReader(open(a.indice, encoding="utf-8"))}
    wb = openpyxl.load_workbook(a.base)

    # ---- Cartera
    ws = wb["Cartera"]
    primera = 6; ultima = ws.max_row
    while ws.cell(ultima, 1).value is None: ultima -= 1
    n_prev = ultima - primera + 1
    ws["A1"] = "OCTAVA · CARTERA DOCUMENTADA DE PROSPECTOS · v2.1"
    ws["A2"] = (f"Corte {CORTE} · {n_prev + len(prospectos)} cuentas · las {n_prev} de la pasada del 4-sep se conservan sin cambios · "
                f"{len(prospectos)} cuentas nuevas de la campaña CDMX-100 (Centro, Condesa, Roma, Juárez, Polanco) verificadas en fuentes públicas el {CORTE} · es-MX · CONFIDENCIAL")
    ws["A3"] = ("La columna «Correo VERIFICADO» solo contiene correos leídos en el dominio oficial o el aviso de privacidad de la propia empresa. "
                "Lo demás va etiquetado [SIN CONFIRMAR] o [SIN DATO]. Ningún correo fue inferido. Pasada CDMX-100: lectura vía buscador (grado MEDIA salvo dominio oficial).")
    ws["S5"] = f"Correo VERIFICADO (04-sep / {CORTE})"
    par = ws.cell(primera, 1).fill.fgColor.rgb == CREMA
    for k, p in enumerate(prospectos):
        r = ultima + 1 + k; idx = n_prev + 1 + k
        fila = fila_cartera(p, idx)
        for c, v in enumerate(fila, 1):
            cell = ws.cell(r, c, v); copiar_estilo(ws.cell(primera, c), cell)
            fill = CREMA if (r - primera) % 2 == 0 else "00000000"
            cell.fill = PatternFill("solid", fgColor=fill) if fill != "00000000" else PatternFill(fill_type=None)
            if c in (18, 19, 20):  # teléfono y correos resaltados como en la v2.0
                cell.fill = PatternFill("solid", fgColor=VERDE if (r - primera) % 2 else CREMA)
                cell.font = Font(name="Arial", size=10, bold=(c == 19))
        ws.row_dimensions[r].height = 99.75
    fin = ultima + len(prospectos)
    ws.auto_filter.ref = f"A5:AF{fin}"

    # ---- Tablero: rangos y bloque de la pasada
    t = wb["Tablero"]
    for row in t.iter_rows():
        for c in row:
            if isinstance(c.value, str) and "Cartera!" in c.value:
                c.value = c.value.replace(f"6:B{ultima}", f"6:B{fin}").replace("6:B26", f"6:B{fin}")
                c.value = re.sub(r"(Cartera!\$?[A-Z]{1,2})6:\$?([A-Z]{1,2})26", lambda m: f"{m.group(1)}6:{m.group(2)}{fin}", c.value)
    t["A2"] = f"Conteos calculados sobre la hoja Cartera. Corte {CORTE}, tras la pasada CDMX-100."
    t["A8"].value, t["C8"].value = t["A8"].value, "Solo ARRRCO (las 100 nuevas aún no se visitan)"
    base_r = t.max_row + 2
    t.cell(base_r, 1, f"LO QUE CAMBIÓ EN LA PASADA DEL {CORTE} · CAMPAÑA CDMX-100").font = Font(name="Arial", size=11, bold=True, color="FFFFFFFF")
    t.cell(base_r, 1).fill = PatternFill("solid", fgColor=COBRE)
    zonas = {}
    for p in prospectos: zonas[p["zona"]] = zonas.get(p["zona"], 0) + 1
    lineas = [f"{len(prospectos)} cuentas nuevas en CDMX: " + " · ".join(f"{z} {n}" for z, n in zonas.items()) + ".",
              f"Con correo leído en dominio oficial: {sum(1 for p in prospectos if not sd(p.get('correo_verificado')).startswith('[SIN'))}. "
              f"Con buzón de tercero [SIN CONFIRMAR]: {sum(1 for p in prospectos if sd(p.get('correo_verificado')).startswith('[SIN') and not sd(p.get('correo_secundario')).startswith('[SIN'))}. "
              f"Sin buzón (WhatsApp, teléfono o carta en mano): {sum(1 for p in prospectos if sd(p.get('correo_verificado')).startswith('[SIN') and sd(p.get('correo_secundario')).startswith('[SIN'))}.",
              "Correos M·2 generados uno por local (HTML, plantilla Asian Bay/Blossom, paleta Edición I) con seguimientos M·6, M·7 y M·8 en texto.",
              "Cinco olas de 20 correos, lunes 21-sep a lunes 19-oct; tres intentos por cuenta y ni uno más (OPS·11).",
              "Excluidas por diseño: cuentas ya en cartera, sus conceptos hermanos, marisquerías (categoría en perímetro), restaurantes chinos y parrillas argentinas (campañas anteriores), corporativos que compran por comité.",
              "La lectura fue vía buscador: los sitios oficiales no se pudieron abrir en automático. Grado ALTA solo donde el dato salió del dominio oficial."]
    for i, l in enumerate(lineas, 1):
        t.cell(base_r + i, 1, l).font = Font(name="Arial", size=10)
    # ---- Fichas
    f = wb["Fichas"]
    f["A2"] = f"Una ficha por cuenta con los 32 campos del maestro. Corte {CORTE}. Los campos de contacto van resaltados. Fichas 22 en adelante: campaña CDMX-100."
    r = f.max_row + 2
    for k, p in enumerate(prospectos):
        idx = n_prev + 1 + k
        fila = fila_cartera(p, idx)
        c = f.cell(r, 1, f"{idx:02d} · {p.get('nombre_cartera') or p['nombre']}"); c.font = Font(name="Arial", size=12, bold=True, color="FFFFFFFF"); c.fill = PatternFill("solid", fgColor=MARINO)
        f.cell(r, 2).fill = PatternFill("solid", fgColor=MARINO); f.row_dimensions[r].height = 19.5
        r += 1
        for campo, valor in zip(CAMPOS, fila[2:]):
            a_ = f.cell(r, 1, campo); b_ = f.cell(r, 2, valor)
            a_.font = Font(name="Arial", size=10, bold=True); b_.font = Font(name="Arial", size=10)
            a_.alignment = Alignment(wrap_text=True, vertical="top"); b_.alignment = Alignment(wrap_text=True, vertical="top")
            if campo.startswith(("Teléfono", "Correo", "Decisor")):
                a_.fill = PatternFill("solid", fgColor=CREMA); b_.fill = PatternFill("solid", fgColor=CREMA)
            r += 1
        r += 1

    # ---- Diccionario
    d = wb["Diccionario"]
    r = d.max_row + 2
    for campo, texto in [
        ("Pasada CDMX-100", f"{CORTE}. {len(prospectos)} cuentas nuevas (Centro, Condesa, Roma, Juárez, Polanco). Lectura por buscador con URL fuente por dato; los sitios oficiales no se abrieron en automático. Correo VERIFICADO solo si el buzón aparece en un resultado del dominio oficial."),
        ("Perfil (Campaña CDMX-100)", "Segmento de la plantilla de correo: alta_cocina · mexicana_tradicional · cantina · taqueria · cafeteria · italiana · japonesa · bistro · contemporanea · cortes · grupo · hotel · cocina_del_mundo · mercado. Cambia el titular, la línea de apertura y las tres zonas del Índice que se citan; el método y el cierre son los mismos."),
        ("Ola", "Lunes de envío del M·2. Ola 1 = 21-sep (Roma) · Ola 2 = 28-sep (Condesa) · Ola 3 = 5-oct (Juárez) · Ola 4 = 12-oct (Polanco) · Ola 5 = 19-oct (Centro). M·6 al día 4, M·7 al día 11, M·8 al día 21; después la cuenta se marca fría seis meses (OPS·11)."),
        ("REGLA 8", "Categoría en perímetro: marisquerías y cocina de mar no se contactan mientras el titular tenga relación laboral con el sector. Se registran, no se tocan."),
        ("REGLA 9", "Un correo de la campaña CDMX-100 cuenta como verificado solo cuando un envío real no rebotó. El rebote pasa la cuenta a teléfono o carta en mano, nunca a un correo adivinado."),
    ]:
        a_ = d.cell(r, 1, campo); b_ = d.cell(r, 2, texto)
        a_.font = Font(name="Arial", size=10, bold=True); b_.font = Font(name="Arial", size=10)
        a_.fill = PatternFill("solid", fgColor=ARENA); b_.alignment = Alignment(wrap_text=True, vertical="top"); r += 1

    # ---- Hoja de campaña
    c = wb.create_sheet("Campaña CDMX-100")
    c["A1"] = "CAMPAÑA CDMX-100 · ESTADO DE ENVÍO POR LOCAL"; c["A1"].font = Font(name="Arial", size=14, bold=True, color=MARINO)
    c["A2"] = f"Corte {CORTE}. Una fila por local. Se actualiza a mano cada mañana: fecha real de envío, rebote, respuesta, visita. Los cinco números del día salen de esta hoja."; c["A2"].font = Font(name="Arial", size=9, color="FF666057")
    cab = ["ID", "Local", "Zona", "Perfil", "Ola", "Fecha M·2 prevista", "Destinatario (correo)", "Estado del buzón", "Teléfono / WhatsApp", "Asunto", "Archivo HTML", "Seguimientos",
           "Enviado (fecha real)", "Rebotó", "Respondió", "Visita agendada", "Visita hecha", "Hoja de 3 hallazgos", "Propuesta", "Etiqueta WhatsApp (01–09)", "Notas"]
    for j, h in enumerate(cab, 1):
        cell = c.cell(4, j, h); cell.font = Font(name="Arial", size=10, bold=True, color="FFFFFFFF"); cell.fill = PatternFill("solid", fgColor=MARINO); cell.alignment = Alignment(wrap_text=True, vertical="center")
    anchos = [5, 28, 12, 18, 8, 14, 34, 40, 26, 40, 40, 40, 14, 8, 10, 14, 12, 16, 12, 18, 50]
    for j, w in enumerate(anchos, 1): c.column_dimensions[get_column_letter(j)].width = w
    for k, p in enumerate(prospectos):
        i = indice.get(p["nombre"], {}); r = 5 + k; idx = n_prev + 1 + k
        vals = [idx, p.get("nombre_cartera") or p["nombre"], p.get("zona", ""), p.get("perfil", ""), p.get("ola", ""), p.get("fecha_envio", ""), i.get("para", ""), i.get("estado", ""),
                sd(p.get("telefono")), i.get("asunto", ""), i.get("archivo", ""), i.get("seguimientos", ""), "", "", "", "", "", "", "", "01 Nuevo", ""]
        for j, v in enumerate(vals, 1):
            cell = c.cell(r, j, v); cell.font = Font(name="Arial", size=10); cell.alignment = Alignment(wrap_text=True, vertical="top")
            if k % 2 == 0: cell.fill = PatternFill("solid", fgColor=CREMA)
    c.freeze_panes = "C5"; c.auto_filter.ref = f"A4:U{4 + len(prospectos)}"
    fin_c = 4 + len(prospectos)
    r = fin_c + 2
    c.cell(r, 1, "LOS CINCO NÚMEROS DE CADA MAÑANA").font = Font(name="Arial", size=11, bold=True, color="FFFFFFFF"); c.cell(r, 1).fill = PatternFill("solid", fgColor=MARINO)
    for k, (nom, formula) in enumerate([("Correos enviados", f'=COUNTA(M5:M{fin_c})'), ("Rebotes", f'=COUNTIF(N5:N{fin_c},"Sí")'), ("Respuestas", f'=COUNTIF(O5:O{fin_c},"Sí")'),
                                        ("Visitas agendadas", f'=COUNTA(P5:P{fin_c})'), ("Visitas hechas", f'=COUNTIF(Q5:Q{fin_c},"Sí")'),
                                        ("Hojas de tres hallazgos entregadas", f'=COUNTIF(R5:R{fin_c},"Sí")'), ("Propuestas", f'=COUNTIF(S5:S{fin_c},"Sí")')], 1):
        c.cell(r + k, 1, nom).font = Font(name="Arial", size=10); c.cell(r + k, 2, formula).font = Font(name="Arial", size=10, bold=True)
    wb.save(a.salida)
    print(f"Guardado {a.salida}: {n_prev} cuentas previas + {len(prospectos)} nuevas = {n_prev + len(prospectos)}")

if __name__ == "__main__":
    main()
