from django.urls import path
from . import views

# app_name='features'

urlpatterns = [

    path('', views.home_page, name='home_page'),
    path('view_schedule/', views.view_schedule, name='view_schedule'),
    path('view_syllabus/', views.view_syllabus, name='view_syllabus'),
    path('view_records/', views.view_records, name='view_records'),
    path('view_highlights/', views.view_highlights, name='view_highlights'),
    path('view_achievements/', views.view_achievements, name='view_achievements'),
    path('view_gallery/', views.view_gallery, name='view_gallery'),
    path('view_contact/', views.view_contact, name='view_contact'),
    path('about/', views.about, name='about'),
    # path('/', views., name=''),

]