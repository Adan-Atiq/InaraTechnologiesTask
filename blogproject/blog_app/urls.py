from django.urls import path, include
from .views import RegisterView, BlogPostViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

#Router for BlogPostViewSet to automatically create blog-related URLs
router = DefaultRouter()
router.register(r'blogs', BlogPostViewSet, basename='blog')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Endpoint for user registration
    path('login/', TokenObtainPairView.as_view(), name='login'),  #JWT login endpoint 
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    #Include blog CRUD API endpoints from the router
    path('', include(router.urls)),
]
