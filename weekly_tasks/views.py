from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'All-Posts' : '/post-list/',
        'Post-Detail' : '/post-detail/<str:pk>/',
        'Create' : '/post-create/',
        'Update' : '/post-update/<str:pk>/',
        'Delete' : 'post-delete/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def postList(request):
    posts=Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def postDetail(request, pk):
    posts=Post.objects.get(id=pk)
    serializer = PostSerializer(posts, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def postDetail(request, pk):
    posts=Post.objects.get(id=pk)
    serializer = PostSerializer(posts, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def postCreate(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def postUpdate(request, pk):
    post=Post.objects.get(id=pk)
    serializer = PostSerializer(instance=post, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['Delete'])
def postDelete(request, pk):
    post=Post.objects.get(id=pk)
    post.delete()

    return Response('Deleted Successfully')

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all().order_by('created_date')
#     serializer_class = PostSerializer

