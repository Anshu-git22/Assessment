from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Profile
from .forms import ProfileForm
import csv


def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/profile_list.html', {'profiles': profiles})


def create_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm()

    return render(request, 'profiles/profile_form.html', {'form': form})


def edit_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profiles/profile_form.html', {'form': form})


def delete_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    profile.delete()
    return redirect('profile_list')


def export_profiles(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="profiles.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'Full Name', 'Age', 'Email', 'Location', 'Bio', 'Visibility'])

    profiles = Profile.objects.all()

    for profile in profiles:
        writer.writerow([
            profile.username,
            profile.full_name,
            profile.age,
            profile.email,
            profile.location,
            profile.bio,
            'Public' if profile.is_public else 'Private'
        ])

    return response

# views.py me
def delete_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)

    if request.method == "POST":
        profile.delete()
        return redirect('profile_list')

    return render(request, 'profiles/delete_confirm.html', {'profile': profile})