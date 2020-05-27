from django.test import TestCase
from django.test.client import Client

class AuthorizationTestCase(TestCase):
    def test_signup(self):
        c1 = Client()
        response_get = c1.get("http://127.0.0.1:8000/signup/")
        self.assertEqual(response_get.status_code, 200)

        user_data_signup = {"username": "check", "first_name": "check", "last_name": "check", "password1": "checkcheck", "password2": "checkcheck"}
        response_post = c1.post("http://127.0.0.1:8000/signup/", user_data_signup, follow=True)
        self.assertEqual(response_post.status_code, 200)
        self.assertEqual(response_post.redirect_chain, [('/', 302)])

    def test_login(self):
        c2 = Client()
        response_get = c2.get("http://127.0.0.1:8000/login/")
        self.assertEqual(response_get.status_code, 200)

        user_data_login = {"username": "check", "password": "checkcheck"}
        response_post = c2.post("http://127.0.0.1:8000/login/", user_data_login, follow=True)
        self.assertEqual(response_post.status_code, 200)

