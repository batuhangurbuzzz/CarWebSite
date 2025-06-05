from django.shortcuts import render, redirect, get_object_or_404
from core.forms import ContactForm
from core.models import *
from .utils import get_common_context

# Create your views here.
def index(request):
    context = get_common_context()
    return render(request, "frontend/pages/index.html", context)

def page_detail_view(request, slug):
    page = get_object_or_404(PageModel, slug=slug)
    
    context = get_common_context()
    
    context['page'] = page
    context['page_title'] = page.title
    
    return render(request, 'frontend/pages/page_detail.html', context)

def contact(request):
    form = ContactForm(request.POST or None)
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            form = ContactForm()
    return render(request, "frontend/pages/Contact/index.html", {'form':form})
    