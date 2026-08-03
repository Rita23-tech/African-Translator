from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

# ─────────────────────────────────────────────────────────────
# ALL AFRICAN LANGUAGES CONFIRMED IN GOOGLE TRANSLATE
# Every code here was verified from Google Translate's own
# supported language list — none of these will throw an error.
# ─────────────────────────────────────────────────────────────
AFRICAN_LANGUAGES = {
    "sw": "Swahili 🇰🇪🇹🇿",
    "am": "Amharic 🇪🇹",
    "ha": "Hausa 🇳🇬🇳🇪",
    "ig": "Igbo 🇳🇬",
    "yo": "Yoruba 🇳🇬🇧🇯",
    "zu": "Zulu 🇿🇦",
    "xh": "Xhosa 🇿🇦",
    "so": "Somali 🇸🇴",
    "om": "Oromo 🇪🇹",
    "rw": "Kinyarwanda 🇷🇼",
    "lg": "Luganda 🇺🇬",
    "ny": "Chichewa 🇲🇼🇿🇲",
    "sn": "Shona 🇿🇼",
    "st": "Sesotho 🇱🇸🇿🇦",
    "nso": "Sepedi 🇿🇦",
    "ts": "Tsonga 🇿🇦🇲🇿",
    "mg": "Malagasy 🇲🇬",
    "ln": "Lingala 🇨🇩🇨🇬",
    "ee": "Ewe 🇬🇭🇹🇬",
    "ak": "Twi 🇬🇭",
    "bm": "Bambara 🇲🇱",
    "ti": "Tigrinya 🇪🇷🇪🇹",
    "kri": "Krio 🇸🇱",
}


@app.route("/")
def home():
    return render_template("index.html", languages=AFRICAN_LANGUAGES)


@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()

    text = data.get("text", "").strip()
    source_lang = data.get("source_lang", "auto")
    target_lang = data.get("target_lang", "en")

    if not text:
        return jsonify({"error": "Please enter some text to translate."}), 400

    try:
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        return jsonify({"translated_text": translated})
    except Exception as e:
        return jsonify({"error": f"Translation failed: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
