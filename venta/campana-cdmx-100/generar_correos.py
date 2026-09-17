#!/usr/bin/env python3
"""OCTAVA · Campaña CDMX-100 · generador de correos de primer contacto (M·2).

Lee la lista privada de prospectos (JSON, fuera del repositorio) y produce, por local:
  - correos/NNN_slug.html      correo HTML de primer contacto (plantilla Asian Bay / Blossom, paleta Edición I)
  - seguimientos/NNN_slug.txt  M·6 (día 4) y M·8 (día 21) en texto plano, listos para pegar
  - indice_envios.csv          una fila por local: destinatario, asunto, preheader, archivo, estado del correo

Uso:
  python3 generar_correos.py --entrada prospectos.json --salida ../../dist/campana-cdmx-100

La entrada es un array JSON con, por local: id, nombre, zona, perfil, atencion, trato, direccion,
correo_verificado, correo_secundario, telefono, reputacion, detalle_para_el_correo, unidades, sitio_web.
Ningún dato de contacto se inventa aquí: si el correo es "[SIN DATO]", el índice lo marca
"SIN BUZÓN → carta en mano / WhatsApp" y el HTML se genera igual para imprimir o adjuntar.
"""
import argparse, csv, html, json, os, re, unicodedata
from urllib.parse import quote

WHATSAPP = "529841878284"
WHATSAPP_VISIBLE = "+52 984 187 8284"
CORREO_CASA = "sberriozabal@gmail.com"

# Paleta Edición I (Manual de Marca MMXXVI, MKT·07): marino de fondo, oro en línea, signo y cifra, crema en soporte claro.
MARINO = "#0B1728"; ORO = "#C6A15C"; CREMA = "#F4EFE6"; CREMA_2 = "#EFE9DD"; GRAFITO = "#1C2321"
LINEA = "#DCD3C7"; GRIS = "#4A4640"; GRIS_2 = "#6E6760"; MARFIL = "#FBF8F1"; WA = "#128C7E"

# Perfiles: cómo se abre el correo y qué tres zonas del Índice se miden primero (IDX·17, Manual de Operaciones Ed. 1).
PERFILES = {
  "alta_cocina": dict(
    etiqueta="Alta cocina",
    sub="Doce zonas medidas en su casa; un sistema que sostiene el nivel cuando el chef no está en el pase.",
    zonas="procedimientos de cocina · ritmo de pase · tablero y dirección",
    titulo="Un nivel que cuesta sostener todos los días."),
  "mexicana_tradicional": dict(
    etiqueta="Cocina mexicana tradicional",
    sub="Doce zonas medidas en su local; un sistema que hace que el martes salga igual que el sábado.",
    zonas="escandallo y carta · mise en place y producción · personal e inducción",
    titulo="Una casa con historia que no debe depender de la memoria."),
  "cantina": dict(
    etiqueta="Cantina",
    sub="Doce zonas medidas en su local; un sistema que aguanta el servicio de las tres de la tarde sin el dueño en la barra.",
    zonas="secuencia de servicio · merma y aprovechamiento · tablero y dirección",
    titulo="Una barra que vende sola exige una casa que opere sola."),
  "taqueria": dict(
    etiqueta="Taquería y antojería",
    sub="Doce zonas medidas en su local; un sistema para que el volumen no se coma el margen.",
    zonas="compras y proveedores · merma y aprovechamiento · ritmo de pase",
    titulo="Volumen alto, margen fino: aquí el procedimiento vale dinero."),
  "cafeteria": dict(
    etiqueta="Cafetería, panadería y brunch",
    sub="Doce zonas medidas en su local; un sistema para que la fila de la mañana no dependa de quién abrió.",
    zonas="mise en place y producción · secuencia de servicio · personal e inducción",
    titulo="La apertura la sabe hacer bien una persona. Eso es el riesgo."),
  "italiana": dict(
    etiqueta="Cocina italiana",
    sub="Doce zonas medidas en su local; un sistema que mantiene la pasta al punto con o sin el chef.",
    zonas="escandallo y carta · procedimientos de cocina · ritmo de pase",
    titulo="Una carta corta y bien hecha merece una operación igual de limpia."),
  "japonesa": dict(
    etiqueta="Cocina japonesa",
    sub="Doce zonas medidas en su local; un sistema que cuida el producto desde la cámara hasta la barra.",
    zonas="almacén y cámara · procedimientos de cocina · higiene y seguridad",
    titulo="El producto es el negocio: la cámara y la barra mandan."),
  "bistro": dict(
    etiqueta="Bistró y cocina de autor",
    sub="Doce zonas medidas en su local; un sistema que sigue funcionando cuando el dueño no está en la sala.",
    zonas="secuencia de servicio · reservas y no-shows · escandallo y carta",
    titulo="Una reputación que vale dinero."),
  "contemporanea": dict(
    etiqueta="Cocina contemporánea",
    sub="Doce zonas medidas en su local; un sistema que sigue funcionando cuando el dueño no está en la sala.",
    zonas="ritmo de pase · secuencia de servicio · tablero y dirección",
    titulo="Una reputación que vale dinero."),
  "cortes": dict(
    etiqueta="Cortes y parrilla",
    sub="Doce zonas medidas en su local; un sistema para que la cocción y los tiempos de pase no dependan de quién está en la parrilla.",
    zonas="almacén y cámara · procedimientos de cocina · ritmo de pase",
    titulo="El corte se paga en la cámara y se cobra en el pase."),
  "grupo": dict(
    etiqueta="Grupo restaurantero",
    sub="Doce zonas medidas en una unidad piloto; la misma vara para comparar todas las casas del grupo.",
    zonas="tablero y dirección · procedimientos de cocina · personal e inducción",
    titulo="Varias casas, una sola vara para medirlas."),
  "hotel": dict(
    etiqueta="Restaurante de hotel",
    sub="Doce zonas medidas en el restaurante; un sistema que separa la operación del restaurante de la del hotel y la hace comparable.",
    zonas="secuencia de servicio · reservas y no-shows · tablero y dirección",
    titulo="Un restaurante dentro de un hotel merece su propio tablero."),
  "cocina_del_mundo": dict(
    etiqueta="Cocina del mundo",
    sub="Doce zonas medidas en su local; un sistema que hace que la receta salga igual sin el cocinero que la trajo.",
    zonas="procedimientos de cocina · compras y proveedores · personal e inducción",
    titulo="Una receta que vive en una sola cabeza es un riesgo con precio."),
  "mercado": dict(
    etiqueta="Mercado gastronómico",
    sub="Doce zonas medidas en el conjunto; un sistema común para que cada concepto opere con la misma regla.",
    zonas="higiene y seguridad · tablero y dirección · personal e inducción",
    titulo="Muchos conceptos bajo un techo piden una sola regla del juego."),
}

def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-")

def sin_dato(v):
    return (not v) or v.strip().startswith("[SIN") or v.strip() in ("—", "-", "")

def rep_split(rep):
    """'Google 4.6/5 · 1,234 reseñas · 17-sep-2026 (url)' -> ('4.6', 'Google · 1,234 reseñas')"""
    m = re.search(r"(\d\.\d)\s*/\s*5", rep or "")
    if not m: return None, None
    n = re.search(r"([\d,\.]+)\s*(reseñas|opiniones|reviews)", rep or "", re.I)
    plat = re.match(r"\s*([A-Za-z ]+?)\s+\d", rep or "")
    detalle = (plat.group(1).strip() if plat else "calificación pública") + (f" · {n.group(1)} reseñas" if n else "")
    return m.group(1), detalle

def semanas_html():
    pasos = ["Línea base", "Hojas de posición", "POE de cocina", "POE de sala", "Formación", "Medición", "Ajuste", "Índice + Sello"]
    celdas = []
    for i, p in enumerate(pasos, 1):
        extremo = i in (1, 8)
        color_num = ORO if extremo else MARINO
        color_txt = ORO if extremo else "#555"
        borde = "" if extremo else f"border:1px solid {LINEA};"
        celdas.append(f'<td align="center" style="{borde}padding:8px 2px" width="12%"><div style="font-family:Georgia,serif;font-size:16px;font-weight:bold;color:{color_num}">{i}</div><div style="font-family:Arial,sans-serif;font-size:8.5px;line-height:1.15;color:{color_txt};margin-top:2px">{p}</div></td>')
    return "".join(celdas)

def correo_html(p):
    perfil = PERFILES.get(p.get("perfil", "contemporanea"), PERFILES["contemporanea"])
    local = p["nombre"]; L = html.escape(local)
    zona = html.escape(p.get("zona_visible") or p.get("zona", "Ciudad de México"))
    atencion = html.escape(p.get("atencion") or f"Dirección · {local}")
    trato = html.escape(p.get("trato") or "")  # cómo se le nombra en el titular de la visita: "Chef Chiu", "Elizabeth", "Estimado equipo"
    titulo_visita = (f"{trato}: 90 minutos en {L}, cuando usted diga." if trato else f"90 minutos en {L}, cuando usted diga.")
    detalle = (p.get("detalle_para_el_correo") or "").strip().rstrip(".")
    detalle_cap = detalle[:1].upper() + detalle[1:] if detalle else ""
    nota, rep_detalle = rep_split(p.get("reputacion_email") or p.get("reputacion", ""))
    if nota and float(nota) < 4.0:
        nota = None  # REGLA 3: la reseña forma la hipótesis, nunca es acusación; por debajo de 4.0 no se muestra
    if nota:
        bloque_veo = (f'<table cellpadding="0" cellspacing="0"><tr><td style="padding-right:12px" valign="middle"><span style="font-family:Arial,sans-serif;font-size:30px;font-weight:bold;color:{ORO}">{nota}</span></td>'
                      f'<td style="font-size:14px;color:{GRIS}" valign="middle">su calificación pública hoy · {html.escape(rep_detalle)}'
                      + (f" · {html.escape(detalle)}" if detalle and not sin_dato(detalle) else "") + '</td></tr></table>')
    else:
        bloque_veo = (f'<div style="font-size:15px;color:{GRIS};line-height:1.5">{html.escape(detalle_cap) + "." if detalle and not sin_dato(detalle) else "Una casa que ya funciona y que quiere funcionar igual el día que usted no está."}</div>')
    wa_txt = quote(f"Soy de {local}. Quiero la visita de OCTAVA.")
    mail_subject = quote(f"{local} — quiero la visita de 90 minutos")
    mail_body = quote(f"Sergio, quiero la visita de OCTAVA en {local}.\nDía y hora que me acomodan: \nMi nombre y cargo: ")
    preheader = f"Mejoro la operación de {local} en ocho semanas. Visita de 90 minutos, sin costo."
    return f"""<!DOCTYPE html>
<html lang="es-MX">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light">
<title>OCTAVA · {L}</title>
</head>
<body style="margin:0;padding:0;background-color:{CREMA};-webkit-text-size-adjust:100%">
<div style="display:none;font-size:1px;color:{CREMA};max-height:0;overflow:hidden">{html.escape(preheader)}</div>
<table cellpadding="0" cellspacing="0" width="100%"><tr><td align="center" style="padding:22px 12px"> <table cellpadding="0" cellspacing="0" style="width:600px;max-width:600px;font-family:Georgia,'Times New Roman',serif;color:{GRAFITO}" width="600"> <tr><td style="padding:14px 28px;border-bottom:1px solid {LINEA};font-size:13px;color:{GRIS}">Atención: <b>{atencion}</b></td></tr> <tr><td style="padding:16px 28px;border-bottom:1px solid {LINEA}"><table cellpadding="0" cellspacing="0" width="100%"><tr> <td style="font-family:Georgia,serif;font-size:19px;letter-spacing:5px;color:{MARINO};font-weight:bold">OCTAVA<div style="font-family:Arial,sans-serif;font-size:8px;letter-spacing:3px;color:{ORO};margin-top:3px">OPERACIÓN GASTRONÓMICA · CDMX</div></td> <td align="right" style="font-family:Arial,sans-serif;font-size:9px;letter-spacing:3px;color:{ORO};text-transform:uppercase">Método · 8 semanas</td></tr></table></td></tr> <tr><td style="padding:0"><table cellpadding="0" cellspacing="0" width="100%"><tr bgcolor="{MARINO}" style="background-color:{MARINO};"> <td style="padding:32px 26px;color:{MARFIL}" valign="middle" width="62%"> <div style="font-family:Arial,sans-serif;font-size:10px;letter-spacing:3px;text-transform:uppercase;color:{ORO};margin-bottom:12px">{html.escape(perfil['etiqueta'])} · {zona} · {L}</div> <div style="font-family:Georgia,serif;font-size:34px;line-height:1.06;margin-bottom:10px;font-weight:bold">Mejoro su operación<br/>en <i style="color:{ORO}">ocho semanas.</i></div> <div style="font-size:15.5px;line-height:1.5;color:{MARFIL}">{html.escape(perfil['sub'])}</div></td> <td align="center" style="padding:24px 14px" valign="middle" width="38%"><table align="center" cellpadding="0" cellspacing="0"><tr><td align="center" style="width:132px;height:132px;border-radius:66px;border:5px solid {ORO}"> <div style="font-family:Georgia,serif;font-size:84px;line-height:1;color:{ORO};font-style:italic;font-weight:bold">8</div> <div style="font-family:Arial,sans-serif;font-size:9px;letter-spacing:4px;color:{ORO}">SEMANAS</div></td></tr></table></td></tr></table> <table cellpadding="0" cellspacing="0" width="100%"><tr><td style="height:4px;background-color:{ORO}"></td></tr></table></td></tr> <tr><td style="padding:26px 28px 6px"> <div style="font-family:Arial,sans-serif;font-size:10px;letter-spacing:3px;color:{ORO};text-transform:uppercase">Lo que veo en {L}</div> <div style="font-family:Georgia,serif;font-size:23px;color:#111;margin:8px 0 10px">{html.escape(perfil['titulo'])}</div> {bloque_veo} <div style="font-size:15px;color:#3b3630;line-height:1.5;margin-top:12px">Lo que mido primero: {html.escape(perfil['zonas'])}. Después, las demás zonas del Índice, en su orden.</div></td></tr> <tr><td style="padding:20px 28px 6px"> <div style="font-family:Arial,sans-serif;font-size:10px;letter-spacing:3px;color:{ORO};text-transform:uppercase">El método · ocho semanas</div> <div style="font-size:14px;color:{GRIS};margin:8px 0 10px">Cada semana usted recibe un entregable:</div> <table cellpadding="0" cellspacing="0" width="100%"><tr>{semanas_html()}</tr></table> <div style="font-size:14px;color:#3b3630;line-height:1.5;margin-top:10px">Doce zonas medidas en la semana 1 y en la 8. Umbral del Sello: <b>86</b> — y se entrega el número aunque no mejore.</div></td></tr> <tr><td style="padding:22px 28px 6px"> <div style="font-family:Arial,sans-serif;font-size:10px;letter-spacing:3px;color:{ORO};text-transform:uppercase">La visita de 90 minutos</div> <div style="font-family:Georgia,serif;font-size:23px;color:#111;margin:8px 0 8px">{titulo_visita}</div> <div style="font-size:15.5px;line-height:1.55;color:#3b3630">Recorro su local en operación, con usted o con su gerente. Al día siguiente le entrego una página con <b>tres hallazgos accionables</b>. <b>Sin costo y sin compromiso.</b></div></td></tr> <tr><td align="center" style="padding:14px 28px 6px"><div style="text-align:center;padding:10px 0 2px"><a href="https://wa.me/{WHATSAPP}?text={wa_txt}" style="background-color:{WA};color:#ffffff;display:inline-block;text-decoration:none;font-weight:bold;border-radius:6px;padding:16px 34px;font-size:14px;letter-spacing:1.2px;text-transform:uppercase;white-space:nowrap;font-family:Arial,Helvetica,sans-serif">Agendar por WhatsApp</a><div style="font-family:Arial,Helvetica,sans-serif;font-size:12.5px;color:{WA};font-weight:bold;margin-top:9px;letter-spacing:0.4px">{WHATSAPP_VISIBLE}</div><div style="font-family:Arial,Helvetica,sans-serif;font-size:11.5px;color:{GRIS_2};margin-top:7px;line-height:1.55">¿Prefiere el correo? Responda a este mensaje o escriba a <a href="mailto:{CORREO_CASA}?subject={mail_subject}&amp;body={mail_body}" style="color:{MARINO};font-weight:bold;text-decoration:underline">{CORREO_CASA}</a>.</div></div> <div style="font-family:Arial,sans-serif;font-size:10px;letter-spacing:2px;color:{GRIS_2};margin-top:12px;text-transform:uppercase">Solo dos implantaciones a la vez · Próximo arranque en noviembre</div></td></tr> <tr><td style="padding:20px 28px 22px;border-top:1px solid {LINEA}"><table cellpadding="0" cellspacing="0" width="100%"><tr> <td valign="top" width="56"><div style="background-color:{MARINO};width:48px;height:48px;border-radius:24px;border:2px solid {ORO};color:{MARFIL};font-family:Georgia,serif;font-size:17px;text-align:center;line-height:48px">SB</div></td> <td style="padding-left:12px" valign="middle"><div style="font-family:Georgia,serif;font-size:16px;color:#111">Sergio Berriozábal Serrano</div> <div style="font-size:13px;line-height:1.45;color:#3b3630">Consultor de operación gastronómica · México y España · {WHATSAPP_VISIBLE}<br/>Más de veinte años dirigiendo hoteles y restaurantes; MBA en Dirección Hotelera.</div></td></tr></table></td></tr> <tr><td bgcolor="{MARINO}" style="background-color:{MARINO};padding:14px 28px;color:{MARFIL};font-family:Arial,sans-serif;font-size:9px;letter-spacing:2px"><table cellpadding="0" cellspacing="0" width="100%"><tr> <td style="white-space:nowrap">OCTAVA · CIUDAD DE MÉXICO</td><td align="right" style="color:{ORO}">SISTEMA MEDIDO · SIN PROMESAS DE VENTAS NI DE RESEÑAS</td></tr></table></td></tr> </table></td></tr></table>
</body>
</html>
"""

def seguimientos_txt(p):
    local = p["nombre"]; trato = p.get("trato") or "Buen día"
    detalle = p.get("detalle_para_el_correo") or "su casa"
    return f"""OCTAVA · {local} · seguimientos (usar como están; solo se cambian los corchetes)

=== M·6 · día 4 · Asunto: Re: Tres hallazgos para {local}, sin costo ===
{trato}, le escribí el [día] por lo de la visita a {local}. Le dejo dos fechas concretas por si es más fácil elegir que contestar: [día 1, hora] o [día 2, hora]. Cualquiera me funciona. Son 90 minutos en hora de servicio y al día siguiente le entrego una página con tres hallazgos; sin costo y sin compromiso.
Sergio Berriozábal · OCTAVA · {WHATSAPP_VISIBLE}

=== M·7 · día 11 · cambio de ángulo · Asunto: Una cosa que puede arreglar esta semana en {local} ===
{trato}, no le vuelvo a mandar el mismo correo. Le cuento qué pasa en la visita: recorro las doce zonas de su operación (compras, cámara, escandallo, mise en place, procedimientos, merma, pase, servicio, reservas, personal, higiene y tablero) y al día siguiente le entrego tres hallazgos con lo que cuesta cada uno. Uno de los tres siempre se resuelve esa misma semana sin gastar y sin mí. ¿[Día 1, hora] o [día 2, hora]?
Sergio Berriozábal · OCTAVA · {WHATSAPP_VISIBLE}

=== M·8 · día 21 · última puerta · Asunto: No le insisto más ===
{trato}, no le insisto más. Le dejo mi contacto por si en algún momento cambia el momento: {WHATSAPP_VISIBLE}. Si conoce a alguien a quien esto sí le sirva hoy, se lo agradezco. Mucho éxito con {detalle if not sin_dato(detalle) else local}.
Sergio Berriozábal · OCTAVA

=== WhatsApp · M·1 (si hay número directo y no hay buzón) ===
{trato}, soy Sergio Berriozábal. Llevo veinte años en piso, sala y cocina, y ahora instalo sistemas de operación en restaurantes: el manual, los POE y el tablero que hacen que un turno no dependa de quién esté ese día. Estoy tomando dos casas este trimestre para hacerlo completo. Antes de proponer nada voy al local, veo 90 minutos de operación y al día siguiente entrego una hoja con tres cosas concretas que ajustaría. Eso no cuesta y no compromete a nada. ¿Le sirve que pase [día] en [franja horaria]?
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--entrada", required=True)
    ap.add_argument("--salida", required=True)
    a = ap.parse_args()
    prospectos = json.load(open(a.entrada, encoding="utf-8"))
    os.makedirs(os.path.join(a.salida, "correos"), exist_ok=True)
    os.makedirs(os.path.join(a.salida, "seguimientos"), exist_ok=True)
    filas = []
    for p in prospectos:
        base = f"{int(p['id']):03d}_{slug(p['nombre'])}"
        with open(os.path.join(a.salida, "correos", base + ".html"), "w", encoding="utf-8") as f:
            f.write(correo_html(p))
        with open(os.path.join(a.salida, "seguimientos", base + ".txt"), "w", encoding="utf-8") as f:
            f.write(seguimientos_txt(p))
        correo = p.get("correo_verificado", "")
        alterno = p.get("correo_secundario", "")
        if not sin_dato(correo):
            estado, para = "ENVIAR · correo leído en dominio oficial", correo.split()[0]
        elif not sin_dato(alterno):
            estado, para = "ENVIAR CON AVISO · buzón de tercero [SIN CONFIRMAR]", alterno.split()[0]
        elif not sin_dato(p.get("telefono", "")):
            estado, para = "SIN BUZÓN → WhatsApp / teléfono (M·1) o carta en mano", ""
        else:
            estado, para = "SIN BUZÓN NI TELÉFONO → carta en mano en el local", ""
        filas.append(dict(id=p["id"], local=p["nombre"], zona=p.get("zona", ""), perfil=p.get("perfil", ""),
                          atencion=p.get("atencion", ""), para=para, estado=estado, telefono=p.get("telefono", ""),
                          asunto=f"Tres hallazgos para {p['nombre']}, sin costo",
                          asunto_b="90 minutos en su piso, una hoja al día siguiente",
                          preheader=f"Mejoro la operación de {p['nombre']} en ocho semanas. Visita de 90 minutos, sin costo.",
                          archivo=f"correos/{base}.html", seguimientos=f"seguimientos/{base}.txt",
                          ola=p.get("ola", ""), fecha_envio=p.get("fecha_envio", "")))
    with open(os.path.join(a.salida, "indice_envios.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys())); w.writeheader(); w.writerows(filas)
    n_env = sum(1 for r in filas if r["estado"].startswith("ENVIAR ·"))
    n_av = sum(1 for r in filas if r["estado"].startswith("ENVIAR CON"))
    print(f"{len(filas)} correos generados · {n_env} con buzón oficial · {n_av} con buzón de tercero · {len(filas)-n_env-n_av} sin buzón")

if __name__ == "__main__":
    main()
