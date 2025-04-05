
from django import forms

class WordForm(forms.Form):
    word = forms.CharField(
        label='Word',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Search for a word...'})
    )

    def clean_word(self):
        word = self.cleaned_data.get('word')
        if not word.isalpha():
            raise forms.ValidationError("Please enter a valid word containing only letters.")
        return word

# اگر به حروف فارسی نیاز دارید، می‌توانید از regex استفاده کنید.
#     import re

# def clean_word(self):
#     word = self.cleaned_data.get('word')
#     if not re.match(r'^[\u0600-\u06FFa-zA-Z]+$', word):
#         raise forms.ValidationError("کلمه باید فقط شامل حروف باشد.")
#     return word
    