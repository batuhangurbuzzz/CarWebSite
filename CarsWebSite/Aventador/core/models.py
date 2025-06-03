from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import os

# Create your models here.
class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull = True)

class AbstractModel(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    
    updatedAt = models.DateTimeField(auto_now=True, verbose_name="Güncelleme Tarihi")
    
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Silinme Tarihi")
    
    objects = models.Manager()
    active_objects = ActiveManager()
    
    class Meta:
        abstract = True
    
    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()
        
    def restore(self):
        self.deleted_at = None
        self.save()
        
        
    def delete(self, *args, **kwargs):
        self.soft_delete()

class PageModel(AbstractModel):
    name = models.CharField(max_length=50, verbose_name="Sayfa Adı")
    
    title = models.CharField(max_length=75, verbose_name="SEO Başlık",null=True, blank=True, help_text="SEO için META title alanı sayfanın google aramalarında gözükecek başlık kısmı için kullanılır. Maksimum 75 karakter uzunlukta olabilir.")
    
    description = models.CharField(max_length=160, verbose_name="SEO Açıklama", null=True, blank=True, help_text="SEO için META description alanı sayfanın google aramalarında gözükecek açıklama kısmı için kullanılır. Maksimum 160 karakter uzunlukta olabilir.")
    
    keywords = models.CharField(max_length=150, verbose_name="SEO Anahtar Kelime", null=True, blank=True, help_text="SEO için META keywords alanı, sayfanın google aramalarında ki anahtar kelimeleri için kullanılır. Maksimum 150 karakter uzunlukta olabilir.")
    
    content = RichTextField(verbose_name="Sayfa İçeriği", help_text="Sayfa içeriğini HTML formatında girip kaydet tuşuna basınız. Düzenleme yapma kısmında yine aynı şekilde html formatında düzenleyip kaydet yapınız.")
    
    isActive = models.BooleanField(default=False, verbose_name="Sayfayı Yayına Al", help_text="Sayfanın aktif ise tik koyunuz değilse ellemeyiniz.")
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Sayfa Ayarı"
        verbose_name_plural = "Sayfa Ayarları"
        
class MenuModel(AbstractModel):
    name = models.CharField(max_length=30, verbose_name="Menü Adı")
    description = models.CharField(max_length=45, verbose_name="Menü Açıklaması", null=True, blank=True, help_text="Opsiyonel olarak bulunmaktadır eğer ki bir açıklama girecekseniz lütfen 45 karakteri geçmeyiniz.")
    
    slug = models.SlugField(null=False, db_index=True, unique=True, blank=True, verbose_name="URL", help_text="Girilen isime göre otomatik oluşturulacaktır. Değiştirmek isterseniz değişiklik yapabilirsiniz.")
    
    page = models.OneToOneField(PageModel, on_delete=models.CASCADE, related_name="menuItem" ,verbose_name="Bağlı Olduğu Sayfa")
    
    addFooter = models.BooleanField(default=False, verbose_name="Footer'e Ekle", help_text="Sayfanın footer kısmında menüyü göstermek isterseniz tik koyunuz istemezseniz ellemeyiniz.")
    
    class Meta:
        verbose_name = "Menü Ayarı"
        verbose_name_plural = "Menü Ayarları"

    def __str__(self):
        return f"{self.name}"
        
class PageTypeModel(AbstractModel):
    name = models.CharField(max_length=100, verbose_name="Sayfa Tipi Adı", help_text="Sayfa tipi adını giriniz. (Örnek: Blog sayfası için Blog yazabilirsiniz).")
    
    page = models.OneToOneField(PageModel, on_delete=models.CASCADE, related_name="pagetype_data",verbose_name="Bağlı Olduğu Sayfa")
    
    class Meta:
        verbose_name="Sayfa Tipi Ayarı"
        verbose_name_plural = "Sayfa Tipi Ayarları"
        
    def __str__(self):
        return f"{self.name}"
       
class BlogModel(AbstractModel):
    name = models.CharField(max_length=100, verbose_name="Blog Adı")
    
    content = RichTextField(verbose_name="Blog İçeriği", help_text="Blog içeriğini HTML formatında girip kaydet tuşuna basınız. Düzenleme yapma kısmında yine aynı şekilde html formatında düzenleyip kaydet yapınız.")
    
    title = models.CharField(max_length=75, verbose_name="SEO Başlık",null=True, blank=True, help_text="SEO için META title alanı sayfanın google aramalarında gözükecek başlık kısmı için kullanılır. Maksimum 75 karakter uzunlukta olabilir.")
    
    description = models.CharField(max_length=160, verbose_name="SEO Açıklama", null=True, blank=True, help_text="SEO için META description alanı sayfanın google aramalarında gözükecek açıklama kısmı için kullanılır. Maksimum 160 karakter uzunlukta olabilir.")
    
    keywords = models.CharField(max_length=150, verbose_name="SEO Anahtar Kelime", null=True, blank=True, help_text="SEO için META keywords alanı, sayfanın google aramalarında ki anahtar kelimeleri için kullanılır. Maksimum 150 karakter uzunlukta olabilir.")
    
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Yazar")
    
    def __str__(self):
        return f"{self.name}"
           
class GeneralSettingsModel(AbstractModel):
    name = models.CharField(verbose_name="Genel Ayar Adı", max_length=100)
    
    bannerImage = models.FileField(upload_to="images", verbose_name="Logo", blank=True, null=True, help_text="Logo varsa resmini yükleyiniz yoksa boş bırakabilirsiniz.")
    
    bannerText = models.CharField(max_length=50, verbose_name="Logo Yazı", blank=True, null=True, help_text="Firma adını logo yerine kullanabilirsiniz. (Örnek: KatmanKod)")
    
    address = models.CharField(verbose_name="Adres", help_text="İş yerinin mevcut adresi varsa giriniz.", null=True, blank=True, max_length=250)
    
    phone = models.CharField(verbose_name="Telefon Numarası", help_text="İş yerinin mevcut telefon numarası varsa giriniz.", null=True, blank=True, max_length=20)
    
    phone2 = models.CharField(verbose_name="Telefon Numarası 2", help_text="İş yerinin mevcut dahili hattı varsa giriniz.", null=True, blank=True, max_length=20)
    
    def __str__(self):
        return f"{self.name}"
    
class SocialMediaModel(AbstractModel):
    icons = (
        ('T','<i class="ri-twitter-x-fill"></i>'),
        ('F','<i class="ri-facebook-fill"></i>'),
        ('L','<i class="ri-linkedin-fill"></i>'),
        ('W','<i class="ri-whatsapp-fill"></i>')
    )
    name = models.CharField(verbose_name="Sosyal Medya Adı", help_text="Hangi sosyal medya alanını eklediğinizin adını giriniz. (Örnek: Twitter)",max_length=50)
    link = models.SlugField(verbose_name="Sosyal Medya Linki", help_text="Sosyal medya adresinizin linkini giriniz.")
    icon = models.CharField(verbose_name="Sosyal Medya İconu", max_length=1, help_text="Eklediğiniz sosyal medyaya göre bir icon seçiniz.", choices=icons)
    
    def __str__(self):
        return f"{self.name}"
        
class SliderModel(AbstractModel):
    name = models.CharField(verbose_name="Slider Adı", max_length=50)
    imageDesktop = models.FileField(upload_to="images", verbose_name="Masaüstü Slider", blank=True, null=True, help_text="Masaüstü Slider Resmi")
    
    imageMobile = models.FileField(upload_to="images", verbose_name="Mobil Slider", blank=True, null=True, help_text="Mobil Slider Resmi")
    
    def __str__(self):
        return f"{self.name}"
    
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if self.imageDesktop:
            imgPathDesktop = self.imageDesktop.path
            
            imgDesktop = Image.open(imgPathDesktop)
            imgDesktop.thumbnail((1000,1000), Image.Resampling.LANCZOS)  # En boy oranını korumak için kullanıyoruz.
            
            thumbIoDesktop = BytesIO()
            
            file_extension_desktop = os.path.splitext(self.imageDesktop.name)[1].lower()
            if file_extension_desktop == '.jpg' or file_extension_desktop == '.jpeg':
                imgDesktop.save(thumbIoDesktop, format='JPEG', quality=90)
            elif file_extension_desktop == '.png':
                imgDesktop.save(thumbIoDesktop, format='PNG')
            elif file_extension_desktop == '.webp':
                imgDesktop.save(thumbIoDesktop, format='WEBP')
            else:
                imgDesktop.save(thumbIoDesktop, format='JPEG', quality=90) 
                
                
            self.imageDesktop.save(os.path.basename(self.imageDesktop.name), 
                                   ContentFile(thumbIoDesktop.getvalue()), 
                                   save=False)
            
            # Mobile 
            
            if self.imageMobile:
                img_path_mobile = self.imageMobile.path
                img_mobile = Image.open(img_path_mobile)
                
                img_mobile.thumbnail((350, 350), Image.Resampling.LANCZOS) # En boy oranını korur

                thumb_io_mobile = BytesIO()
                file_extension_mobile = os.path.splitext(self.imageMobile.name)[1].lower()
                if file_extension_mobile == '.jpg' or file_extension_mobile == '.jpeg':
                    img_mobile.save(thumb_io_mobile, format='JPEG', quality=90)
                elif file_extension_mobile == '.png':
                    img_mobile.save(thumb_io_mobile, format='PNG')
                elif file_extension_mobile == '.webp':
                    img_mobile.save(thumb_io_mobile, format='WEBP')
                else:
                    img_mobile.save(thumb_io_mobile, format='JPEG', quality=90)
                
                self.imageMobile.save(os.path.basename(self.imageMobile.name), 
                                    ContentFile(thumb_io_mobile.getvalue()), 
                                    save=False)

            super().save(*args, **kwargs)
                
class CarsModel(AbstractModel):
    name = models.CharField(verbose_name="Araç Adı", max_length=100, help_text="Aracın Marka ve Modelini Giriniz.")
    
    image = models.FileField(upload_to="images", verbose_name="Araç Resmi", help_text="Aracın Resmini Ekleyiniz.")


class ContactModel(AbstractModel):
    email = models.EmailField(verbose_name="E Posta Adresi")
    
    messages = models.TextField(verbose_name="Mesaj") 
    
    