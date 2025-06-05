from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    
    # Cars Start
    path('arac', views.carsIndex, name='carsList'),
    path('arac/olustur', views.createCarsView, name='carsCreate'),
    path('arac/guncelle/<int:id>', views.updateCarsView, name='carsUpdate'),
    path('arac/sil/<int:id>', views.deleteCarsView, name='carsDelete'),
    # Cars Finish
    
    # Blog Start
    path('blog', views.blogIndex, name='blogList'),
    path('blog/olustur', views.createBlogView, name='blogCreate'),
    path('blog/guncelle/<int:id>', views.updateBlogView, name='blogUpdate'),
    path('blog/sil/<int:id>', views.deleteBlogView, name='blogDelete'),
    # Blog Finish
    
    # Contact Start
    path('iletisim', views.contactIndex, name='contactList'),
    path('iletisim/<int:id>', views.contactDetails, name='contactDetails'),
    # Contact Finish
    
    # General Settings Start
    path('genel-ayarlar', views.blogIndex, name='generalSettingsList'),
    path('genel-ayarlar/olustur', views.createGeneralSettingsView, name='generalSettingsCreate'),
    path('genel-ayarlar/guncelle/<int:id>', views.updateGeneralSettingsView, name='generalSettingsUpdate'),
    path('genel-ayarlar/sil/<int:id>', views.deleteGeneralSettingsView, name='generalSettingsDelete'),
    # General Settings Finish
    
    # Menu Start
    path('menu',views.menuIndex, name="menuList"),
    path('menu/olustur',views.createMenuView, name="menuCreate"),
    path('menu/guncelle/<int:id>', views.updateMenuView, name="menuUpdate"),
    path('menu/sil/<int:id>', views.deleteMenuView, name="menuDelete"),
    # Menu Finish
    
    # Pages Start
    path('sayfalar',views.pageIndex, name="pageList"),
    path('sayfalar/olustur',views.createPageView, name="pageCreate"),
    path('sayfalar/guncelle/<int:id>', views.updatePageView, name="pageUpdate"),
    path('sayfalar/sil/<int:id>', views.deletePageView, name="pageDelete"),
    # Pages Finish
    
    # Pages Type Start
    path('sayfa-tipi-ayarlari',views.pageTypeIndex, name="pageTypeList"),
    path('sayfa-tipi-ayarlari/olustur',views.createPageType, name="pageTypeCreate"),
    path('sayfa-tipi-ayarlari/guncelle/<int:id>', views.updatePageType, name="pageTypeUpdate"),
    path('sayfa-tipi-ayarlari/sil/<int:id>', views.deletePageType, name="pageTypeDelete"),
    # Pages Type Finish
    
    # Social Media Start
    path('sosyal-medya',views.pageTypeIndex, name="socialMediaList"),
    path('sosyal-medya/olustur',views.createPageType, name="socialMediaCreate"),
    path('sosyal-medya/guncelle/<int:id>', views.updatePageType, name="socialMediaUpdate"),
    path('sosyal-medya/sil/<int:id>', views.deletePageType, name="socialMediaDelete"),
    # Social Media Finish
    
    # Social Media Start
    path('slider',views.pageTypeIndex, name="sliderList"),
    path('slider/olustur',views.createPageType, name="sliderCreate"),
    path('slider/guncelle/<int:id>', views.updatePageType, name="sliderUpdate"),
    path('slider/sil/<int:id>', views.deletePageType, name="sliderDelete"),
    # Social Media Finish
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)