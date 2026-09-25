#!/usr/bin/env python3
import json
import os

# Datos del libro por idioma
guiones_data = {
    "es": {
        "titulo": "Lina y el Bosque Mágico",
        "subtitulo": "Una aventura de amistad y valentía",
        "autor": "Claude Haiku 4.5",
        "idioma": "Español",
        "flag": "🇪🇸",
        "palabras_totales": 8750,
        "horas_estimadas": 0.94,
        "capitulos": 8,
    },
    "en": {
        "titulo": "Lina and the Magical Forest",
        "subtitulo": "An adventure of friendship and courage",
        "autor": "Claude Haiku 4.5",
        "idioma": "English",
        "flag": "🇬🇧",
        "palabras_totales": 9200,
        "horas_estimadas": 0.99,
        "capitulos": 8,
    },
    "fr": {
        "titulo": "Lina et la Forêt Magique",
        "subtitulo": "Une aventure d'amitié et de courage",
        "autor": "Claude Haiku 4.5",
        "idioma": "Français",
        "flag": "🇫🇷",
        "palabras_totales": 9100,
        "horas_estimadas": 0.98,
        "capitulos": 8,
    },
    "de": {
        "titulo": "Lina und der magische Wald",
        "subtitulo": "Ein Abenteuer von Freundschaft und Mut",
        "autor": "Claude Haiku 4.5",
        "idioma": "Deutsch",
        "flag": "🇩🇪",
        "palabras_totales": 8900,
        "horas_estimadas": 0.96,
        "capitulos": 8,
    },
    "pt_br": {
        "titulo": "Lina e a Floresta Mágica",
        "subtitulo": "Uma aventura de amizade e coragem",
        "autor": "Claude Haiku 4.5",
        "idioma": "Português (Brasil)",
        "flag": "🇧🇷",
        "palabras_totales": 9000,
        "horas_estimadas": 0.97,
        "capitulos": 8,
    },
    "it": {
        "titulo": "Lina e la Foresta Magica",
        "subtitulo": "Un'avventura di amicizia e coraggio",
        "autor": "Claude Haiku 4.5",
        "idioma": "Italiano",
        "flag": "🇮🇹",
        "palabras_totales": 8950,
        "horas_estimadas": 0.96,
        "capitulos": 8,
    },
    "ru": {
        "titulo": "Лина и Волшебный Лес",
        "subtitulo": "Приключение дружбы и смелости",
        "autor": "Claude Haiku 4.5",
        "idioma": "Русский",
        "flag": "🇷🇺",
        "palabras_totales": 8800,
        "horas_estimadas": 0.95,
        "capitulos": 8,
    },
    "zh": {
        "titulo": "丽娜和魔法森林",
        "subtitulo": "一场友谊和勇气的冒险",
        "autor": "Claude Haiku 4.5",
        "idioma": "中文",
        "flag": "🇨🇳",
        "palabras_totales": 7800,
        "horas_estimadas": 0.84,
        "capitulos": 8,
    },
    "ja": {
        "titulo": "リナと魔法の森",
        "subtitulo": "友情と勇気の冒険",
        "autor": "Claude Haiku 4.5",
        "idioma": "日本語",
        "flag": "🇯🇵",
        "palabras_totales": 7900,
        "horas_estimadas": 0.85,
        "capitulos": 8,
    },
}

# Idiomas adicionales (traducción fallback a inglés)
idiomas_fallback = {
    "pt_pt": {"titulo": "Lina e a Floresta Mágica", "idioma": "Português (Portugal)", "flag": "🇵🇹"},
    "hi": {"titulo": "लीना और जादुई जंगल", "idioma": "हिंदी", "flag": "🇮🇳"},
    "ar": {"titulo": "لينا والغابة السحرية", "idioma": "العربية", "flag": "🇸🇦"},
    "ko": {"titulo": "리나와 마법의 숲", "idioma": "한국어", "flag": "🇰🇷"},
    "vi": {"titulo": "Lina và Khu Rừng Thần Kỳ", "idioma": "Tiếng Việt", "flag": "🇻🇳"},
    "th": {"titulo": "ลีน่าและป่าวิเศษ", "idioma": "ไทย", "flag": "🇹🇭"},
    "id": {"titulo": "Lina dan Khu Rừng Thần Kỳ", "idioma": "Bahasa Indonesia", "flag": "🇮🇩"},
    "tl": {"titulo": "Lina at ang Mahiwagang Kagubatan", "idioma": "Tagalog", "flag": "🇵🇭"},
    "pl": {"titulo": "Lina i Magiczny Las", "idioma": "Polski", "flag": "🇵🇱"},
    "tr": {"titulo": "Lina ve Sihirli Orman", "idioma": "Türkçe", "flag": "🇹🇷"},
    "nl": {"titulo": "Lina en het Magische Bos", "idioma": "Nederlands", "flag": "🇳🇱"},
    "sv": {"titulo": "Lina och den Magiska Skogen", "idioma": "Svenska", "flag": "🇸🇪"},
    "no": {"titulo": "Lina og Skogen Magisk", "idioma": "Norsk", "flag": "🇳🇴"},
    "da": {"titulo": "Lina og Skovens Trylleri", "idioma": "Dansk", "flag": "🇩🇰"},
    "el": {"titulo": "Λίνα και το Μαγικό Δάσος", "idioma": "Ελληνικά", "flag": "🇬🇷"},
    "fi": {"titulo": "Lina ja Taikametsä", "idioma": "Suomi", "flag": "🇫🇮"},
    "uk": {"titulo": "Ліна та Чарівний Ліс", "idioma": "Українська", "flag": "🇺🇦"},
}

# Completar con datos fallback
for code, data in idiomas_fallback.items():
    # Usar datos de EN como base para fallback
    guiones_data[code] = {
        **guiones_data.get("en", {}),
        "titulo": data["titulo"],
        "idioma": data["idioma"],
        "flag": data["flag"],
    }

# Crear directorio para guiones
os.makedirs("audiolibros/guiones", exist_ok=True)

# Generar resumen
print("=" * 70)
print("📚 PREPARACIÓN DE GUIONES PARA AUDIOLIBROS — Lina y el Bosque Mágico")
print("=" * 70)
print()

total_palabras = 0
total_horas = 0
costos_h2 = []

for code, data in sorted(guiones_data.items()):
    total_palabras += data.get("palabras_totales", 9000)
    total_horas += data.get("horas_estimadas", 0.97)
    
    # Calcular costos
    horas = data.get("horas_estimadas", 0.97)
    costo_es = int(horas * 2000)  # $2,000 MXN por hora terminada (El Taller de las Voces)
    costo_en = int(horas * 150 * 16.96)  # 150 USD por hora (VoiceBros) × 16.96 cambio
    
    print(f"✅ {data['flag']} {data['idioma']:20} | Horas: {horas:.2f} | CAP: {data.get('capitulos', 8)}")
    print(f"   → {data['titulo']}")
    print(f"   → Costo narrador ES: ${costo_es:,} MXN | Narrador EN: ${costo_en:,} MXN")
    print()
    
    costos_h2.append({"idioma": data["idioma"], "horas": horas, "costo_es": costo_es, "costo_en": costo_en})

print("=" * 70)
print(f"📊 TOTALES PROYECTO")
print("=" * 70)
print(f"Total idiomas: 26")
print(f"Total palabras (agregadas): {total_palabras:,}")
print(f"Total horas terminadas: {total_horas:.1f} h")
print(f"Coste narrador ES (promedio $2,000/h): ${int(total_horas * 2000):,} MXN por idioma")
print(f"Coste narrador EN (promedio 150 USD/h): ${int(total_horas * 150 * 16.96):,} MXN por idioma")
print()

# Generar archivo de configuración
config = {
    "proyecto": "Lina y el Bosque Mágico - Audiolibros",
    "derechos": "PROPIO",
    "titular": "sergio@redcontramar.com",
    "idiomas_total": len(guiones_data),
    "palabras_por_idioma": {code: data.get("palabras_totales", 9000) for code, data in guiones_data.items()},
    "horas_por_idioma": {code: data.get("horas_estimadas", 0.97) for code, data in guiones_data.items()},
    "costos_presupuesto": {
        "narrador_es_por_hora": 2000,
        "narrador_en_por_hora": 150 * 16.96,
        "por_idioma": costos_h2
    }
}

with open("audiolibros/config_audiolibros.json", "w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

print("✅ Configuración guardada en: audiolibros/config_audiolibros.json")
