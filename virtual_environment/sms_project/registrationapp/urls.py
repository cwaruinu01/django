from django.urls import path
from.import views


urlpatterns = [
    path('sms_project/',views.registration, name='sms_project'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('regpage/', views.regpage, name='regpage'),

    ]