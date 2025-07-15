from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import BlogPost, CustomUser
from .serializers import BlogPostSerializer, RegisterSerializer
from .permissions import IsWriterOrReadOnly


#handling CRUD operations
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsWriterOrReadOnly]  #Only writers can create/update/delete

    # Automatically set the current user as the author of the blog post
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


#View for user registration
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
