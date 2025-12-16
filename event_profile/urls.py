from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.event_list, name='event_list'),
    path('events/<int:pk>/', views.event_detail, name='event_detail'),
    path('events/create/', views.event_create, name='event_create'),
    path('categories/', views.category_list, name='category_list'),
    path('companies/', views.company_list, name='company_list'),
    path('profile/', views.profile_detail, name='profile_detail'),
]