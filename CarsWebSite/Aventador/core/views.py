from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *

def index(request):
    return render(request, "pages/index.html")

# Blog Ayarları Başlangıç

def blogIndex(request):
    blogs = BlogModel.active_objects.all()
    
    return render(request, "pages/BlogTemp/index.html", {'blogs':blogs})

def createBlogView(request):
    form = BlogForm(request.POST or None)
    
    if request.method == 'POST':
        form = BlogForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('blogList')
        else:
            form = BlogForm()
    return render(request, "pages/BlogTemp/createBlog.html", {'form':form})

def updateBlogView(request, id):
    blog = get_object_or_404(BlogModel, pk=id)
    
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        
        if form.is_valid():
            form.save()
            return redirect('blogList')
    else:
        form = BlogForm(instance=blog)
            
    context = {
        'form':form,
        'blog':blog
    }
    return render(request, "pages/BlogTemp/updateBlog.html", context)

def deleteBlogView(request, id):
    blog = get_object_or_404(BlogModel, pk=id)
    
    if request.method == 'POST':
        blog.delete()
        return redirect('blogList')
    return render(request, "pages/BlogTemp/deleteBlog.html", {'blog':blog})

# Blog Ayarları Bitiş

# Genel Ayarlar Başlangıç

def generalSettingsIndex(request):
    generals = GeneralSettingsModel.active_objects.all()
    
    return render(request, "pages/GeneralSettingsTemp/index.html", {'generals':generals})

def createGeneralSettingsView(request):
    form = GeneralSettingsForm(request.POST or None)
    
    if request.method == 'POST':
        form = GeneralSettingsForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('generalSettingsList')
        else:
            form = BlogForm()
    return render(request, "pages/GeneralSettingsTemp/createGeneralSettings.html", {'form':form})

def updateGeneralSettingsView(request, id):
    general = get_object_or_404(GeneralSettingsModel, pk=id)
    
    if request.method == 'POST':
        form = GeneralSettingsForm(request.POST, instance=general)
        
        if form.is_valid():
            form.save()
            return redirect('generalSettingsList')
    else:
        form = GeneralSettingsForm(instance=general)
            
    context = {
        'form':form,
        'general':general
    }
    return render(request, "pages/GeneralSettingsTemp/updateGeneralSettings.html", context)

def deleteGeneralSettingsView(request, id):
    general = get_object_or_404(GeneralSettingsModel, pk=id)
    
    if request.method == 'POST':
        general.delete()
        return redirect('generalSettingsList')
    return render(request, "pages/GeneralSettingsTemp/deleteGeneralSettings.html", {'general':general})

# Genel Ayarlar Bitiş

# Menü Ayarları Başlangıç
def menuIndex(request):
    menus = MenuModel.active_objects.all()
    return render(request, "pages/MenusTemp/index.html", {'menus':menus})

def createMenuView(request):
    form = MenuForm(request.POST or None)
    if request.method == 'POST':
        form = MenuForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('menuList')
    else:
        form = MenuForm()
    return render(request, 'pages/MenusTemp/createMenu.html', {'form':form})

def updateMenuView(request, id):
    menu = get_object_or_404(MenuModel, pk=id)
    
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        
        if form.is_valid():
            form.save()
            return redirect('menuList')
    else:
            form = MenuForm(instance=menu)
            
    context={
        'form' : form,
        'menu' : menu
    }
    return render(request, 'pages/MenusTemp/updateMenu.html', context)

def deleteMenuView(request, id):
    menu = get_object_or_404(MenuModel, pk=id)
    if request.method == 'POST':
        menu.delete()
        return redirect('menuList')
    return render(request, "pages/MenusTemp/deleteMenu.html", {"menu":menu})

# Menü Ayarları Bitiş

# Sayfa Ayarları Başlangıç

def pageIndex(request):
    pages = PageModel.active_objects.all()
    
    return render(request, "pages/PagesTemp/index.html", {'pages':pages})

def createPageView(request):
    form = PageForm(request.POST or None)
    
    if request.method == 'POST':
        form = PageForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('pageList')
        else:
            form = PageForm()
    return render(request, "pages/PagesTemp/createPage.html", {'form':form})

def updatePageView(request, id):
    page = get_object_or_404(PageModel, pk=id)
    
    if request.method == 'POST':
        form = PageForm(request.POST, instance=page)
        
        if form.is_valid():
            form.save()
            
            return redirect('pageList')
        else:
            form = PageForm(request.method, instance=page)
    context={
        'form' : form,
        'pages' : page
    }
    return render(request, "pages/PagesTemp/updatePage.html", context)

def deletePageView(request, id):
    page = get_object_or_404(PageModel, pk=id)
    if request.method == 'POST':
        page.delete()
        return redirect('pageList')
        
    return render(request, "pages/PagesTemp/delete.html", {'pages':page})

# Sayfa Ayarları Bitiş


# Sayfa Tipi Ayarları Başlangıç

def pageTypeIndex(request):
    pageTypes = PageTypeModel.active_objects.all()
    
    return render(request, "pages/PageTypeTemp/index.html", {'pageTypes':pageTypes})

def createPageType(request):
    form = PageTypeForm(request.POST or None)
    
    if request.method == 'POST':
        form = PageTypeForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('pageTypeList')
            
        else:
            form = PageTypeForm()
            
    return render(request, "pages/PageTypeTemp/createPageType.html", {"form":form})

def updatePageType(request, id):
    pageType = get_object_or_404(PageTypeModel, pk=id)
    
    if request.method == 'POST':
        form = PageTypeForm(request.POST, instance=pageType)
        
        if form.is_valid():
            form.save()
            return redirect('pageTypeList')
        else:
            form = PageTypeForm(instance=pageType)
            
    context={
        'form' : form,
        'pageType' : pageType
    }
    return render(request, "pages/PageTypeTemp/updatePageType.html", context)

def deletePageType(request, id):
    pageType = get_object_or_404(PageTypeModel, pk=id)
    
    if request.method == 'POST':
        pageType.delete()
        return redirect('pageTypeList')
    return render(request, "pages/PageTypeTemp/deletePageType.html", {"pageType":pageType})
# Sayfa Tipi Ayarları Bitiş

# Sosyal Medya Ayarları Başlangıç

def socialMediaIndex(request):
    socialMedias = SocialMediaModel.active_objects.all()
    
    return render(request, "pages/SocialMediaTemp/index.html", {'socialMedias':socialMedias})

def createsocialMediaView(request):
    form = SocialMediaForm(request.POST or None)
    
    if request.method == 'POST':
        form = SocialMediaForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('socialMediaList')
        else:
            form = SocialMediaForm()
    return render(request, "pages/SocialMediaTemp/createSocialMedia.html", {'form':form})

def updatesocialMediaView(request, id):
    socialMedia = get_object_or_404(SocialMediaModel, pk=id)
    
    if request.method == 'POST':
        form = SocialMediaForm(request.POST, instance=socialMedia)
        
        if form.is_valid():
            form.save()
            return redirect('socialMediaList')
    else:
        form = SocialMediaForm(instance=socialMedia)
            
    context = {
        'form':form,
        'socialMedia':socialMedia
    }
    return render(request, "pages/SocialMediaTemp/updateSocialMedia.html", context)

def deletesocialMediaView(request, id):
    socialMedia = get_object_or_404(SocialMediaModel, pk=id)
    
    if request.method == 'POST':
        socialMedia.delete()
        return redirect('socialMediaList')
    return render(request, "pages/SocialMediaTemp/deleteSocialMedia.html",{'socialMedia':socialMedia})

# Sosyal Medya Ayarları Bitiş

# Slider Ayarları Başlangıç

def sliderIndex(request):
    sliders = SliderModel.active_objects.all()
    
    return render(request, "pages/SliderTemp/index.html", {'sliders':sliders})

def createSliderView(request):
    form = SliderForm(request.POST or None)
    
    if request.method == 'POST':
        form = SliderForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('sliderList')
        else:
            form = SliderForm()
    return render(request, "pages/SliderTemp/createSlider.html", {'form':form})

def updateSliderView(request, id):
    slider = get_object_or_404(SliderModel, pk=id)
    
    if request.method == 'POST':
        form = SliderForm(request.POST, instance=slider)
        
        if form.is_valid():
            form.save()
            return redirect('sliderList')
    else:
        form = SliderForm(instance=slider)
            
    context = {
        'form':form,
        'slider':slider
    }
    return render(request, "pages/SliderTemp/updateSlider.html", context)

def deleteSliderView(request, id):
    slider = get_object_or_404(SliderModel, pk=id)
    
    if request.method == 'POST':
        slider.delete()
        return redirect('sliderList')
    return render(request, "pages/SliderTemp/deleteSlider.html",{'slider':slider})

# Slider Ayarları Bitiş

# Cars Başlangıç

def carsIndex(request):
    cars = CarsModel.active_objects.all()
    
    return render(request, "pages/CarsTemp/index.html", {'cars':cars})

def createCarsView(request):
    form = CarsForm(request.POST or None)
    
    if request.method == 'POST':
        form = CarsForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('carsList')
        else:
            form = CarsForm()
    return render(request, "pages/CarsTemp/create.html", {'form':form})

def updateSliderView(request, id):
    car = get_object_or_404(CarsModel, pk=id)
    
    if request.method == 'POST':
        form = CarsForm(request.POST, instance=car)
        
        if form.is_valid():
            form.save()
            return redirect('carsList')
    else:
        form = CarsForm(instance=car)
            
    context = {
        'form':form,
        'car':car
    }
    return render(request, "pages/CarsTemp/update.html", context)

def deleteSliderView(request, id):
    car = get_object_or_404(CarsModel, pk=id)
    
    if request.method == 'POST':
        car.delete()
        return redirect('carsList')
    return render(request, "pages/CarsTemp/delete.html",{'car':car})

# Cars Bitiş


# Contact Başlangıç
def contactIndex(request):
    contacts = ContactModel.active_objects.all()
    
    return render(request, "pages/ContactTemp/index.html", {'cars':contacts})

# Contact Bitiş