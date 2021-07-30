from django.urls import path

from agro_user import views

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('search-user/', views.AgroUserSearchView.as_view()),
]