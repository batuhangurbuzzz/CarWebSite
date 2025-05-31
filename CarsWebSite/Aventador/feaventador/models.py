from core.models import AbstractModel
from django.db import models
class CarsModel(AbstractModel):
    name = models.CharField(verbose_name="Araç Adı", max_length=100, help_text="Aracın Marka ve Modelini Giriniz.")
    
    image = models.FileField(upload_to="images", verbose_name="Araç Resmi", help_text="Aracın Resmini Ekleyiniz.")


class ContactModel(AbstractModel):
    email = models.EmailField(verbose_name="E Posta Adresi")
    
    messages = models.TextField(verbose_name="Mesaj")