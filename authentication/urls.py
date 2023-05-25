from django.urls import path
from .views import *

urlpatterns = [
    path('books/', BookViews.as_view(), name='post-bbok'),
    path('register/', sign_up, name='register'),
    path('login/', login_page, name='login')
]