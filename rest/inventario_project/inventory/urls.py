from django.urls import path
from .views import ServerCreateView

urlpatterns = [
    path('inventory', ServerCreateView.as_view(), name='server-create'),
]