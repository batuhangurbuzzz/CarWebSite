from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget

class BaseMeta:
    fields = '__all__'
    exclude = ['createdAt','updatedAt','deleted_at',]

class BaseForm(forms.ModelForm):
    class Meta(BaseMeta):
        pass


class MenuForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = MenuModel
        
        
class PageForm(BaseForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta(BaseForm.Meta):
        model = PageModel
        
        
class PageTypeForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = PageTypeModel

        
class BlogForm(BaseForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta(BaseForm.Meta):
        model = BlogModel
        
class GeneralSettingsForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = GeneralSettingsModel
        
class SocialMediaForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = SocialMediaModel
        
class SliderForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = SliderModel
        
class CarsForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = CarsModel
        
class ContactForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = ContactModel