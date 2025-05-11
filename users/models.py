from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Role choices for the user
    ADMIN = 'admin'
    STAFF = 'staff'
    USER = 'user'
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (STAFF, 'Staff'),
        (USER, 'User'),
    ]
    
    # The 'role' field with default as 'user'
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=USER)

    # Custom related_name for 'groups' and 'user_permissions'
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Custom related name for groups
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Custom related name for user permissions
        blank=True
    )

    # Optionally, you can override the save method to add custom behavior (like logging)
    # def save(self, *args, **kwargs):
    #     # Custom save logic (if needed)
    #     super(User, self).save(*args, **kwargs)
