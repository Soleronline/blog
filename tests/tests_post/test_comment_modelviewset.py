from rest_framework import status

from tests.test_setup import TestSetUp
from tests.factories.post.post_factories import PostFactory, CommentFactory

from post.models import Comment


class CommentTestCase(TestSetUp):
    url_post = '/api/posts/'
    url = '/api/posts/{post_id}/comment/'

    def test_new_comment(self):
        post = PostFactory().build_post_JSON()
        response = self.client.post(
            self.url_post,
            post,
            format='json'
        )
        post = response.data
        comment = CommentFactory().build_comment_JSON(post['id'])
        response = self.client.post(
            self.url.format(**{'post_id': post['id']}),
            comment,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.all().count(), 1)
        self.assertEqual(response.data['comment'], comment['comment'])
