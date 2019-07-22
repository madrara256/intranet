from django import forms
from .models import *
import django_filters

class DocumentFilter(django_filters.FilterSet):
    class Meta:
        model = Document
        fields = [
            'document_category',
        ]

    document_category = django_filters.ModelMultipleChoiceFilter(queryset = DocumentCategory.objects.all(), widget=forms.CheckboxSelectMultiple)
