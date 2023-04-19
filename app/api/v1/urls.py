from django.urls import path

from app.api.v1.views import FileAPIView

urlpatterns = [
    path('file/', FileAPIView.as_view())
]
