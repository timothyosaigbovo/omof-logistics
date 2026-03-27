from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    """Display and edit user profile"""
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
    else:
        form = UserProfileForm(instance=user_profile)

    template = 'accounts/profile.html'
    context = {
        'form': form,
        'profile': user_profile,
    }
    return render(request, template, context)


@login_required
def dashboard(request):
    """Customer dashboard"""
    user_profile = get_object_or_404(UserProfile, user=request.user)

    template = 'accounts/dashboard.html'
    context = {
        'profile': user_profile,
    }
    return render(request, template, context)