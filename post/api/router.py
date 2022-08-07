from rest_framework.routers import DefaultRouter
from post.api.views import PostApiViewSet, CommentApiViewSet

router_post = DefaultRouter()

router_post.register(r'posts', PostApiViewSet, basename='posts')
router_post.register(r'posts/(?P<post_id>\d+)/comment', viewset=CommentApiViewSet, basename='comments')
# router_post.register(prefix='post', basename='post', viewset=PostApiViewSet)
# router_post.register(r'(?P<client_id>\d+)/comment', prefix='comment', basename='post', viewset=CommentApiViewSet)
