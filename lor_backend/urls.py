from django.contrib import admin
from django.urls import path
from lor_backend import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('champion/<int:id>', views.get_champion),
    path('data/<str:file>', views.get_data),
    path('random_champion', views.get_random_champion),
]
