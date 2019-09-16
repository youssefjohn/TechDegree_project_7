from django.test import TestCase, Client
from accounts.views import register_view, login_view, logout_view, edit_profile_view, edit_password_view
from django.urls import resolve, reverse





class TestViews(TestCase):


    #  This setup runs before every test method.
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('accounts:register')
        self.login_url = reverse('accounts:login')
        self.logout_url = reverse('accounts:logout')
        self.profile_url = reverse('accounts:profile')
        self.editprofile_url = reverse('accounts:editprofile')
        self.editpassword_url = reverse('accounts:editpassword')


    def test_register_GET(self):
        # grab the response self.client contains when directed towards the register url.
        # basically, when someone clicks on 'register' it GETS the page.
        response = self.client.get(self.register_url)

        # Then test to see if 'response' is the same code as 200 (GET request)
        self.assertEqual(response.status_code, 200)

        # Test if the response, which points to the register url, is using the same template as the second argument
        self.assertTemplateUsed(response, 'accounts/register.html')


    def test_login_GET(self):

        response = self.client.get(self.login_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')


    def test_logout_GET(self):
        response = self.client.get(self.logout_url)

        self.assertEqual(response.status_code, 302)


    def test_profile_GET(self):
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile.html')

    def test_editpassword_GET(self):
        response = self.client.get(self.editpassword_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/edit_password.html')


    # def test_editprofile_GET(self):
    #     response = self.client.get(self.editprofile_url)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'accounts/edit_profile.html')





















