from faker import Faker

from post.models import Post, Comment

faker = Faker()


class PostFactory:
    def build_post_JSON(self):
        # faker.seed(0)
        return {
            'title': faker.paragraph(nb_sentences=1),
            'content': faker.paragraph(nb_sentences=5),
        }

    def create_post(self):
        return Post.objects.create(**self.build_post_JSON())


class CommentFactory:
    def build_comment_JSON(self, post_id):
        # faker.seed(0)
        return {
            'post_id': post_id,
            'comment': faker.paragraph(nb_sentences=5),
        }

    def create_post(self, post_id):
        return Comment.objects.create(**self.build_post_JSON(post_id))
