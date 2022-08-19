from django.test import TestCase, Client
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from blog.models import Post

# Create your tests here.
class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_trump = User.objects.create_user(
            username='trump',
            password='somepassword'
        )

    def test_landing(self):
        post_001 = Post.objects.create(
            title='첫 번째 포스트다.',
            content='집에 가고 싶잖아?',
            author=self.user_trump,
        )

        post_002 = Post.objects.create(
            title='두 번째 포스트다.',
            content='숨 참고 러브 다이브',
            author=self.user_trump,
        )
        post_003 = Post.objects.create(
            title='세 번째 포스트다.',
            content='도비는 자유에요',
            author=self.user_trump,
        )
        post_004 = Post.objects.create(
            title='네 번째 포스트다.',
            content='행복했던 날들이었다.',
            author=self.user_trump,
        )

        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')

        body = soup.body
        self.assertNotIn(post_001.title, body.text)
        self.assertIn(post_002.title, body.text)
        self.assertIn(post_003.title, body.text)
        self.assertIn(post_004.title, body.text)
