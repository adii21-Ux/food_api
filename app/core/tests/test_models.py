from django.test import TestCase
from django.contrib.auth import get_user_model

class model_test(TestCase):

    def test_create_user_with_email_pass(self):
        """Test that user is getting created successfully using email and password"""
        email = "test@gmail.com"
        password = "test123"

        user=get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@LONDONAPPDEV.com'
        user = get_user_model().objects.create_user(email, 'test123')
        
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')