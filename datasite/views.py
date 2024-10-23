# views.py
from django.shortcuts import render, redirect
from .forms import ContactForm

def index(request):
    form = ContactForm()  # Create an instance of the form
    return render(request, 'index.html', {'form': form}) 
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data
            return redirect('success')  # Assuming you have a success URL
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')
