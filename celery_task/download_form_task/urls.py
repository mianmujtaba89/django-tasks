from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.handle_download_form, name='download'),
    path('form0/', views.handle_download_form_html, name='handle_download_form_html'),
    path('success/', views.SuccessView.as_view(), name='success'),
]