from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Blog
from .serializers import BlogSerializer

# class BlogViewSet(ModelViewSet):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def blogview(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)

    if request.method == "POST":
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.data, status=status.HTTP_200_OK)
