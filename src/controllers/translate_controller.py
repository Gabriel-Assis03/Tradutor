from flask import Blueprint, render_template, request
from deep_translator import GoogleTranslator
from models.language_model import LanguageModel
# from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    data = LanguageModel.find()
    formatLang = []
    text_to_translate = (
        request.form.get("text-to-translate")
        or "O que deseja traduzir?"
    )
    translate_from = request.form.get("translate-from") or "pt"
    translate_to = request.form.get("translate-to") or "en"
    translated = GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(
        text_to_translate
    )
    for language in data:
        formatLang.append(language.to_dict())
    return render_template(
        "index.html",
        languages=formatLang,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated
    )


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    data = LanguageModel.find()
    formatLang = []
    translated = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")
    text_to_translate = GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(
        translated
    )
    for language in data:
        formatLang.append(language.to_dict())
    return render_template(
        "index.html",
        languages=formatLang,
        text_to_translate=text_to_translate,
        translate_from=translate_to,
        translate_to=translate_from,
        translated=translated
    )
