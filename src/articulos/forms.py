from django import forms
from .models import Articulo
from ckeditor.widgets import CKEditorWidget

class CrearArticuloForm(forms.ModelForm):    
    contenido = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Articulo
        fields = '__all__'
        exclude = ('autor',)
        
        widgets = {
            'titulo' : forms.TextInput(attrs= {'class' : 'form-control'}),
            'bajada' : forms.TextInput(attrs= {'class' : 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control-file'}),
            'publicado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'categoria' : forms.Select(attrs={'class' : 'form-select'}),
            'etiqueta': forms.CheckboxSelectMultiple
        }