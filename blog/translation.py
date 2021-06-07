from modeltranslation.translator import TranslationOptions, translator


from blog.models import Post





class PostTranslationOptions(TranslationOptions):
    fields = ("title","content",)









translator.register(Post,PostTranslationOptions)