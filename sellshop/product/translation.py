from modeltranslation.translator import translator, TranslationOptions
from product.models import Category, Tag

class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(Category, CategoryTranslationOptions)
translator.register(Tag)