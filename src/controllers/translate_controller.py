from flask import Blueprint, render_template, request
# from deep_translator import GoogleTranslator
from models.language_model import LanguageModel
# from models.history_model import HistoryModel
from deep_translator import GoogleTranslator


translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    languages = LanguageModel.list_dicts()
    text_to_translate = "O que deseja traduzir"
    translate_from = "pt"
    translate_to = "en"
    google_translator = "Tradução"
    if request.method == "POST":
        text_to_translate = request.form.get("text-to-translate")
        translate_from = request.form.get("translate-from")
        translate_to = request.form.get("translate-to")
        google_translator = GoogleTranslator(
            source=translate_from,
            target=translate_to
        ).translate(text_to_translate)
        return render_template(
            "index.html",
            languages=languages,
            text_to_translate=text_to_translate,
            translate_from=translate_from,
            translate_to=translate_to,
            translated=google_translator
        )


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    languages = LanguageModel.list_dicts()
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate_to")
    google_translator = GoogleTranslator(
        source=translate_from,
        target=translate_to
    ).translate(text_to_translate)
    return render_template(
            "index.html",
            languages=languages,
            text_to_translate=text_to_translate,
            translate_from=translate_to,
            translate_to=translate_from,
            translated=google_translator
        )

