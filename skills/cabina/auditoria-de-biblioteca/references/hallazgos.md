# Catalogo de hallazgos: que significa cada uno y como se arregla

Para cada categoria: que detecta el script, por que importa en cabina, como se
arregla y si el arreglo necesita oir el audio.

---

## ruta_rota — CRITICO
**Detecta:** el `Location` del XML apunta a un fichero que no existe en disco.
Solo se comprueba con `--comprobar-rutas` y en la maquina del DJ.
**En cabina:** el track no carga. Es el clasico "track not found" con el signo
de exclamacion.
**Causa habitual:** se movio, renombro o cambio de disco la carpeta de musica.
**Arreglo:** relocalizar desde el propio software. Si son muchos y cambio el
prefijo de la ruta, Lexicon remapea rutas en lote.
**¿Necesita oir?** No.

## sin_beatgrid — CRITICO
**Detecta:** el TRACK no tiene ningun nodo `TEMPO`.
**En cabina:** no hay sync posible; la forma de onda no cuadra con la rejilla.
**Arreglo:** analizar en el software. Si la rejilla sale mal (caso frecuente en
tracks con intro sin percusion o groove complejo), hay que fijar el primer beat
a mano, track por track.
**¿Necesita oir?** Si, para corregirla. No, para detectar que falta.

## sin_bpm — ALTO
**Detecta:** `AverageBpm` vacio o cero.
**En cabina:** el track no aparece al filtrar por tempo. Existe pero es invisible.
**Arreglo:** analizar en el software.
**¿Necesita oir?** No: lo hace el analisis automatico.

## sin_clave — ALTO
**Detecta:** `Tonality` vacio o no reconocible como Camelot, Open Key o nombre.
**En cabina:** queda fuera de cualquier seleccion armonica.
**Arreglo:** analizar. Ojo con la precision: un test sobre 200 tracks dio 69%
de acierto a rekordbox 7 frente a 89% de Mixed In Key
(<https://blog.dubspot.com/dubspot-lab-report-mixed-in-key-vs-beatport>).
**¿Necesita oir?** No para detectar; si para verificar que la clave es correcta.

**Nota util:** si la clave existe pero en otra notacion (Open Key desde Traktor,
clasica desde Beatport), el script la normaliza y NO la cuenta como ausente.
Comprobar una suelta:
```bash
python3 scripts/dj_toolkit.py key "1m"
```

## bitrate_bajo — ALTO
**Detecta:** `BitRate` por debajo de 256 kbps (umbral configurable).
**En cabina:** en un equipo de club se oye. En cascos de casa, no.
**Arreglo:** recomprar en 320 kbps o WAV. No se puede "subir" un MP3 de 128.
**¿Necesita oir?** No.

## sin_cue_points — MEDIO
**Detecta:** ningun `POSITION_MARK`.
**En cabina:** se entra a ciegas y se pierde tiempo buscando el drop.
**Arreglo:** colocarlos a mano, o generarlos automaticamente (Mixed In Key
genera hasta 8 por track; Lexicon Ultimate incluye generador).
**¿Necesita oir?** Si para colocarlos con criterio.

**Contexto importante:** en una biblioteca recien montada es normal que sea el
100%. No es averia, es trabajo pendiente. Priorizar solo los del proximo bolo.

## duplicados — MEDIO
**Detecta:** mismo artista y titulo tras normalizar (sin acentos, sin
puntuacion, sin marcas de version tipo Original Mix o Radio Edit).
**En cabina:** dudas de version en directo y busquedas con ruido.
**Arreglo:** revisar uno a uno. **Muchos duplicados son intencionados:**
Clean/Dirty, Extended/Radio, 320 y WAV del mismo tema. Borrar en bloque es un
error. Nunca borrar desde fuera del software: rompe las playlists.
**¿Necesita oir?** A veces, para decidir cual se queda.

## genero_inconsistente — MEDIO
**Detecta:** variantes del mismo genero que solo difieren en mayusculas,
espacios o puntuacion ("Progressive House" / "progressive house").
**En cabina:** los filtros por genero dejan de funcionar y las playlists
inteligentes se vacian.
**Arreglo:** unificar vocabulario. Lexicon tiene "Genre Cleanup" en lote.
**¿Necesita oir?** No.

## muy_corto — BAJO
**Detecta:** duracion menor de 120 segundos.
**En cabina:** normalmente no es un problema: son jingles, acapellas, drops o
efectos. Tambien puede ser una descarga truncada.
**Arreglo:** revisar. No borrar por sistema.
**¿Necesita oir?** Si, para saber si esta truncado.

## sin_rating — BAJO
**Detecta:** `Rating` a cero.
**En cabina:** solo importa si el DJ organiza por estrellas.
**Arreglo:** puntuar segun se pincha.
**Detalle tecnico:** rekordbox codifica el rating como 0/51/102/153/204/255, no
como 0-5. Un script que escriba 0-5 directamente deja el rating vacio.

---

## Indice de salud: que mide y que no

Media ponderada de los hallazgos por peso de riesgo, normalizada a 0-100.

**Mide** higiene de metadatos.
**No mide** calidad musical, ni si la seleccion es buena, ni si el DJ mezcla
bien. Una biblioteca de 100/100 llena de musica mediocre sigue siendo mediocre.

Referencias orientativas de lectura, no baremo oficial:

| Rango | Lectura |
|---|---|
| 85-100 | Mantenimiento al dia |
| 70-84 | Normal en biblioteca activa; revisar lo critico antes del bolo |
| 50-69 | Acumulacion de anios; merece una sesion de limpieza |
| < 50 | Hay riesgo real de fallo en cabina; priorizar antes del proximo bolo |
