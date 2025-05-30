# Generated by Django 5.2.1 on 2025-05-25 10:35

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updatedAt', models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Silinme Tarihi')),
                ('name', models.CharField(max_length=100, verbose_name='Blog Adı')),
                ('content', ckeditor.fields.RichTextField(help_text='Blog içeriğini HTML formatında girip kaydet tuşuna basınız. Düzenleme yapma kısmında yine aynı şekilde html formatında düzenleyip kaydet yapınız.', verbose_name='Blog İçeriği')),
                ('title', models.CharField(blank=True, help_text='SEO için META title alanı sayfanın google aramalarında gözükecek başlık kısmı için kullanılır. Maksimum 75 karakter uzunlukta olabilir.', max_length=75, null=True, verbose_name='SEO Başlık')),
                ('description', models.CharField(blank=True, help_text='SEO için META description alanı sayfanın google aramalarında gözükecek açıklama kısmı için kullanılır. Maksimum 160 karakter uzunlukta olabilir.', max_length=160, null=True, verbose_name='SEO Açıklama')),
                ('keywords', models.CharField(blank=True, help_text='SEO için META keywords alanı, sayfanın google aramalarında ki anahtar kelimeleri için kullanılır. Maksimum 150 karakter uzunlukta olabilir.', max_length=150, null=True, verbose_name='SEO Anahtar Kelime')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updatedAt', models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Silinme Tarihi')),
                ('name', models.CharField(max_length=50, verbose_name='Sayfa Adı')),
                ('title', models.CharField(blank=True, help_text='SEO için META title alanı sayfanın google aramalarında gözükecek başlık kısmı için kullanılır. Maksimum 75 karakter uzunlukta olabilir.', max_length=75, null=True, verbose_name='SEO Başlık')),
                ('description', models.CharField(blank=True, help_text='SEO için META description alanı sayfanın google aramalarında gözükecek açıklama kısmı için kullanılır. Maksimum 160 karakter uzunlukta olabilir.', max_length=160, null=True, verbose_name='SEO Açıklama')),
                ('keywords', models.CharField(blank=True, help_text='SEO için META keywords alanı, sayfanın google aramalarında ki anahtar kelimeleri için kullanılır. Maksimum 150 karakter uzunlukta olabilir.', max_length=150, null=True, verbose_name='SEO Anahtar Kelime')),
                ('content', ckeditor.fields.RichTextField(help_text='Sayfa içeriğini HTML formatında girip kaydet tuşuna basınız. Düzenleme yapma kısmında yine aynı şekilde html formatında düzenleyip kaydet yapınız.', verbose_name='Sayfa İçeriği')),
                ('isActive', models.BooleanField(default=False, help_text='Sayfanın aktif ise tik koyunuz değilse ellemeyiniz.', verbose_name='Sayfayı Yayına Al')),
            ],
            options={
                'verbose_name': 'Sayfa Ayarı',
                'verbose_name_plural': 'Sayfa Ayarları',
            },
        ),
        migrations.CreateModel(
            name='MenuModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updatedAt', models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Silinme Tarihi')),
                ('name', models.CharField(max_length=30, verbose_name='Menü Adı')),
                ('description', models.CharField(blank=True, help_text='Opsiyonel olarak bulunmaktadır eğer ki bir açıklama girecekseniz lütfen 45 karakteri geçmeyiniz.', max_length=45, null=True, verbose_name='Menü Açıklaması')),
                ('bannerImage', models.FileField(blank=True, help_text='Logo varsa resmini yükleyiniz yoksa boş bırakabilirsiniz.', null=True, upload_to='images', verbose_name='Logo')),
                ('bannerText', models.CharField(blank=True, help_text='Firma adını logo yerine kullanabilirsiniz. (Örnek: KatmanKod)', max_length=50, null=True, verbose_name='Logo Yazı')),
                ('slug', models.SlugField(blank=True, help_text='Girilen isime göre otomatik oluşturulacaktır. Değiştirmek isterseniz değişiklik yapabilirsiniz.', unique=True, verbose_name='URL')),
                ('page', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='menuItem', to='core.pagemodel', verbose_name='Bağlı Olduğu Sayfa')),
            ],
            options={
                'verbose_name': 'Menü Ayarı',
                'verbose_name_plural': 'Menü Ayarları',
            },
        ),
        migrations.CreateModel(
            name='PageTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updatedAt', models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Silinme Tarihi')),
                ('name', models.CharField(help_text='Sayfa tipi adını giriniz. (Örnek: Blog sayfası için Blog yazabilirsiniz).', max_length=100, verbose_name='Sayfa Tipi Adı')),
                ('page', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pagetype_data', to='core.pagemodel', verbose_name='Bağlı Olduğu Sayfa')),
            ],
            options={
                'verbose_name': 'Sayfa Tipi Ayarı',
                'verbose_name_plural': 'Sayfa Tipi Ayarları',
            },
        ),
    ]
