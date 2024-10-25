from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post
 

class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'bot',
            email = 'botbot@gmail.com',
            password = '1234',
        )

        self.post = Post.objects.create(
            title = 'Title',
            body = 'A good content',
            author = self.user
        )

    def test_string_representation(self):
        post = Post(title = 'A sample text')
        return self.assertEqual(str(post),post.title)
    
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}','Title')
        self.assertEqual(f'{self.post.body}','A good content')
        self.assertEqual(f'{self.post.author}','bot')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A good content')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/1000000/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Title')
        self.assertTemplateUsed(response,'post_detail.html') 
    
    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'),{
        'title':'New_title',
        'body':'New_text',
        'author':self.user.id,}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title,'New_title')
        self.assertEqual(Post.objects.last().body, 'New_text')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit',args = '1'),{
        'title':'Update_title',
        'body': 'Update_text'
        })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.post(
            reverse('post_delete',args = '1'))
        self.assertEqual(response.status_code, 302)

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(),'/post/1/')