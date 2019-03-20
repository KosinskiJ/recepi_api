from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase) :

    def test_create_user_with_email_successful(self) :
        """Test creating a new user with email are properly"""
        email = "test@test.com"
        password = 'adminadmin'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalize(self) :
        """Test email for new user is normalized"""
        email = 'test@TEST.TEST'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self) :
        """Testing creating user with no email raises error"""
        with self.assertRaises(ValueError) :
            get_user_model().objects.create_user(None, 'test')

    def test_create_superuser(self) :
        """Testing creating superuser proprely"""
        user = get_user_model().objests.create_superuser(
            'admin@admin.com'
            'admin'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
