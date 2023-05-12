from django.contrib import admin
from django.urls import path, include
from app.views import home, form, create, delete, update_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('perg/', form, name='perg'),
    path('update_view/<int:id>', update_view, name='update_view'),
    path('create/', create, name='create'),
    path('delete/<int:id>', delete, name='delete'),
    path('accounts/', include('accounts.urls')),
    path("accounts/", include("django.contrib.auth.urls")),

]
