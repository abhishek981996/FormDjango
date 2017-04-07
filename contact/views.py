from contact.forms import ContactForm
from django.shortcuts import render

# add to your views
def contact(request):
    form_class = ContactForm
    
    return render(request, 'contact.html', {
        'form': form_class,
    })