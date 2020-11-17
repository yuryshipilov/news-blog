from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

from .models import Articles


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'News title'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'News announcement'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'News text'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date of published'
            }),


        }
