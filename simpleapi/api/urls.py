from django.urls import path
from .views import ProfileListCreateView, ProfileRetrieveUpdateDestroyView

urlpatterns = [
    path('profile/', ProfileListCreateView.as_view(), name='Profile-list-create'),
    path('profile/<int:pk>/', ProfileRetrieveUpdateDestroyView.as_view(), name='Profile-retrieve-update-destroy'),
]
