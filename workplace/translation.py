from modeltranslation.translator import TranslationOptions, translator
from workplace.models import Category,Room,Product



class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)

class RoomTranslationOptions(TranslationOptions):
    fields = ("position",)

class ProductTranslationOptions(TranslationOptions):
    fields = ("name","info",)



translator.register(Category,CategoryTranslationOptions)
translator.register(Room,RoomTranslationOptions)
translator.register(Product,ProductTranslationOptions)
