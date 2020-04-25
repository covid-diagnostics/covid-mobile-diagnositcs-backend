from modeltranslation.translator import translator, TranslationOptions
from .models import Question


class QuestionOptions(TranslationOptions):
    fields = ("display_name", "extra_data")


translator.register(Question, QuestionOptions)
