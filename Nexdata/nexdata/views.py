from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm

def main(request):
    context = {
        'main_text': "Gør dine data til indsigter", 
    }
    return render(request, 'main.html', context)

def contact(request):
    success_message = None  # a variable for success message
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            success_message = "Tak for din besked! Vi vender tilbage til dig snart." 
            form = ContactForm()  # Reset the form after submission
    else:
        form = ContactForm()

    # Pass the form and success message to the template
    return render(request, 'contact.html', {'form': form, 'success_message': success_message})

def about(request):
    context = {
        'about_text':"Om Nexdata.",
        }
    return render(request, 'about.html', context)

def portfolio(request):
    context = {
        'portfolio_text':"Nysgerrighed i Tal: En Data Portefølje",
        }
    return render(request, 'portfolio.html', context)
