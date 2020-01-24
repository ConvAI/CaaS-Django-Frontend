from django import forms
from userpanel.models import Bot,Language

class LanguageForm(forms.ModelForm):
    class Meta():
        model = Language
        fields = ('lang_code',)
        
class BotForm(forms.ModelForm):
    class Meta():
        model = Bot
        fields = ('bot_name','bot_desc')