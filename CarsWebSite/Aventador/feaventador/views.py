from django.shortcuts import render, redirect
from core.forms import ContactForm
# Create your views here.
def index(request):
    pass


def contact(request):
    pass

def createCarsView(request):
    form = ContactForm(request.POST or None)
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            form = ContactForm()
    return render(request, "pages/CarsTemp/create.html", {'form':form})