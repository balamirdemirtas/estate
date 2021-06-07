from modeltranslation.translator import TranslationOptions, translator

from real.models import Category,Room,Product,Comment,About



class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)




class RoomTranslationOptions(TranslationOptions):
    fields = ("position",)



class ProductTranslationOptions(TranslationOptions):
    fields = ("name","info",)


class CommentTranslationOptions(TranslationOptions):
    fields = ("text",)


class AboutTranslationOptions(TranslationOptions):
    fields = ("info",)









translator.register(Category,CategoryTranslationOptions)
translator.register(Room,RoomTranslationOptions)
translator.register(Product,ProductTranslationOptions)
translator.register(Comment,CommentTranslationOptions)
translator.register(About,AboutTranslationOptions)