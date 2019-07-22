
from django.contrib.auth.models import BaseUserManager

"""
Define a UserManager for our custom model User.
"""
class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, password=None, **extra_fields):
        if username is None:
            raise TypeError('Username must be provided.')
        if not email:
            raise ValueError('Email must be provided.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Super Users must have password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
