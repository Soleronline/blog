from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

from post.models import Post
from post.api.serializer import PostSerializer, CommentSerializer


class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentApiViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.filter(post_id=self.kwargs.get('post_id'))

    def create(self, request, post_id):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(post=post)
            data = serializer.data
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
