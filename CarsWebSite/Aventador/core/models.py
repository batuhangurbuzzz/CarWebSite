from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)


class AbstractModel(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    
    updatedAt = models.DateTimeField(auto_now=True, verbose_name="Güncelleme Tarihi")
    
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Silinme Tarihi")
    
    objects = models.Manager()
    active_objects = ActiveManager()
    
    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()
        
    def restore(self):
        self.deleted_at = None
        self.save()
        
        
    def delete(self, *args, **kwargs):
        self.soft_delete()
    

class MenuModel(AbstractModel):
    name = models.CharField(max_length=30, verbose_name="Menü Adı")
    
    description = models.CharField(max_length=45, verbose_name="Menü Açıklaması", null=True, blank=True, help_text="Opsiyonel olarak bulunmaktadır eğer ki bir açıklama girecekseniz lütfen 45 karakteri geçmeyiniz.")
    
    bannerImage = models.FileField(upload_to="images", verbose_name="Logo", blank=True, null=True, help_text="Logo varsa resmini yükleyiniz yoksa boş bırakabilirsiniz.")
    
    bannerText = models.CharField(max_length=50, verbose_name="Logo Yazı", blank=True, null=True, help_text="Firma adını logo yerine kullanabilirsiniz. (Örnek: KatmanKod)")
    
    slug = models.SlugField(null=False, db_index=True, unique=True, blank=True, verbose_name="URL", help_text="Girilen isime göre otomatik oluşturulacaktır. Değiştirmek isterseniz değişiklik yapabilirsiniz.")
    
    # page 
    
    class Meta:
        verbose_name = "Menü Ayarı"
        verbose_name_plural = "Menü Ayarları"

    def __str__(self):
        return f"{self.name}"
    
class PageModel(AbstractModel):
    name = models.CharField(max_length=50, verbose_name="Sayfa Adı")
    
    title = models.CharField(max_length=75, verbose_name="SEO Başlık",null=True, blank=True, help_text="SEO için META title alanı sayfanın google aramalarında gözükecek başlık kısmı için kullanılır. Maksimum 75 karakter uzunlukta olabilir.")
    
    description = models.CharField(max_length=160, verbose_name="SEO Açıklama", null=True, blank=True, help_text="SEO için META description alanı sayfanın google aramalarında gözükecek açıklama kısmı için kullanılır. Maksimum 160 karakter uzunlukta olabilir.")
    
    keywords = models.CharField(max_length=150, verbose_name="SEO Anahtar Kelime", null=True, blank=True, help_text="SEO için META keywords alanı, sayfanın google aramalarında ki anahtar kelimeleri için kullanılır. Maksimum 150 karakter uzunlukta olabilir.")
    
    content = RichTextField(verbose_name="Sayfa İçeriği", help_text="Sayfa içeriğini HTML formatında girip kaydet tuşuna basınız. Düzenleme yapma kısmında yine aynı şekilde html formatında düzenleyip kaydet yapınız.")
    
    isActive = models.BooleanField(default=False, verbose_name="Sayfayı Yayına Al", help_text="Sayfanın aktif ise tik koyunuz değilse ellemeyiniz.")
    
    # pageType
    
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Sayfa Ayarı"
        verbose_name_plural = "Sayfa Ayarları"
        
class PageTypeModel(AbstractModel):
    name = models.CharField(max_length=100, verbose_name="Sayfa Tipi Adı", help_text="Sayfa tipi adını giriniz. (Örnek: Blog sayfası için Blog yazabilirsiniz).")
    
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
        
    
    
    
    