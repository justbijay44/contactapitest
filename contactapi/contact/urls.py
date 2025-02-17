from django.urls import path, include
from .views import ContactCreateView, ContactDetail

urlpatterns = [

    path('', ContactCreateView.as_view()),

    path('<int:pk>/', ContactDetail.as_view()),

]
