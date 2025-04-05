from django.urls import path
from chatapp.views import chat_view

urlpatterns = [
    path('', chat_view, name='chat'),
]
