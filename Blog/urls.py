from django.urls import path
from .views import about,announcements,event,resources,contact
from .views import PostListView, PostDetailView,PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', about, name='blog-about'),  
    path('announcement/',announcements , name='blog-anouncement'), 
    path('event/',event,name='blog-event'),
    path('resources/',resources,name='blog-resources'),
    path('contact/', contact, name='blog-contact'),
    # Add more URL patterns as needed
]