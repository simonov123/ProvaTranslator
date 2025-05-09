#pytranslator
import http.client
import urllib.parse
import json
import sys
import locale
from PyQt6.QtWidgets import QWidget,QTextEdit,QPushButton,QApplication,QComboBox,QVBoxLayout,QLabel
system_locale, _ = locale.getdefaultlocale()
lang_code = system_locale.split('_')[0] if system_locale else 'en'



language_names = [
    "Afrikaans", "Albanian", "Amharic", "Arabic", "Armenian", "Azerbaijani",
    "Basque", "Belarusian", "Bengali", "Bosnian", "Bulgarian", "Catalan",
    "Cebuano", "Chinese (Simplified)", "Chinese (Traditional)", "Corsican",
    "Croatian", "Czech", "Danish", "Dutch", "English", "Esperanto", "Estonian",
    "Finnish", "French", "Frisian", "Galician", "Georgian", "German", "Greek",
    "Gujarati", "Haitian Creole", "Hausa", "Hawaiian", "Hebrew", "Hindi",
    "Hmong", "Hungarian", "Icelandic", "Igbo", "Indonesian", "Irish", "Italian",
    "Japanese", "Javanese", "Kannada", "Kazakh", "Khmer", "Kinyarwanda", "Korean",
    "Kurdish", "Kyrgyz", "Lao", "Latin", "Latvian", "Lithuanian", "Luxembourgish",
    "Macedonian", "Malagasy", "Malay", "Malayalam", "Maltese", "Maori", "Marathi",
    "Mongolian", "Myanmar (Burmese)", "Nepali", "Norwegian", "Nyanja (Chichewa)",
    "Odia (Oriya)", "Pashto", "Persian", "Polish", "Portuguese", "Punjabi",
    "Romanian", "Russian", "Samoan", "Scots Gaelic", "Serbian", "Sesotho",
    "Shona", "Sindhi", "Sinhala", "Slovak", "Slovenian", "Somali", "Spanish",
    "Sundanese", "Swahili", "Swedish", "Tagalog (Filipino)", "Tajik", "Tamil",
    "Tatar", "Telugu", "Thai", "Turkish", "Turkmen", "Ukrainian", "Urdu",
    "Uyghur", "Uzbek", "Vietnamese", "Welsh", "Xhosa", "Yiddish", "Yoruba", "Zulu"
]

language_codes = [
    "af", "sq", "am", "ar", "hy", "az",
    "eu", "be", "bn", "bs", "bg", "ca",
    "ceb", "zh-CN", "zh-TW", "co",
    "hr", "cs", "da", "nl", "en", "eo", "et",
    "fi", "fr", "fy", "gl", "ka", "de", "el",
    "gu", "ht", "ha", "haw", "he", "hi",
    "hmn", "hu", "is", "ig", "id", "ga", "it",
    "ja", "jv", "kn", "kk", "km", "rw", "ko",
    "ku", "ky", "lo", "la", "lv", "lt", "lb",
    "mk", "mg", "ms", "ml", "mt", "mi", "mr",
    "mn", "my", "ne", "no", "ny",
    "or", "ps", "fa", "pl", "pt", "pa",
    "ro", "ru", "sm", "gd", "sr", "st",
    "sn", "sd", "si", "sk", "sl", "so", "es",
    "su", "sw", "sv", "tl", "tg", "ta",
    "tt", "te", "th", "tr", "tk", "uk", "ur",
    "ug", "uz", "vi", "cy", "xh", "yi", "yo", "zu"
]

ui_strings = {
    "en": {
        "input_language": "Input language",
        "output_language": "Output language",
        "button_ok": "Translate"
    },
    "it": {
        "input_language": "Lingua di origine",
        "output_language": "Lingua di destinazione",
        "button_ok": "Traduci"
    },
    "fr": {
        "input_language": "Langue source",
        "output_language": "Langue cible",
        "button_ok": "Traduire"
    },
    "de": {
        "input_language": "Ausgangssprache",
        "output_language": "Zielsprache",
        "button_ok": "Übersetzen"
    },
    "es": {
        "input_language": "Idioma de origen",
        "output_language": "Idioma de destino",
        "button_ok": "Traducir"
    },
    "pt": {
        "input_language": "Idioma de origem",
        "output_language": "Idioma de destino",
        "button_ok": "Traduzir"
    },
    "pl": {
        "input_language": "Język źródłowy",
        "output_language": "Język docelowy",
        "button_ok": "Tłumacz"
    },
    "ru": {
        "input_language": "Исходный язык",
        "output_language": "Язык перевода",
        "button_ok": "Перевести"
    },
    "tr": {
        "input_language": "Giriş dili",
        "output_language": "Hedef dil",
        "button_ok": "Çevir"
    },
    "zh-CN": {
        "input_language": "源语言",
        "output_language": "目标语言",
        "button_ok": "翻译"
    },
    "ar": {
        "input_language": "اللغة المصدر",
        "output_language": "اللغة الهدف",
        "button_ok": "ترجمة"
    }
}

lang_ui = lang_code if lang_code in ui_strings else "en"
app=QApplication(sys.argv)
def trequest(text,source_lang,target_lang):
    
    params = urllib.parse.urlencode({
    'client': 'gtx',
    'sl': source_lang,
    'tl': target_lang,
    'dt': 't',
    'q': text
})

    conn = http.client.HTTPSConnection("translate.googleapis.com")
    conn.request("GET", f"/translate_a/single?{params}")

    res = conn.getresponse()
    data = res.read()

    translated = json.loads(data.decode("utf-8"))
    return translated[0][0][0]

class translator(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 200)
        self.setWindowTitle("ProvaTranslator")
        self.input1=QTextEdit()
        self.lab=QLabel(ui_strings[lang_ui]["input_language"])
        self.input2=QComboBox()
        self.label=QLabel(ui_strings[lang_ui]["output_language"])
        self.input3=QComboBox()
        self.output=QTextEdit()
        self.confirm=QPushButton(ui_strings[lang_ui]["button_ok"])
        layout=QVBoxLayout()
        layout.addWidget(self.input1)
        layout.addWidget(self.lab)
        layout.addWidget(self.input2)
        layout.addWidget(self.label)
        layout.addWidget(self.input3)
        layout.addWidget(self.output)
        layout.addWidget(self.confirm)
        self.input2.addItems(language_names)
        self.input3.addItems(language_names)
        self.confirm.clicked.connect(self.req)
        if lang_code in language_codes:
            index = language_codes.index(lang_code)
            self.input2.setCurrentIndex(index)
        self.setLayout(layout)
    def req(self):
        text=self.input1.toPlainText()
        source_lang=self.input2.currentText()
        target_lang=self.input3.currentText()
        source_index = self.input2.currentIndex()
        target_index = self.input3.currentIndex()
        source_lang = language_codes[source_index]
        target_lang = language_codes[target_index]
        result=trequest(text,source_lang,target_lang)
        print(result)
        self.output.setText(result)


trans=translator()
trans.show()
sys.exit(app.exec())
