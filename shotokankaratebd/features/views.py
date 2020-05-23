from django.shortcuts import render
from .models import Photo, Contact

def home_page(request):
    return render(request, 'features/home_page.html', {})

def view_schedule(request):
    return render(request, 'features/view_schedule.html', {})

def view_syllabus(request):
    return render(request, 'features/view_syllabus.html', {})

def view_notice(request):
    return render(request, 'features/view_notice.html', {})

def view_records(request):
    return render(request, 'features/view_records.html', {})

def view_highlights(request):
    return render(request, 'features/view_highlights.html', {})

def view_achievements(request):
    return render(request, 'features/view_achievements.html', {})

def view_gallery(request):
    photo_list = Photo.objects.all()
    context = {

        'photo_list' : photo_list

    }
    return render(request, 'features/view_gallery.html', context)

def view_contact(request):
    contact_list = Contact.objects.all()
    context = {

        'contact_list' : contact_list

    }
    return render(request, 'features/view_contact.html', context)

def about(request):
    return render(request, 'features/about.html', {})