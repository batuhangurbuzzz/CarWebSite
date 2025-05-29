from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget

class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuModel
        fields = '__all__'
        exclude = ['createdAt','updatedAt','deleted_at',]
        
        
class PageForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = PageModel
        fields = '__all__'
        exclude = ['createdAt','updatedAt','deleted_at',]
        
        
class PageTypeForm(forms.ModelForm):
    class Meta:
        model = PageTypeModel
        fields = '__all__'
        exclude = ['createdAt','updatedAt','deleted_at',]
        
        
class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = BlogModel
        fields = '__all__'
        exclude = ['createdAt','updatedAt','deleted_at',]
        