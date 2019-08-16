from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    
    def test_create_user_with_email_successful(self):
        """Test creating with a new email is successful"""
        email = "test@abc.com"
        password = "Pass@123"
        user = get_user_model().objects.create_user(
            email=email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password, password)

    def test_new_user_email_normalised(self):
        email = "test@abc.com"
        user = get_user_model().objects.create_user(email,"test@123")
        self.assertTrue(user.email, email.lower())

    def test_create_new_super_user(self):
        user = get_user_model().objects.create_superuser(
            'test@abc.com',
            'test@123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
