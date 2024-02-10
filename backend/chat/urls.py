from django.urls import path
from .views import lobby

app_name = 'chat'

urlpatterns = [
    path('', lobby, name='lobby')
]