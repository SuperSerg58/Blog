from django import forms
from django.core.exceptions import ValidationError
from .models import *


class TagForm(forms.ModelForm):
    # Связываем форму Тэг с моделью Тег в базе данных с указанием полей и виджетов
    class Meta:
        model = Tag
        fields = ('title', 'slug')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    # так как у нас слаг должен быть с маленькой буквы создаем функцию clean_slug

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()  # приводим слаг к нижнему регистру

        # выполяняем проверку, что слаг не может быть 'create' так как конфликт с ссылкой
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')

        # выполняем проверку на уникальность тега
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique. We have "{}" slug already'.format(new_slug))

        return new_slug


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
        }
