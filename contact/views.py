from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    # Pre-fill name and email for logged-in users
    initial = {}
    if request.user.is_authenticated:
        initial['email'] = request.user.email
        initial['name'] = request.user.get_full_name() or request.user.username

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Thank you for your message. We will be in touch shortly.'
            )
            return redirect('contact:contact')
    else:
        form = ContactForm(initial=initial)
    return render(request, 'contact/contact.html', {'form': form})
