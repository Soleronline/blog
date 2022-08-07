from rest_framework import status

from tests.test_setup import TestSetUp
from tests.factories.post.post_factories import PostFactory

from post.models import Post


class PostTestCase(TestSetUp):
    url = '/api/posts/'

    def test_new_post(self):
        post = PostFactory().build_post_JSON()
        response = self.client.post(
            self.url,
            post,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.all().count(), 1)
        self.assertEqual(response.data['title'], post['title'])
