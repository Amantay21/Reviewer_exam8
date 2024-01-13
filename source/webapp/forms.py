from django import forms

from webapp.models import Products, Reviews


class ProductForms(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('title', 'description', 'category', 'image')


class ReviewForms(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('author', 'product', 'description', 'grade', 'moderation')


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')
