"""
URL configuration for Aventador project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('katman-panel', views.index, name="index"),
    
    # Blog Start
    path('blog', views.blogIndex, name='blogList'),
    path('blog/olustur', views.createBlogView, name='blogCreate'),
    path('blog/guncelle/<int:id>', views.updateBlogView, name='blogUpdate'),
    path('blog/sil/<int:id>', views.deleteBlogView, name='blogDelete'),
    # Blog Finish
    
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