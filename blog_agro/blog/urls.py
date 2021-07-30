from django.urls import path
from blog import views

urlpatterns = [
    path('posts/', views.PostListView.as_view()),
    path('posts/create/', views.PostCreateView.as_view()),
    path('posts/<int:pk>/', views.PostDetailView.as_view()),
    path('posts/<int:pk>/update/', views.PostUpdateView.as_view()),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view()),
    path('categories/', views.CategoryListView.as_view()),
    # path('comments/', views.CommentListCreateView.as_view()),
    # path('comments/<int:pk>/', views.CommentDetailView.as_view()),
    path('search-posts/', views.PostSearchView.as_view()),
]
