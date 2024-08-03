from .models import UserProfile
from modeltranslation.translator import TranslationOptions, register

@register(UserProfile)
class UserProfileTranslationOptions(TranslationOptions):
    fields = ('nickname', 'bio')

