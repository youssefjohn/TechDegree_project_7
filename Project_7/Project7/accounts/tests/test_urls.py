from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from accounts.views import register_view, login_view, logout_view, profile_view, edit_profile_view, edit_password_view

# https://www.youtube.com/watch?v=hA_VxnxCHbo&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=3


class TestUrls(SimpleTestCase):


    def test_register_url_resolve(self):
        url = reverse('accounts:register')
        self.assertEqual(resolve(url).func, register_view)



    def test_login_url_resolve(self):
        url = reverse('accounts:login')
        self.assertEqual(resolve(url).func,login_view)


    def test_logout_url_resolve(self):
        url = reverse('accounts:logout')
        self.assertEqual(resolve(url).func, logout_view)


    def test_profile_url_resolve(self):
        url = reverse('accounts:profile')
        self.assertEqual(resolve(url).func, profile_view)


    def test_editprofile_url_resolve(self):
        url = reverse('accounts:editprofile')
        self.assertEqual(resolve(url).func, edit_profile_view)


    def test_editpassword_url_resolve(self):
        url = reverse('accounts:editpassword')
        self.assertEqual(resolve(url).func, edit_password_view)









