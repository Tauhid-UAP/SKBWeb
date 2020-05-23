from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Photo(models.Model):
    image = models.ImageField(upload_to='gallery_images')
    description = models.CharField(max_length=200, default="")
    pub_date = models.DateField(auto_now_add=True)
    # username = models.OneToOneField(to=User)

class Contact(models.Model):

    HEAD_INSTRUCTOR = 'Head Instructor'
    INSTRUCTOR = 'Instructor'
    ASSISTANT_INSTRUCTOR = 'Assistant Instructor'

    CONTACT_ROLE_CHOICES = [

        (HEAD_INSTRUCTOR, HEAD_INSTRUCTOR),
        (INSTRUCTOR, INSTRUCTOR),
        (ASSISTANT_INSTRUCTOR, ASSISTANT_INSTRUCTOR)

    ]

    name = models.CharField(max_length=100, help_text='Contact name')
    role = models.CharField(max_length=50, choices=CONTACT_ROLE_CHOICES)
    phone_number = models.CharField(max_length=14, default='+880', help_text='Contact phone number')
    email_address = models.EmailField(blank=True, help_text='Contact email address')
    image = models.ImageField(upload_to='contact_images')