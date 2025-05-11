# users/tests.py

from django.test import TestCase
from django.contrib.auth import get_user_model

class UserModelTest(TestCase):

    def test_user_creation_with_role(self):
        user = get_user_model().objects.create_user(
            username="testuser", email="testuser@example.com", password="password123", role="user"
        )
        self.assertEqual(user.role, 'user')
        self.assertTrue(user.check_password('password123'))
        
    def test_admin_user_creation(self):
        admin = get_user_model().objects.create_user(
            username="adminuser", email="adminuser@example.com", password="password123", role="admin"
        )
        self.assertEqual(admin.role, 'admin')
# users/tests.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class RoleBasedAccessTest(TestCase):

    def setUp(self):
        self.admin = get_user_model().objects.create_user(
            username="admin", email="admin@example.com", password="password123", role="admin"
        )
        self.staff = get_user_model().objects.create_user(
            username="staff", email="staff@example.com", password="password123", role="staff"
        )
        self.user = get_user_model().objects.create_user(
            username="user", email="user@example.com", password="password123", role="user"
        )

    def test_admin_access(self):
        self.client.login(username="admin", password="password123")
        response = self.client.get(reverse('admin_page'))  # Replace with actual URL
        self.assertEqual(response.status_code, 200)

    def test_staff_access(self):
        self.client.login(username="staff", password="password123")
        response = self.client.get(reverse('staff_page'))  # Replace with actual URL
        self.assertEqual(response.status_code, 200)

    def test_user_access(self):
        self.client.login(username="user", password="password123")
        response = self.client.get(reverse('user_page'))  # Replace with actual URL
        self.assertEqual(response.status_code, 200)

    def test_admin_restricted_page(self):
        self.client.login(username="user", password="password123")
        response = self.client.get(reverse('admin_page'))  # Replace with actual URL
        self.assertEqual(response.status_code, 403)  # Forbidden for normal user
