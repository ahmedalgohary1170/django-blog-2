from .models import Post ,Comment

from .serializers import CommentSerializer , PostSerializer

from rest_framework import viewsets

# from rest_framework import generics




# class PostListCreateApiView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class CommentListCreateApiView(generics.ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer


# class CommentRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer




class PostViewSets(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class= PostSerializer



class CommentViewSets(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class= CommentSerializer