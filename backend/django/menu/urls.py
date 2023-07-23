from django.urls import path
from phone_numbers import views

urlpatterns = [
    path('add/', views.add_phone_number, name='add_phone_number'),
    path('list/', views.list_phone_numbers, name='list_phone_numbers'),
    path('delete/<int:phone_number_id>/', views.delete_phone_number, name='delete_phone_number'),
]
