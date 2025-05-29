# seed_data.py

import os
import django
from faker import Faker
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.utils.text import slugify
import random

# Django'yu yapılandır
# BURAYI KENDİ PROJENİZİN ANA KLASÖR ADIYLA DEĞİŞTİRİN
# Örn: 'MyProject.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Aventador.settings')
django.setup()

# Modelleri import et
from django.contrib.auth.models import User
# core/models.py dosyanızdan modelleri import ediyoruz
from core.models import PageModel, MenuModel, PageTypeModel, BlogModel

fake = Faker('tr_TR') # Türkçe karakterler ve formatlar için

def generate_dummy_data(
    num_users=5,
    num_pages=15,
    num_blog_posts=20
):
    print("--- Sahte veri oluşturuluyor... ---")

    # --- Kullanıcı Oluşturma ---
    print(f"\n{num_users} adet kullanıcı oluşturuluyor...")
    created_users = []
    
    # Süper kullanıcıyı kontrol et veya oluştur
    try:
        super_user = User.objects.get(username='superadmin')
        print("Süper Kullanıcı 'superadmin' zaten mevcut. Yeni oluşturulmadı.")
    except User.DoesNotExist:
        super_user = User.objects.create(
            username='superadmin',
            email='admin@example.com',
            first_name='Admin',
            last_name='User',
            password=make_password('adminpass'), # Admin için özel şifre
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        print(f"Süper Kullanıcı oluşturuldu: {super_user.username}")
    created_users.append(super_user)

    # Diğer normal kullanıcıları oluştur
    for i in range(num_users - 1): # num_users kadar kullanıcı istiyorsak, 1 tanesi superuser
        username_base = fake.user_name()
        username = username_base
        k = 0
        while User.objects.filter(username=username).exists():
            username = f"{username_base}{k}"
            k += 1

        email_base = fake.email()
        email = email_base
        k = 0
        while User.objects.filter(email=email).exists():
            email = f"user{k}_{email_base}"
            k += 1

        first_name = fake.first_name()
        last_name = fake.last_name()
        password = make_password('12345')

        user = User.objects.create(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_staff=False,
            is_superuser=False,
            is_active=True
        )
        print(f"Normal Kullanıcı oluşturuldu: {user.username}")
        created_users.append(user)

    # --- Sayfa Oluşturma (PageModel) ---
    print(f"\n{num_pages} adet Sayfa (PageModel) oluşturuluyor...")
    created_pages = []
    
    # PageModel için maksimum uzunluklar
    PAGE_NAME_MAX_LENGTH = 50
    PAGE_SEO_TITLE_MAX_LENGTH = 75
    PAGE_SEO_DESCRIPTION_MAX_LENGTH = 160
    PAGE_SEO_KEYWORDS_MAX_LENGTH = 150

    for _ in range(num_pages):
        page_name = fake.sentence(nb_words=random.randint(2, 5)).replace('.', '').strip()[:PAGE_NAME_MAX_LENGTH]
        seo_title = fake.sentence(nb_words=random.randint(5, 10)).replace('.', '').strip()[:PAGE_SEO_TITLE_MAX_LENGTH]
        seo_description = fake.paragraph(nb_sentences=random.randint(1, 2)).replace('.', '').strip()[:PAGE_SEO_DESCRIPTION_MAX_LENGTH]
        seo_keywords = ", ".join(fake.words(nb=random.randint(5, 10)))[:PAGE_SEO_KEYWORDS_MAX_LENGTH]
        
        # isActive alanını rastgele belirle
        is_active = fake.boolean(chance_of_getting_true=70) # %70 ihtimalle aktif olsun

        page = PageModel.objects.create(
            name=page_name,
            title=seo_title,
            description=seo_description,
            keywords=seo_keywords,
            content=f"<p>{fake.paragraphs(nb=random.randint(5, 15), ext_word_list=None)}</p>", # RichTextField için HTML içeriği
            isActive=is_active
        )
        created_pages.append(page)
        print(f"Sayfa oluşturuldu: '{page.name}' (Aktif: {page.isActive})")

    # --- Sayfa Tipi Oluşturma (PageTypeModel) ve Sayfalara Bağlama ---
    # PageTypeModel'in PageModel ile OneToOneField ilişkisi var.
    # Her PageModel'e yalnızca bir PageTypeModel bağlanabilir.
    print(f"\n{len(created_pages)} adet Sayfa Tipi (PageTypeModel) oluşturuluyor ve sayfalara bağlanıyor...")
    page_type_suggestions = ["Ana Sayfa Tipi", "Hakkımızda Tipi", "Hizmetlerimiz Tipi", "İletişim Tipi", "Galeri Tipi",
                             "Blog Tipi", "Ürünler Tipi", "Sıkça Sorulanlar Tipi", "Kariyer Tipi", "Gizlilik Politikası Tipi",
                             "Referanslar Tipi", "Ekibimiz Tipi", "Projeler Tipi", "Destek Tipi", "Basın Odası Tipi"]

    # Sayfaları karıştırarak PageType ve Menu için farklı eşleşmeler sağlayabiliriz
    random.shuffle(created_pages) 
    
    # Her bir PageModel için bir PageTypeModel oluşturuyoruz
    for i, page_obj in enumerate(created_pages):
        # Yeterli öneri adı varsa onu kullan, yoksa rastgele kelime üret
        type_name = page_type_suggestions[i] if i < len(page_type_suggestions) else fake.word().capitalize() + " Tipi"
        
        # OneToOneField hatasını önlemek için try-except kullanıyoruz
        # Aynı sayfaya birden fazla PageTypeModel veya MenuModel bağlanamaz
        try:
            PageTypeModel.objects.create(
                page=page_obj,
                name=type_name # PageTypeModel'de 'name' alanı var, 'description' yok
            )
            print(f"Sayfa Tipi '{type_name}' oluşturuldu ve '{page_obj.name}' sayfasına bağlandı.")
        except Exception as e:
            print(f"Uyarı: Sayfa Tipi oluşturulurken hata oluştu (muhtemelen ilişkilendirme hatası veya veri mevcut): {e}")

    # --- Menü Öğesi Oluşturma (MenuModel) ve Sayfalara Bağlama ---
    # MenuModel'in de PageModel ile OneToOneField ilişkisi var.
    print(f"\n{len(created_pages)} adet Menü Öğesi (MenuModel) oluşturuluyor ve sayfalara bağlanıyor...")
    menu_item_suggestions = ["Anasayfa", "Hakkımızda", "Hizmetler", "İletişim", "Galeri",
                             "Blog", "Ürünler", "SSS", "Kariyer", "Gizlilik",
                             "Referanslar", "Ekip", "Projeler", "Destek", "Basın"]
    
    MENU_NAME_MAX_LENGTH = 30
    MENU_DESCRIPTION_MAX_LENGTH = 45
    MENU_BANNER_TEXT_MAX_LENGTH = 50

    # created_pages listesi zaten karıştırılmıştı
    for i, page_obj in enumerate(created_pages):
        # Yeterli öneri adı varsa onu kullan, yoksa rastgele kelime üret
        menu_name = menu_item_suggestions[i] if i < len(menu_item_suggestions) else fake.word().capitalize() + " Menü"
        
        # Slug oluşturma
        menu_slug = slugify(menu_name)
        # Benzersiz slug sağlamak için kontrol
        k = 0
        original_slug = menu_slug
        while MenuModel.objects.filter(slug=menu_slug).exists():
            menu_slug = f"{original_slug}-{k}"
            k += 1

        try:
            MenuModel.objects.create(
                page=page_obj,
                name=menu_name[:MENU_NAME_MAX_LENGTH],
                description=fake.sentence(nb_words=random.randint(5, 8))[:MENU_DESCRIPTION_MAX_LENGTH],
                # bannerImage ve bannerText alanlarını boş bırakıyoruz (null=True, blank=True)
                bannerText=fake.company()[:MENU_BANNER_TEXT_MAX_LENGTH] if fake.boolean(chance_of_getting_true=50) else None,
                slug=menu_slug
            )
            print(f"Menü Öğesi '{menu_name}' oluşturuldu ve '{page_obj.name}' sayfasına bağlandı.")
        except Exception as e:
            print(f"Uyarı: Menü Öğesi oluşturulurken hata oluştu (muhtemelen ilişkilendirme hatası veya veri mevcut): {e}")

    # --- Blog Yazısı Oluşturma (BlogModel) ---
    print(f"\n{num_blog_posts} adet Blog Yazısı (BlogModel) oluşturuluyor...")
    
    # BlogModel için maksimum uzunluklar
    BLOG_NAME_MAX_LENGTH = 100
    BLOG_SEO_TITLE_MAX_LENGTH = 75
    BLOG_SEO_DESCRIPTION_MAX_LENGTH = 160
    BLOG_SEO_KEYWORDS_MAX_LENGTH = 150

    # Sadece normal kullanıcıları (is_superuser=False olanları) yazar olarak kullan
    normal_users = [u for u in created_users if not u.is_superuser]
    if not normal_users:
        print("Uyarı: Hiç normal kullanıcı oluşturulmadığı için blog yazıları oluşturulamadı.")
        print("Lütfen 'num_users' değerini artırın veya oluşturulan kullanıcıları kontrol edin.")
    else:
        for _ in range(num_blog_posts):
            author = random.choice(normal_users)
            
            blog_name = fake.sentence(nb_words=random.randint(3, 8)).replace('.', '').strip()[:BLOG_NAME_MAX_LENGTH]
            seo_title = fake.sentence(nb_words=random.randint(5, 10)).replace('.', '').strip()[:BLOG_SEO_TITLE_MAX_LENGTH]
            seo_description = fake.paragraph(nb_sentences=random.randint(1, 2)).replace('.', '').strip()[:BLOG_SEO_DESCRIPTION_MAX_LENGTH]
            seo_keywords = ", ".join(fake.words(nb=random.randint(5, 10)))[:BLOG_SEO_KEYWORDS_MAX_LENGTH]

            blog_post = BlogModel.objects.create(
                name=blog_name,
                content=f"<p>{fake.paragraphs(nb=random.randint(3, 7), ext_word_list=None)}</p>", # RichTextField için HTML içeriği
                title=seo_title,
                description=seo_description,
                keywords=seo_keywords,
                author=author,
            )
            print(f"Blog yazısı oluşturuldu: '{blog_post.name[:30]}...' yazan: {blog_post.author.username}")

    print("\n--- Sahte veri oluşturma tamamlandı. ---")

if __name__ == '__main__':
    # DİKKAT: Bu kısım aktifken, script her çalıştığında
    #         mevcut TÜM verileriniz silinecektir!
    #         Veri silme sırası önemlidir: ilişkili nesnelerden bağımsız nesnelere doğru silin.
    print("\nMevcut veriler siliniyor...")
    try:
        BlogModel.objects.all().delete()
        MenuModel.objects.all().delete()
        PageTypeModel.objects.all().delete()
        PageModel.objects.all().delete()
        # Sadece normal kullanıcıları silin. Süper kullanıcıyı koruyun.
        User.objects.filter(is_superuser=False).delete()
        print("Mevcut veriler silindi.")
    except Exception as e:
        print(f"Veri silinirken hata oluştu: {e}. Muhtemelen tablolar boş veya bir bağımlılık sorunu var.")

    generate_dummy_data(num_users=5, num_pages=15, num_blog_posts=20)