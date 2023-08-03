from django.urls import path, include
from phone_numbers import views
from django.contrib import admin
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'phone-numbers', views.PhoneNumberViewSet)

urlpatterns = [
    path('add/', views.add_phone_number, name='add_phone_number'),
    path('list/', views.list_phone_numbers, name='list_phone_numbers'),
    path('delete/<int:phone_number_id>/', views.delete_phone_number, name='delete_phone_number'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
